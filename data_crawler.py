def list_of_dict(datas: list[dict], find_key: str, find_value: str):

    list_found = []

    for data in datas:
        for key, value in data.items():
            if key == find_key and value == find_value:
                list_found.append(data)

    return list_found