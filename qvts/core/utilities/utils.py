from django.conf import settings


def setting(name, default=None):
    """
    Helper function to get a Django setting by name. If setting doesn't exists
    it will return a default.

    :param name: Name of setting
    :type name: str
    :param default: Value if setting is unfound
    :returns: Setting's value

    example: setting("EMAIL_BACKEND")
    """
    return getattr(settings, name, default)
