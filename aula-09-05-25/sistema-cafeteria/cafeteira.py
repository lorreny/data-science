# cafeteira.py

from cliente import Cliente
from produto import Produto
import csv
import os

class Cafeteira():
    def __init__(self, nome, endereco, cnpj):
        self.nome = nome
        self.endereco = endereco
        self.cnpj = cnpj
        self.clientes = []
        self.produtos = []

    def cadastrar_cliente(self):
        cliente_nome = input('Digite seu nome: ')
        cliente_sobrenome = input('Digite seu sobrenome: ')
        cliente_endereco = input('Digite seu endereço: ')
        cliente_email = input('Digite seu e-mail: ')
        cliente_senha = input('Digite sua senha: ')

        cliente = Cliente(cliente_nome, cliente_sobrenome, cliente_endereco, cliente_email, cliente_senha)
        self.clientes.append(cliente)
        print(f'Cliente {cliente_nome} cadastrado com sucesso!')
        return cliente

    def cadastrar_produto(self):
        nome_produto = input('Informe o nome do produto: ')
        categoria = input('Informe a categoria do produto: ')
        tamanho_quantidade = input('Informe o tamanho do produto (ml ou g): ')
        peso_volume = input('Informe se é ml ou g: ')
        preco = input('Valor do produto: ')
        desconto_promocao = input('Valor do produto promocional: ')
        data_desconto_promocao = input('Data da validade do desconto: ')
        ingredientes = input('Ingredientes do produto: ')
        estoque = input('Disponibilidade (Disponível/Indisponível): ')
        data_validade = input('Data de validade do produto: ')
        quantidade_em_estoque = input('Quantidade em estoque: ')
        status = input('Status (Ativo/Inativo): ')

        produto = Produto(nome_produto, categoria, estoque, data_validade, ingredientes, desconto_promocao,
                          data_desconto_promocao, tamanho_quantidade, peso_volume, preco, quantidade_em_estoque, status)
        self.produtos.append(produto)
        print(f'O Produto {nome_produto} foi cadastrado com sucesso!')
        return produto

    def salvar_dados_csv(self):
        # Salvar dados de clientes
        if not os.path.exists('clientes.csv'):  # Se o arquivo não existir
            with open('clientes.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Nome', 'Sobrenome', 'Email', 'Endereco', 'Senha'])  # Escreve o cabeçalho

        with open('clientes.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for cliente in self.clientes:
                writer.writerow([cliente.nome, cliente.sobrenome, cliente.email, cliente.endereco, cliente.senha])

        # Salvar dados de produtos
        if not os.path.exists('produtos.csv'):  # Se o arquivo não existir
            with open('produtos.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Nome Produto', 'Categoria', 'Preço', 'Desconto', 'Quantidade Estoque', 'Status'])  # Cabeçalho de produtos

        with open('produtos.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for produto in self.produtos:
                writer.writerow([produto.nome_produto, produto.categoria, produto.preco, produto.desconto_promocao,
                                 produto.quantidade_em_estoque, produto.status])
    def carregar_dados_csv(self):
        # Método para carregar dados de um CSV
        pass
