# flake8: noqa: C901
def get_render(data, indent_level=1):
    output = ""
    spaces = get_spaces(indent_level)
    sorting_content = sorted(data, key=lambda i: i['key'])
    for i in sorting_content:
        if i['type'] == 'added':
            if type(i['value']) == dict:
                output += f"\n{spaces}+ {i['key']}: " \
                          f"{make_pack(i['value'], indent_level)}"
            else:
                output += f"\n{spaces}+ {str(i['key'])}: " \
                          f"{str(make_pack(i['value'], indent_level))}"
        elif i['type'] == 'removed':
            if type(i['value']) == dict:
                output += f"\n{spaces}- {i['key']}: " \
                          f"{make_pack(i['value'], indent_level)}"
            else:
                output += f"\n{spaces}- {str(i['key'])}: " \
                          f"{str(make_pack(i['value'], indent_level))}"
        elif i['type'] == 'changed':
            if type(i['value']) == tuple:
                output += f"\n{spaces}- {i['key']}: " \
                          f"{str(make_pack(i['value'][0], indent_level))}"
                output += f"\n{spaces}+ {i['key']}: " \
                          f"{str(make_pack(i['value'][1], indent_level))}"
        elif i['type'] == 'unchanged':
            if type(i['value']) == dict:
                output += f"\n{spaces}  {i['key']}: " \
                          f"{make_pack(i['value'], indent_level)}"
            else:
                output += f"\n{spaces}  {i['key']}: " \
                          f"{make_pack(i['value'], indent_level)}"
        elif i['type'] == 'nested':
            output += f"\n{spaces}  {i['key']}: " \
                      f"{get_render(i['value'], indent_level + 1)}"
    if indent_level > 1:
        result = '{' + output + '\n' + get_spaces(indent_level - 1) + '  }'
    else:
        result = '{' + output + '\n' + get_spaces(indent_level - 1) + '}'
    return result


def make_pack(node, indent_level=0):
    if node is None:
        return 'null'
    if type(node) is bool:
        return 'true' if node else 'false'
    if isinstance(node, dict):
        output_text = '{'
        for key, value in node.items():
            spaces = get_spaces(indent_level + 1)
            if isinstance(value, dict):
                output_text += f'\n{spaces}  {key}: ' \
                    f'{make_pack(value, indent_level + 1)}'
            else:
                output_text += f'\n{spaces}  {key}: {value}'
        output_text += f'\n{get_spaces(indent_level)}  }}'
        return output_text
    else:
        return node


def get_spaces(depth):
    return ' ' * (depth * 4 - 2)
