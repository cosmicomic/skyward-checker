class Assignment(object):
	name = "None"
	letterGrade = "None"
	percentGrade = "None"
	date = "None"
	
	def __hash__(self):
		return hash((self.name, self.letterGrade, self.percentGrade, self.date))
		
	def __eq__(self, other):
		return (self.name, self.letterGrade, self.percentGrade, self.date) == (other.name, other.letterGrade, other.percentGrade, other.date)
	
def readInAssignments(filename):
	lines = open(filename, "r").read().splitlines()
	assignments = []
	for line in lines:
		assignment = Assignment()
		lineList = line.split(";")
		assignment.name = lineList[0].split(": ")[1]
		assignment.letterGrade = lineList[1].split(": ")[1]
		assignment.percentGrade = lineList[2].split(": ")[1]
		assignment.date = lineList[3].split(": ")[1]
		assignments.append(assignment)
	return assignments
	
assignmentsNew = readInAssignments("assignmentsNew.txt")
assignmentsOld = readInAssignments("assignmentsOld.txt")

assignmentsDifferent = list(set(assignmentsNew) - set(assignmentsOld))

# interact with GUI here
