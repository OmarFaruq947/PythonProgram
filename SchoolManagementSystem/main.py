from school import School
from person import Student, Teacher, Person
from subject import Subject
from classroom import ClassRoom



school = School("BAUET", "Dhaka")

# adding class room
eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)


# adding student
rahim = Student("Rahim", eight)
korim = Student("korim", nine)
nahin = Student("Nahin", ten)
fahim = Student("fahim", ten)
hamim = Student("hamim", eight)


school.student_admission(rahim)
school.student_admission(korim)
school.student_admission(nahin)
school.student_admission(fahim)
school.student_admission(hamim)


# Adding Teachers
abul = Teacher("Abul khan")
kabul = Teacher("kabul khan")
babul = Teacher("babul khan")



# adding subjects

bangla = Subject("Bangla", abul)
english = Subject("English", abul)
ict = Subject("ICT", kabul)
physics = Subject("Physics", kabul)
chemistry = Subject("Chemistry", babul)
biology = Subject("Biology", babul)



eight.add_subject(bangla)
eight.add_subject(ict)
eight.add_subject(english)


nine.add_subject(bangla)
nine.add_subject(ict)
nine.add_subject(english)
nine.add_subject(physics)
nine.add_subject(chemistry)
nine.add_subject(biology)


ten.add_subject(bangla)
ten.add_subject(ict)
ten.add_subject(english)
ten.add_subject(physics)
ten.add_subject(chemistry)
ten.add_subject(biology)



eight.take_semester_final_exam()

print(school)