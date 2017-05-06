"""Datetime wizardry."""

from datetime import datetime, timedelta


def getTomorrow():
    """Return a datetime for tomorrow."""
    return datetime.now() + timedelta(hours=24)


def getIncrement(inc):
    """Return a datetime with an increment."""
    return datetime.now() + timedelta(hours=inc)
