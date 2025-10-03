class Category:
    def __init__(self, nome):
        self.nome = nome
        self.ledger = []
    
    def check_funds(self, amount):
        return amount <= self.get_balance()
            
    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance+= i['amount']
        return balance
    
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False
 
    def transfer(self, amount, destino):
        if self.withdraw(amount, f"Transfer to {destino.nome}"):
            destino.deposit(amount, f"Transfer from {self.nome}")
            return True
        else:
            return False
    
    def __str__(self):
        # Título
        titulo = self.nome.center(30, '*')
        output = titulo + "\n"

        # Ledger
        for item in self.ledger:
            descricao = item['description'][:23].ljust(23)
            valor = f"{item['amount']:.2f}".rjust(7)
            output += f"{descricao}{valor}\n"
        
        # Total
        output += f"Total: {self.get_balance():.2f}"
        return output

def create_spend_chart(categories):
    # Cálcular gastos (apenas retiradas) e total geral
    gasto_cat = {}
    total_gasto = 0
    for categoria in categories:
        gasto = 0
        for item in categoria.ledger:
            if item['amount'] < 0:
                gasto += abs(item['amount'])
    
        gasto_cat[categoria.nome] = gasto
        total_gasto += gasto

    # Calcular percentuais
    percentual_cat = {}
    for categoria, gasto in gasto_cat.items():
        if total_gasto == 0:
            percentual_cat[categoria] = 0
        else:
            percentual = (gasto / total_gasto) * 100
        percentual_arredondado = int(percentual // 10) * 10
        percentual_cat[categoria] = percentual_arredondado

    # Construção do Gráfico
    output = "Percentage spent by category\n"
    for i in range (100, -1, -10):
        linha = f"{i}|".rjust(4)
        for percentual in percentual_cat.values():
            if percentual >= i:
                linha += " o "
            else:
                linha += "   "
        output += linha + ' \n'
        
    # Linha horizontal (3 dashes por categoria)
    linha_final = "    " + ('---'*len(categories)) + '-' + '\n'
    output += linha_final

    # Nomes das categorias
    nomes_categorias = [categoria.nome for categoria in categories]
    maior_nome = max(len(nome) for nome in nomes_categorias) if nomes_categorias else 0
    for i in range(maior_nome): 
        linha_nome = '    '
        for nome in nomes_categorias:
            char = nome[i] if i < len(nome) else " "
            linha_nome += f" {char} " 

        output += linha_nome + ' '
        if i < maior_nome - 1:
            output += '\n'
    return output

# --- TESTE COM 3 CATEGORIAS ---

food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

# DEPOSITOS
food.deposit(1000, "Depósito Inicial")
clothing.deposit(500, "Depósito Inicial")
auto.deposit(200, "Depósito Inicial")

# GASTOS (Retiradas)
food.withdraw(150, "Mercado Grande")
food.withdraw(25, "Lanche") 
clothing.withdraw(80, "Casaco Novo")
auto.withdraw(15, "Gasolina")
auto.withdraw(10, "Lava Jato")

# TRANSFERÊNCIA
food.transfer(50, clothing)

# Lista de Categorias
categories = [food, clothing, auto]

# Imprime o extrato de uma categoria para verificar __str__
print("--- Extrato da Categoria Food ---")
print(food)
print("\n" + "="*40 + "\n")

# Imprime o gráfico de gastos
print("--- Gráfico de Gastos ---")
print(create_spend_chart(categories))
        


