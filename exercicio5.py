# Solicitando a entrada do usuário
string = input("Digite uma string para inverter: ")

# Inicializando a string invertida
string_invertida = ""

# Iterando sobre a string original de trás para frente
for i in range(len(string) - 1, -1, -1):
    string_invertida += string[i]

# Exibindo a string invertida
print("String original:", string)
print("String invertida:", string_invertida)
