using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OCP
{
    public class Siparis
    {
        public static void OdemeYap(Kullanici kullanici)
        {
            double toplamTutar = 0;

            // C#'ta foreach döngüsü
            foreach (Urun urun in kullanici.Urunler)
            {
                toplamTutar += urun.Fiyat; // Fiyat özelliği kullanılıyor
            }

            toplamTutar = kullanici.GetToplamTutar(toplamTutar);
            Console.WriteLine($"{kullanici.GetType().Name} Toplam Tutar = {toplamTutar}");
        }
    }
}
