import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(21, 103)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(262, 40)
		self._label2.TabIndex = 1
		self._label2.Text = "Duplicates"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(21, 45)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(262, 40)
		self._label3.TabIndex = 2
		self._label3.Text = "Enter Text:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(298, 103)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(262, 40)
		self._label4.TabIndex = 3
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(46, 259)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 4
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(298, 45)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(262, 40)
		self._textBox1.TabIndex = 5
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaption
		self.ClientSize = System.Drawing.Size(717, 427)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Name = "MainForm"
		self.Text = "interview questions"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		self._label3.Text = ""
		myStr = self._textBox1.Text.lower()
		for lcv in range (len(myStr)):
			for lcv2 in range(lcv + 1, len(myStr)):
				ltr1 = myStr[lcv]
				ltr= myStr[lcv2]
				if ltr1 == ltr2:
					self._label3.Text += ltr2 + ""