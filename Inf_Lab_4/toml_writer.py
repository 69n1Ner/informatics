from utils import format_value
from binary_storage import deserialize_binary

def to_toml(obj, table_name="item", prefix=""):
    # Результат
    lines = []

    if isinstance(obj, list):
        for element in obj:
            # Новая таблица [[item]]
            lines.append(f"[[{table_name}]]")

            # Рекурсивно обрабатываем элемент списка
            # все вложен. табл. будут начинаться с "item."
            lines.extend(to_toml(element, table_name, prefix=f"{table_name}."))
            lines.append("")
        return lines

    # Классификация полей (что бы вывести их в правильном порядке)

    scalar_entries = []         # key = value
    list_scalar_entries = []    # key = [1, 2, 3]
    dict_entries = []           # key = { ... }
    list_dict_entries = []      # key = [ { ... }, { ... } ]

    for key, value in obj.items():
        if isinstance(value, dict):
            dict_entries.append((key, value))
        elif isinstance(value, list) and value and isinstance(value[0], dict):
            list_dict_entries.append((key, value))
        elif isinstance(value, list):
            list_scalar_entries.append((key, value))
        else:
            scalar_entries.append((key, value))

    # Скаляры
    for key, value in scalar_entries:
        lines.append(f"{key} = {format_value(value)}")

    # Списки
    for key, value in list_scalar_entries:
        arr = ", ".join(format_value(v) for v in value)
        lines.append(f"{key} = [{arr}]")

    # Вложенные табл.
    for key, value in dict_entries:
        section = f"{prefix}{key}"
        lines.append(f"[{section}]")
        lines.extend(to_toml(value, table_name, prefix=section + "."))
        lines.append("")

    # Массивы табл.
    for key, lst in list_dict_entries:
        for element in lst:
            lines.append(f"[[{prefix}{key}]]")
            lines.extend(to_toml(element, table_name, prefix=f"{prefix}{key}."))
            lines.append("")

    # Возвращаем готовые строки TOML
    return lines

restored = deserialize_binary("data.bin")
toml_lines = to_toml(restored)
with open("output.toml", "w", encoding="utf-8") as f:
    print(toml_lines)
    f.write("\n".join(toml_lines))