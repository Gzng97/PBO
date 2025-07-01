class Hero:

    __jumlah = 0

    def __init__(self, nama, health, attPower, armor):
        self.__nama = nama
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level
        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return "{} level {}:\n\thealth = {}/{}\n\tattack = {}\n\tarmor = {}".format(
            self.__nama, self.__level, self.__health, self.__healthMax,
            self.__attPower, self.__armor
        )

    @property
    def status(self):
        return "EXP: {} | Level: {}".format(self.__exp, self.__level)

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        while self.__exp >= 100:
            print(f"{self.__nama} level up!")
            self.__level += 1
            self.__exp -= 100
            # Update stats
            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level
            self.__health = self.__healthMax  # Optional: refill health on level up

    def attack(self, musuh):
        print(f"{self.__nama} menyerang {musuh.__nama} dengan power {self.__attPower}")
        musuh.terimaSerangan(self.__attPower)
        self.gainExp = 50

    def terimaSerangan(self, power):
        damage = max(0, power - self.__armor)
        self.__health -= damage
        print(f"{self.__nama} menerima {damage} damage! (armor: {self.__armor})")
        if self.__health <= 0:
            self.__health = 0
            print(f"{self.__nama} telah kalah!")

# Contoh penggunaan
sladar = Hero('Sladar', 100, 5, 10)
axe = Hero('Axe', 100, 5, 10)

print(sladar.info)
print(axe.info)

# Sladar menyerang Axe beberapa kali
for i in range(3):
    print(f"\nSerangan ke-{i+1}")
    sladar.attack(axe)

print("\nStatus akhir:")
print(sladar.info)
print(sladar.status)
print(axe.info)