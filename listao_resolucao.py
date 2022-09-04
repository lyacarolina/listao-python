#exerc 10

nome = input("Insira seu nome: ")
cidade = input("Insira a cidade onde nasceu: ")
ano_nasc = input("Insira o ano que nasceu: ")
print(nome+'\n'+cidade+'\n'+ano_nasc)
x = int(ano_nasc)
idade = 2030 - x
print("Em 2030 você terá {} anos.".format(idade))
