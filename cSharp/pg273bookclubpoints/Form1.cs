using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace pg273bookclubpoints
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int books = int.Parse(textBox1.Text);
            int points = 0;
            if (books <= 0) points = 0;
            else if (books == 1) points = 5;
            else if (books ==2) points = 15;
            else if (books ==3) points = 30;
            else if (books >= 4) points = 60;


            label2.Text = "Your purchase earned you " + points.ToString() + " points!";
        }
    }
}
