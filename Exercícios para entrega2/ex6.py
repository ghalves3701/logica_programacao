#Faça um Programa que verifique se uma letra digitada é vogal ou consoante. Utilize “in” na construção da condicional. Se o caractere digitado não for uma letra de A a Z, escreva: ‘Letra inválida!
letra=str(input("Entre com a letra: "))

if letra in ("a","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y" "z"):
    if letra in ("a", "e", "i", "o", "u"):
        print(f" A Letra ''{letra}'' é uma vogal")
    else:
        print(f" A Letra ''{letra}'' é uma consoante")
else:
    print(f" A Letra ''{letra}'' é uma letra inválida")        