from utils import parse_scalar, next_non_empty
from binary_storage import serialize_binary

def parse_yaml(lines):
    # Стек: (текущий объект, уровень отступа)
    stack = [({}, -1)]

    for i, raw in enumerate(lines):
        # Пропускаем пустые строки и комментарии
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue

        indent = len(raw) - len(raw.lstrip())
        line = raw.strip()

        while stack and indent <= stack[-1][1]:
            stack.pop()

        # Текущий родительский объект
        parent, parent_indent = stack[-1]

        # Обрабатываем один элемент списка
        if line.startswith("-"):
            value = line[1:].strip()

            # Если родитель — dict, значит здесь должен быть список
            if isinstance(parent, dict):
                lst = []
                stack[-1] = (lst, stack[-1][1])
                parent = lst

            # Если key: value -> словарь
            if ":" in value:
                key, val = value.split(":", 1)
                obj = {key.strip(): parse_scalar(val.strip())}
                parent.append(obj)
                stack.append((obj, indent))

            elif value == "":
                obj = {}
                parent.append(obj)
                stack.append((obj, indent))

            else:
                parent.append(parse_scalar(value))

            continue

        # Обработка key:value
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        #  Если значение пустое -> дальше вложенная структура
        if value == "":
            # Нужно понять что будет: список или словарь
            # для этого смотрим след. непустую строку
            next_line = next_non_empty(lines, i + 1)
            if next_line and next_line.lstrip().startswith("-"):
                obj = []
            else:
                obj = {}

            parent[key] = obj
            stack.append((obj, indent))
        else:
            parent[key] = parse_scalar(value)

    # Возвращаем корневой объект
    return stack[0][0]

with open("input2.yaml") as f:
    text = f.readlines()
    print(parse_yaml(text))
    serialize_binary(parse_yaml(text),"data.bin")