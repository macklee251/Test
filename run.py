from src.calculadora import Calculadora
from src.operations.add import AddOperation
from src.operations.sub import SubOperations

calculadora = Calculadora(AddOperation(), SubOperations())

op1 = calculadora.add(2, 5, True)
op2 = calculadora.sub(5, 3, True)

print(op1) 
print(op2)