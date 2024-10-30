using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OCP
{
    public class PremiumKullanici:Kullanici
    {
        public override double GetToplamTutar(double fiyat)
        {
            return fiyat * 0.9;
        }
    }
}
