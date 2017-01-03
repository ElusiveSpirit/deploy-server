import os
from config import BASE_DIR, TOKENS_DIR


def get_token_list():
    """Returns a list with tokens

    Check all files in BASE_DIR + tokens
    Data in a one file is a one token
    """
    token_list = []
    tokens_dir_path = os.path.join(BASE_DIR, TOKENS_DIR)
    for dir, dirs, files in os.walk(tokens_dir_path):
        for file_name in files:
            file = open(os.path.join(tokens_dir_path, file_name), 'r')
            token_list.append(file.read().strip())
            file.close()
    return token_list



