"""
    Módulo cliente -
    Classe Cliente - 
"""
from tipocliente  import TipoCliente

class Cliente():
    def __init__(self, id, nome, codigo, cnpjcpf, tipo):
        self._id = id
        self._nome = nome
        self._codigo = codigo
        self._cnpjcpf = cnpjcpf
        self._tipo = tipo
        
    def str(self):
        string = ("ID: {0}", "Nome: {1}", "Codigo: {2}", "CNPJ/CPF: {3}", "Tipo: {4}").format(self._id, self._nome, self._codigo, self._cnpjcpf, self._tipo)
        return string
    
if __name__ == '__main__':
    cliente = Cliente(1, "Jose Maria", 1200, "200.100.345-34", TipoCliente.PESSOA_FISICA)
    print(cliente.str())
    

