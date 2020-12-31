def tri (l, compare):
    """Tri à peigne, recoit en paramètre une fonction
     de comparaison pour portativité sur les listes à caractères
     @:param l: liste à trier
     @:param compare: fonction de comparaison entre deux elements de la liste
     """
    permut = True
    gap = len(l)
    while (permut or (gap >1)):
        permut = False
        gap = int(gap//1.3)
        if gap < 1:
            gap = 1
        for i in range (len(l) - gap):
            if compare(l[i], l[i+gap]):
                permut = True
                l[i], l[i+gap] = l[i+gap],l[i]
    return l


def compItem(comp1, comp2):
    """Comparison function: return true when the word stored in comp1[0] is greater
    in dictionnary order then the word stored in comp2[0]
    @:param comp1: a list of two strings
    @:param comp2: a list of two strings
    """
    word1,word2 = comp1[0],comp2[0]

    for i in range (min(len(word1),len(word2))):
        if not(word1[i] == word2[i]):
            return word1[i] > word2[i]
    return False

def splitting(str, car):
    """Split function: return a list of two strings produced from the splitting of string
    given in parameter after firstly encountered char in param
    @:param str: a string to split
    @param car: the char to detect to split the string
    """
    l = ["",""]
    split = False
    for c in str:
        if split:
            l[1] += c
        elif c != car and not(split):
            l[0] += c
        else:
            split = True
    return l


def loadDictionnary(path):
    """loadDictionnary: return the dictionnary contained in a file
    @:param path: the path of the dictionnary file
    """
    dico = []
    with open(path, "r") as file:
        line = file.readline()
        line = file.readline()
        while line != None and line != '' and line != "":
            dico.append(splitting(line," "))
            line = file.readline()

        file.close()
    return dico

def writeDictionnary (dico, path):
    """writeDictionnary: write the dictionnary given in parameter at path given in parameter
    @:param dico: the dictionnary to write in a file
    @:param path: the path to the file to write in
    """
    with open(path, "w+") as file:
        for item in dico:
            file.write(item[0] + " " + item[1])
        file.close()




if __name__ == "__main__":
    #Process steps of the script
    print("loading dict")
    dict  =loadDictionnary("Dictionnaire.txt")
    print("loading done,beginning tri")
    dict = tri(dict,compItem)
    print("dictionnary has been processed, printing in newDico.txt")
    writeDictionnary(dict, "newDico.txt")
    print("done")


