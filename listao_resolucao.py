#exerc10
nome = input("Insira seu nome: ")
cidade = input("Insira a cidade onde nasceu: ")
ano_nasc = input("Insira o ano que nasceu: ")
print(nome+'\n'+cidade+'\n'+ano_nasc)
x = int(ano_nasc)
idade = 2030 - x
print("Em 2030 você terá {} anos.".format(idade))

#exerc 11
lado = input("Informe o tamanho do lado: ")
x = float(lado)
area = x**2
print("A área é de {} unidades de medida²".format(area))

#exerc 12
b = input("Informe o tamanho da base: ")
h = input("Informe o tamanho da altura: ")
x = float(b)
y = float(h)
area = (x*y)/2

#exerc 16
valor_emprestimo = input("Informe o valor emprestado: ")
taxa = input("Informe quantos porcento será a taxa (somente número): ")
tempo = input("Informe em quantos meses o empréstimos será pago: ")
x = float(valor_emprestimo)
y = float(taxa)
z = int(tempo)
w = y/100
valor_final = x + (x * w * z)
print(valor_final)
