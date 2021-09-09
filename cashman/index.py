import os
from cashman.model.transaction import Transaction, TransactionSchema
from flask import Flask, jsonify, request #inclucion de elementos de flask

from cashman.model.database import Database
from cashman.model.expense import Expense, ExpenseSchema
from cashman.model.income import Income, IncomeSchema
from cashman.model.transaction_type import TransactionType #importacion de dependencias creadas y uso de sus clases

app = Flask(__name__) #declaracion de objeto de flask

#establecimiento de la conexion usando la funcion
Database.initialize()

#funcion que da mensaje en caso de funcionar correnctamente el programa
@app.route('/')
def index():
    return jsonify(
        status=True,
        message='Bienvenido a la app de dockerizacion de flask-mongoDB!'
    )

transactions = []
#	Income('Salary', 5000),
#  	Income('Dividends', 200),
#  	Expense('pizza', 50),
#  	Expense('Rock Concert', 100)
#] #arreglo inicializado, esta variable es la que se modificara


@app.route('/incomes')#ruta de incomes
def get_incomes():#funcion para la obtencion de datos
  schema = IncomeSchema(many=True)
  incomes = schema.dump(
    filter(lambda t: t.type == TransactionType.INCOME, transactions)#filtrado de los datos
  )
  #print(jsonify(incomes.data))
  #loades_objet= Database.load_from_db(incomes.data)#esto nos obtendra los datos de la base de datos y los inicializara en una variable
  #print(loades_objet)
  return jsonify(incomes.data)

@app.route('/incomes',methods=['POST']) # ruta del archivo con parametros adicionales
def add_income(): #creacion del metodo add_income
	income = IncomeSchema().load(request.get_json()) #objeto de IncomeSchema
	Database.save_to_db({income.data})#se pasa el arreglo a la base de datos
	transactions.append(income.data) #adicion a la cadena
	
	return 'save',201 #retorna mensaje guardado

#se continua usando la variable transactions para el filtrado de la informacion

@app.route('/expenses') #ruta de la expences
def get_expenses(): #metodo get_expenses
	schema = ExpenseSchema(many=True) #objeto de ExpenseSchema que recibe a su vez un parametro
	expenses = schema.dump(
	  filter(lambda t: t.type == TransactionType.EXPENSE, transactions) #filtro de datos  
	) 
	loades_objects = Database.load_from_db({expenses.data})
	print(loades_objects)#imprecion de los datos que se obtienen a traves de load_from_db
	return jsonify(loades_objects) #retorno de una cadena codificada a json


@app.route('/expenses', methods=['POST']) #ruta de expenses
def add_expense(): #metodo add_expense
	expense = ExpenseSchema().load(request.get_json())
	Database.save_to_db(expense.data)#alamcenamiento de la cadena en la DB
	transactions.append({expense.data})#adicion de cadena al arreglo
	return 'saved', 201 #retorna mensaje de guardado

if __name__ == "__main__": #solo se ejecuta en consola
	#uso de variables de entorno para el puerto y el modo del debug
	ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
	ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
	app.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG) #metodo ejecutor con salida por ip publica o local host y puerto 5000

#***************************
#el codigo de Securing Python APIs with Auth0 no se incluyo
#debido a que s genero problema con la dependecia, sin embargo su fucion basica
#era el generar tokens de autenticacion para incrementar la seguridad de los accesos