from bs4 import BeautifulSoup
import codecs
import re

class Assignment(object):
	name = "None"
	letter_grade = "None"
	percent_grade = "None"
	date = "None"
	period = "None"
	
	def __hash__(self):
		return hash((self.name, self.letter_grade, self.percent_grade, self.date))
		
	def __eq__(self, other):
		return (self.name, self.letter_grade, self.percent_grade, self.date) == (other.name, other.letter_grade, other.percent_grade, other.date)
		
	def print_assignment(self):
		print "Name: " + self.name;
		print "Letter Grade: " + self.letter_grade;
		print "Percent Grade: " + self.percent_grade;
		print "Date: " + self.date;
	
def all_tag_strings_none(tr):
	strings_none = True
	for td in tr.find_all("td"):
		if td.string is not None and td.string.strip() != "":
			strings_none = False
	return strings_none
	
def tr_ception(tr):
	if tr.find("tr") is None:
		return False
	else:
		return True
		
def assignment_row(tr):
	for td in tr.find_all("td"):
		if td.string is not None and (td.string.strip() == "Grade Mark" or td.string.strip() == "Default Grade Mark Group"):
			return False
	return True
	
def check_grade_code(string):
	grade_codes = ["NOT GRADED", "NO COUNT", "GIP", "GRADING IN PROGRESS"]
	is_grade_code = False
	for code in grade_codes:
		if code == string:
			is_grade_code = True
	return is_grade_code
	
def sort(tr):
	assignment = Assignment()
	for td in tr.find_all("td"):
		if td.string is not None and td.string.strip() != "":
			if bool(re.match(r'(\d+/\d+/\d+)', td.string.strip())):
				assignment.date = td.string.strip()
			elif check_grade_code(td.string.strip()) or re.match(r'(\b[A-Z]\b)', td.string.strip()):
				assignment.letter_grade = td.string.strip()
			elif bool(re.match(r'(\d+\.\d+)', td.string.strip())):
				assignment.percent_grade = td.string.strip()
			else:
				assignment.name = td.string.strip()
	return assignment
	
def write_assignments(assignments):
	file_name = "per" + assignments[0].period + ".txt"
	assignment_file = open(file_name, "w")
	
	for assignment in assignments:
		if assignment.name == "None" or assignment.name == "There are no graded assignments in this category":
			continue
		assignment_file.write("Name|| " + assignment.name + "//")
		assignment_file.write("Letter Grade|| " + assignment.letter_grade + "//")
		assignment_file.write("Percent Grade|| " + assignment.percent_grade + "//")
		assignment_file.write("Date|| " + assignment.date + "//")
		assignment_file.write("Period|| " + assignment.period + "//")
		assignment_file.write("\n")
		
def strip_irrelevant_data(data):
	before, itself, after = data.partition('<div style="display: none;" id="GradeMarkDiv">')
	before1, itself1, after1 = before.partition('This student is over the attendance threshold.')
	return after1
	
def compare_assignments(new_assignments, class_period):
	file_name = "per" + str(class_period) + ".txt"
	old_assignments = read_in_assignments(file_name)
	return list(set(new_assignments) - set(old_assignments))
	
def read_in_assignments(filename):
	lines = open(filename, "r").read().splitlines()
	assignments = []
	for line in lines:
		assignment = Assignment()
		line_list = line.split("//")
		assignment.name = line_list[0].split("|| ")[1]
		assignment.letter_grade = line_list[1].split("|| ")[1]
		assignment.percent_grade = line_list[2].split("|| ")[1]
		assignment.date = line_list[3].split("|| ")[1]
		assignment.period = line_list[4].split("|| ")[1]
		assignments.append(assignment)
	return assignments
	
def make_assignments(data, class_period):
	soup = BeautifulSoup(strip_irrelevant_data(data), "html5lib")

	assignments = []
			
	for tr in soup.find_all('tr'):
		if assignment_row(tr):
			if not all_tag_strings_none(tr):
				if not tr_ception(tr):
					assignment = sort(tr)
					assignment.period = str(class_period + 1)
					if assignment.name == "None" or assignment.name == "There are no graded assignments in this category":
						continue
					else:
						assignments.append(assignment)
					
	return assignments
	
def gradebook_changes(gradebook, class_period):
	new_assignments = make_assignments(gradebook, class_period)
	return compare_assignments(new_assignments, class_period)
 
# with codecs.open ("file.html", "r", "utf-8") as file:
   # data = file.read()
 


# write_assignments(assignments)

				
