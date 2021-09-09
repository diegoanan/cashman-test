from marshmallow import post_load

from .transaction import Transaction, TransactionSchema #uso de  los metodos de la clase transaction
from .transaction_type import TransactionType


class Income(Transaction): #clase Income que recibe un objeto tipo Transaction
  def __init__(self, description, amount): #funcion que se llama a si mismo
    super(Income, self).__init__(description, amount, TransactionType.INCOME)

  def __repr__(self): #funcion que devolvera los valores
    return '<Income(name={self.description!r})>'.format(self=self) #retorno de cadena con la infomacion


class IncomeSchema(TransactionSchema): #clase que recibe un objeto de tipo TransactionSchema

  @post_load #metodo para deserializar datos de una direccion recibida
  def make_income(self, data): #funcion make_income que se llama a si misma y recibe un objeto tipo data
    return Income(**data) #retorna la informacion del arreglo data
