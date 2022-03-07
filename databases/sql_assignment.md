https://colab.research.google.com/drive/1Ce5wvEVLIGDw93XDF1SC-1DP05xoH-eZ?usp=sharing

Homework:

sql_query_string = """
SELECT s.first, s.last, s.studentID, s.grade, s.scanTime, s.status, p.date, p.courseSection, 
p.attendance, p.period, p.teacher, substr(s.scanTime, 1,instr(s.scanTime, ' ')-1) as scanDate
FROM scan as s
INNER JOIN periodAtt as p
on s.studentID=p.studentID AND p.Attendance = 'A'
and substr(s.scanTime, 1,instr(s.scanTime, ' ')-1) = p.date
order by s.last ASC
"""

Async:

sql_query_string = """
select teacher, count(*) as total from (SELECT s.first, s.last, s.studentID, s.grade, s.scanTime, s.status, p.date, p.courseSection, 
p.attendance, p.period, p.teacher, substr(s.scanTime, 1,instr(s.scanTime, ' ')-1) as scanDate
FROM scan as s
INNER JOIN periodAtt as p
on s.studentID=p.studentID AND p.Attendance = 'A'
and substr(s.scanTime, 1,instr(s.scanTime, ' ')-1) = p.date
order by s.last ASC) as allCuts
group by teacher
order by total desc

"""
