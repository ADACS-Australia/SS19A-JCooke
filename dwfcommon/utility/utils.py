"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

import ast
import uuid

from django.db import models

from dwfjob.models import MaryJob

from .display_names import (
    SUBMITTED,
    QUEUED,
    IN_PROGRESS,
    DRAFT,
    COMPLETED,
    PENDING,
    ERROR,
    CANCELLED,
    WALL_TIME_EXCEEDED,
    OUT_OF_MEMORY,
    PUBLIC,
    DISPLAY_NAME_MAP,
)

# Units of file size
B = 'B'
KB = 'KB'
MB = 'MB'
GB = 'GB'
TB = 'TB'
PB = 'PB'


def get_readable_size(size, unit=B):
    """
    Converts a size into human readable format: ex: 1024 MB -> 1.0 GB
    :param size: float number
    :param unit: unit of measurement
    :return: human readable format
    """
    units = [B, KB, MB, GB, TB, PB]

    # invalid inputs should return 0.0 B
    # 0 B, 0 KB, 0 ... should also return 0.0 B
    if size <= 0 or unit not in units:
        return '0.0 B'

    # checking whether we need go for another step
    # that is unit is not already in PB and size = 1024
    if unit in units[:-1] and size >= 1024:

        # get new size
        size = size / 1024

        # get next unit
        unit = units[units.index(unit) + 1]

        # call the function again for further checking
        return get_readable_size(size, unit)

    else:

        # return the string format to 2 decimal point
        return ' '.join([str(round(size / 1, 2)), unit])


def get_to_be_active_tab(tabs, tabs_indexes, active_tab, previous=False):
    """
    Finds out the next active tab based on user input
    :param tabs: Tabs that shows up in the UI
    :param tabs_indexes: indexed tabs to show them in order
    :param active_tab: Current active tab
    :param previous: Whether or not previous is pressed
    :return: To be Active tab, Whether it is the last tab or not
    """

    # keep track of out of index tab, beneficial to detect the last tab
    no_more_tabs = False

    # find the current active tab index
    active_tab_index = tabs_indexes.get(active_tab)

    # next active tab index based on the button pressed
    if previous:
        active_tab_index -= 1
    else:
        active_tab_index += 1

    # checks out the last tab or not
    try:
        active_tab = tabs[active_tab_index]
    except IndexError:
        no_more_tabs = True

    return active_tab, no_more_tabs


def list_job_actions(job, user):
    """
    List the actions a user can perform on this DWF Job
    :param job: A DWF Job instance
    :param user: User for whom the actions will be generated
    :return: Nothing
    """

    job_actions = []

    # DWFJob Owners and Admins get most actions
    if job.user == user or user.is_admin:

        # any job can be copied
        job_actions.append('copy')

        # job can only be deleted if in the following status:
        # 1. draft
        if job.status in [DRAFT]:
            job_actions.append('delete')

        # edit a job if it is a draft
        if job.status in [DRAFT]:
            job_actions.append('edit')

        # completed job can be public and vice versa
        if job.status in [COMPLETED]:
            job_actions.append('make_it_public')
        elif job.status in [PUBLIC]:
            job_actions.append('make_it_private')

    else:
        # non admin and non owner can copy a PUBLIC job
        if job.status in [PUBLIC]:
            job_actions.append('copy')

    return job_actions


def generate_draft_job_name(job, user):
    """
    Generates draft job name for a Job by checking existing user, job constraint to prevent database failure.
    :param job: Job model instance
    :param user: user instance
    :return:
    """
    if not job:
        return None

    # try to generate a unique name for the job owner
    name = job.name
    while MaryJob.objects.filter(user=user, name=name).exists():
        name = (job.name + '_' + uuid.uuid4().hex)[:255]

        # This will be true if the job has 255 Characters in it,
        # In this case, we cannot get a new name by adding something to it.
        # This can be altered later based on the requirement.
        if name == job.name:
            # cannot generate a new name, returning none
            return None

    return name


def find_display_name(value):
    """
    Find and return the display name that corresponds the value
    :param value: String of the name
    :return: Display name or names separated by comma if a list
    """

    # displaying array (for detector choice at this moment)
    try:
        value_list = ast.literal_eval(value)
        display_list = [DISPLAY_NAME_MAP.get(x, x) for x in value_list]
        return ', '.join(display_list)
    except (ValueError, TypeError, SyntaxError):
        pass

    return DISPLAY_NAME_MAP.get(value, value)


def remove_suffix(name):
    """
    Removes the suffix from the name of the parameters. For distinguishing purpose, some parameter names have suffix.
    For example: psi___cw, starttime___cw. However, we don't want those in the json file.
    This method removes any suffix like above.
    :param name: String name of the parameter.
    :return: json compatible name for a Job
    """
    return ''.join(name.split('___')[:-1]) if '___' in name else name


def get_formatted_value_for_json(field, value):
    if not value:
        return value

    if type(field) in [models.CharField]:
        return value
    elif type(field) in [models.DateField, models.DateTimeField]:
        return value.strftime('%d/%m/%Y')
    else:
        return value
