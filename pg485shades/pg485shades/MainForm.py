﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._comboBox2 = System.Windows.Forms.ComboBox()
		self._label3 = System.Windows.Forms.Label()
		self._comboBox3 = System.Windows.Forms.ComboBox()
		self._button1 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# comboBox1
		# 
		self._comboBox1.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
		self._comboBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["Regular",
			"Folding",
			"Roman"]))
		self._comboBox1.Location = System.Drawing.Point(12, 58)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(557, 41)
		self._comboBox1.TabIndex = 0
		self._comboBox1.SelectedIndexChanged += self.ComboBox1SelectedIndexChanged
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(557, 46)
		self._label1.TabIndex = 1
		self._label1.Text = "What type of shades would you like?"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 102)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(557, 46)
		self._label2.TabIndex = 3
		self._label2.Text = "How wide would you like the shades?"
		# 
		# comboBox2
		# 
		self._comboBox2.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
		self._comboBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._comboBox2.FormattingEnabled = True
		self._comboBox2.Items.AddRange(System.Array[System.Object](
			["25 in.",
			"27 in.",
			"32 in.",
			"40 in."]))
		self._comboBox2.Location = System.Drawing.Point(12, 151)
		self._comboBox2.Name = "comboBox2"
		self._comboBox2.Size = System.Drawing.Size(557, 41)
		self._comboBox2.TabIndex = 2
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 195)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(610, 46)
		self._label3.TabIndex = 5
		self._label3.Text = "What color would you like your shades?"
		# 
		# comboBox3
		# 
		self._comboBox3.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
		self._comboBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._comboBox3.FormattingEnabled = True
		self._comboBox3.Items.AddRange(System.Array[System.Object](
			["Natural",
			"Blue",
			"Teal",
			"Red",
			"Green"]))
		self._comboBox3.Location = System.Drawing.Point(12, 244)
		self._comboBox3.Name = "comboBox3"
		self._comboBox3.Size = System.Drawing.Size(557, 41)
		self._comboBox3.TabIndex = 4
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 292)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(263, 87)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate Price"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(283, 292)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(286, 87)
		self._label4.TabIndex = 7
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
		self.ClientSize = System.Drawing.Size(652, 383)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._comboBox3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._comboBox2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._comboBox1)
		self.Name = "MainForm"
		self.Text = "pg485shades"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)


	def ComboBox1SelectedIndexChanged(self, sender, e):
		pass

	def MainFormLoad(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		price = 50
		style = self._comboBox1.Text
		color = self._comboBox3.Text
		width = self._comboBox2.Text
		if style == "Roman":
			price += 15
		elif style == "Folding":
			price += 10
		if color == "Natural":
			price += 5
		if width == "27 in.":
			price += 2
		elif width == "32 in.":
			price += 4
		elif width == "40 in.":
			price += 6
		self._label4.Text = "Your shades will cost $" + str(price)
		