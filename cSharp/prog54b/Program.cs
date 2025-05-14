using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace prog54b
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("enter num1: ");
            int num1 = int.Parse(Console.ReadLine());
            Console.Write("enter num2: ");
            int num2 = int.Parse(Console.ReadLine());
            Console.Write("enter num3: ");
            int num3 = int.Parse(Console.ReadLine());
            Console.Write("enter num4: ");
            int num4 = int.Parse(Console.ReadLine());
            int sum = num1 + num2 + num3 + num4;
            double average = sum / 4;
            Console.WriteLine("Sum: " + sum);
            Console.Write("Average: " + Math.Round(average));
            Console.ReadLine();
        }
    }
}
