using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OCP
{
    public class Urun
    {
        protected int id {  get; set; }
        protected string isim {  get; set; }
        protected double fiyat { get; set; }
        public Urun(string isim,double fiyat) 
        {
            this.isim=isim;
            this.fiyat = fiyat;
        }

        public double Fiyat
        {
            get { return fiyat; } 
        }
    }
}
