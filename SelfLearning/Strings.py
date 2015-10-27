from __future__ import print_function, division

import io
def find(word, letter, start=0):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


def letterCount(word,letter):
    count = 0
    for l in word:
        if l == letter:
            count = count + 1
    if count != 0:
        return count
    else:
        return -1


def rotate_letter(letter, n):
    """Rotates a letter by n places.  Does not change other chars.

    letter: single-letter string
    n: int

    Returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    """Rotates a word by n places.

    word: string
    n: integer

    Returns: string
    """
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res

def createCodeBook(dict="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", shift=0):
    length = len(dict)
    result = ""
    for i in range(0,length):
        result+=dict[(i+shift)%length]
    return result

def rotateWord(word, n):
    dict = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ +-!?#$,.;:*%&/()="
    code = createCodeBook(dict, n)
    result = ""
    for letter in word:
        result += code[dict.find(letter)]
    return result

def print20andmore():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if len(word)>=20:
            print(word)
    fin.close()

def has_no_e(word):
    if word.find('e') != -1:
        return False
    else:
        return True

def exercise92():
    fin = open('words.txt')
    lineCounter=0
    noECounter=0
    for line in fin:
        word = line.strip()
        lineCounter += 1
        if has_no_e(word):
            noECounter += 1
            print(word)
    fin.close()
    return 100/lineCounter*noECounter

def avoids(word,forbidden):
    for letter in forbidden:
        if word.find(letter) != -1:
            return False
    return True

def createSearchPattern():
    #
    # How to generate serach patterns
    # abcde
    # abcdf
    # ... bcdef
    s = ""
    for i in range(0,26-4):
        str = chr(ord('a')+i)+chr(ord('a')+i+1)+chr(ord('a')+i+2)+chr(ord('a')+i+3)+chr(ord('a')+i+4)+'\n'
        s = s + str.__str__()
    return s.__str__()

def exercise93():
    s = createSearchPattern()+"    "
    forbiddenList = io.StringIO(s)
    lowestScore = 100000
    lowestPattern = ""
    while (len(forbiddenList.read())>0):
        pattern = forbiddenList.readline().strip()
        print("Pattern",pattern)
        fin = open('words.txt')
        matches=0
        for line in fin:
            word = line.strip()
            if avoids(word,pattern):
                matches += 1
                print(word,pattern)
        fin.close()
        if matches < lowestScore:
            lowestScore = matches
            lowestPattern = pattern
    return lowestScore,lowestPattern


if __name__ == '__main__':

    print(rotate_word('cheer', 7))
    print(rotate_word('melon', -10))
    print(rotate_word('sleep', 9))

    print(rotateWord('cheer', 7))
    print(rotateWord('melon', -10))
    print(rotateWord('sleep', 9))
    for i in range(0,70):
        r = rotateWord('This is a simple test which is a bit bigger than ususal',i)
        print(r)


    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    print(abc[find(abc,'W',0)])
    print(find(abc,'Z',12))
    print(find(abc,'Z'))
    print(letterCount(abc,'a'))
    print(letterCount("banana",'z'))

    ratio = exercise92()
    print("Ratio:",ratio)

    print(avoids("test","ab"))
    print(avoids("test","abe"))

    print(exercise93())


