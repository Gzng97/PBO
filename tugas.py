class hero():
    jumlahhero = 0
    def __init__(self,name, health, power, armor) :
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        hero.jumlahhero += 1
    
hero1 = hero("angela", "130", "200", "50")
hero2 = hero("gatotkaca", "200", "100", "70")
hero3 = hero("alucrot", "999", "999", "999")

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
print("Jumlah hero yang ada adalah =", hero.jumlahhero)


select = input("Pilih hero 1-3 : ")
if select == "1":
    print(hero1.name, ",Health :", hero1.health, ",Power :", hero1.power, ",Armor :", hero1.armor)
if select == "2":
    print(hero2.name,",Health :", hero2.health, ",Power :", hero2.power, ",Armor :", hero2.armor)
if select == "3":
    print(hero3.name,",Health :", hero3.health, ",Power :", hero3.power, ",Armor :", hero3.armor)
