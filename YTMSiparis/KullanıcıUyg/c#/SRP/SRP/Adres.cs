using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SRP
{
    public class Adres
    {
        private string il {  get; set; }
        private string ulke {  get; set; }
        private string ilce {  get; set; }
        private int postaKodu {  get; set; }
        public string Ulke
        {
            get { return ulke; }
            set { ulke = value; }
        }

        public string Il
        {
            get { return il; }
            set { il = value; }
        }

        public string Ilce
        {
            get { return ilce; }
            set { ilce = value; }
        }

        public int PostaKodu
        {
            get { return postaKodu; }
            set { postaKodu = value; }
        }

        public override string ToString()
        {
            return $"{ulke}{il}{ilce}{postaKodu}";
        }
    }
}
