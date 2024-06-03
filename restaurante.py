class Restaurante:
    categoria = None

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

# 1) Atribuir o valor 'Italiana' ao atributo categoria da instância restaurante_praca
restaurante_praca = Restaurante("Restaurante Praça", "Italiana")

# 2) Acessar o valor do atributo nome da instância restaurante_praca
nome_restaurante_praca = restaurante_praca.nome
print("Nome do restaurante Praça:", nome_restaurante_praca)

# 3) Verificar o valor inicial do atributo ativo para a instância restaurante_praca e exibir uma mensagem informando se o restaurante está ativo ou inativo
if restaurante_praca.ativo:
    print("O restaurante Praça está ativo.")
else:
    print("O restaurante Praça está inativo.")

# 4) Acessar o valor do atributo de classe categoria diretamente da classe Restaurante e armazenar em uma variável chamada categoria
categoria = Restaurante.categoria
print("Categoria de restaurante:", categoria)

# 5) Alterar o valor do atributo nome para 'Bistrô'
restaurante_praca.nome = "Bistrô"

# 6) Criar uma nova instância da classe Restaurante chamada restaurante_pizza com o nome ‘Pizza Place' e categoria 'Fast Food'
restaurante_pizza = Restaurante("Pizza Place", "Fast Food")

# 7) Verificar se a categoria da instância restaurante_pizza é 'Fast Food'
if restaurante_pizza.categoria == "Fast Food":
    print("A categoria do restaurante Pizza é Fast Food.")

# 8) Mudar o estado da instância restaurante_pizza para ativo
restaurante_pizza.ativo = True

# 9) Imprimir no console o nome e a categoria da instância restaurante_praca
print("Nome do restaurante Praça:", restaurante_praca.nome)
print("Categoria do restaurante Praça:", restaurante_praca.categoria)
