"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

# VARIABLES of this file must be unique
from django_hpc_job_controller.client.scheduler.status import JobStatus


# Dictionary to map names and corresponding display names (for UI)
DISPLAY_NAME_MAP = dict()
DISPLAY_NAME_MAP_HPC_JOB = dict()


# Job Status
NONE = 'none'
NONE_DISPLAY = 'None'
DRAFT = 'draft'
DRAFT_DISPLAY = 'Draft'
PENDING = 'pending'
PENDING_DISPLAY = 'Pending'
SUBMITTING = 'submitting'
SUBMITTING_DISPLAY = 'Submitting'
SUBMITTED = 'submitted'
SUBMITTED_DISPLAY = 'Submitted'
QUEUED = 'queued'
QUEUED_DISPLAY = 'Queued'
IN_PROGRESS = 'in_progress'
IN_PROGRESS_DISPLAY = 'In Progress'
CANCELLING = 'cancelling'
CANCELLING_DISPLAY = 'Cancelling'
CANCELLED = 'cancelled'
CANCELLED_DISPLAY = 'Cancelled'
ERROR = 'error'
ERROR_DISPLAY = 'Error'
WALL_TIME_EXCEEDED = 'wall_time_exceeded'
WALL_TIME_EXCEEDED_DISPLAY = 'Wall Time Exceeded'
OUT_OF_MEMORY = 'out_of_memory'
OUT_OF_MEMORY_DISPLAY = 'Out of Memory'
COMPLETED = 'completed'
COMPLETED_DISPLAY = 'Completed'
SAVED = 'saved'
SAVED_DISPLAY = 'Saved'
DELETING = 'deleting'
DELETING_DISPLAY = 'Deleting'
DELETED = 'deleted'
DELETED_DISPLAY = 'Deleted'
PUBLIC = 'public'
PUBLIC_DISPLAY = 'Public'

DISPLAY_NAME_MAP.update({
    DRAFT: DRAFT_DISPLAY,
    PENDING: PENDING_DISPLAY,
    SUBMITTING: SUBMITTING_DISPLAY,
    SUBMITTED: SUBMITTED_DISPLAY,
    QUEUED: QUEUED_DISPLAY,
    IN_PROGRESS: IN_PROGRESS_DISPLAY,
    CANCELLING: CANCELLING_DISPLAY,
    CANCELLED: CANCELLED_DISPLAY,
    ERROR: ERROR_DISPLAY,
    WALL_TIME_EXCEEDED: WALL_TIME_EXCEEDED_DISPLAY,
    OUT_OF_MEMORY: OUT_OF_MEMORY_DISPLAY,
    COMPLETED: COMPLETED_DISPLAY,
    SAVED: SAVED_DISPLAY,
    DELETING: DELETING_DISPLAY,
    DELETED: DELETED_DISPLAY,
    PUBLIC: PUBLIC_DISPLAY,
})

DISPLAY_NAME_MAP_HPC_JOB.update({
    JobStatus.DRAFT: DRAFT,
    JobStatus.PENDING: PENDING,
    JobStatus.SUBMITTING: SUBMITTING,
    JobStatus.SUBMITTED: SUBMITTED,
    JobStatus.QUEUED: QUEUED,
    JobStatus.RUNNING: IN_PROGRESS,
    JobStatus.CANCELLING: CANCELLING,
    JobStatus.CANCELLED: CANCELLED,
    JobStatus.ERROR: ERROR,
    JobStatus.WALL_TIME_EXCEEDED: WALL_TIME_EXCEEDED,
    JobStatus.OUT_OF_MEMORY: OUT_OF_MEMORY,
    JobStatus.DELETING: DELETING,
    JobStatus.DELETED: DELETED,
    JobStatus.COMPLETED: COMPLETED,
})


# Job Parameter Names
OLD_TEMPLATE = 'old_template'
OLD_TEMPLATE_DISPLAY = 'Old Template'
NEW_TEMPLATE = 'new_template'
NEW_TEMPLATE_DISPLAY = 'New Template'
FIELD = 'field'
FIELD_DISPLAY = 'Field'
DATE = 'date'
DATE_DISPLAY = 'Date'
TEMPLATE = 'template'
TEMPLATE_DISPLAY = 'Template'
MARY_SEED_NAME = 'mary_seed_name'
MARY_SEED_NAME_DISPLAY = 'Mary run seed name'
STEPS = 'steps'
STEPS_DISPLAY = 'Number of images to be coadded'
CLOBBER = 'clobber'
CLOBBER_DISPLAY = 'Clobber run'
FILTER = 'filter'
FILTER_DISPLAY = 'Filter'
MARY_RUN_TEMPLATE = 'mary_run_template'
MARY_RUN_TEMPLATE_DISPLAY = 'Date of mary template'
MARY_RUN_TEMPLATE_SEQUENCE_NUMBER = 'mary_run_template_sequence_number'
MARY_RUN_TEMPLATE_SEQUENCE_NUMBER_DISPLAY = 'Sequence number of previous mary run'
IMAGE_NAMES = 'image_names'
IMAGE_NAMES_DISPLAY = '6 digit code in the NOAO name'
TEMPLATE_DATE = 'template_date'
TEMPLATE_DATE_DISPLAY = 'Template date'
OLD_TEMPLATE_NAME = 'old_template_name'
OLD_TEMPLATE_NAME_DISPLAY = 'Name of old template (downloaded from NOAO portal)'
RUN_DATES = 'run_dates'
RUN_DATES_DISPLAY = 'Run dates'
LAST_MARY_RUN = 'last_mary_run'
LAST_MARY_RUN_DISPLAY = 'Last mary run'
TEMPLATE_IMAGES = 'template_images'
TEMPLATE_IMAGES_DISPLAY = 'Template images'


DISPLAY_NAME_MAP.update({
    OLD_TEMPLATE: OLD_TEMPLATE_DISPLAY,
    NEW_TEMPLATE: NEW_TEMPLATE_DISPLAY,
    FIELD: FIELD_DISPLAY,
    DATE: DATE_DISPLAY,
    TEMPLATE: TEMPLATE_DISPLAY,
    MARY_SEED_NAME: MARY_SEED_NAME_DISPLAY,
    STEPS: STEPS_DISPLAY,
    CLOBBER: CLOBBER_DISPLAY,
    FILTER: FILTER_DISPLAY,
    MARY_RUN_TEMPLATE: MARY_RUN_TEMPLATE_DISPLAY,
    MARY_RUN_TEMPLATE_SEQUENCE_NUMBER: MARY_RUN_TEMPLATE_SEQUENCE_NUMBER_DISPLAY,
    IMAGE_NAMES: IMAGE_NAMES_DISPLAY,
    TEMPLATE_DATE: TEMPLATE_DATE_DISPLAY,
    OLD_TEMPLATE_NAME: OLD_TEMPLATE_NAME_DISPLAY,
    RUN_DATES: RUN_DATES_DISPLAY,
    LAST_MARY_RUN: LAST_MARY_RUN_DISPLAY,
    TEMPLATE_IMAGES: TEMPLATE_IMAGES_DISPLAY,
})
