using System;
using System.Configuration;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace testingfiles
{
    

    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
    public class MyUserSettings:ApplicationSettingsBase {
        [UserScopedSetting()]
        [DefaultSettingValue("")]
        public string BackgroundColor
        {
            get
            {
                return ((string)this["BackgroundColor"]);
            }
            set
            {
                this["BackgroundColor"] = (string)value;
            }
        }
    }

        private void button1_Click(object sender, EventArgs e)
        {
            label1.Text =Properties.Settings.Default.Username1;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Properties.Settings.Default.Username1 = textBox1.Text;
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            Properties.Settings.Default.Save();
        }
        
        private void button3_Click(object sender, EventArgs e)
        {
            MyUserSettings mus = new MyUserSettings();
            mus.BackgroundColor = "fartballs";
            this.DataBindings.Add(new Binding("string", mus, "string"));
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}


