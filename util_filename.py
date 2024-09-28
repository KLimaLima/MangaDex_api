def get_file_type(file_name: str):

    file_name = file_name.split('.')

    return file_name[-1]

def get_page_number(file_name: str):

    file_name = file_name.split('-')

    return file_name[0]