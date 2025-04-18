from django import template


register = template.Library()


@register.filter(name="dict_get")
def dict_get(dictionary, key):
    """
    Custom template filter to safely get a value from a dictionary.
    If the key does not exist, it returns an empty string.
    """
    if isinstance(dictionary, dict):
        return dictionary.get(key, "")
    return ""
