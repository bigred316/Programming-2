class numSort:
    def __init__(self,num):
        self.num = num
        self.tof = False

    def Count(self):
        if self.num < 500:
            self.tof = "zero"
        elif self.num >= 500:
            self.tof = "one"

    def __str__(self):
        return self.tof





