# coding=utf-8
# player b=black, w=white
#upper=white, lower=black
player = None
winner = None
field = []


def init_game():
    global field
    global player
    field = [["t", "h", "b", "q", "k", "b", "h", "t"],
             ["p", "p", "p", "p", "p", "p", "p", "p"],
             [".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."],
             ["P", "P", "P", "P", "P", "P", "P", "P"],
             ["T", "H", "B", "Q", "K", "B", "H", "T"]]
    player = "w"


def human_play():
    permitida_from = False
    permitida_to = False
    if game_ended() == 0:
        while (not permitida_from) or (not permitida_to):
            de, para = get_input()
            permitida_from = check_from(de)
            permitida_to = check_to(para)

            if not permitida_from:
                print "posiçao de partida inválida"
            elif not permitida_to:
                print "posiçao de chegada inválida"

                #TODO
                #obedece as regras


#devolve 0 se o jogo ainda nao acabou, 1 se o branco ganhou e 2 se o preto ganhou
def game_ended():
    w_king = False
    b_king = False
    for l in field:
        if "k" in l:
            b_king = True
        if "K" in l:
            w_king = True
    if w_king and b_king:
        return 0  # ninguem ganhou
    elif w_king and not b_king:
        return 1  # branco ganhou
    elif not w_king and b_king:
        return 2  # preto ganhou
    return 3


#verifica se para onde se esta a tentar jogar e um lugar vazio ou uma peça do outro jogador
def check_to(para):
    p = get_piece(para)
    if p == ".":  # posiçao vazia
        return True
    if p.isupper() and player == "w":  # peça branca e branco a tentar comer
        return False
    if (not p.isupper()) and player == "b":  # peça preta e preto a tentar comer
        return False
    return True  # interracional only


#verifica se existe a peça e se pertence ao jogador
def check_from(de):
    p = get_piece(de)
    if p.isupper() and player != "w":  # peça branca e nao e o branco a jogar
        return False
    if (not p.isupper()) and player != "b":  # peça preta e nao e o preto a jogar
        return False
    if p == ".":  # nao existe peça nesta posiçao
        return False
    return True


#devolve a peça presente na posiçao dada
def get_piece(pos):
    dic = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
    linha = int(pos[1]) + (2 * (4 - int(pos[1])))
    coluna = dic[pos[0].upper()]
    return field[linha][coluna]


#devolve 2 posicoes existentes no jogo: de e para
def get_input():
    de = None
    para = None
    permitida = False
    while not permitida:
        print "Jogada. De: "
        de = raw_input()
        permitida = check_input(de)  # posicao existe
        if not permitida:
            print "Posiçao inválida"

    permitida = False
    while not permitida:
        print "Para: "
        para = raw_input()
        permitida = check_input(para)
        if de == para:  # de e para tem de ser diferentes
            permitida = False
        if not permitida:
            print "Posiçao inválida"

    return de, para


#verifica se dada posiçao existe no jogo
def check_input(pos):
    accepted_alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    accepted_num = ['1', '2', '3', '4', '5', '6', '7', '8']
    if len(pos) != 2:
        return False
    if pos[0] in accepted_alfa and pos[1] in accepted_num:
        return True
    return False


def print_field():
    x = 8
    print "    A B C D E F G H "
    print "  -------------------"
    for l in field:
        print '{linha} | {0} {1} {2} {3} {4} {5} {6} {7} | {linha}'.format(*l, linha=x)
        x -= 1
    print "  -------------------"
    print "    A B C D E F G H "


init_game()
print_field()
print game_ended()
print check_to(raw_input("pos: "))
human_play()
print_field()