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
            print('Sem fundos suficiente')
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
    output = 'Percentage spent by category\n'
    
        


