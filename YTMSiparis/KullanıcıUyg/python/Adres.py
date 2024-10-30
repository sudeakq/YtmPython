class Adres:
    def __init__(self, ulke=None, il=None, ilce=None, posta_kodu=None):
        self._ulke = ulke
        self._il = il
        self._ilce = ilce
        self._posta_kodu = posta_kodu

    @property
    def ulke(self):
        return self._ulke

    @ulke.setter
    def ulke(self, value):
        self._ulke = value

    @property
    def il(self):
        return self._il

    @il.setter
    def il(self, value):
        self._il = value

    @property
    def ilce(self):
        return self._ilce

    @ilce.setter
    def ilce(self, value):
        self._ilce = value

    @property
    def posta_kodu(self):
        return self._posta_kodu

    @posta_kodu.setter
    def posta_kodu(self, value):
        self._posta_kodu = value

    def __str__(self):
        return f"{self.ulke}, {self.il}, {self.ilce}, Posta Kodu: {self.posta_kodu}"