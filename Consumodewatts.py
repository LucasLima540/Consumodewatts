nome = input("Nome do aparelho: ")
num1 = int(input("Quantos watts de potência ele tem? "))
num2 = int(input("Tempo médio de uso em horas? "))
operacao = (num1 * num2 * 30) / 1000
print("consumo estimado:", operacao, "Kwh/mês")
