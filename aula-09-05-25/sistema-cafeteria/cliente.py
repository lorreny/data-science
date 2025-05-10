# cliente.py

class Cliente():
    def __init__(self, nome, sobrenome, email, endereco, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.endereco = endereco
        self.senha = senha

    def __str__(self):
        return f"Nome: {self.nome}, Sobrenome: {self.sobrenome}, Email: {self.email}"
