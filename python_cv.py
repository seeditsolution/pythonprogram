class Myclass :
    def __init__(self,a,b):
        self.num1=a
        self.num2=b

    def add(self):
        self.sum=self.num1+self.num2

    def show(self) :
        print(self.sum)


a=Myclass(5,3)
a.add()
a.show()
a.num1=90
a.num2=90
a.add()
a.show()


print(a.add())
a.show()


