import math




def test_cle():
    cle = input()
    if len(cle) != 15:
        cle = int(input())
    elif int(cle) % 1000000000000 == 97 - int(cle[:-2]) % 97:
        print('validé')
    elif int(cle) % 1000000000000 != 97 - int(cle[:-2]) % 97:
        print('pas bon')


test_cle()



def decomposition(nombre):
    decomposer = []
    

