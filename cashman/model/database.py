#este archivo establece la conexion con mongodb mediante el uso de la dependencia pymongo 
#y usando la dependencia os, se usan las variables de entorno para obtener los parametros necesarios para la conexion
import pymongo
import os

#en esta clase se define la conexion con la base de datos
class Database:
	@classmethod
    #metodo de inicializacion de la conexion
	def initialize(cls):
		#se hace uso de las veriables de entorno para establecer la conexion con la bse de datos
		#se almacena la cadena en una variable y posteriormente esta se pasa por la funcion de pymongo
		conn = os.environ['MONGODB_HOSTNAME']+"://"+os.environ['MONGODB_USERNAME']+":"+os.environ['MONGODB_PASSWORD']+"@localhost:27017/"+os.environ['MONGODB_DATABASE']
		client = pymongo.MongoClient(conn)
		#client = pymongo.MongoClient("mongodb://diego:abc123@localhost:27017/cashman")
		cls.database = client.get_default_database()
		#print para saber si se creo la conexion
		print(client.PORT)
	#metodo para almacenar elementos	
	@classmethod
	def save_to_db(cls, data):
		cls.database.stores.insert_one(data)
		
    #metodo para leer los elementos
	@classmethod
	def load_from_db(cls, query):
		return cls.database.stores.find(query)