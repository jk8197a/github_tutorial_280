class Student:

	#establish Student class with relevant attributes
	def __init__(self, name, year, gpa, current_classes):

		self.name = name
		self.year = year
		self.gpa = gpa
		self.current_classes = current_classes

	#use method to print current year and how long until graduation
	def addYear(self): 

		if (self.year < 4):

			A = 4 - self.year

			print ("Current year:", self.year)
			print ("Years until graduation:", A)

		else: 

			print ("Current year:", self.year)
			print ("You are graduating this year.")

	#allow user to input desired gpa and display user input in relation to current gpa
	def setGPA(self):

		goal_gpa = float(input("Enter desired GPA: "))

		print("Current GPA:", self.gpa, "vs. Desired GPA:", goal_gpa)

		if (self.gpa < goal_gpa):

			print("Go study to increase your GPA.")

	#allow user to change course load
	def addClass(self):

		print("Current course load:", self.current_classes)

		class_number = int(input("Enter number of classes to add: "))

		for i in range (0, class_number):

			new_class = input("Enter class: ")

			new_class_credit = int(input("Enter credits: "))

			self.current_classes.update ({new_class : new_class_credit})

		print("New course load:", self.current_classes)

#create athlete subclass with relavent attributes
class Athlete(Student):

	def __init__(self, name, year, gpa, current_classes, sport, years_of_experience, onScholarship, starter):

		#instatiate attributes from student class and for athlete subclass
		super().__init__(name, year, gpa, current_classes)
		self.sport = sport
		self.years_of_experience = years_of_experience
		self.onScholarship = onScholarship
		self.starter = starter

def main():

	#create instance of athlete subclass with relavant attributes
	student1 = Athlete(

			name = "Steve", 
			year = 3, 
			gpa = 3.9,
			current_classes = {"Calc I" : 3, "Jewish Studies" : 4},
			sport = "Tennis", 
			years_of_experience = 10, 
			onScholarship = True,
			starter = True

			)

	#print name, sport, years of experience
	print("Name:", student1.name)
	print("Sport:", student1.sport)
	print("Years of experience:", student1.years_of_experience)

	#determine whether or not student is on scholarship or is a starter
	print("On scholarship:", student1.onScholarship)
	print("Starter:", student1.starter)

	#run methods established in student class 
	student1.addYear()
	student1.setGPA()
	student1.addClass()
	print("Hell")


if __name__ == '__main__':
	main()