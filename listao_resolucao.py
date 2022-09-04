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
