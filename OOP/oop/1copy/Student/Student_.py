class Student:
    def __init__(self, name, id, major, gpa, isactive):
        self.name = name
        self.id = id
        self.major = major
        self.gpa = gpa
        self.isactive = isactive

    def studyabroad(self):
        if self.isactive and self.gpa > 3.5:
            if self.major == "Computer Science":
                print("Congratulations "+ self.name +"! You are eligible for our Study Abroad Program in MIT")
            elif self.major == "Business":
                print("Congratulations "+ self.name +"! You are eligible for our Study Abroad Program in Harvard")
                print(f"Mr/ms {self.name}! your {self.gpa} score means you are eligible for our Study Abroad Program in Harvard")
            else:
                print("We don't have any study abroad programs for your Major")
        else:
            print("You are not eligible for any study abroad programs")
