Question 1
select dogs.name,customers.first_name,customers.last_name 
from dogs inner join customers
on dogs.owner_id = customers.id


Question 2
select dogs.id,count(*) as number_of_bookings
from dogs inner join bookings
on dogs.id = bookings.dog_id
group by dogs.id

Question 3
select bookings.id, customers.surname,sum(bookings.end-bookings.start) over (order by bookings.start)
from bookings inner join dogs
on bookings.dog_id = dogs.id inner join customers
on dogs.owner_id = customers.id
where bookings.kennel_id = 7
and (bookings.start is null or (bookings.start is not null and bookings.end is null))
order by customers.surname

Question 4
select sum(capacity)
from kennels 

Question 5
select dogs.owner_id,sum(bookings.end-bookings.start) as amount_of_time
from dogs inner join bookings
on dogs.id = bookings.dog_id
where bookings.start is not null
and bookings.end is not null
group by dogs.owner_id


Question 6
select dogs.owner_id,count(distinct dogs.id) as number_of_dog,sum(payments.amnount) as total_payment 
from dogs inner join bookings 
on dogs.id = bookings.id inner join payments
bookings.id = payments.booking_id
group by dogs.owner_id
order by total_payment desc
limit 10

