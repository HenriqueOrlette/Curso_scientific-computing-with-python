'''
Finalize a função arithmetic_arranger que recebe uma lista de strings contendo problemas aritméticos e retorna os problemas organizados verticalmente e lado a lado. 
Opcionalmente, a função deve aceitar um segundo argumento. Quando esse segundo argumento for definido como True, as respostas devem ser exibidas.

Regras
A função retornará a conversão correta se os problemas fornecidos estiverem formatados adequadamente. Caso contrário, ela retornará uma string que descreve um erro de forma clara para o usuário.

Situações que retornarão um erro:

Se houver problemas demais fornecidos para a função. O limite é cinco, qualquer valor acima disso retornará: 'Error: Too many problems.'

Os operadores apropriados que a função aceitará são adição e subtração. Multiplicação e divisão retornarão um erro. Outros operadores não mencionados neste tópico não precisarão ser testados. O erro retornado será: "Error: Operator must be '+' or '-'."

Cada número (operando) deve conter apenas dígitos. Caso contrário, a função retornará: 'Error: Numbers must only contain digits.'

Cada operando (ou seja, o número de cada lado do operador) tem um máximo de quatro dígitos de largura. Caso contrário, a string de erro retornada será: 'Error: Numbers cannot be more than four digits.'

Se o usuário fornecer o formato correto dos problemas, a conversão que você retornará seguirá estas regras:

Deve haver um único espaço entre o operador e o mais longo dos dois operandos. O operador ficará na mesma linha que o segundo operando. Ambos os operandos estarão na mesma ordem fornecida (o primeiro será o de cima e o segundo será o de baixo).

Os números devem ser alinhados à direita.   

Deve haver quatro espaços entre cada problema.

Deve haver traços na parte inferior de cada problema. Os traços devem percorrer todo o comprimento de cada problema individualmente. (O exemplo acima mostra como isso deve ser.)
'''

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    for problem in problems:
        partes = problem.split()

        operando1 = partes[0]
        operador = partes[1]
        operando2 = partes[2]

        if operador == '*' or operador == '/':
            return "Error: Operator must be '+' or '-'."
        elif len(operando1) > 4 or len(operando2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        elif not operando1.isdigit() or not operando2.isdigit():
            return 'Error: Numbers must only contain digits.'

        linha1 = []
        linha2 = []
        linha3 = []
        linha_resultado = []

        for problem in problems:
            operando1, operador, operando2 = problem.split()
            num1 = int(operando1)
            num2 = int(operando2)

            if operador == '+':
                resultado = num1 + num2
            else:
                resultado = num1 - num2

            largura_total = max(len(operando1), len(operando2)) + 2

            linha1.append(operando1.rjust(largura_total))
            linha2.append(f'{operador}{operando2.rjust(largura_total - 1)}')
            linha3.append('-' * largura_total)
            linha_resultado.append(str(resultado).rjust(largura_total))

        linha1_final = "    ".join(linha1)
        linha2_final = "    ".join(linha2)
        linha3_final = "    ".join(linha3)
        linha_resultado_final = "    ".join(linha_resultado)

        if show_answers:
            arranged_problems = linha1_final + '\n' + linha2_final + '\n' + linha3_final + '\n' + linha_resultado_final
        else:
            arranged_problems = linha1_final + '\n' + linha2_final + '\n' + linha3_final

    return arranged_problems


def main():
    problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    print(arithmetic_arranger(problems))

main()

