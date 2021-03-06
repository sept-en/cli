from builtins import int, range, str
from past.builtins import basestring

from pyinfrabox import ValidationError

def check_text(t, path, allowEmpty=False):
    if not isinstance(t, basestring):
        raise ValidationError(path, "is not a string")

    if not allowEmpty and not t:
        raise ValidationError(path, "empty string not allowed")

def check_allowed_properties(d, path, allowed):
    if not isinstance(d, dict):
        raise ValidationError(path, "must be an object")

    for key in d:
        if key not in allowed:
            raise ValidationError(path, "invalid property '%s'" % key)

def check_required_properties(d, path, required):
    if not isinstance(d, dict):
        raise ValidationError(path, "must be an object")

    for key in required:
        if key not in d:
            raise ValidationError(path, "property '%s' is required" % key)

def check_string_array(e, path):
    if not isinstance(e, list):
        raise ValidationError(path, "must be an array")

    if not e:
        raise ValidationError(path, "must not be empty")

    for i in range(0, len(e)):
        elem = e[i]
        path = "%s[%s]" % (path, i)
        check_text(elem, path)

def check_boolean(d, path):
    if not isinstance(d, bool):
        raise ValidationError(path, "must be a boolean")

def check_number(d, path):
    if not isinstance(d, int):
        raise ValidationError(path, "must be a number")

def check_color(d, path):
    if d not in ("red", "green", "blue", "yellow", "orange", "white", "black", "grey"):
        raise ValidationError(path, "not a valid value")
