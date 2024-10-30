using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SRP
{
    public class Kullanici
    {
        private string isim {  get; set; }
        private string mail { get; set; }
        private Adres adres;
        public string Isim
        {
            get { return isim; }
            set { isim = value; }
        }

        public string Mail
        {
            get { return mail; }
            set { mail = value; }
        }

        public Adres Adres
        {
            get { return adres; }
            set { adres = value; }
        }
        public void adresGuncelle(Adres adres)
        {
            this.adres = adres;
        }
        public string getAdres()
        {
            return adres.ToString();
        }
        public override string ToString()
        {
            return $"{isim} {mail} {getAdres()}";
        }
        public void girisYap()
        {
            Console.WriteLine("Giriş Yapıldı.");
        }
    }
}
