import logging

logging.basicConfig(level=logging.INFO)

numerics = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]


def brute_force(keyword: str, data_to_brute: list, word: list = [], level_func_recursive: int = 1, max_level_func_recursive: int = 2):
    total_data_to_brute = len(data_to_brute)

    for i in range(0, total_data_to_brute):
        if level_func_recursive == 1:
            word = []

        letter = data_to_brute[i]
        word.append(letter)
        word_to_text = ''.join(word)
        word_text_reverse = word_to_text[::-1]

        logging.debug('level: %s', level_func_recursive)
        logging.debug('word: %s', word_to_text)

        if word_to_text == keyword:
            logging.info('found keyword: %s', word_to_text)
            exit(0)

        if word_text_reverse == keyword:
            logging.info('found keyword reverse: %s', word_text_reverse)
            exit(0)

        if level_func_recursive < total_data_to_brute and level_func_recursive < max_level_func_recursive:
            brute_force(keyword, data_to_brute, word, level_func_recursive + 1, max_level_func_recursive)

        if letter != 'z':
            word.pop()



user_keyword = str(input('digit keyword: '))

data = numerics + alphabet
user_max_level = len(user_keyword)

brute_force(keyword=user_keyword.upper(), data_to_brute=data, max_level_func_recursive=user_max_level)
