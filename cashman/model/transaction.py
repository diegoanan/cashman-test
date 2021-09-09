#basicamente lo que hace esta parte de la funcion es preparar los elementos para su adicion al arreglo que se almacenara a la DB

import datetime as dt #importacion de datetime creando el objeto dt
from marshmallow import Schema, fields #importacion de schema y fields de marshmallow


class Transaction(): #creacion de la clase Transaction
  def __init__(self, description, amount, type): #funcion dentrode la clase 
    self.description = description #variable que se llama a si misma
    self.amount = amount
    self.created_at = dt.datetime.now() #variable igualada con el tiempo consultado
    self.type = type 

  def __repr__(self): #funcion de la clase
    return '<Transaction(name={self.description!r})>'.format(self=self) #retorna una cadena con la infomacion


class TransactionSchema(Schema): #creacion de clase que recibe parametros tipo Schema
  #uso de metodos fiels para casting de tipo de dato y evitar incongruencias
  description = fields.Str() 
  amount = fields.Number()
  created_at = fields.Date()
  type = fields.Str()
