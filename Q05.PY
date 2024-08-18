nome = input('Digite o seu nome: ')
disciplina = input('Digite a disciplina: ')
nota = float(input('Digite sua nota: '))
status = ' '
if nota >=0 and nota <=5.4 :
    status = 'reprovado'
    print(f'{nome} está {status} em {disciplina} com nota {nota}')
elif nota >=5.5 and nota <=10 :
    status = 'aprovado'
    print(f'{nome}, está {status} em {disciplina} com nota {nota}')
else :
    print('nota inválida, tente novamente') 