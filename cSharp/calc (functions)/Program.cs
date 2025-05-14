using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace calc__functions_
{
    class Program
    {
        //functions
        static int add(int x, int y) {return x+y}

        static int subtract(int x, int y) {return x-y}
        static int mult(int x, int y) { return x*y}
        static int div(int x, int y) {return x,y}
        static void wait() { //void means returns nothing
            Console.ReadLine();
        }
        
        static void Main(string[] args)
        {
            // access level static or not return type name(args) {}
            //in console app so always static
            //not static in forms apps; always "public"
            //static = doesnt use class variables
            Random rand = new Random;
            int n1 = rand.Next(1,100);
            int n2 = rand.Next(150, 200);
            Console.Write("Choose an option: add, sub, mult, or div");
            string op = Console.ReadLine().ToLower();
            int result = 0;
            if (op == "add"){
                result = add(n1,n2);

            }else if (op == "sub"){
                result = subtract(n1,n2);
            }else if (op == "mult"){
                result = mult(n1,n2);
            }else if (op == "div"){
                result = div(n1,n2);
            }else{
                Console.WriteLine("Error");
            }




        }
    }
}
