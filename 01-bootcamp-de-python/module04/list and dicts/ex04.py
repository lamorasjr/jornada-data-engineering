# 4. Contar ocorrências de caracteres

def count_characters(string_input):
    char_dict = {}

    for char in string_input:
        char_dict[char] = char_dict.get(char, 0) + 1

    return char_dict

print(count_characters("engenharia de dados"))