def next_non_empty(lines, start):
    for i in range(start, len(lines)):
        if lines[i].strip() and not lines[i].lstrip().startswith("#"):
            return lines[i]
    return None


def parse_scalar(value):
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    if value == "true":
        return True
    if value == "false":
        return False
    if value.isdigit():
        return int(value)
    return value


def format_value(v):
    if isinstance(v, str):
        return f"\"{v}\""
    if isinstance(v, bool):
        return "true" if v else "false"
    return str(v)
