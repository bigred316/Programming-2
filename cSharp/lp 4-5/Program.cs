using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lp_4_5
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter grade percent:");
            double grade = double.Parse(Console.ReadLine());
            char letGrade = ' ';
            if (grade > 90)
            {
                letGrade = 'A';

            }
            else if (grade >= 80)
            {
                letGrade = 'B';

            }
            else if (grade >= 70){

            
                letGrade = 'C';
            }
            else if (grade >= 60)
            {
                letGrade = 'D';

            }
            else { letGrade = 'F'; }
            Console.WriteLine(letGrade);
            Console.WriteLine();


                

        }
    }
}
