class hero:
    jumlahhero = 0  #class variable, diakses dengan nama classnya
    def __init__(self, name, health, power, armor):
        #instance variable, diakses dengan self
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        hero.jumlahhero += 1
        self.__age= 97 #private variable, tidak bisa diakses dari luar class
        self.weight = 50 #public variable, bisa diakses dari luar class

    def siapa(self): #method tanpa return, tanpa argumen
        print("Nama hero adalah"+ self.name)

    def healthup(self, up): #method dengan argumen, tanpa return
        self.health += up

    def gethealth(self):  #method dengan argumen, dengan return
        return self.health

suparman = hero("Suparman", 100, 50, 20)
hero2 = hero("Gatotkaca", 200, 100, 70)

suparman.siapa()
suparman.healthup(10)
print(suparman.gethealth())
print('health :',str(suparman.gethealth()))
print("Jumlah hero yang ada adalah =", hero.jumlahhero)

suparman.__age = 100 #ini tidak bisa diakses dari luar class, karena private
print(suparman.__age) #ini tidak bisa diakses dari luar class, karena private

suparman.weight = 60 #ini bisa diakses dari luar class, karena public
print(suparman.weight) #ini bisa diakses dari luar class, karena public
print(suparman.__dict__) #ini bisa diakses dari luar class, karena public