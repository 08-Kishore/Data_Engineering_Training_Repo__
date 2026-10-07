SET SQL_SAFE_UPDATES = 0;
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    city VARCHAR(50)
);
INSERT INTO students VALUES
(1, 'Arun', 'Hyderabad'),
(2, 'Megha', 'Mumbai'),
(3, 'Zaid', 'Hyderabad'),
(4, 'Pooja', 'Pune'),
(5, 'Rohan', 'Delhi'),
(6, 'Sana', NULL),
(7, 'Vijay', 'Bangalore');
CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    fee DECIMAL(10,2)
);
INSERT INTO courses VALUES
(101, 'Python', 15000),
(102, 'Data Engineering', 25000),
(103, 'Power BI', 12000),
(104, 'Cloud Computing', 20000),
(105, 'Cyber Security', 22000),
(106, 'Machine Learning', 28000);
CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE
);
INSERT INTO enrollments VALUES
(1001, 1, 101, '2026-09-01'),
(1002, 1, 102, '2026-09-03'),
(1003, 2, 103, '2026-09-04'),
(1004, 3, 102, '2026-09-05'),
(1005, 4, 104, '2026-09-06'),
(1006, 2, 101, '2026-09-07'),
(1007, 3, 105, '2026-09-08'),
(1008, 20, 102, '2026-09-09'),
(1009, 5, NULL, '2026-09-10');

select s.student_name,c.course_name 
from enrollments e 
left join students s on 
e.student_id=s.student_id
left join courses c on
e.course_id = c.course_id;

select 
	s.student_name,
	s.city,
	c.course_name,
    c.fee
from enrollments e 
left join students s on 
e.student_id=s.student_id
left join courses c on
e.course_id = c.course_id;

select s.student_name from enrollments e 
left join students s 
on e.student_id=s.student_id 
left join courses c on
e.course_id=c.course_id 
where c.course_name='Data Engineering';

select * from students s 
inner join enrollments e on 
s.student_id = e.student_id 
left join courses c on
e.course_id=c.course_id;

select * from students;

select s.student_name from 
enrollments e left join students s
on e.student_id=s.student_id where e.course_id is null;

select c.course_name,e.student_id from courses c 
left join enrollments e on 
c.course_id=e.course_id;

select c.course_name,e.enrollment_id from courses c 
left join enrollments e on 
c.course_id=e.course_id where e.enrollment_id is null;

SELECT e.enrollment_id,
       e.student_id,
       e.course_id
FROM enrollments e
LEFT JOIN students s 
       ON e.student_id = s.student_id
WHERE s.student_id IS NULL;

SELECT e.enrollment_id,
       e.student_id,
       e.course_id
FROM enrollments e
LEFT JOIN courses c 
       ON e.course_id = c.course_id
WHERE c.course_id IS NULL;


SELECT 
    e.student_id,
    COUNT(e.course_id) AS total_courses
FROM enrollments e
GROUP BY e.student_id;

SELECT 
    e.student_id,
    SUM(c.fee) AS total_fees
FROM enrollments e
JOIN courses c 
    ON e.course_id = c.course_id
GROUP BY e.student_id;

SELECT 
    e.student_id,
    COUNT(e.course_id) AS total_courses
FROM enrollments e
GROUP BY e.student_id
HAVING COUNT(e.course_id) > 1;

SELECT 
    e.course_id,
    COUNT(e.student_id) AS total_students
FROM enrollments e
GROUP BY e.course_id
HAVING COUNT(e.student_id) > 1;

SELECT 
    e.course_id,
    SUM(c.fee) AS total_revenue
FROM enrollments e
JOIN courses c 
    ON e.course_id = c.course_id
GROUP BY e.course_id;

SELECT 
    e.course_id,
    SUM(c.fee) AS total_revenue
FROM enrollments e
JOIN courses c 
    ON e.course_id = c.course_id
GROUP BY e.course_id
ORDER BY total_revenue DESC
LIMIT 1;



