from faker import Faker
faker = Faker()

class AddOperationSpy:
    
    def __init__(self) -> None:
        self.soma_atributes = {}
    
    def soma(self, n1, n2):
        self.soma_atributes['n1'] = n1 
        self.soma_atributes['n2'] = n2
        
        return faker.random_number(n1 , n2)
    