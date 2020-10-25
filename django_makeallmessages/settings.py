from django.conf import settings


def str_to_list(value):
    """
    Converts a string value to a list, otherwise just keep it as it is.

    @param value: The value to convert to a list
    @return: [value] if value is a string, otherwise returns just value
    """
    if isinstance(value, str):
        return [value]
    else:
        return value


__DEFAULT_VALUES = getattr(settings, "MAM_DEFAULT", {})
__DEFAULT_LOCALE = getattr(__DEFAULT_VALUES, "locale", [])
__DEFAULT_EXTENSION = getattr(__DEFAULT_VALUES, "extension", [])
__DEFAULT_IGNORE = getattr(__DEFAULT_VALUES, "ignore", [])
__DEFAULT_NO_WRAP = getattr(__DEFAULT_VALUES, "no_wrap", None)

# Make it possible to write in the values as strings if it's only 1 value
__DEFAULT_LOCALE = str_to_list(__DEFAULT_LOCALE)
__DEFAULT_EXTENSION = str_to_list(__DEFAULT_EXTENSION)
__DEFAULT_IGNORE = str_to_list(__DEFAULT_IGNORE)

DEFAULT_VALUES = {
    'locale': __DEFAULT_LOCALE,
    'extension': __DEFAULT_EXTENSION,
    'ignore': __DEFAULT_IGNORE,
    'no_wrap': __DEFAULT_NO_WRAP,
}

__all__ = [DEFAULT_VALUES]
