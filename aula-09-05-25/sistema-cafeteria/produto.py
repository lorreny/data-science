# produto.py

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

