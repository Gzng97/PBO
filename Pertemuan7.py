#Class pertama: DataPribadi
class DataPribadi:
    def __init__(self, nama, umur):
        self.__nama = nama
        self.__umur = umur
        
    @property
    def nama(self):
        return self.__nama
    
    @property
    def umur(self):
        return self.__umur
    
    @nama.setter
    def nama(self, nama_baru):
        self.__nama =input

    @umur.setter
    def umur(self, umur_baru):
        if input > 0:
            self.__umur = input

