class Student:
    def __init__(self,score):
        self.score=score

    def grade(self):
        if self.score>=80 and self.score<=100:
            print("A")
        elif self.score>=73 and self.score<=79:
            print("B")

        elif self.score>=65 and self.score<=72:
            print("C")
        elif self.score>=0 and self.score<=64:
            print("D")
        else:
            print("Z")
s=Student(95)
s.grade()
