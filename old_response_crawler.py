def list_of_dict(datas: list[dict], find_key: str, find_value: str):

    list_found = []

    for data in datas:
        for key, value in data.items():
            if key == find_key and value == find_value:
                list_found.append(data)

    return list_found

def dict_of_dict(datas: dict[dict], find_key: str, find_value: str):
    pass

# TODO: create a crawler that crawls deep into the response to find a key(etc. 'title') and returns all values with the searched key
# cont. and it only gives the string, not a dict or a list

def deep_search(response: list, find_key: str):

    result = []

    for data in response:
        if type(data) is dict:
            result.append(deep_search_dict(data, find_key))

def deep_search_dict(dict_data: dict, find_key: str):

    for key, value in dict_data.items():

        if key == find_key:
            return value
        
    return None