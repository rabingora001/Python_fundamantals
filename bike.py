class bike:
    def __init__(self, price, max_speed, miles=0):
        self.price= price
        self.max_speed= max_speed
        self.miles= miles

    def displayinfo(self):
        print(self.price, self.max_speed, self.miles)
        return self

    def ride(self):
        self.miles += 10
        print("riding")
        return self

    def reverse(self):
        self.miles -=5
        if self.miles < 0:
            self.miles=0
        print("reversing")
        return self


bike1 = bike(200, "25mph").ride().ride().ride().reverse().displayinfo()