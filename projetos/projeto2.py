DIAS_DA_SEMANA = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

def add_time(start, duration, day=None):
    tempo, periodo = start.split()
    horas, minutos = map(int,tempo.split(':'))
    duracao_horas, duracao_minutos = map(int,duration.split(':'))

    dias_depois, novo_minuto = '', 0
    novo_periodo = periodo

    # Tratamento do dia da semana
    if day:
        dia_tratado = (day.lower()).capitalize()
        novo_dia = 0
    
    # Trocar para 24h (0-23)
    if periodo == 'PM':
        horas += 12
    elif periodo == 'AM' and horas == 12:
        horas = 0

    nova_hora = int(horas) + int(duracao_horas)

    # Soma minutos
    if minutos + duracao_minutos >= 60:
        novo_minuto = str((minutos + duracao_minutos) - 60).zfill(2)
        nova_hora += 1
    else:
        novo_minuto = str(minutos + duracao_minutos).zfill(2)

    # Contagem de dias
    dias_depois = nova_hora // 24

    # Cálculo horário para 12h novamente
    nova_hora = nova_hora % 24

    if nova_hora < 12:
        novo_periodo = 'AM'
        if nova_hora == 0:
            nova_hora = 12
    else:
        novo_periodo = 'PM'
        if nova_hora == 12:
            nova_hora = 12
        else:
            nova_hora -= 12

    resultado = f"{nova_hora}:{novo_minuto} {novo_periodo}"

    # Cálculo se for incluído o dia da semana
    if day:
        novo_dia = DIAS_DA_SEMANA.index(dia_tratado)
        novo_dia = (novo_dia + dias_depois) % 7
        novo_dia = DIAS_DA_SEMANA[novo_dia]
        resultado += f", {novo_dia}"

    # Lógica do print
    if dias_depois == '':
        resultado = resultado
    elif dias_depois == 1:
        resultado += ' (next day)'
    elif dias_depois > 1:
        resultado += f" ({dias_depois} days later)"

    return resultado


print(add_time('8:16 PM', '466:02'))
    

