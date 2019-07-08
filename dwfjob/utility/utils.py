"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.utils import timezone


def utc_current_yymmdd_date():
    """
    Get current utc time as yymmdd format
    :return: String in yymmdd format
    """
    now = timezone.now()
    return now.strftime('%y%m%d')
