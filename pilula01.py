def validarSenha(s):
    if len(s) < 8:
        return "Senha inválida, muito curta."
    temNumero = False
    temMaisucula = False
    simbolos = "!@#$%¨&*()_+=-"
    temSimbolo = False

    for c in s:
        if c == " ":
            return "Senha inválida, não pode ter espaços"
        if c >= "0" and c <= "9":
            temNumero = True
        if c >= "A" and c <= "Z":
            temMaiuscula = True
        if c in simbolos: 
            temSimbolo = True

    if not temNumero:
            return "Senha inválida, precisa de um numero pelo menos."

    if not temMaiuscula:
            return "Senha inválida, precisa de uma letra maiúscula pelo menos."

    if not temSimbolo:
            return "Senha inválida, precisa de um simbolo pelo menos."

    return "Senha Válida"

#main (programa principal)
senha = input("Digite a senha: ")
r = validarSenha(senha)
print (r)