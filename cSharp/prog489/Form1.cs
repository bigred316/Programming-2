using Microsoft.VisualBasic;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace prog489
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        const int intMAX_EMPLOYEES = 5;
        const decimal decHOURLY_PAY_RATE = 6.0m;
        private void button1_Click(object sender, EventArgs e)
        {
            //calc and display gross pay earned by  the employed
            int[] intHours = new int[intMAX_EMPLOYEES]; // array
            // <type>[] varName = new <type>[capacity];
            int intCount = 0;
            int EmpHours = 0;
            decimal EmpPay = 0;
            for (intCount = 0; intCount < intMAX_EMPLOYEES; intCount++)
            {
                while (int.TryParse(
                    Interaction.InputBox("Enter # of hours worked by employees" + (intCount+1).ToString(), "Need hours worked"),
                    out EmpHours) == false)
                {
                    MessageBox.Show("Please enter an integer for hours worked");
                }
            }


        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
