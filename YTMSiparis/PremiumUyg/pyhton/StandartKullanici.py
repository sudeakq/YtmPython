import Kullanici


class StandartKullanici(Kullanici):
    def get_toplam_tutar(self, fiyat):
        return fiyat  # Standart kullanıcı için fiyatı olduğu gibi döner