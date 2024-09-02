#IFRN Campus Ceará-Mirim;
#Turma: INFO1M;
#Disciplina: Introdução a Programação;
#Professora: Pricilla Suene;
#Componentes: Maikson Santiago, Eros Santos, Lucas Nunes, Matheus Gessle.

def quiz_futebol():
    acerto = 0
    print("Questão 1: Um time de futebol joga uma partida de 90 minutos com 11 jogadores. Se o mesmo sofrer 4 expulsões, quantos jogadores restariam?")
    print("a) 7")
    print("b) 9")
    print("c) 6")
    print("d) 5")
    n1 = input("Responda: ")
    if n1 == "a":
        print("Resposta certa")
        acerto += 1
    else:
        print("Resposta errada")
    
    print("Questão 2: Qual dos nomes abaixo é o do jogador brasileiro que ganhou a Copa do Mundo três vezes?")
    print("a) Garrincha")
    print("b) Maradona")
    print("c) Oliver Kahn")
    print("d) Pelé")
    n2 = input("Responda: ")
    if n2 == "d":
        print("Resposta certa")
        acerto += 1
    else:
        print("Resposta errada")
    
    print("Questão 3: Qual das seleções abaixo ganhou a taça da Copa do Mundo duas vezes?")
    print("a) Brasil")
    print("b) Alemanha")
    print("c) França")
    print("d) Espanha")
    n3 = input("Responda: ")
    if n3 == "b":
        print("Resposta certa")
        acerto += 1
    else:
        print("Resposta errada")
    
    print("Questão 4: Qual o nome do jogador que conquistou o prêmio da Bola de Ouro (prêmio dado ao melhor jogador do mundo em uma determinada temporada) 8 vezes?")
    print("a) Cristiano Ronaldo")
    print("b) Lionel Messi")
    print("c) Ronaldinho Gaúcho")
    print("d) Ronaldo Fenômeno")
    n4 = input("Responda: ")
    if n4 == "b":
        print("Resposta certa")
        acerto += 1
    else:
        print("Resposta errada")
    
    print("A quantidade de acertos será:", (acerto / 4) * 100)

def quiz_geografia():
    acerto = 0
    print("Questão 1: Quantos continentes existem no mundo (Planeta Terra)?")
    print("a) 7 continentes")
    print("b) 4 continentes")
    print("c) 6 continentes")
    print("d) 5 continentes")
    print("e) 8 continentes")
    n1 = input("Responda: ")
    if n1 == "a":
        print("Resposta certa")
        acerto += 1
    else:
        print("Resposta errada")
    
    print("Questão 2: Em qual continente está localizado o Brasil?")
    print("a) América do Sul")
    print("b) Europa")
    print("c) África")
    print("d) Oceania")
    print("e) Antártida")
    n2 = input("Responda: ")
    if n2 == "a":
        print("Resposta certa")
        acerto += 1
    else:
        print("Resposta errada")
    
    print("Questão 3: Quantos estados compõem a República Federativa do Brasil?")
    print("a) 27 estados")
    print("b) 26 estados")
    print("c) 24 estados")
    print("d) 18 estados")
    print("e) 32 estados")
    n3 = input("Responda: ")
    if n3 == "a":
        print("Resposta certa")
        acerto += 1
    else:
        print("Resposta errada")
    
    print("Questão 4: Quantas regiões tem o Brasil?")
    print("a) 8 regiões")
    print("b) 3 regiões")
    print("c) 6 regiões")
    print("d) 4 regiões")
    print("e) 5 regiões")
    n4 = input("Responda: ")
    if n4 == "e":
        print("Resposta certa")
        acerto += 1
    else:
        print("Resposta errada")
    
    print("Questão 5: Em qual região está localizado o Rio Grande do Norte (RN)?")
    print("a) Sudeste")
    print("b) Centro-Oeste")
    print("c) Norte")
    print("d) Nordeste")
    print("e) Sul")
    n5 = input("Responda: ")
    if n5 == "d":
        print("Resposta certa")
        acerto += 1
    else:
        print("Resposta errada")
    
    print("A quantidade de acertos será:", (acerto / 5) * 100)

def quiz_autoria_web():
    acerto = 0
    print("Questão 1: Qual tag é usada para incluir link?")
    print("a) img")
    print("b) a")
    print("c) h3")
    print("d) p")
    n1 = input("Responda: ")
    if n1 == "b":
        print("Resposta certa")
        acerto += 1
    else:
        print("Resposta errada")
    
    print("Questão 2: Qual tag é usada para incluir imagem?")
    print("a) img")
    print("b) hr")
    print("c) form")
    print("d) table")
    n2 = input("Responda: ")
    if n2 == "a":
        print("Resposta certa")
        acerto += 1
    else:
        print("Resposta errada")
    
    print("Questão 3: Qual atributo da tag <img> deve ser definido o caminho da imagem?")
    print("a) link")
    print("b) path")
    print("c) href")
    print("d) src")
    n3 = input("Responda: ")
    if n3 == "d":
        print("Resposta certa")
        acerto += 1
    else:
        print("Resposta errada")
    
    print("Questão 4: Qual o valor do atributo que definirá o caminho até a imagem?")
    print("a) ../capa.gif")
    print("b) capa.gif")
    print("c) imagem/capa.gif")
    print("d) imagem/site/capa.gif")
    n4 = input("Responda: ")
    if n4 == "c":
        print("Resposta certa")
        acerto += 1
    else:
        print("Resposta errada")
    
    print("A quantidade de acertos será:", (acerto / 4) * 100)

def main():
    while True:
        print("Digite: 1 para o Quiz de Futebol, 2 para o Quiz de Geografia, 3 para o Quiz de Autoria Web, 4 para sair")
        x = input("Digite: ")
        
        if x == "1":
            quiz_futebol()
        elif x == "2":
            quiz_geografia()
        elif x == "3":
            quiz_autoria_web()
        elif x == "4":
            print("Sair do site")
            break
        else:
            print("Inválido")

if __name__ == "__main__":
    main()