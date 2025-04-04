import System.Drawing
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
		self._label5 = System.Windows.Forms.Label()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._checkBox4 = System.Windows.Forms.CheckBox()
		self._checkBox5 = System.Windows.Forms.CheckBox()
		self.SuspendLayout()
		# 
		# comboBox1
		# 
		self._comboBox1.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
		self._comboBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["The Master Thrasher ($60)",
			"The Dictator of Grind ($45)",
			"The Street King ($50)"]))
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
		self._label1.Text = "What deck would you like?"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 102)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(557, 46)
		self._label2.TabIndex = 3
		self._label2.Text = "What axle would you like?"
		# 
		# comboBox2
		# 
		self._comboBox2.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
		self._comboBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._comboBox2.FormattingEnabled = True
		self._comboBox2.Items.AddRange(System.Array[System.Object](
			["7.75 Axle ($35)",
			"8 Axle ($40)",
			"8.5 Axle ($45)",
			""]))
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
		self._label3.Size = System.Drawing.Size(557, 46)
		self._label3.TabIndex = 5
		self._label3.Text = "What wheels would you like?"
		# 
		# comboBox3
		# 
		self._comboBox3.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
		self._comboBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._comboBox3.FormattingEnabled = True
		self._comboBox3.Items.AddRange(System.Array[System.Object](
			["51mm ($20)",
			"55 mm ($22)",
			"58 mm ($24)",
			"61 mm($28)"]))
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
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(587, 9)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(319, 46)
		self._label5.TabIndex = 8
		self._label5.Text = "Misc."
		# 
		# checkBox1
		# 
		self._checkBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox1.Location = System.Drawing.Point(621, 69)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(196, 30)
		self._checkBox1.TabIndex = 9
		self._checkBox1.Text = "Grip Tape ($10)"
		self._checkBox1.UseVisualStyleBackColor = True
		# 
		# checkBox2
		# 
		self._checkBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox2.Location = System.Drawing.Point(621, 118)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(196, 30)
		self._checkBox2.TabIndex = 10
		self._checkBox2.Text = "Bearings ($30)"
		self._checkBox2.UseVisualStyleBackColor = True
		# 
		# checkBox3
		# 
		self._checkBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox3.Location = System.Drawing.Point(621, 162)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(196, 30)
		self._checkBox3.TabIndex = 11
		self._checkBox3.Text = "Riser Pads ($2)"
		self._checkBox3.UseVisualStyleBackColor = True
		# 
		# checkBox4
		# 
		self._checkBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox4.Location = System.Drawing.Point(621, 211)
		self._checkBox4.Name = "checkBox4"
		self._checkBox4.Size = System.Drawing.Size(226, 30)
		self._checkBox4.TabIndex = 12
		self._checkBox4.Text = "Nuts and Bolts ($3)"
		self._checkBox4.UseVisualStyleBackColor = True
		# 
		# checkBox5
		# 
		self._checkBox5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox5.Location = System.Drawing.Point(621, 255)
		self._checkBox5.Name = "checkBox5"
		self._checkBox5.Size = System.Drawing.Size(196, 30)
		self._checkBox5.TabIndex = 13
		self._checkBox5.Text = "Assembly ($10)"
		self._checkBox5.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
		self.ClientSize = System.Drawing.Size(918, 383)
		self.Controls.Add(self._checkBox5)
		self.Controls.Add(self._checkBox4)
		self.Controls.Add(self._checkBox3)
		self.Controls.Add(self._checkBox2)
		self.Controls.Add(self._checkBox1)
		self.Controls.Add(self._label5)
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
		price = 0
		body = self._comboBox1.Text
		axle = self._comboBox2.Text
		wheel = self._comboBox3.Text
		price = 0
		if body == "The Master Thrasher ($60)":
			price += 60
		if body == "The Dictator of Grind ($45)":
			price += 45
		if body == "The Street King ($50)":
			price += 50
		if axle == "7.75 Axle ($35)":
			price += 35
		if axle == "8 Axle ($40)":
			price += 40
		if axle == "8.5 Axle ($45)":
			price += 45
		if wheel == "51mm ($20)":
			price += 20
		if wheel == "55 mm ($22)":
			price += 22
		if wheel == "58 mm ($24)":
			price +=24
		if wheel == "61 mm($28)":
			price +=28
		if self._checkBox1.Checked:
			price += 10
		if self._checkBox2.Checked:
			price += 30
		if self._checkBox3.Checked:
			price += 2
		if self._checkBox4.Checked:
			price += 3
		if self._checkBox5.Checked:
			price += 10		

		
		self._label4.Text = "Your total is $" + str(price)
