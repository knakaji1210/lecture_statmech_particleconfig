# 粒子のエネルギー準位への可能な配置を計算
import math
import itertools
import numpy as np
from fractions import Fraction
import matplotlib.pyplot as plt
import time

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

def checkEnergyLevel(GroundLevel, NumExpressList, TotalEnergy):
# 基底状態が0か1かでエネルギー準位のリストを作成
    if GroundLevel == 0:
        EnergyLevels = LevelList
    if GroundLevel == 1:
        EnergyLevels = [l+1 for l in LevelList]
    matchedNumExpressList = []
    for i in range(len(NumExpressList)):
        # エネルギーの総和を計算
        EnergySum = np.sum([n * e for (n, e) in zip(NumExpressList[i], EnergyLevels)])
        # エネルギーの総和が全エネルギーに等しい粒子数表示のみを選択
        if EnergySum == TotalEnergy:
            matchedNumExpressList.append(NumExpressList[i])
    return EnergyLevels, matchedNumExpressList

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
    configId = 1
    configAttributeList = []
    for i in range(numConfig):
        # 可能な配置それぞれに対して配置の重みを計算
        weight = calcWeight(matchedNumExpressList[i])
        configAttribute = [configId, matchedNumExpressList[i], weight]
        configId += 1
        configAttributeList.append(configAttribute)
        print('Id{0} : configration = {1}, weight = {2}'.format(configAttribute[0], configAttribute[1],configAttribute[2]))
    # 配置の重みのリストを抽出
    weightList = [w[-1] for w in configAttributeList]
    totalWeight = np.sum(weightList)
    print('The total number of configration = {}'.format(totalWeight))
    print('')
    print('most probable configuration:')
    # 最適配置（配置の重みの値が最大の配置）の抽出
    mostProbConfigId = [i for i, w in enumerate(weightList) if w == max(weightList)]
    mostProbConfigList = []
    for i in mostProbConfigId:
        print('Id{0} : configration = {1}, weight = {2}'.format(configAttributeList[i][0],configAttributeList[i][1],configAttributeList[i][2]))
        mostProbConfigList.append(configAttributeList[i])
    # 最適配置に見出す確率を計算
    prob_MostProbConfig1 = Fraction(int(len(mostProbConfigId)*max(weightList)), int(np.sum(weightList)))
    prob_MostProbConfig2 = len(mostProbConfigId)*max(weightList) / int(np.sum(weightList))  
    print('The probability of most probable configuration = {0} = {1:.3f}'.format(prob_MostProbConfig1, prob_MostProbConfig2))
    return totalWeight, prob_MostProbConfig2, mostProbConfigList

NumLevels = int(input('the number of energy levels: '))
GroundLevel = int(input('the ground state of energy level = 0 or 1: '))
TotalEnergy = int(input('the total energy: '))
NumParticles = int(input('the number of particles: '))

start_time = time.process_time()

LevelList = list(range(NumLevels))
NumExpressList = calcNumExpressList(LevelList, NumParticles)
EnergyLevels, matchedNumExpressList = checkEnergyLevel(GroundLevel, NumExpressList, TotalEnergy)

totalWeight, prob_MostProbConfig2, mostProbConfigList = calcResults(matchedNumExpressList)

# 進行ごとに時間を計測するように変更
end_time = time.process_time()
elapsed_time = end_time - start_time
print('t = {0:.5f} s'.format(elapsed_time))

color_list = ['r', 'b', 'g', 'y']

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(0,NumParticles)

height = 0.3
for i in range(len(mostProbConfigList)):
    eLevel = [e+height*i for e in EnergyLevels]
    ax.barh(eLevel, mostProbConfigList[i][1], height=height, color=color_list[i], align='center')

plt.show()

fig.savefig("./png/distribution.png", dpi=300)