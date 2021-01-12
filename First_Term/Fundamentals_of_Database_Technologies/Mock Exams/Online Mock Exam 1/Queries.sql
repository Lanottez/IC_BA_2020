Mock Exam 1

Question 1 Correct
select * from employees



Question 2 Correct
select employees.first_name ||' '|| employees.last_name,jobs.job_title from
employees inner join jobs
on employees.job_id = jobs.job_id


Question 3 Correct
select department_id,AVG(salary) from 
employees 
group by department_id


Question 4 Correct
select locations.country_id,count(employee.employee_id) from
locations inner join departments
on locations.location_id = departments.location_id inner join employees
on employees.department_id = departments.department_id
group by locations.country_id


Question 5 Correct
select first_name,last_name,department_id, 
avg(salary) over (partition by department_id)
from employees


Question 6 Correct
i). The two departments will be considered as the same one. 

ii). 
SELECT departments.department_name, COUNT(employee_id)
FROM employees INNER JOIN departments
ON employees.department_id = departments.department_id 
GROUP BY departments.department_id

Question 7 