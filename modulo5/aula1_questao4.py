from datetime import date, timezone, timedelta, datetime
data = date.today()
dataTexto = data.strftime('%d/%m/%Y')
hora = datetime.now()
diferenca = timedelta(hours=-3)
fusoHorario = timezone(diferenca)
horaMg = hora.astimezone(fusoHorario)
horaMg_texto = horaMg.strftime('%H:%M')
print(f"Data: {dataTexto}")
print(f"Hora: {horaMg_texto}")