import Kullanici


class PremiumKullanici(Kullanici):
    def get_toplam_tutar(self, fiyat):
        return fiyat * 0.9  # Premium kullanıcı için %10 indirim