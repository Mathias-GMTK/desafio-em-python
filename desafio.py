import string

def calculador_senha(senha):
    numero_caracteres = len(senha)
    maiusculas = sum (1 for c in senha if c.isupper())
    minusculas = sum(1 for c in senha if c.islower())
    numeros = sum(1 for c in senha if c.isdigit())
    simbolos = sum(1 for c in senha if c in string.punctuation)
    meio = sum(1 for c in senha [1:-1] if c.isdigit() or c in string.punctuation)


    pontuacao = (numero_caracteres * 4) + ((numero_caracteres - maiusculas) * 2) + \
                ((numero_caracteres - minusculas) * 2) + (numeros * 4) + \
                (simbolos * 6) + (meio * 2)
    
    regras = sum([
        numero_caracteres >=8,
        maiusculas > 0,
        minusculas > 0,
        numeros > 0,
        simbolos > 0
    ])
    
    pontuacao += (regras * 2)

    if senha.isalpha():
        pontuacao -= numero_caracteres
    if senha.isdigit():
        pontuacao -= numeros

    repetidos = sum(senha.lower().count(c) - 1 for c in set(senha.lower()) if senha.lower().count(c) > 1)
    pontuacao -= repetidos

    repeticao_maiusculas = sum(1 for i in range (1, numero_caracteres)if senha [i].isupper() and senha [i - 1 ].isupper())
    repeticao_minusculas = sum(1 for i in range (1, numero_caracteres) if senha [i].islower() and senha [i - 1].islower())
    repeticao_numeros = sum(1 for i in range(1, numero_caracteres) if senha [i].isdigit() and senha [i - 1].isdigit())
    pontuacao -=(repeticao_maiusculas * 2 + repeticao_minusculas * 2 + repeticao_numeros * 2)

    def sequencia(caracteres):
        contador = 0
        for i in range (len(caracteres) - 2):
            if caracteres[i] + 1 == caracteres[i + 1] and caracteres[i + 1] + 1 == caracteres[i + 2]:
                contador += 1
            return contador
            
    repeticao_maiusculas = sequencia([ord(c.lower()) for c in senha if c.isalpha()])
    repeticao_minusculas = sum(1 for i in range(1, numero_caracteres) if senha[i].islower() and senha[i - 1].islower())
    repeticao_numeros = sequencia([int(c) for c in senha if c.isdigit()])
    pontuacao -= (repeticao_maiusculas * 2 + repeticao_minusculas * 2 + repeticao_numeros * 2)
    
    if pontuacao < 20:
        classificacao = "Muito fraca"
    elif pontuacao < 40:
        classificacao = "Fraca"
    elif pontuacao < 60:
        classificacao = "Boa"
    elif pontuacao < 80:
        classificacao = "Forte"
    else:
        classificacao = "Muito Forte"

    return pontuacao, classificacao
    
senha = input("Digite sua senha para a validação:")
pontuacao, classificacao = calculador_senha(senha)
print(f"Sua senha tem uma pontuação de {pontuacao}. classificação:{classificacao}")

