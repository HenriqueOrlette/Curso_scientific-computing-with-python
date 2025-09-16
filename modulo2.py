#Algoritmo de Luhn

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    #Inverte o número do cartão
    card_number_reversed = card_number[::-1]
    #Lista os números com index par
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        #Soma os números em posição de index par
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    #Lista os números com index ímpar
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        #Se o número for maior ou igual a 10, soma-se os algarismos
        if number >= 10:
            # Divisão inteira retorna o primeiro algarismo e Módulo retorna o segundo
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    #Retorna true ou false
    return total % 10 == 0

def main():
    card_number = '4111-1111-4555-1241'
    #Limpa o número
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()