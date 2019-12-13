salario = int(input('Entrar com salário '))
inss = salario*9/100
vale_transporte = salario*3/100
plano_de_saude = 347*15/100
print('salário bruto ', salario)
print('salário descontado do INSS ', salario-inss)
print('salário descontado do vale transporte ', salario-vale_transporte)
print('salário descontado do plano de saúde ', salario-plano_de_saude)
print('salário líquido ', salario-inss-vale_transporte-plano_de_saude)
sim = input('Quer continuar a rodar o projeto [s/n]')
while sim == 's':
  salario = int(input('Entrar com salário '))
  inss = salario * 9 / 100
  vale_transporte = salario * 3 / 100
  plano_de_saude = 347 * 15 / 100
  print('salário bruto ', salario)
  print('salário descontado do INSS ', salario - inss)
  print('salário descontado do vale transporte ', salario - vale_transporte)
  print('salário descontado do plano de saúde ', salario - plano_de_saude)
  print('salário líquido ', salario - inss - vale_transporte - plano_de_saude)
  sim = input('Quer continuar a rodar o projeto [s/n]')
print('Tchau')

