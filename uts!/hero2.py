class Hero:
    jumlah_hero = 0 #class variable
    def __init__(self, name, health, power, armor):
        self.name= name
        self.health=health
        self.power=power
        self.armor=armor
        Hero.jumlah_hero +=1
        self.__age=70 #private
        self._weight=110 #protected

    def siapa(self): #method tanpa return, tanpa argumen
        print("Nama hero : "+self.name)

    def healthUp(self,up): #method dengan argumen, tanpa return
        self.health+=up

    def getHealth(self): #method dengan return
        return self.health

superman=Hero('Superman',100,10,6)
hero2=Hero('Wonder Woman',80,10,10)
superman.siapa()
superman.healthUp(10) #menambahkan health object
print('Healthnya : '+str(superman.getHealth()))
print('Jumlah hero : '+str(Hero.jumlah_hero))
print('============ Memanggil var jumlah ===============')
print('punya object : '+str(superman.jumlah_hero))
print('punya class : '+str(Hero.jumlah_hero))
print('=== Nilai jumlah hero di object dirubah ===')
superman.jumlah_hero=10
print('punya object : '+str(superman.jumlah_hero))
print('punya class : '+str(Hero.jumlah_hero))
print('=== Nilai jumlah hero di class dirubah ===')
Hero.jumlah_hero=20
print('punya object : '+str(superman.jumlah_hero))
print('punya class : '+str(Hero.jumlah_hero))

# print('umurnya object : '+str(superman.__age))
superman.__age=17
print((superman.__dict__))
superman._weight=80
print(superman.__dict__)
