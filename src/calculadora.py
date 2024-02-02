class Calculadora:
    def __init__(self, adicao, subtracao) -> None:
        self.adicao = adicao
        self.subtracao = subtracao
        
    def add(self, n1, n2, op):
        if op:
            return self.adicao.soma(n1, n2)
        return None
        
    def sub(self, n1, n2, op):
        if op:
            return self.subtracao.diferenca(n1, n2)
        return None