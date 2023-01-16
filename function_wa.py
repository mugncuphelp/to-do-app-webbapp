def save_to_do(filepath, to_do_list):
    with open(filepath, "w") as save_file:
        for line in to_do_list:
            save_file.writelines(line + "\n")


def read_todo_from_file(filepath):
    with open(filepath, "r") as save_file:
        to_do_list = [line.rstrip() for line in save_file]
    return to_do_list
