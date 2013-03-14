from bs4 import BeautifulSoup
import re
import codecs

class Assignment(object):
	name = "None"
	letterGrade = "None"
	percentGrade = "None"
	date = "None"
	
	def __hash__(self):
		return hash((self.name, self.letterGrade, self.percentGrade, self.date))
		
	def __eq__(self, other):
		return (self.name, self.letterGrade, self.percentGrade, self.date) == (other.name, other.letterGrade, other.percentGrade, other.date)
		
def allTagStringsNone(tr):
	stringsNone = True
	for td in tr.find_all("td"):
		if td.string is not None and td.string.strip() != "":
			stringsNone = False
	return stringsNone
	
def trCeption(tr):
	if tr.find("tr") is None:
		return False
	else:
		return True
		
def assignmentRow(tr):
	for td in tr.find_all("td"):
		if td.string is not None and (td.string.strip() == "Grade Mark" or td.string.strip() == "Default Grade Mark Group"):
			return False
	return True
	
def checkGradeCode(string):
	gradeCodes = ["NOT GRADED", "NO COUNT", "GIP", "GRADING IN PROGRESS"]
	for code in gradeCodes:
		if re.match(code, string):
			return True
		else:
			return False
	
def sort(tr):
	assignment = Assignment()
	for td in tr.find_all("td"):
		if td.string is not None and td.string.strip() != "":
			if bool(re.match(r'(\d+/\d+/\d+)', td.string.strip())):
				assignment.date = td.string.strip()
			elif checkGradeCode(td.string.strip()) or re.match(r'(\b[A-Z]\b)', td.string.strip()):
				assignment.letterGrade = td.string.strip()
			elif bool(re.match(r'(\d+\.\d+)', td.string.strip())):
				assignment.percentGrade = td.string.strip()
			else:
				assignment.name = td.string.strip()
	return assignment
	
def writeAssignments(assignments):
	assignmentFile = open("assignmentsOld.txt", "w")
	
	for assignment in assignments:
		if assignment.name == "None" or assignment.name == "There are no graded assignments in this category":
			continue
		assignmentFile.write("Name: " + assignment.name + ";")
		assignmentFile.write("Letter Grade: " + assignment.letterGrade + ";")
		assignmentFile.write("Percent Grade: " + assignment.percentGrade + ";")
		assignmentFile.write("Date: " + assignment.date + ";")
		assignmentFile.write("\n")
		
def stripIrrelevantData(data):
	before, itself, after = data.partition('id="GradeMarkDiv"')
	before1, itself1, after1 = before.partition('This student is over the attendance threshold.')
	return after1

def makeAssignments(gradebook_data):
	assignments = []
	for gradebook in gradebook_data:
		raw = BeautifulSoup(gradebook)
		stripped = BeautifulSoup(stripIrrelevantData(raw))
		for tr in soup.find_all('tr'):
			if assignmentRow(tr):
				if not allTagStringsNone(tr):
					if not trCeption(tr):
						assignments.append(sort(tr))						
	return assignments
	
def save_assignments(gradebook_data):
	with codecs.open("gradebook.txt", "w", "utf-8") as f:
		for gradebook in gradebook_data:
			f.write(gradebook)
			f.write("\n" + "\n" + "----------------------------" + "\n" + "\n")
	
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
	
def compare_assignments(new_assignments):
	old_assignments = readInAssignments("assignments_old.txt")
	return list(set(assignmentsNew) - set(assignmentsOld))