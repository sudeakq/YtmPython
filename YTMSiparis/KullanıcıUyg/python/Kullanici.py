class Kullanici:
    def __init__(self, isim=None, mail=None, adres=None):
        self._isim = isim
        self._mail = mail
        self._adres = adres

    @property
    def isim(self):
        return self._isim

    @isim.setter
    def isim(self, value):
        self._isim = value

    @property
    def mail(self):
        return self._mail

    @mail.setter
    def mail(self, value):
        self._mail = value

    @property
    def adres(self):
        return self._adres

    @adres.setter
    def adres(self, value):
        self._adres = value

    def adres_guncelle(self, yeni_adres):
        self.adres = yeni_adres

    def giris_yap(self):
        print("Giriş Yapıldı.")

    def __str__(self):
        return f"{self.isim} {self.mail} {self.adres}"