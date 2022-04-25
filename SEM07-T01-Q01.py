dia = int(input())
mes = int(input())
ano = int(input())

dia_nas = int(input())
mes_nas = int(input())
ano_nas = int(input())
idade = ano - ano_nas


if ano_nas <= ano and mes_nas <= mes and dia_nas <= dia:
    idade = ano - ano_nas
    print(idade)
else:
    print(idade - 1)


