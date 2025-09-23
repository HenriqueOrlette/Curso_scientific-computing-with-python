'''
Descrição:
List Comprehension é uma maneira de construir uma nova lista em Python a partir de tipos iteráveis: listas, tuplas e strings. 
Tudo isso sem usar um loop for ou o método de lista .append().
Neste projeto, você escreverá um programa que recebe uma string formatada em Camel Case ou Pascal Case e a converte para Snake Case.
O projeto tem duas fases: primeiro você usará um loop for para implementar o programa. 
Depois, você aprenderá a usar List Comprehension em vez de um loop para alcançar os mesmos resultados.
'''

def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('IAmAPascalCasedString'))

main()

#Utilizando loop for:

# snake_cased_char_list = []
    # for char in pascal_or_camel_cased_string:
    #     if char.isupper():
    #       converted_character = '_' + char.lower()
    #       snake_cased_char_list.append(converted_character)
    #     else:
    #         snake_cased_char_list.append(char)
    # snake_cased_string = ''.join(snake_cased_char_list)
    # clean_snake_cased_string = snake_cased_string.strip('_')

    # return clean_snake_cased_string