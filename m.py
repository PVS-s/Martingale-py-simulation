import math
import random


def Spin():
    r = random.randrange(0, 38) # european version, from 0 to 37, we're bettin' on reds and blacks from 1(included) to 18(not included)
#    if r == 0:
 #       print(False, 'Retry')
    if 0 < r < 18:
#        print(r, 'You placed 10 dollars and won')
        return True
    else:
#        print(r, 'You placed 10 dollars and lost')
        return False
    return

Spin()




def Martingale():
    IntitialMoney = int(1000)
    CurrentMoney = IntitialMoney
    TableLimit = int(500)
    Goal = int(50)
    TotalGoal = IntitialMoney + Goal
    BetSeed = int(10)
    CurrentBet = BetSeed
    while True:
        CurrentMoney -= CurrentBet;
        if CurrentMoney < 0.0:
#            print(False, 'You lost all of your money')
            return False
        if Spin():
            CurrentMoney += CurrentBet * 2
            CurrentBet = BetSeed
            if CurrentMoney >= TotalGoal:
#                print("It's", True, 'You actually did it, what a surprise')
                return True
        else:
            CurrentBet *= 2
            if CurrentBet > TableLimit:
                CurrentBet = BetSeed


# million people walk into a casino and play using martingale system 
wins = []
balance = []

for i in range(0,1000000): 
    x = Martingale()
#    print(x)
    if x == True:
         plus = 1
         wintime = 50
         wins.append(plus)
         balance.append(wintime)
    else:
         lost = "-1000"
         balance.append(lost)

#count itmes on a list and assign a variable
win = wins.count(1)
balancing = balance.count(50)
fall = balance.count("-1000")
balancingreale = balancing * 50
realfall = fall * 1000
realsum = balancingreale - realfall
#print(balancing)
#print(fall)
print(balancingreale)
print(realfall)
print(realsum)

# %
totals = win/1000000
winExpected = math.log(0.5, totals)
print("The punters won $" + str(realsum))
print("Expected walk in and out with an extra $50 is " + str(winExpected) + " times")
print('% of ppl that won: ' + str(totals))



# 43875000 =  balancing
# 122500000 =  fall
# -78625000 =  realsum = total money won
# The punters won $-78625000, do you see how much money they "won"?
# Expected walk in and out with an extra $50 is 5.304224612325462 times
# % of ppl that won: 0.8775
# if there's a 94% chance we'll win $50 and a 6% chance we'll lose 1000, then our expected value for this bet is -$13
# log(sub 0.94)0.5 = 11.2, means we're likely to lose at least once if we try Martingale 12 times with the odds above
# it's likely to lose $1000 before we gain 12*$50 = $600
# so would you stake $1000 for a 48% chance at winning $600? of course not.
