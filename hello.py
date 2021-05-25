import os

path = input('Enter Path: ' )

def SwapData():
    A, B = os.listdir(path) 

    AP = path + '/' + A
    BP = path + '/' + B

    AF = open(AP, 'r')
    BF = open(BP, 'r')

    AD = AF.read()
    BD = BF.read()

    AF = open(AP, 'w')
    BF = open(BP, 'w')

    AF.write(BD)
    BF.write(AD)
            
        
SwapData()

    