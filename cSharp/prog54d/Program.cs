using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace prog54d
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("What is the base of the triangle");
            double bas = double.Parse(Console.ReadLine());
            Console.WriteLine("What is the height of the triangle");
            double height = double.Parse(Console.ReadLine());
            double hyp = Math.Sqrt(Math.Pow(bas , 2) + Math.Pow(height,2));
            double perim = hyp + height + bas;
            double area = 0.5 * bas * height;
            Console.WriteLine("The Hypotenuse is equal to " + hyp);
            Console.WriteLine("The Area is equal to " + area);
            Console.WriteLine("The Perimeter is equal to " + perim);
            Console.ReadLine();



        }
    }
}
