try: 
    from add import AddOperation 
except:
    from .add import AddOperation 
from faker import Faker

faker = Faker()
    
# Teste unitário
def test_some():
    n1 = faker.random_number()
    n2 = faker.random_number()
    addOperation = AddOperation()
    resultado = addOperation.soma(n1, n2)
    expect = n1 + n2
    
    print(expect)
    print(resultado)
    
    assert resultado == expect
    