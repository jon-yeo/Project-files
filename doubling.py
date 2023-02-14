import random
import numpy as np

#0 is win, 1 is lose
def doublefunc(start_amt, total_amt, times):
    for x in range(times):
        if total_amt > 0 and start_amt < total_amt:
            result = random.randint(0,1)
            if(result == 0):
                total_amt += start_amt
            else:
                total_amt -= start_amt
                start_amt *= 2
        else:
            break
    return total_amt

trys = 10000

start_bet_amt = 1
total_money = 30000
num_times_bet = 100

#0 - 5000
range_1 = 0
#5100 - 10000
range_2 = 0
#10100 - 15000
range_3 = 0
#15100 - 20000
range_4 = 0
#20100 - 25000
range_5 = 0
#25100 - 30000
range_6 = 0
#more than 30000
range_7 = 0

for x in range(trys):
    amount = doublefunc(start_bet_amt, total_money, num_times_bet)
    if(amount <= 5000):
        range_1 += 1
    elif(5000 < amount <= 10000):
        range_2 += 1
    elif(10000 < amount <= 15000):
        range_3 += 1
    elif(15000 < amount <= 20000):
        range_4 += 1
    elif(20000 < amount <= 25000):
        range_5 += 1
    elif(25000 < amount <= 30000):
        range_6 += 1
    elif(amount > 30000):
        range_7 += 1

print("Collation of trials")        
print("0 - 50: " + str((range_1 / trys) * 100) + "%")
print("51 - 100: " + str((range_2 / trys) * 100) + "%")
print("101 - 150: " + str((range_3 / trys) * 100) + "%")
print("151 - 200: " + str((range_4 / trys) * 100) + "%")
print("201 - 250: " + str((range_5 / trys) * 100) + "%")
print("251 - 300: " + str((range_6 / trys) * 100) + "%")
print("More than 300: " + str((range_7 / trys) * 100) + "%")
