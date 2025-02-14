import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(75, 283)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(386, 61)
		self._button1.TabIndex = 0
		self._button1.Text = "show new form"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(31, 73)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(472, 29)
		self._textBox1.TabIndex = 1
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(534, 376)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "multiforms"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		from Form1 import *
		msg = self._textBox1.Text
		form1 = Form1(self, msg)
		form1.Show()
		self.Hide()
		
		"""from SecondForm import *
		form2 = SecondForm()
		form2.Show()"""

	def MainFormLoad(self, sender, e):
		pass
