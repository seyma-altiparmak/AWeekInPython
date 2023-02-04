#Question 3
#Maksimum point is '20'
# GS vs FB here we go.

import random

class GS:
    point = random.randint(0,20)
    faul = random.randint(0,3)

class FB:
    point = random.randint(0,20)
    faul = random.randint(0,3)

if GS.point > FB.point and GS.faul != 3:
    winner = "Galatasaray"
    print("GS - FB :" + str(GS.point) + " - " + str(FB.point))
    print(winner)
elif GS.point < FB.point and FB.faul != 3:
    winner = "Fenerbahce"
    print("GS - FB :" + str(GS.point) + " - " + str(FB.point))
    print(winner)
elif GS.point == FB.point and FB.faul != 3 and GS.faul !=3:
    winner = "Draw"
    print("GS - FB :" + str(GS.point) + " - " + str(FB.point))
    print(winner)
else:
    print("Due to the disrespect of the people, one side was forfeited in the match.")
    if GS.faul == 3 and FB.faul == 3:
        print("NO Winner")
    elif GS.faul == 3 or FB.faul == 3 :
        if GS.faul == 3:
            winner = "Fenerbahce"
            print("Winner is : " + winner)
        else:
            winner = "Galatasaray"
            print("Winner is : "+winner)
    else:
        pass