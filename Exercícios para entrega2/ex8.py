#Faça um algoritmo que leia a sigla de um dos estados do Brasil e informe a qual região ele pertence.

est=str(input("Entre com a sigla do seu estado: "))

if est.lower() in ("ac", "al", "ap", "am", "ba", "ce", "df", "es", "go", "ma", "mt", "ms", "mg", "pa","pb", "pb", "pi", "rj", "rn", "rs", "ro", "rr", "sc", "sp", "se", "to"):
    if est in ("ac", "ap", "am", "pa", "ro", "rr", "to"): #"lower()" ignora letras maiúsculas / "in" torna verdade somente os termos pré programados

        reg="Norte"
        
        if (est=="ac"):
            est="Acre"
        elif (est=="ap"):
            est="Amapá"
        elif (est=="am"):
            est="Amazonas"
        elif (est=="pa"):
            est="Pará"
        elif (est=="ro"):
            est="Rondônia"
        elif (est=="rr"):
            est="Roraima"
        else:
            est="Tocantins"
    elif est in ("ba", "ce", "ma", "pb", "pe", "pi", "rn", "se"):
           
        reg="Nordeste"

        if (est=="ba"):
            est="Bahia"
        elif (est=="ce"):
            est="Ceará"
        elif (est=="ma"):
            est="Maranhão"
        elif (est=="pb"):
            est="Paraíba"
        elif (est=="pe"):
            est="Pernambuco"
        elif (est=="pi"):
            est="Piauí"
        elif (est=="rn"):
            est="Rio Grande do Norte"
        else:
            est="Sergipe"
    
    elif est in ("df", "go", "ms", "mt"):

        reg= "Centro Oeste" 
        
        if (est=="df"):
            est="Distrito Federal"
        elif (est=="go"):
            est="Goiás"
        elif (est=="ms"):
            est="Mato Grosso do Sul"
        else:
            est="Mato Grosso"

    elif est in ("es", "mg", "rj", "sp"):
        
        reg= "Sudeste"

        if (est=="es"):
            est="Espírito Santo"
        elif (est=="mg"):  
            est= "Minas Gerais"
        elif (est=="rj"):
            est= "Rio de Janeiro"
        else:
            est="São Paulo"

    else:
         
        reg="Sul"
        if (est=="pr"):
            est="Paraná"
        elif (est=="rs"):
            est="Rio Grande do Sul"
        else:
            est="Santa Catarina"
    print("Olá, seu estado é {est} e sua região é {reg}")
else:
    print("Estado incorreto")