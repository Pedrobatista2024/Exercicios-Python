print('Ola já que voce vai devolver o carro, preciso de algumas informações')
km = float(input('quantos km foram rodados? '))
dias = int(input('quantos dias o carro ficou locado? '))
preço = (km * 0.15) + (dias * 60)
print('o preço a pagar é {:.2F}$ '.format(preço))
