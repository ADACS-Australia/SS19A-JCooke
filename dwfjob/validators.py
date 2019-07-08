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
