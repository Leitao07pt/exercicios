'''
Olá eu sou o Torga Bot!

Qual é o teu nome?
Que idade tens?
Onde vives?
o que gostas de fazer?

Olá {nome}, tens {idade} ano(s) de idade. E vives em {cidade} e gostas de fazer {interesse}
'''

print("Olá eu sou o Torga Bot!")

# Input

nome = input("Qual é o nome? ")
idade = input("Que idade tens? ")
cidade = input("Onde vives? ")
gostos = input("O que gostas de fazer? ")

# Output

print(f"\nOlá {nome}, tens {idade} ano(s) de idade. E vives em {cidade} e gostas de {gostos}.")
