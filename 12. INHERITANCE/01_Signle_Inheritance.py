class a:
    def displayA(self):
        print("Ekhlakh")
class b(a):
    def displayB(self):
        print("Ahmad")

obj = b()
obj.displayA()
obj.displayB()