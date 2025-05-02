using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lp_4_2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("please input weight in kilos");
            double weight = double.Parse(Console.ReadLine());
            Console.WriteLine("please input length in cm");
            double length = double.Parse(Console.ReadLine());
            Console.WriteLine("please input width in cm");
            double width = double.Parse(Console.ReadLine());
            Console.WriteLine("please input height in cm");
            double height = double.Parse(Console.ReadLine());
            if (length * width * height >= 100000 && weight > 27)
            {
                Console.WriteLine("The package is too heavy and too large");
            }
            else if (length * width * height >= 100000)
            {
                Console.WriteLine("Your package is too large");
            }
            else if (weight > 27)
            {
                Console.WriteLine("Your package is too heavy");
            }
            else
            {
                Console.WriteLine("your package is good to ship!");
                Console.ReadLine();
            }
            



        }
    }
}
