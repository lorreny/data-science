# main.py

from cafeteira import Cafeteira

def main():
    meuCafe = Cafeteira('Meu Café', 'Rua Tretas', '000')
    
    # Cadastrar Cliente
    meuCafe.cadastrar_cliente()

    # Cadastrar Produto
    meuCafe.cadastrar_produto()

    # Salvar dados em CSV
    meuCafe.salvar_dados_csv()

if __name__ == "__main__":
    main()
    
def main():
    meuCafe = Cafeteira()
    meuCafe.carregar_dados_csv()  # Carrega os dados do CSV para as listas de clientes e produtos
    
    # Agora, você pode continuar a interagir com o sistema normalmente
    meuCafe.cadastrar_cliente()
    meuCafe.cadastrar_produto()

    # Salvar os dados de volta no CSV
    meuCafe.salvar_dados_csv()
