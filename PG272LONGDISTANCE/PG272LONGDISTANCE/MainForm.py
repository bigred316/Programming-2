import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._label1 = System.Windows.Forms.Label()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
		self._groupBox1.Controls.Add(self._radioButton3)
		self._groupBox1.Controls.Add(self._radioButton2)
		self._groupBox1.Controls.Add(self._radioButton1)
		self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox1.Location = System.Drawing.Point(22, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(391, 290)
		self._groupBox1.TabIndex = 3
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "What time is it?"
		self._groupBox1.Enter += self.GroupBox1Enter
		# 
		# radioButton1
		# 
		self._radioButton1.Location = System.Drawing.Point(6, 43)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(358, 72)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "6:00 a.m. - 5:59 p.m."
		self._radioButton1.UseVisualStyleBackColor = True
		self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
		# 
		# radioButton2
		# 
		self._radioButton2.Location = System.Drawing.Point(6, 112)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(379, 72)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "6:00 p.m. - 11:59 p.m. "
		self._radioButton2.UseVisualStyleBackColor = True
		self._radioButton2.CheckedChanged += self.RadioButton2CheckedChanged
		# 
		# radioButton3
		# 
		self._radioButton3.Location = System.Drawing.Point(6, 175)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(379, 72)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "12:00 a.m. - 5:59 a.m."
		self._radioButton3.UseVisualStyleBackColor = True
		self._radioButton3.CheckedChanged += self.RadioButton3CheckedChanged
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(533, 34)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(14, 23)
		self._label1.TabIndex = 4
		self._label1.Text = "label1"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self.ClientSize = System.Drawing.Size(903, 317)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "pg272longdistance"
		self.Load += self.MainFormLoad
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)


	def MainFormLoad(self, sender, e):
		pass

	def GroupBox1Enter(self, sender, e):
		pass

	def RadioButton2CheckedChanged(self, sender, e):
		pass

	def RadioButton1CheckedChanged(self, sender, e):
		pass

	def RadioButton3CheckedChanged(self, sender, e):
		pass