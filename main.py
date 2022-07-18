import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
import re
import time
import os


# ===============>> CONEXÃO <<===============

config = {
  'user': 'u526069146_resoluteIT',
  'password': '3f:1wsIL^c',
  'host': 'sql532.main-hosting.eu',
  'database': 'u526069146_pResoluteIT',
  'raise_on_warnings': True
}

conn = mysql.connector.connect(**config)

# ===============>> VARIAVEIS G <<===============


Data = datetime.now().strftime('%d-%m-%Y')
Hora = datetime.now().strftime('%H:%M:%S')

cVermelho = "\033[1;31m"
cAmarelo = '\033[1;33m'
cVerde = '\033[1;32m'
cAzul = '\033[1;34m'
ResetF = "\033[0;0m"

fAzulC = '\033[1;104m'

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# ===============>> INICIO <<===============

if conn:
	print("Banco de dados "+cVerde+"CONECTADO")
	cursor = conn.cursor()
else:
	print("Banco de dados "+cVermelho+"NÃO CONECTADO")
	conn.close()

# =====>> MENU INICIAL <<=====
def MenuI():
	cls()
	print(cAzul+"\n=========="+cVermelho+" MENU "+cAzul+"=========="+ResetF)
	print("O que deseja fazer?")
	print("1 = Entrar")
	print("2 = Registrar")
	print("3 = Sair")
	print(cAzul+"=========================="+ResetF)
	resposta = input("\nO que deseja fazer: ")
	
	if resposta == "1":
		Login()
	elif resposta == "2" :
		Registrar_Conta()
	elif resposta == "3" :
		exit()
		
	else : 
		print("Valor inválido")
	Menu()









# =====>> LOGIN <<=====
def Login():
	cls()
	print(cVerde+"\nBEM VINDO AO SYSTEMA DE PONTOS"+ResetF)

	# USUÁRIO
	while True:
		Usuario = input(cVermelho+"USUÁRIO:"+ResetF+" ")
		Quant = len(Usuario)
		if(Quant >= 3):
			break
		else:
			print("\nO numero de digitos deve ser maior ou igual a " +cVermelho+"3"+ResetF+"!\n") 
	
	# SENHA
	while True:
		Senha = input(cVermelho+"SENHA:"+ResetF+" ")
		Quant = len(Senha)
		if(Quant >= 3):
			break
		else:
			print("\nO numero de digitos deve ser maior ou igual a " +cVermelho+"3"+ResetF+"!\n") 
	
	
	cursor = conn.cursor()

	taskL = (Usuario, Senha)
	testel = ("SELECT * FROM Admins WHERE Usuario=%s and Senha=%s")
	cursor.execute(testel, taskL)
	#cursor.execute("SELECT * FROM Admins WHERE Usuario=? and Senha=?", (Usuario,Senha,))
	resultado = cursor.fetchall()
	time.sleep(1)

	if resultado:
		for i in resultado:	
			print(cAzul+"\n\n=========================="+ResetF)
			print("Seja Bem vindo "+cVermelho+ i[4] +ResetF)
			print(cAzul+"==========================\n"+ResetF)
			time.sleep(2)
			Menu()
			#break
	else:
		print("Usuário/Senha invalida!")
		a = input('Deseja tentar novamente?['+cVerde+'S'+ResetF+'/'+cVermelho+'N'+ResetF+'] ').lower()
		if a == 's':
			Login()
		else:
			print(cVerde+"Carregando...")
			time.sleep(1)
			MenuI()
	return resultado






def Registrar_Conta():
	cls()
	# USUÁRIO
	while True:
		UsuarioR = input(cVerde+"USUÁRIO:"+ResetF+" ")
		Quant = len(UsuarioR)
		if(Quant >= 3):
			break
		else:
			print("\nO numero de digitos deve ser maior ou igual a " +cVermelho+"3"+ResetF+"!\n") 
      
	# SENHA
	while True:
		SenhaR = input(cVerde+"SENHA:"+ResetF+" ")
		Quant = len(SenhaR)
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


	# NOME
	while True:
		NomeR = input(cVerde+"Nome:"+ResetF+" ")
		Quant = len(NomeR)
		if NomeR.isnumeric():
			print('\nFormato errado '+cVermelho+'(Somente Letras)\n'+ResetF)
		else:
			if(Quant >= 3):
				break
			else:
				print("\nO numero de digitos deve ser maior ou igual a " +cVermelho+"3"+ResetF+"!\n") 


	taskR = (UsuarioR, SenhaR, N_Cracha, NomeR)
	sql = "INSERT INTO Admins(Usuario, Senha, N_Crachá, Nome) VALUES (%s,%s,%s,%s)"

	cursor.execute(sql, taskR)
	conn.commit()
	#return cursor.lastrowid
	
	a = input('Deseja cadastrar outro usuário??['+cVerde+'S'+ResetF+'/'+cVermelho+'N'+ResetF+'] ').lower()
	if a == 's':
		Registrar_Conta()
	else:
		MenuI()




# =====>> MENU <<=====
def Menu():
	cls()
	#print("Bem vindo "+cVerde+" %s, O que deseja fazer? " % i[4])
	print(cAzul+"\n=========="+cVermelho+" MENU "+cAzul+"=========="+ResetF)
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
	cls()
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

	task = Nome, N_Cracha, CPF, email, Fone, Cidade, Atendente
	sql = ''' INSERT INTO Funcionarios(Nome, N_Crachá, CPF, Email, Fone, Cidade, Atendente)
              VALUES(?,?,?,?,?,?,?) '''

	cursor.execute(sql, task)
	conn.commit()
	return cursor.lastrowid

	print(cVermelho + '\nCadastro realizado com sucesso!\n\n\n'+ ResetF)
	
	if __name__ == '__main__':
		Menu()




# =====>> CONSULTAR FUNCIONARIO <<=====
def Consultar_Func():
	cls()
	print('\nIremos pedir algumas informações!\n')

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
	
	cursor = conn.cursor()

	taskC = (N_Cracha,)
	testel = ("SELECT * FROM Funcionarios WHERE N_Crachá=%s")
	cursor.execute(testel, taskC)
	rows = cursor.fetchall()

	try:
			for row in rows:
				print(row)
	except mysql.connector.Error as err:
			print(err)
	

# =====>> PONTO ENTRADA FUNCIONARIO <<=====
def Ponto_Entrada():

  	print("Teste3")

# =====>> PONTO SAIDA FUNCIONARIO <<=====
def Ponto_Saida():

 	print("Teste4")



MenuI()