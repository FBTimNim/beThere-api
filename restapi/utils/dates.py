"""Datetime wizardry."""

from datetime import datetime, timedelta


def getTomorrow():
    """Return a datetime for tomorrow."""
    return datetime.now + timedelta(hours=24)
