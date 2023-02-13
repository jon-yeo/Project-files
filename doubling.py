import random
import numpy as np

#0 is win, 1 is lose
def doublefunc(start_amt, total_amt, times):
    for x in range(times):
        print("Bet amount: " + str(start_amt))
        print("Amount of money left: " + str(total_amt))
        if total_amt > 0 and start_amt < total_amt:
            result = random.randint(0,1)
            if(result == 0):
                total_amt += start_amt
            else:
                total_amt -= start_amt
                start_amt *= 2
        else:
            break
    print("Next"+ "\n")
    return total_amt

trys = 10

start_bet_amt = 1
total_money = 300
num_times_bet = 100

#0 - 50
range_1 = 0
#51 - 100
range_2 = 0
#101 - 150
range_3 = 0
#151 - 200
range_4 = 0
#201 - 250
range_5 = 0
#251 - 300
range_6 = 0
#more than 300
range_7 = 0

for x in range(trys):
    amount = doublefunc(start_bet_amt, total_money, num_times_bet)
    if(amount <= 50):
        range_1 += 1
    elif(50 < amount <= 100):
        range_2 += 1
    elif(100 < amount <= 150):
        range_3 += 1
    elif(150 < amount <= 200):
        range_4 += 1
    elif(200 < amount <= 250):
        range_5 += 1
    elif(250 < amount <= 300):
        range_6 += 1
    elif(amount > 300):
        range_7 += 1

print("Collation of trials")        
print("0 - 50: " + str(range_1))
print("51 - 100: " + str(range_2))
print("101 - 150: " + str(range_3))
print("151 - 200: " + str(range_4))
print("201 - 250: " + str(range_5))
print("251 - 300: " + str(range_6))
print("More than 300: " + str(range_7))
