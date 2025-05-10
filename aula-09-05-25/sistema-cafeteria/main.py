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
