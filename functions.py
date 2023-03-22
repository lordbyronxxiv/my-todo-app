FILEPATH = "todos.txt"


def get_todos(filepath_input_local=FILEPATH):
    """ This function reads a text file and returns
    the list of to do items.
    """
    with open(filepath_input_local, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_arg, filepath_input_local=FILEPATH):
    """write the to do items list in the text file"""
    with open(filepath_input_local, 'w') as file_local:
        file_local.writelines(todos_arg)
