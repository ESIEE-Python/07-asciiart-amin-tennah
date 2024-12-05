""" la fonction"""
import sys
sys.setrecursionlimit(1500)
#### Imports et définition des variables globales


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de 
    caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici

    if not s:
        return []

    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append((s[i - 1], count))
            count = 1
    result.append((s[-1], count))  # Ajouter le dernier groupe
    return result


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de 
    caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici

    # cas de base
    # recherche nombre de caractères identiques au premier
    # appel récursif
    if not s:
        return []

    # Identifier le premier caractère et compter les occurrences consécutives
    char = s[0]
    count = 1
    while count < len(s) and s[count] == char:
        count += 1
    return [(char,count)]+ artcode_r(s[count:])


#### Fonction principale


def main():
    """ le main """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
