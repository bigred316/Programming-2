import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(152, 6)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(261, 47)
		self._textBox1.TabIndex = 0
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(134, 39)
		self._label1.TabIndex = 1
		self._label1.Text = "Radius"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
		self._label2.Font = System.Drawing.Font("Microsoft Tai Le", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 76)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(401, 121)
		self._label2.TabIndex = 2
		self._label2.Text = "label2"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.White
		self._button1.Location = System.Drawing.Point(12, 210)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(134, 69)
		self._button1.TabIndex = 3
		self._button1.Text = "Calc"
		self._button1.UseVisualStyleBackColor = False
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.White
		self._button2.Location = System.Drawing.Point(139, 210)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(143, 69)
		self._button2.TabIndex = 4
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.White
		self._button3.Location = System.Drawing.Point(279, 210)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(134, 69)
		self._button3.TabIndex = 5
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self.ClientSize = System.Drawing.Size(433, 290)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "prog54c"
		self.ResumeLayout(False)
		self.PerformLayout()

