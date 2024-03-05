from datetime import datetime, date


def dias_restantes(fp):
    constante = 30
    fp = datetime.strptime(fp, '%Y-%m-%d').date()
    fa = date.today()

    print(f'Fecha de pago: {fp}')
    print(f'Fecha actual: {fa}')

    dias_transcurridos = (fa - fp).days
    print(dias_transcurridos)
    dias_restante = max(constante - dias_transcurridos, 0)
    return dias_restante


print(dias_restantes('2024-01-18'))
