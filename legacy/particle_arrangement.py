import itertools

NumLevels = int(input('the number of energy levels: '))
NumParticles = int(input('the number of particles: '))

LevelList = list(range(NumLevels))

allAlloc = itertools.combinations_with_replacement(LevelList, NumParticles)

NumExpressList = []

for x in allAlloc:
    NumExpress = []
    print(x)
    for i in range(NumLevels):
        NumExpress.append(x.count(i)) 
    NumExpressList.append(NumExpress)   

print(NumExpressList)
print(len(NumExpressList))