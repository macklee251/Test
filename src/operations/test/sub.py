from faker import Faker
faker = Faker()

class SubOperationSpy:
    
    def __init__(self) -> None:
        self.diferenca_atributes = {}
    
    def diferenca(self, n1, n2):
        self.diferenca_atributes['n1'] = n1 
        self.diferenca_atributes['n2'] = n2
        
        return faker.random_number()
    