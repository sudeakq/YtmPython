using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace OCP
{
    public abstract class Kullanici
    {
        protected int id;
        protected string isim;
        protected string mail;
        protected List<Urun> urunler;

        public Kullanici()
        {
            urunler = new List<Urun>();
        }
        public abstract double GetToplamTutar(double fiyat);
        public string Isim
        {
            get { return isim; }
        }
        public List<Urun> Urunler { get { return urunler; } }
        public Urun GetUrun(int index)
        {
            return Urunler[index];
        }
        public void AddUrun(Urun urun)
        {
            Urunler.Add(urun);
        }
    }
}

