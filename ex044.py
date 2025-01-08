produto = float(input('valor da compra: '))
print("""essas são as opsções de pagamento 
---------------------------------------------------------
opção 1º dinheiro/cheque a vista (ganha 10% de desconto)
---------------------------------------------------------
opção 2º cartão a vista (ganha 5 % de desconto)
---------------------------------------------------------
opção 3º cartão em 2x (preço normal)
---------------------------------------------------------
opção 4º cartão em 3x (juros de 20%)
---------------------------------------------------------""")
pag = int(input('Escola umas das opções digitando seu numero correspondente: '))
if pag == 1 :
    print('O valor a ser pago é ${} '.format(produto - produto * 0.10))
elif pag == 2 :
    print('o valor a ser pago é ${} '.format(produto - produto * 0.05))
elif pag == 3 :
    print('o valor a ser pago é ${} '.format(produto))
elif pag == 4 :
    print('O valor a ser pago é ${} '.format(produto + produto * 0.20))
else :
    print('Essa opção de pagamento não existe')