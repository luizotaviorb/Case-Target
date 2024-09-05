# Função que calcula a sequência de Fibonacci e verificar se um número pertence a ela
def pertence_fibonacci(numero):
    # Iniciando os dois primeiros números da sequência
    a, b = 0, 1
    
    # Gerando a sequência de Fibonacci até que b seja maior ou igual ao número
    while b < numero:
        a, b = b, a + b
    
    # Verificando se o número pertence à sequência
    if b == numero or numero == 0:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."


# Número a ser verificado (pode ser alterado ou usado como entrada)
numero_verificado = 21

# Chamando a função e imprimindo o resultado
print(pertence_fibonacci(numero_verificado))


