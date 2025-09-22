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

