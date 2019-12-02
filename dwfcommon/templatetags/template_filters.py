"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django import template

from ..utility.display_names import (
    DRAFT,
    PENDING,
    SUBMITTING,
    SUBMITTED,
    QUEUED,
    IN_PROGRESS,
    COMPLETED,
    CANCELLING,
    CANCELLED,
    ERROR,
    WALL_TIME_EXCEEDED,
    OUT_OF_MEMORY,
    DELETING,
    DELETED,
    PUBLIC,
)
from ..utility.utils import find_display_name

register = template.Library()


@register.filter
def field_type(field):
    """
    Returns the field type of an input
    :param field: input field
    :return: string representing the class name
    """
    return field.field.widget.__class__.__name__


@register.filter(name='status_color')
def status_color(status):
    """
    Return the status colour for the bootstrap theme
    :param status: String (status name)
    :return: a bootstrap class according to the dictionary mapping
    """
    status_color_map = {
        DRAFT: 'secondary',
        PENDING: 'secondary',
        SUBMITTING: 'primary',
        SUBMITTED: 'primary',
        QUEUED: 'primary',
        IN_PROGRESS: 'primary',
        COMPLETED: 'success',
        CANCELLING: 'dark',
        CANCELLED: 'dark',
        ERROR: 'danger',
        WALL_TIME_EXCEEDED: 'warning',
        OUT_OF_MEMORY: 'warning',
        DELETING: 'muted',
        DELETED: 'muted',
        PUBLIC: 'info',
    }

    return status_color_map.get(status, 'secondary')


@register.filter(name='display_name')
def display_name(value):
    """
    Finding the display name for displaying in the UI.
    :param value: value for what display name will be searched.
    :return: display name of the value
    """

    # calling a utility function that does the same
    return find_display_name(value)
