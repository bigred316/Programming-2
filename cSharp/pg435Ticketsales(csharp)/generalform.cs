using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace pg435Ticketsales_csharp_
{
    public partial class generalform : Form
    {
        private Form myParent;
        public generalform()
        {
            InitializeComponent();
            this.myParent = myParent;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.myParent.Show();
            this.Close();

        }

        private void generalform_FormClosing(object sender, FormClosingEventArgs e)
        {
            this.myParent.Show();
        }
        //TODO: tax
    }
}
