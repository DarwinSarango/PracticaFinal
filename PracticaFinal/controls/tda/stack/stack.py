from controls.tda.stack.stackOperation import StackOperation

#Encuapsulamos para que no se vean esos metodos que no pertenecen a stack, PATRON DE DEISEÑO FACADE
class Stack():
    def __init__(self, tope):
        self.__stack = StackOperation(tope)

    def push(self, data):
        self.__stack.push(data)
     
    @property
    def pop(self):
        return self.__stack.pop
    
    @property
    def print(self):
        self.__stack.print

    def verifyTope(self):
        self.__stack.verifyTope

    