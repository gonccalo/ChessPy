# coding=utf-8
#player b=black, w=white
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
    de, para = get_input()
    check_from(de)
    #TODO
    #verificar se existe peca na 1 posicao e pertence ao jogador
    #verificar se a segunda posicao esta livre ou tem peça do outro jogador
    #obedece as regras


#verifica se existe a peça e se pertence ao jogador
def check_from(de):
    return 0


#devolve a peça presente na posiçao dada
def get_piece(pos):
    dic = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
    linha = int(pos[1]) + (2*(4-int(pos[1])))
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
        permitida = check_input(de)        # posicao existe
        if not permitida:
            print "Posiçao inválida"

    permitida = False
    while not permitida:
        print "Para: "
        para = raw_input()
        permitida = check_input(para)
        if de == para:                     # de e para tem de ser diferentes
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
print get_piece(raw_input("pos: "))
human_play()
print_field()