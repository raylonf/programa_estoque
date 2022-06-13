# 1 - Escreva um sofware em Python capaz de administrar uma estrutura de dados, referente a um cadastro de produtos para um comércio local,
# com as seguintes funções:
# a) Incluir cadastro.
# b) modificar cadastro.
# c) consultar cadastro.
# d) Deletar cadastro.
# e) Encerrar programa
#
# 2 - Seguindo o exemplo anterior, implemente as seguintes opções:
# a) Criar um backup do cadastro.
# b) Deletar todos os cadastros.

import os


class Cadastro:

    def __init__(self):
        self.produto = []
        self.load()

    def incluir_produto(self, produto, valor, quantidade):
        if self.consultar_produto_existe(produto):
            return print('\nProduto já cadastrado.')
        else:
            self.produto.append([produto, valor, quantidade])
            return print('\nProduto cadastrado com sucesso.')

    def deletar_produto(self, produto):
        if self.consultar_produto_existe(produto):
            x = 0
            y = int
            for list in self.produto:
                if list[0] == produto:
                    y = x
                x += 1
            self.produto.pop(y)
            return print('\nProduto excluido com sucesso.')
        else:
            return print('\nProduto não cadastrado ou já excluido.')

    def listar_produtos(self):
        if len(self.produto) != 0:
            print('Produto    Valor    Qtd')
            for list in self.produto:
                print(f'{list[0]}  {list[1]}  {list[2]}')
        else:
            print('Lista vazia!')

    def modificar_produto(self, produto, valorModificado, quantidadeModificado):
        if self.consultar_produto_existe(produto):
            x = 0
            y = int
            for list in self.produto:
                if list[0] == produto:
                    y = x
                x += 1
            self.produto[y] = [produto, valorModificado, quantidadeModificado]
            return print('\nProduto modificado com sucesso.')

    def consultar_produto_existe(self, produto):
        for list in self.produto:
            if list[0] == produto:
                return True

    def consultar_produto(self, produto):
        if self.consultar_produto_existe(produto):
            for list in self.produto:
                if list[0] == produto:
                    total = float(list[1]) * int(list[2])
                    return print(f'Produto: {list[0]} \nValor: {list[1]}\nQuantidade: {list[2]}\nTotal: {total:.2f}')
        else:
            return print('\nProduto não cadastrado ou incorreto.')

    def load(self):
        if not os.path.exists('produtos_cadastrados.txt'):
            return
        with open('produtos_cadastrados.txt', 'r') as f:
            prod = f.readline()
            while prod:
                prod = prod.replace('\n', '')
                produto_formatado = prod.split(',')
                self.produto.append(produto_formatado)
                prod = f.readline()


    def backup(self):
        with open('produtos_cadastrados.txt', 'w') as f:
            for prod in self.produto:
                f.write(f'{prod[0]}, {prod[1]}, {prod[2]}\n')

            return print('\nSalvo com sucesso!')

    def del_todos_cadastros(self):
        self.produto.clear()
        print(self.produto)
        self.backup()
        return print('Estoque foi completamente zerado!')


print('-#-#-#-#-#-#-#-#-#-#-# CADASTROS DE PRODUTOS -#-#-#-#-#-#-#-#-#-#-#')
produto = Cadastro()

while True:
    print('\nMenu: \n'
          '\n(1) - Incluir cadastro de produto'
          '\n(2) - Modificar cadastro'
          '\n(3) - Consultar cadastro'
          '\n(4) - Deletar cadastro'
          '\n(5) - Listar todos produtos já cadastrados'
          '\n(6) - Criar um Backup do produtos cadastrados'
          '\n(7) - Deletar todos os cadastros'
          '\n(8) - Encerrar programa.')
    menu = input('\nDigite uma opção: ')

    match menu:
        case '1':
            prod_nome = input('Digite o nome do produto: ')
            prod_valor = float(input('Digite o valor do produto: '))
            prod_qntdade = int(input('Digite a quantidade: '))
            produto.incluir_produto(prod_nome, prod_valor, prod_qntdade)

        case '2':
            prod_nome_mod = input('Digite o nome do produto que será modificado: ')
            prod_valor_modificado = float(input('Digite o valor do produto: '))
            prod_qntdade_modificado = int(input('Digite a quantidade do produto: '))
            produto.modificar_produto(prod_nome_mod, prod_valor_modificado, prod_qntdade_modificado)

        case '3':
            prod_consulta = input('Digite o nome do produto de gostaria de consultar: ')
            produto.consultar_produto(prod_consulta)

        case '4':
            prod_nome_del = input('Digite o nome do produto que será deletado: ')
            produto.deletar_produto(prod_nome_del)

        case '5':
            produto.listar_produtos()

        case '6':
            produto.backup()

        case '7':
            produto.del_todos_cadastros()

        case '8':
            print('\n-#-#-#-#-#-#-#-#-#-#Encerrando o Programa-#-#-#-#-#-#-#-#-#-#-#-#-#'
                  '\n                    -#-#-#-#-#-#-#-#-#-#-#  \n')
            break
