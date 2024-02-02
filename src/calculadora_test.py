try:
    from .calculadora import Calculadora
    from .operations.add import AddOperation
    from .operations.sub import SubOperations
    from .operations.test.add import AddOperationSpy
    from .operations.test.sub import SubOperationSpy
except:
    from calculadora import Calculadora
from faker import Faker
from faker import Faker

faker = Faker()

def test_add_unitario():
    addOperation = AddOperationSpy()
    subOperations = SubOperationSpy()
    calculadora = Calculadora(addOperation, subOperations)
    
    faker = Faker()
    n1 = faker.random_number()
    n2 = faker.random_number()
    
    resultado = calculadora.add(n1, n2, True)

    # Teste de entrada  
    assert addOperation.soma_atributes['n1'] == n1
    assert addOperation.soma_atributes['n2'] == n2
    # Teste de saida
    assert resultado is not None
    
    print(resultado)

def test_add_integracao():
    calculadora = Calculadora(AddOperation(), SubOperations())
    n1 = faker.random_number()    
    n2 = faker.random_number()    
    resultado = calculadora.add(n1, n2, True)
    expect = n1 + n2 
    print(resultado)
    print(expect)
    assert resultado == expect
    