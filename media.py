def calcular_media(n1, n2, n3, n4):
    return (n1 + n2 + n3 + n4) / 4


def classificar_media(media):
    if media >= 7:
        return "Aprovado(a) ✅"
    elif media >= 5:
        return "Recuperação ⚠️"
    else:
        return "Reprovado(a) ❌"
    
nome = input("Digite o nome do aluno: ") 


nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
nota3 = float(input("Digite a 3ª nota: "))
nota4 = float(input("Digite a 4ª nota: "))


media = calcular_media(nota1, nota2, nota3, nota4)
situacao = classificar_media(media)


print(f"\nAluno: {nome}")
print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")