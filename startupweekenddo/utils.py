from django.conf import settings
from datetime import datetime
import pytz


def localized_date(date=None, timezone=None):
    """
    Returns the given date, localized to the default timezone.

    If no date is given, return the localized current date.

    timezone should be a valid timezone object obtained via pytz.
    """
    if not timezone:
        default_tz = settings.TIME_ZONE
        timezone = pytz.timezone(default_tz)

    if not date:
        date = pytz.utc.localize(datetime.utcnow())

    return date.astimezone(timezone)
