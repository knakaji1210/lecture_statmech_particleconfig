# 粒子のエネルギー準位への可能な配置を計算
import math
import itertools
import numpy as np
from fractions import Fraction

def calcNumExpressList(LevelList, NumParticles):
    allAlloc = itertools.combinations_with_replacement(LevelList, NumParticles)
    # 重複組み合わせですべての可能な配置を列挙
    # 例えば(0, 2, 4, 4, 4)は5つの粒子が0から4のどの準位に入るかを意味する
    NumExpressList = []

    for x in allAlloc:
        NumExpress = []
# 配置を書き下す場合
#        print(x)
# 配置を粒子数表示に変更
# 例えば(0, 2, 4, 4, 4)は(1, 0, 1, 0, 3)に対応
        for i in range(NumLevels):
            NumExpress.append(x.count(i)) 
        NumExpressList.append(NumExpress)   

    return NumExpressList

def add_unity(n):
    return n + 1

def checkEnergyLevel(GroundLevel, NumExpressList, TotalEnergy):
# 基底状態が0か1かでエネルギー準位のリストを作成
    if GroundLevel == 0:
        EnergyLevels = LevelList
    if GroundLevel == 1:
        EnergyLevels = list(map(add_unity, LevelList))
    matchedNumExpressList = []
    for i in range(len(NumExpressList)):
        # エネルギーの総和を計算
        EnergySum = np.sum([n * e for (n, e) in zip(NumExpressList[i], EnergyLevels)])
        # エネルギーの総和が全エネルギーに等しい粒子数表示のみを選択
        if EnergySum == TotalEnergy:
            matchedNumExpressList.append(NumExpressList[i])
    return matchedNumExpressList

def calcWeight(list):
    # 与えられた粒子数表示に対して配置の重みを計算
    num = len(list)
    numer = math.factorial(np.sum(list))
    denom = 1
    for i in range(num):
        denom *= math.factorial(list[i])
    weight = numer / denom
    return weight

def calcResults(matchedNumExpressList):
    # 可能な配置の総数
    numConfig = len(matchedNumExpressList)
    weightList = []
    idConfig = 1
    configAttributeList = []
    for i in range(numConfig):
        # 可能な配置それぞれに対して配置の重みを計算
        weight = calcWeight(matchedNumExpressList[i])
        configAttribute = [idConfig, matchedNumExpressList[i], weight]
        weightList.append(weight)
        idConfig += 1
        configAttributeList.append(configAttribute)
        print('Id{0} : configration = {1}, weight = {2}'.format(configAttribute[0], configAttribute[1],configAttribute[2]))
    print('')
    print('most probable configuration:')
    probConfigIndex = [i for i, v in enumerate(weightList) if v == max(weightList)]
    for i in range(len(probConfigIndex)):
        print('configration: {0}'.format(matchedNumExpressList[probConfigIndex[i]]))
    pMostProbConfig1 = Fraction(int(len(probConfigIndex)*max(weightList)), int(np.sum(weightList)))
    pMostProbConfig2 = len(probConfigIndex)*max(weightList) / int(np.sum(weightList))  
    print('The probability of most probable configuration = {0} = {1:.3f}'.format(pMostProbConfig1, pMostProbConfig2))
    return configAttributeList

NumLevels = int(input('the number of energy levels: '))
GroundLevel = int(input('the ground state of energy level = 0 or 1: '))
TotalEnergy = int(input('the total energy: '))
NumParticles = int(input('the number of particles: '))

LevelList = list(range(NumLevels))
NumExpressList = calcNumExpressList(LevelList, NumParticles)
matchedNumExpressList = checkEnergyLevel(GroundLevel, NumExpressList, TotalEnergy)

print('')
configAttributeList = calcResults(matchedNumExpressList)
print(configAttributeList)
