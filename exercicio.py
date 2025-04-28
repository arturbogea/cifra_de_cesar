# Exercício cifra de César

alfabeto = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# Função principal para criptografar e descriptografar
def cifra_cesar(texto, deslocamento, direcao):
    resultado = ""

    for letra in texto:
        if letra in alfabeto:
            posicao = alfabeto.index(letra)

            if direcao == "esconder":
                nova_posicao = (posicao + deslocamento) % 26
            elif direcao == "mostrar":
                nova_posicao = (posicao - deslocamento) % 26

            resultado += alfabeto[nova_posicao]
        else:
            # Mantém espaços, números ou pontuação
            resultado += letra

    print(f"\n🔐 Mensagem {direcao}da: {resultado}")

# Interface simples com o usuário
print("🕵️‍♂️ Bem-vindo ao programa da Cifra de César!")

direcao = input("Digite 'esconder' para criptografar ou 'mostrar' para descriptografar:\n").lower()
texto = input("Digite a sua mensagem:\n").lower()
deslocar = int(input("Digite o número do deslocamento:\n"))

# Chama a função
cifra_cesar(texto, deslocar, direcao)