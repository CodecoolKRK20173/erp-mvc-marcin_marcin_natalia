""" Common functions for models
implement commonly used functions here
"""
import random

def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """
    generated = ''
    # your code
    table_ids = [row[0] for row in table]
    generated = generate()
    while generated in table_ids:
        generated = generate()

    return generated 
    
def generate():
    number = ('1','2','3','4','5','6','7','8','9','0')
    letter = ('a','b','c','d','e','f','g','h','i','j','k',/
    'l','m','n','o','p','r','s','t','u','w','y','z','x','q')
    special = ('!','@','#','$','%','&')
    
    digit = random.choice(number)
    big = random.choice(letter).upper()
    small = random.choice(letter).lower()
    specific = random.choice(special)
    table = digit + big + small + specific 

    digits = random.choice(number)
    bigs = random.choice(letter).upper()
    smalls = random.choice(letter).lower()
    specifics = random.choice(special)
    tables = digits + bigs + smalls + specifics   

    generated = table + tables
    #random.shuffle(generated)                #doesn't work ???

    #print (generated)
    return ''.join(generated) 
