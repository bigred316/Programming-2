using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace prog85cpt2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            label1.Text = ("");
            double num = int.Parse(textBox1.Text);
            double month = 0;
            double day = 0;
            num -= 165;
            month = Math.Floor(num/100);
            day = num/100 - month;
            day *= 100;
            label1.Text = ("Your birthday is " + month.ToString() + "/" + day.ToString());


            
            




        }
    }
}
