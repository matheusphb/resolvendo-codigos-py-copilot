# Solicite dois números e depois realize uma operação simples entre eles.
# Solicite dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicite a operação desejada
operacao = input("Digite a operação desejada (+, -, *, /): ")

# Realize a operação e exiba o resultado
if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: Divisão por zero"
else:
    resultado = "Operação inválida"

print(f"O resultado da operação é: {resultado}")