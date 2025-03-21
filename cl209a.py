class numSort:
    def __init__(self,num):
        self.num = num
        self.tof = False

    def Count(self):
        if self.num < 500:
            self.tof = False
        elif self.num >= 500:
            self.tof = True

    def __str__(self):
        return self.tof





