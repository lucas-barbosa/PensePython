"""
Exercise 11.6

Aqui está outro quebra-cabeça do programa Car Talk (http://www.cartalk.com/content/puzzlers):

Ele foi enviado por Dan O’Leary. Dan descobriu uma palavra comum, com uma sílaba e cinco letras que
tem a seguinte propriedade única. Ao removermos a primeira letra, as letras restantes formam um
homófono da palavra original, que é uma palavra que soa exatamente da mesma forma. Substitua a
primeira letra, isto é, coloque-a de volta, retire a segunda letra e o resultado é um outro homófono
da palavra original. E a pergunta é, qual é a palavra?

Agora vou dar um exemplo que não funciona. Vamos usar a palavra de cinco letras, ‘wrack’ (mover,
eliminar). W-R-A-C-K, como na expressão ‘wrack with pain’ (se contorcer de dor). Se eu retirar a
primeira letra, sobra uma palavra de quatro letras, ‘R-A-C-K’ (galhada). Como na frase, ‘Holy cow,
did you see the rack on that buck! It must have been a nine-pointer!’ (‘Minha nossa, você viu a
galhada daquele cervo! Deve ter nove pontas!’). É um homófono perfeito. Se puser o ‘w’ de volta e
retirar o ‘r’ em vez disso, sobra a palavra ‘wack’, que é uma palavra de verdade, mas não é um
homófono das outras duas palavras.

Mas há pelo menos uma palavra que Dan e eu conhecemos, que produz dois homófonos se você retirar
qualquer uma das duas primeiras letras, e duas novas palavras de quatro letras são formadas. A
pergunta é, qual é a palavra?

Você pode usar o dicionário do Exercício 11.1 para verificar se uma string está na lista de palavras.

Para verificar se duas palavras são homófonas, você pode usar o Dicionário de pronúncia CMU. Ele
pode ser baixado em http://www.speech.cs.cmu.edu/cgi-bin/cmudict ou em 
http://thinkpython2.com/code/c06d. Você também pode baixar http://thinkpython2.com/code/pronounce.py,
que tem uma função chamada read_dictionary, que lê o dicionário de pronúncia e retorna um dicionário
de Python que mapeia cada palavra a uma string que descreve sua pronúncia primária.

Escreva um programa que liste todas as palavras que resolvem o quebra-cabeça.
"""

def make_sound_dict():
    d = {}
    fin = open('c06d.txt')

    for line in fin:
        if line[0] == '#':
            continue            
        t = line.split()
        word = t[0].lower()
        sound = ''.join(t[1:])
        d[word] = sound
    
    return d

def make_words_dict():
    d = []
    fin = open('words.txt')

    for line in fin:
        word = line.strip().lower()
        d.append(word)
    
    return d

def check_homophone(word1, word2, pronounce_dic):
    if word1 not in pronounce_dic or word2 not in pronounce_dic:
        return False

    return pronounce_dic[word1] == pronounce_dic[word2]

def check_word(word, words_dic, pronounce_dic):
    word1 = word[1:]
    if word1 not in words_dic:
        return False
    if not check_homophone(word, word1, pronounce_dic):
        return False

    word2 = word[0] + word[2:]
    if word2 not in words_dic:
        return False
    if not check_homophone(word1, word2, pronounce_dic):
        return False

    return True

if __name__ == '__main__':
    words_dic = make_words_dict()
    pronounce_dic = make_sound_dict()

    for word in words_dic:
        if check_word(word, words_dic, pronounce_dic):
            print(word, word[1:], word[0] + word[2:])
    