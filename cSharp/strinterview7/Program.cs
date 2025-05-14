using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace strinterview7
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter a string");
            string word = Console.ReadLine().ToLower();
            int vowels = 0;
            int consonants = 0;
            for (int i = 0; i < word.Length; i++)
            {
                char let = word[i];
                if (let == 'a' || let == 'e' || let == 'i' || let == 'o' || let == 'u') vowels++;
                else if (let >= 'a' && let <= 'z') consonants++;//checking ascii table
            }
            Console.WriteLine("There are \"{0}\" Consonants in your string", consonants);
            Console.WriteLine("There are \"{0}\" Vowels in your string", vowels);
            Console.ReadLine();

            
        }
    }
}
