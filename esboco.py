import random


def jogar_dado():
    return random.randint(1, 6)


perguntas = {
    "Quais são as cores primárias?": "azul, amarelo e vermelho",
    "Qual é a capital do Brasil?": "Brasília",
    "Qual o maior estado brasileiro?": "Amazonas",
    "Qual é o maior animal terrestre?": "Elefante",
    "Qual é a moeda oficial do Japão?": "Yen",
    "Qual o maior planeta do sistema solar?": "Júpiter",
    "Quem foi o autor de 'Romeu e Julieta'?": "William Shakespeare",
    "Quem foi o famoso cientista que formulou a teoria da evolução das espécies?": "Charles Darwin",
    "Qual é o país conhecido como 'terra do sol nascente'?": "Japão",
    "Qual é a capital da Espanha?": "Madri"
}


def fazer_pergunta(pergunta):
    resposta = input(f"{pergunta} ")
    return resposta.lower() == perguntas[pergunta].lower()


def mover_jogador(posicao, dado):
    return posicao + dado


posicoes = [0, 0]  
num_jogadores = len(posicoes)
final = len(perguntas)  
turno = 0


while True:
    print(f"\nÉ a vez do Jogador {turno + 1}")
    input("Pressione Enter para lançar o dado...")
    dado = jogar_dado()
    print(f"Você tirou um {dado}!")


    nova_posicao = mover_jogador(posicoes[turno], dado)


    if nova_posicao >= final:
        nova_posicao = final


    # Se o jogador alcançar a última posição, deve responder a pergunta final
    if nova_posicao == final:
        pergunta = list(perguntas.keys())[nova_posicao - 1]
        if fazer_pergunta(pergunta):
            print(f"Parabéns, Jogador {turno + 1}! Você venceu!")
            print("O jogo terminou. Obrigado por jogar!")
            break
        else:
            print("Resposta incorreta. Você volta para a posição anterior.")
            posicoes[turno] = max(0, posicoes[turno] - dado)
    else:
        posicoes[turno] = nova_posicao
        print(f"Você está agora na casa {posicoes[turno]}.")


        pergunta = list(perguntas.keys())[posicoes[turno] - 1]  # Pergunta para a casa atual
        if fazer_pergunta(pergunta):
            print("Resposta correta!")
        else:
            print("Resposta incorreta. Você volta para a posição anterior.")
            posicoes[turno] = max(0, posicoes[turno] - dado)  # Volta para a posição anterior


    # Troca de turno
    turno = (turno + 1) % num_jogadores