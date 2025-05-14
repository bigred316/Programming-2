using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace strinterview16
{
    class Program
    {
        static bool SearchText(string text, string search)
        {
          
            int tLen = text.Length;
            int sLen = search.Length;
            if (sLen > tLen) return false;
            for (int i = 0; i <= tLen - sLen; i++)
            {
                if (text.Substring(i, sLen) == search) return true; // OR if (text[i..(i + sLen)] == search) return true;


            }
            return false;

        }
        static void Main(string[] args)
        {
            Console.Write("Enter a string:");
            string text = Console.ReadLine();
            Console.Write("Enter a string to search for:");
            string search = Console.ReadLine();
            bool result = SearchText(text, search);
            Console.WriteLine("Does \"{0}\" contain \"{1}\"?: {2}", text, search, result);
            Console.ReadLine();




        }
    }
}
