# Config #
DONT_CHECK_NOTES = ['Inbox']
IGNORE_TAG = '#'

try:
    from config_local import DONT_CHECK_NOTES, IGNORE_TAG  # noqa
except ImportError:
    pass
