import codecs

class Assignment(object):
	name = "None"
	letter_grade = "None"
	percent_grade = "None"
	date = "None"
	
	def __hash__(self):
		return hash((self.name, self.letter_grade, self.percent_grade, self.date))
		
	def __eq__(self, other):
		return (self.name, self.letter_grade, self.percent_grade, self.date) == (other.name, other.letter_grade, other.percent_grade, other.date)
		
	def print_assignment(self):
		print "Name: " + self.name;
		print "Letter Grade: " + self.letter_grade;
		print "Percent Grade: " + self.percent_grade;
		print "Date: " + self.date;
	
def readInAssignments(filename):
	lines = open(filename, "r").read().splitlines()
	assignments = []
	for line in lines:
		assignment = Assignment()
		lineList = line.split(";")
		assignment.name = lineList[0].split(": ")[1]
		assignment.letter_grade = lineList[1].split(": ")[1]
		assignment.percent_grade = lineList[2].split(": ")[1]
		assignment.date = lineList[3].split(": ")[1]
		assignments.append(assignment)
	return assignments
	
assignmentsNew = readInAssignments("assignmentsNew.txt")
assignmentsOld = readInAssignments("assignmentsOld.txt")

assignmentsDifferent = list(set(assignmentsNew) - set(assignmentsOld))

for assignment in assignmentsDifferent:
	assignment.print_assignment()
	print "\n"

# interact with GUI here
