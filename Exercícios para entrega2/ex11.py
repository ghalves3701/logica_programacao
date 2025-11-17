#Faça um algoritmo que receba os seguintes dados de um determinado aluno: Nome do aluno; Nome da disciplina; Valor da nota de Avaliação Contínua (AC); Valor da nota de Avaliação Final (AF); Nota de atividades (AT)
#Regras para gerar o status do aluno: Média de 0 a 3.9: “Reprovado!”|4 a 5.9: “Exame!” | acima de 5.9: “Aprovado!”
#Calcule a média e escreva uma mensagem conforme os modelos abaixo:
#O aluno Claudemir obteve a média 7 na Disciplina Algoritmos e seu status é: Aprovado!
#O aluno Túlio obteve a média 4,5 na Disciplina Algoritmos e seu status é: Exame!

aluno=str(input("Ente com o nome do aluno: "))
disciplina=str(input("Entre com a disciplina: "))
nota_ac=float(input("Entre com a Nota de Avaliação Contínua: "))

if 0 <= nota_ac <=10:
    nota_af=float(input("Entre com a nota de Avaliação Final: "))
    if 0 <= nota_af <=10:
        nota_at=float(input("Entre com a nota de Atividades: "))
        if 0 <= nota_at <=10:
            media= (nota_ac + nota_at + nota_af)/3
            if 0 <=media <= 3.9 :
                status="Reprovado"
            elif 4 <= media <= 5.9:
                status="Exame"
            else:
                status= "Aprovado"
            print(f'O aluno {aluno} obteve a média {media} na Disciplina Algoritmos e seu status é: {status}!')    
        else:
            print("Nota inválida")
    else:
        print("Nota Inválida")
else:
    print("Nota Inválida")        


