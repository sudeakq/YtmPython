class Siparis:
    @staticmethod
    def odeme_yap(kullanici):
        toplam_tutar = 0

        # Python'da döngü
        for urun in kullanici.urunler:
            toplam_tutar += urun.fiyat  # fiyat özelliği kullanılıyor

        toplam_tutar = kullanici.get_toplam_tutar(toplam_tutar)
        print(f"{type(kullanici).__name__} Toplam Tutar = {toplam_tutar}")