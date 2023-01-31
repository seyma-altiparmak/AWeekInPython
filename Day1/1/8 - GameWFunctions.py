CharactersPowers = {
    "Heidi" : 1000,
    "Ales" : 500,
    "Xavier" : 740
}

CharactersHealth = {
    "Heidi" : 500,
    "Ales" : 500,
    "Xavier" : 100
}

def attack(power:dict,hpn:dict,choosed,enemy):
    ACAN = power[choosed]
    hpn[enemy] = power[choosed] - ACAN

def choose(CHM,CHE):
    myPow = Powers(CHM)
    enemyPow = Powers(CHE)

def Powers(X):
    if CHM=="A" or "a":
        power = CharactersPowers.get("Heidi")
        hpn = CharactersHealth.get("Heidi")
    elif CHM=="B" or "b":
        power = CharactersPowers.get("Ales")
        hpn = CharactersHealth.get("Ales")
    elif CHM == "C" or "c":
        power= CharactersPowers.get("Xavier")
        hpn = CharactersHealth.get("Xavier")
    else:
        print("UNDEFINED.")

def XAt():
    me = str(input("""
    Choose your character
    A.Heidi
    B.Ales
    C.Xavier
    """))
    you = str(input("""
    Choose enemy character
    A.Heidi
    B.Ales
    C.Xavier
    """))
    choose(me,you)

while True:
    XAt()