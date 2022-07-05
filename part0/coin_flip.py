# Coin Flip Streaks


import random

streaks=0
total=10 # Simplifying calculations
reps=10

for experimentNumber in range(total):
    coin_flips=[] # You must reset the coin_flips list. Your program keeps appending values to ur list without deleting the old ones.

    for j in range(reps):
        coin_flips.append(random.choice(['H','T']))

    repetition=1 # any flip is a streak of at least 1
    for i in range(1,len(coin_flips)):
        if coin_flips[i]== coin_flips[i-1]:
            repetition+=1
        else:
            repetition=1
        if repetition==4:
            streaks+=1
            break

    print(coin_flips)


total_strks=(reps//4)*total # calculating the total num of strks within all lists

streaks_per=100*streaks/total_strks # calculating the percent of strks

print('Chance of streak: %s%%' % (streaks_per))
print(f'{streaks} of {total_strks}') # In order to test the streaks' counter