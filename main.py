#coding: utf-8

# Exercice (1):

def est_valide(mot, schema):
    """
    chaine de caractère, chaine de caractère -> booléan
    
    Retourne si un chaine de caractère est correspond a un schéma donner
    cet a dire par exemple le schema p?p? ou ? sont des caractère quelqu'onque
    
    papa, pipi respecterons ce schema mais pas le mot caca par exemple ! 
    """
    
    if len(mot) != len(schema):
        return False
    
    for i in range(len(mot)):
        if mot[i] != schema[i] and schema[i] != '?':
            return False 
        
    return True

# Exercice (2)

def est_prefixe(prefixe, mot):
    """
    chaine de caractère, chaine de caractère -> booléan
    
    Retourne True si prefixe et le prefixe de mot faux sinon 
    """
    return prefixe == mot[:len(mot) - len(prefixe) - 1]

# Exercice (3)

def est_suffixe(suffixe, mot):
    """
    chaine de caractère, chaine de caractère -> booléan
    
    Retourne True si suffixe et le suffixe de mot faux sinon 
    """
    return suffixe == mot[len(suffixe)-1:]

# Exercice (4)

def contient_dans_ordre(sequence_lettres, chaine):
    """
    chaine de caractère, chaine de caractère -> Booléan
    
    Retourne True si la sequence de lettres est dans l'ordre dans la chaine False sinon
    """
    
    recuperer_lettres = ''
    
    for letter in chaine:
        if letter in sequence_lettres:
            recuperer_lettres += letter 
    
    return recuperer_lettres[: len(chaine) - len(sequence_lettres) - 1] == sequence_lettres
    

# Exercice (5)

def miroir(chaine):
    """
    chaine de caractère -> chaine de caractère

    Retourne la chaine de caractère en paramètre, a l'envers
    """
    
    renverser = ''
    
    for i in range(len(chaine)-1, -1, -1):
        renverser += chaine[i]
    return renverser

# Exercice (6)

def palindrome(chaine):
    """
    chaine de caractère -> booléan 
    
    Retourne True si chaine est un palindrome Faux sinon 
    """
    
    return chaine == miroir(chaine)
    
    