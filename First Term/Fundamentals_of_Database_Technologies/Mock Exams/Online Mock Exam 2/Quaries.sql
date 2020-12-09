Mock Exam 2


Question 1 Correct
Select * from titles


Question 2 Correct
select price*ytd_sales from titles


Question 3 Correct
select authoers.lname ||' '|| authors.fname,avg(titles.price) from 
authors inner join titleauthor
on authors.au_id = titleauthor.au_id inner join titles
on titleauthor.title_id = titles.title_id 
group by authoers.au_id

Question 4 Correct
select stores.stor_id,count(*)
from discounts left outer join stores
on discounts.stor_id = stores.stor_id
group by stores.stor_id

Question 5 Redo 
select fname,lname,pub_id,avg(salary) over (PARTITION by pub_id)
from employees 


Question 6
(i) Correct
select sum(titles.price * sales.qty) over (order by ord_date)
from sales inner join titles
on sales.title_id = titles.title_id

(ii) Incorrect
select sum(titles.price * sales.qty) over (PARTITION by ord_date)
from sales inner join titles
on sales.title_id = titles.title_id