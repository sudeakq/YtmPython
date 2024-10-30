using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SRP
{
    public class Program
    {
        static void Main(string[] args) 
        {
            Kullanici kullanici = new Kullanici();
            kullanici.Isim="Yunus Emre Görmüş";
            kullanici.Mail="yunusgormus812@gmail.com";

            Adres adres = new Adres();
            adres.Ulke = "Türkiye";
            adres.Il="Trabzon";
            adres.Ilce="Of";


            kullanici.adresGuncelle(adres);

            Console.WriteLine(kullanici.ToString());

            adres.PostaKodu=61000;
            kullanici.adresGuncelle(adres);

            Console.WriteLine(kullanici.ToString());
            Console.ReadKey();

        }
        
       
        
    }
}
