def dict_1_value_chooser(data: dict, keys: tuple):

    for key in keys:

        try:
            return data[key]
        except:
            pass

    for value in data.values():
        return value
    
def dict_values_grabber(data: dict, keys: tuple):

    result = {}

    for key in keys:
        if key in data.keys():
            result[key]= data[key]

    if not result:
        for key, value in data.items():
            result[key]= value
            break

    return result

def list_dict_to_dict_list(datas: list[dict]):

    result = {}

    for data in datas:
        for key, value in data.items():
            result.setdefault(key, []).append(value)

    return result