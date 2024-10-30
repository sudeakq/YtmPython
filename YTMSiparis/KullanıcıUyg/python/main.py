import Kullanici, Adres


kullanici = Kullanici()
kullanici.isim = "Yunus Emre Görmüş"
kullanici.mail = "yunusgormus812@gmail.com"

adres = Adres()
adres.ulke = "Türkiye"
adres.il = "Trabzon"
adres.ilce = "Of"

kullanici.adres_guncelle(adres)

print(kullanici)

adres.posta_kodu = 61000
kullanici.adres_guncelle(adres)

print(kullanici)