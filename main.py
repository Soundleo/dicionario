# inclusão de dados no dicionário
dicionario = {
    'nome': input('informe o seu nome: '),
    'CPF': input ('inforne o seu CPF: '),
    'RG': input('inforne o seu RG: '),
    'Data de nascimento': input('inforne a sua data de nascimento '),
    'Gênero': input('inforne o seu gênero: '),
    'E-mail': input('inforne o seu E-mail: '),
    'Telefone': input('inforne o seu telefone: '),
    'Tipo sanguineo': input('inforne o seu tipo sanguineo: '),
    'Profissão': input('inforne a sua profissão: '),
    'Empresa': input('inforne qual empresa que trabalha: '),
}

for i in dicionario:
    print(f'{i}:{dicionario.get(i)}')
