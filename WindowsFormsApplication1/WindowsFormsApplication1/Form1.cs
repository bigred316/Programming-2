using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Configuration;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public class MyUserSettings : ApplicationSettingsBase
        {
            [UserScopedSetting()]
            [DefaultSettingValue("white")]
            public Color BackgroundColor
            {
                get
                {
                    return ((Color)this["BackgroundColor"]);
                }
                set
                {
                    this["BackgroundColor"] = (Color)value;
                }
            }
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            MyUserSettings mus = new MyUserSettings();
            mus.BackgroundColor = Color.AliceBlue;
            this.DataBindings.Add(new Binding("BackColor", mus, "BackgroundColor"));
            mus.Save();
        }
        
    }
}
