import PremiumKullanici
import Siparis
import StandartKullanici
import Urun


class Program:
    @staticmethod
    def main():
        ali = StandartKullanici()
        veli = PremiumKullanici()

        telefon = Urun("telefon", 3000)
        bilgisayar = Urun("bilgisayar", 5000)

        ali.add_urun(telefon)
        ali.add_urun(bilgisayar)

        veli.add_urun(telefon)
        veli.add_urun(bilgisayar)

        Siparis.odeme_yap(ali)
        Siparis.odeme_yap(veli)

if __name__ == "__main__":
    Program.main()