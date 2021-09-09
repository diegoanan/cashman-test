from marshmallow import post_load #metodo deseralizador post_load de marshmallow

from .transaction import Transaction, TransactionSchema #uso de metodos de transaction
from .transaction_type import TransactionType


class Expense(Transaction): #clase que resive un objeto tipo Transaction
  def __init__(self, description, amount): #funcion que se llama a si misma
    super(Expense, self).__init__(description, -abs(amount), TransactionType.EXPENSE)

  def __repr__(self): #funcion para retornar los datos
    return '<Expense(name={self.description!r})>'.format(self=self)


class ExpenseSchema(TransactionSchema): #clase que resive objetos tipo TransactionSchema
  
  @post_load#metodo deserializador de datos recibidos de alguna direccion  
  def make_expense(self, data):
    return Expense(**data) #retorno de una cadena bidimencional
