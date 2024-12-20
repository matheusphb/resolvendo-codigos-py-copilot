
# este se uma palavra é um palíndromo (lê-se da mesma forma de trás para frente).

def eh_palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")
    return palavra == palavra[::-1]

# Teste da função
palavras = ["arara", "radar", "python", "A man a plan a canal Panama"]
for palavra in palavras:
    if eh_palindromo(palavra):
        print(f'"{palavra}" é um palíndromo.')
    else:
        print(f'"{palavra}" não é um palíndromo.')