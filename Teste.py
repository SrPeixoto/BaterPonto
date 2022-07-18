import sqlite3
from sqlite3 import Error
from datetime import datetime
import re


# ===============>> CONEXÃO <<===============
conn = sqlite3.connect('Funcionarios.db')
cursor = conn.cursor()


# ===============>> VARIAVEIS G <<===============


Data = datetime.now().strftime('%d-%m-%Y')
Hora = datetime.now().strftime('%H:%M:%S')

cVermelho = "\033[1;31m"
cAmarelo = '\033[1;33m'
cVerde = '\033[1;32m'
cAzul = '\033[1;34m'
ResetF = "\033[0;0m"






# ===============>> INICIO <<===============

# =====>> MENU <<=====
def Menu():
  print(cAzul+"\n=========="+cVermelho+" MENU "+cAzul+"=========="+ResetF)
  print("O que deseja fazer? ")
  print("1 = Cadastrar Funcionario")
  print("2 = Consultar Funcionario")
  print("3 = Bater Ponto Entrada")
  print("4 = Bater Ponto Saída")
  print("5 = Fechar")
  print(cAzul+"=========================="+ResetF)
  resposta = input("\nO que deseja fazer: ")
  
  if resposta == "1":
    Cadastrar_Func()
  elif resposta == "2" :
    Consultar_Func()
  elif resposta == "3" :
    Ponto_Entrada()
  elif resposta == "4" :
    Ponto_Saida()
  elif resposta == "5" :
    exit()
  else : 
    print("Valor inválido")
  Menu()



# =====>> CADASTRAR FUNCIONARIO <<=====

def Cadastrar_Func():
  print('\nIremos pedir algumas informações!\n')
  
# NOME
  while True:
    Nome = input("Nome: ")
    Quant = len(Nome)
    if Nome.isnumeric():
      print('\nFormato errado '+cVermelho+'(Somente Letras)\n'+ResetF)
    else:
      if(Quant >= 3):
        break
      else:
        print("\nO numero de digitos deve ser maior ou igual a " +cVermelho+"3"+ResetF+"!\n") 
      

# NÚMERO DO CRACHÁ  
  while True:
    N_Cracha = input("Número do Crachá "+cVermelho+"(Somente Números)"+ResetF+": ")
    Quant = len(N_Cracha)
    if N_Cracha.isnumeric():
      if(Quant > 0):
        break
      else:
        print("\nO numero de digitos deve ser maior que " +cVermelho+"0"+ResetF+"!\n") 
    else:
      print('\nFormato errado '+cVermelho+'(Somente Numeros)\n'+ResetF)

# CPF
  while True:
    CPF = input("CPF "+cVermelho+"(Somente Números)"+ResetF+": ")
    Quant = len(CPF)
    if CPF.isnumeric():
      #if(Quant == 11):
      if (10 < Quant < 12):
        break
      else:
        print("\nO numero de digitos deve ser igual a " +cVermelho+"11"+ResetF+"!\n") 
    else:
      print('\nFormato errado '+cVermelho+'(Somente Numeros)\n'+ResetF)

# E-MAIL
  while True:
    email = input("E-mail: ").lower()
    proc = re.search(".com", email)
    if(proc):
      break 
      #print('\nTudo certo!\n')
    else:
      print('\nFormato de E-mail '+cVermelho+'ERRADO!\n'+ResetF)

# TELEFONE
  while True:
    Fone = input("Numero de Telefone: ")
    Quant = len(Fone)
    if Fone.isnumeric():
      if(Quant >= 8):
        break
      else:
        print("\nNumero errado. Exemplo: " +cVermelho+"22223333"+ResetF+"!\n") 
    else:
      print('\nFormato errado '+cVermelho+'(Somente Números)\n'+ResetF)

# CIDADE
  while True:
    Cidade = input("Cidade: ")
    Quant = len(Cidade)
    if Cidade.isnumeric():
      print('\nFormato errado '+cVermelho+'(Somente Letras)\n'+ResetF)
    else:
      if(Quant >= 3):
        break
      else:
        print("\nO numero de digitos deve ser maior ou igual a " +cVermelho+"3"+ResetF+"!\n") 

  Atendente = input("Atendente: ")

# PRINTs
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  print(cAzul + "Nome:" + ResetF + " %s" % Nome)
  print(cAzul + "Cracha:" + ResetF + " %s" % N_Cracha)
  print(cAzul + "CPF:" + ResetF + " %s" % CPF)
  print(cAzul + "Email:" + ResetF + " %s" % email)
  print(cAzul + "Telefone:" + ResetF + " %s" % Fone)
  print(cAzul + "Cidade:" + ResetF + " %s" % Cidade)

 # Sql = "INSERT INTO Funcionarios (Nome, N_Cracha, CPF, Email, Fone, Cidade) VALUES ('"+Nome+"', '"+N_Cracha+"', '"+CPF+"', '"+email+"', '"+Fone+"', '"+Cidade+"')"

  Sql = " INSERT INTO Funcionarios(Nome, N_Cracha, CPF, Email, Fone, Cidade) VALUES(?,?,?,?,?,?)", (Nome, N_Cracha, CPF, email, Fone, Cidade,)

  cursor.execute(Sql)
  conn.commit()

  print(cVermelho + '\nCadastro realizado com sucesso!\n\n\n'+ ResetF)

# REALIZAR OUTRO CADASTRO
  a = input('Deseja realizar outro?['+cVerde+'S'+ResetF+'/'+cVermelho+'N'+ResetF+'] ').lower()
  if a == 's':
    Cadastrar_Func()
  else:
    Menu()




# =====>> CONSULTAR FUNCIONARIO <<=====
def Consultar_Func():
  while True:
    N_Cracha = input("Número do Crachá "+cVermelho+"(Somente Números)"+ResetF+": ")
    Quant = len(N_Cracha)
    if N_Cracha.isnumeric():
      if(Quant > 1):
        break
      else:
        print("\nO numero de digitos deve ser maior ou igual a " +cVermelho+"1"+ResetF+"!\n") 
    else:
      print('\nFormato errado '+cVermelho+'(Somente Numeros)\n'+ResetF)
  
  #Sql = "SELECT * FROM Funcionarios WHERE (N_Cracha) VALUES ('"+N_Cracha+"')"
  Sql = "SELECT * FROM Funcionarios WHERE N_Cracha=?", (N_Cracha,)

  cursor.execute(Sql)

  rows = cursor.fetchall()

  for row in rows:
    print(row)

# =====>> PONTO ENTRADA FUNCIONARIO <<=====
def Ponto_Entrada():
  print("Teste3")

# =====>> PONTO SAIDA FUNCIONARIO <<=====
def Ponto_Saida():
  print("Teste4")

Menu()