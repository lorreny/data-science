class Cafeteira():
    def __init__(self, nome, endereco, cnpj):
        self.nome = nome
        self.endereco = endereco
        self.cnpj = cnpj
        self.clientes = []
        self.produto = []

    def cadastrar_cliente(self):
        cliente_nome = input('Digite seu nome: ')
        cliente_sobrenome = input('Digite seu sobrenome: ')
        cliente_endereco = input('Digite seu endereço: ')
        cliente_email = input('Digite seu e-mail: ')
        cliente_senha = input('Digite sua senha: ')

        cliente = Cliente(cliente_nome, cliente_sobrenome, cliente_endereco, cliente_email, cliente_senha)

        print(f'Cliente {cliente_nome} cadastrado com sucesso!')
        return cliente

    def cadastrar_produto(self):
        nome_produto = input('Informe o nome do produto: ')
        categoria = input('Informe a categoria do produto se é: Café, Chá, Doces, Lanches: ')
        tamanho_quantidade = input('Informe o tamanho do produto, ex: 200, 300, 400: ')
        peso_volume = input('Informe se é ml ou g: ')
        preco = input('Valor do produto: ')
        desconto_promocao = input('Valor do produto promocional: ')
        data_desconto_promocao = input('Data da validade do valor promocional: ')
        ingredientes = input('Informe o ingrediente do produto, ex: café, leite, açúcar, etc: ')
        estoque = input('Informe se o produto esta Disponível ou Indisponível: ')
        data_validade = input('Informe a data de validade do produto: ')
        quantidade_em_estoque = input('Quantidade do produto em estoque: ')
        status = input('Informe se o produto está Ativo ou Inativo: ')
        
        produto = Produto(nome_produto, categoria, estoque, data_validade, ingredientes, desconto_promocao, data_desconto_promocao, tamanho_quantidade, preco, quantidade_em_estoque, peso_volume, status)

        print(f'O Produto {nome_produto} foi cadastrado com sucesso!')
        return produto

class Cliente():
    def __init__(self, nome, sobrenome, email, endereco, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.endereco = endereco
        self.senha = senha

    def __str__(self):
        return f"""
        Nome: {self.nome}
        Sobrenome: {self.sobrenome}
        Email: {self.email}
        """



class Produto():
    def __init__(self, nome_produto, categoria, estoque, data_validade, ingredientes, desconto_promocao, 
                 data_desconto_promocao, tamanho_quantidade, preco, quantidade_em_estoque, peso_volume, status):
        self.nome_produto = nome_produto
        self.categoria = categoria
        self.estoque = estoque
        self.data_validade = data_validade
        self.ingredientes = ingredientes
        self.desconto_promocao = desconto_promocao
        self.data_desconto_promocao = data_desconto_promocao
        self.tamanho_quantidade = tamanho_quantidade
        self.preco = preco
        self.quantidade_em_estoque = quantidade_em_estoque
        self.peso_volume = peso_volume
        self.status = status

    def __str__(self):
        return f"Produto cadastrado na categoria: {self.categoria}\nValor: {self.preco}\n" \
               f"Data de Validade: {self.data_validade}\n"

meuCafe = Cafeteira('Meu Café', 'Rua Tretas', '000')
meuCafeProduto = Cafeteira('Meu Café', 'Rua Tretas', '000')
print(meuCafe.cadastrar_cliente())
print(meuCafeProduto.cadastrar_produto())
