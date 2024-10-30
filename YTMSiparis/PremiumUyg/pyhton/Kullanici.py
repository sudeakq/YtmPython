class Kullanici:
    def __init__(self):
        self.id = None  # id için bir başlangıç değeri
        self.isim = None  # isim için bir başlangıç değeri
        self.mail = None  # mail için bir başlangıç değeri
        self.urunler = []  # ürünler listesi

    def get_toplam_tutar(self, fiyat):
        raise NotImplementedError("Bu metot, alt sınıflar tarafından geçersiz kılınmalıdır.")

    @property
    def isim(self):
        return self.isim

    @property
    def urunler(self):
        return self.urunler

    def get_urun(self, index):
        return self.urunler[index]

    def add_urun(self, urun):
        self.urunler.append(urun)