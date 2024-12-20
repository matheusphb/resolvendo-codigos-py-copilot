
### 1. **Concatenando Dados 🐾**
**Descrição**: Receba dois dados diferentes do usuário e concatene-os em uma única string.

**Exemplo de código**:

```python
# Solicitar ao usuário dois dados
dado1 = input("Digite o primeiro dado: ")
dado2 = input("Digite o segundo dado: ")

# Concatenando os dados
resultado = dado1 + dado2

# Exibindo o resultado
print("A concatenação dos dados é:", resultado)
```

Neste exercício, o GitHub Copilot pode ajudar a sugerir o uso da função `input()` e como concatenar strings.

---

### 2. **Repetindo Textos ✏️**
**Descrição**: Solicite uma string e um número inteiro como entrada e retorne a string repetida o número de vezes informado.

**Exemplo de código**:

```python
# Solicitar a string e o número inteiro
texto = input("Digite a string que deseja repetir: ")
repeticoes = int(input("Digite o número de vezes para repetir a string: "))

# Repetindo a string
resultado = texto * repeticoes

# Exibindo o resultado
print("Resultado:", resultado)
```

O Copilot pode sugerir o uso do operador de multiplicação (`*`) para repetir a string a quantidade de vezes fornecida.

---

### 3. **Operações Matemáticas Simples 📐**
**Descrição**: Solicite dois números e depois realize uma operação simples entre eles.

**Exemplo de código**:

```python
# Solicitar dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Realizar operação (exemplo: soma)
resultado = numero1 + numero2

# Exibir resultado
print("Resultado da soma:", resultado)
```

Aqui, o Copilot pode sugerir operadores matemáticos para realizar a operação entre os dois números, como soma, subtração, multiplicação ou divisão.

---

### 4. **Verificando Números Pares e Ímpares 🧮**
**Descrição**: Receba um número inteiro e verifique se ele é par ou ímpar.

**Exemplo de código**:

```python
# Solicitar um número
numero = int(input("Digite um número inteiro: "))

# Verificar se o número é par ou ímpar
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
```

O Copilot pode sugerir o uso do operador módulo (`%`) para verificar se o número é divisível por 2, determinando se é par ou ímpar.

---

### 5. **Calculando Média de Notas 📚**
**Descrição**: Calcule a média de três notas fornecidas.

**Exemplo de código**:

```python
# Solicitar as três notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcular a média
media = (nota1 + nota2 + nota3) / 3

# Exibir o resultado
print("A média das notas é:", media)
```

O Copilot pode sugerir o uso de variáveis para armazenar as notas e a aplicação do operador aritmético de soma e divisão para calcular a média.

---

### 6. **Verificando Palíndromos 🔄**
**Descrição**: Teste se uma palavra é um palíndromo (lê-se da mesma forma de trás para frente).

**Exemplo de código**:

```python
# Solicitar a palavra
palavra = input("Digite uma palavra: ")

# Verificar se a palavra é um palíndromo
if palavra == palavra[::-1]:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")
```

Aqui, o Copilot pode sugerir o uso de slicing (`[::-1]`) para inverter a string e compará-la com a original.
