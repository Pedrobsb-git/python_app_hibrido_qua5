# entrada de dados
aluno = input("Informe o nome do aluno: ").strip().title()
nota = float (input("Informe a nota: ").strip().replace(",","."))

# verifica a nota do aluno
if nota >= 0 and nota <= 10:
    if nota >= 7:
        print(f"{aluno} está Aprovado.")
    elif nota >= 5:
        print(f"{aluno} está de Recuperação.")
    else:
        print(f"{aluno} esta Reprovado.")

else:
    print(f"Nota do {aluno} inválida.")