class Course:
    grade_points = {'A':4, 'A-':3.67, 'B': 3, 'B+':3.33, 'B-': 2.67, 'C+': 2.33, 'C':2, 'C-':1.67, 'D+':1.33, 'D':1, 'D-':0.67, 'E':0 }

    def __init__(self, crs_id, title, hours, grade):
        self.crs_id = crs_id
        self.title = title
        self.hours = hours
        self.grade = grade

    def __str__(self):
        return "(crs_id:{}, title:{}, hours:{}, grade:{})".format(self.crs_id, self.title, self.hours, self.grade)

    def gpa_crs_points(self):
        pts = Course.grade_points[self.grade]
        return pts * self.hours
#semesterschedule -- contains a student's name and a list of course for a particular semester
class SemesterSchedule:

#Constructor
    def __init__(self, student_name):
        self.student_name = student_name
        self.course = []

#adds a course to the students's schedule
    def add_course(self, course ):
        self.course.append(course)
#returns the number of courses in the schedule
    def __len__(self, other):  # returns the length of the list
        return len(self.course)


#provides a string representation of the schedule
    def __str__(self):    # illustrates the string representation
        tmp = " "
        tmp = self.student_name
        for i in range(len(self.course)):
            tmp += "\n{}: {} " .format(i, self.course[i])

        return tmp
#returns the total number of hours
    def hours(self):
        total = 0
        for i in range(len(self.course)):
          total += self.course[i].hours
        return total
# returns the semester's non discounted tuition
#see: https://www.bluffton.edu/current-students/billing.aspx
#uses 2020-21 Fee schedule
    def tuition(self):
        total_hours = self.hours()
        if total_hours < 12:
            return 1415 * total_hours
        elif total_hours <= 17:
            return 999 * total_hours
        elif total_hours <= 20:
            return 999 * total_hours
        elif total_hours > 20:
            return 1415 * total_hours


#Boolean function indicating the student is full time(at least 12 hours)
    def full_time(self):
        if self.hours() >= 12:
            return True
        else:
            return False
#Boolean functionindicating the student is full time (at least 15 hours)
    def over_load(self):
        if self.hours() >= 15:
            return True
        else:
            return False
#Returns a student's semester gpa
    def gpa(self):  # add all the course points and divide them by their hours
        total_hours = 0
        total_points = 0
        for i in range(len(self.course)):
          total_points += self.course[i].gpa_crs_points()
          total_hours += self.course[i].hours

        return total_points/total_hours

crs = Course('2020-2U CPS112-01', 'OOP', 3, 'C')
print(crs.gpa_crs_points() )
print("Gpa course points:", crs.gpa_crs_points())
print( crs )


sch = SemesterSchedule('J Denny Beaver')
sch.add_course(crs)
sch.add_course( Course('2020-2U MAT136-01', 'CALCULUS 2', 2, 'B') )
sch.add_course( Course('2020-2U SWK141-01', 'Und Soc Welfare', 3, 'C') )
sch.add_course( Course('2020-2U ECN142-02', 'Principles  Microeconomics', 3, 'D') )
sch.add_course( Course('2020-2U HFS240-01', 'Coaching Methods', 3, 'A') )

print( sch )  # this statment does the output



print()
print( "Hours:", sch.hours())

print( "Full time:", sch.full_time())

print( "Overload:", sch.over_load())
print( 'GPA: {:.2f}'.format(sch.gpa()))
#print( 'GPA: {}'.format(sch.gpa()))

print()
print('Tuition: ${:,.2f}'.format(sch.tuition()) )
print()
print( 'GPA: {:.2f}'.format(sch.gpa()))
