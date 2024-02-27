# Write your MySQL query statement below
SELECT Students.student_id, student_name, Subjects.subject_name, count(Examinations.subject_name) AS attended_exams FROM Students
cross join subjects
left JOIN Examinations ON Students.student_id = Examinations.student_id 
and subjects.subject_name = examinations.subject_name
group by students.student_id, Subjects.subject_name
order by students.student_id, Subjects.subject_name