from gendiff.format.stylish import get_render
from gendiff.format.json import get_json
from gendiff.format.plain import get_plain


def get_right_formatter(data, formatter=None):
    if formatter is None:
        return get_render(data)
    if formatter == 'plain':
        return get_plain(data)
    elif formatter == 'json':
        return get_json(data)
    else:
        raise ValueError('Unknown formatter')