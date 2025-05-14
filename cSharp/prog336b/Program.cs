using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace prog336b
{
    class Program
    {
        static int f(int x){return (int)Math.Pow(x, 2)-x + 41};
        static bool IsPrime(int n, int f) {
            if (n<=1) return false;
            if (n==2 || f*f > n) return true;
            if (n % f == 0) return false;}
        static int FindSmallestFactor(int n) {
            for (int i =2; i <= Math.Sqrt(n); i++)
                if (n% i == 0) return i;
            return n;
        }
        }

        static void Main(string[] args)
        {
            interface x =1;
                while (true) {
                int num = f(x);
                if (IsPrime(num , 2))
            }
        }
    }
}
