"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from datetime import datetime

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_yymmdd_date(value):
    try:
        int(value)
    except (TypeError, ValueError):
        raise ValidationError(
            _('Must be a date in yymmdd format')
        )
    else:
        try:
            datetime.strptime(value, '%y%m%d').date()
        except (TypeError, ValueError):
            raise ValidationError(
                _('Must be a date in yymmdd format')
            )


def validate_cs_yymmdd_dates(value):
    """
    Validates multiple comma separated yymmdd dates
    :param value: String containing dates in comma-separated format
    :return: None
    """
    try:
        dates = [x.strip() for x in value.split(',')]
        for date in dates:
            validate_yymmdd_date(date)
    except ValidationError:
        raise ValidationError(
            _('Must be dates in yymmdd, yymmdd format')
        )
