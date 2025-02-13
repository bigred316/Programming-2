import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(14, 162)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(244, 55)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(266, 162)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(244, 55)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(246, 38)
		self._label1.TabIndex = 2
		self._label1.Text = "word 1?"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 56)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(246, 38)
		self._label2.TabIndex = 3
		self._label2.Text = "word 2?"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 105)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(246, 38)
		self._label3.TabIndex = 4
		self._label3.Text = "Anagram?"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(264, 105)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(246, 38)
		self._label4.TabIndex = 5
		self._label4.Text = "label4"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(264, 9)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(246, 44)
		self._textBox1.TabIndex = 6
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(264, 56)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(246, 44)
		self._textBox2.TabIndex = 7
		self._textBox2.TextChanged += self.TextBox2TextChanged
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(521, 220)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "anagrams"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		self._label4.Text = ""
		word1 = self._textBox1.Text.lower()
		word2 = self._textBox2.Text.lower()
		if len(word1) != len(word2):
			self._label3.Text = "False"
		else:
			for lcv in range(len(word1)):
				c = word1[lcv]
				index = word2.find(c)
				if index == -1:
					self._label3.Text = "False"
				else:
					word2 = word2[0:index] + word2[index+1:]
		self._label4.Text = str(len(word2)==0)
				
				
					

	def TextBox2TextChanged(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		self._label4.Text = ""