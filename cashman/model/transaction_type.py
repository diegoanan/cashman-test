from enum import Enum #uso del metodo Enum de la dependencia enum


class TransactionType(Enum): #clase TransactionType que recibe un objeto de tipo Enum
  INCOME = "INCOME" #variable tipo string inicializado
  EXPENSE = "EXPENSE"
