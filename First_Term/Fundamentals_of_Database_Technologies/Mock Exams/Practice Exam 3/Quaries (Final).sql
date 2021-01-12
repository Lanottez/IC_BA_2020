Mock Exam 3

Question 1
Yes, such as the relationship between alliances and countries. An alliances could be corresponding to multiple countries, and a country could be corresponding to multiple alliances. The table countries_in_alliances is the junction table between alliances and countries.

Question 2
No, becuase there only two 

Question 3 Correct
select name,in_office_start 
from leaders 

Question 4 Correct
select leader.*,count(*) as number_of_titles
from leaders left outer join given_titles
on leaders.id = given_titles.leader_id
group by leaders.id

Question 5 Correct
select countries.id, countries.name,min(alliances.start)
from countries inner join countries_in_alliances
on countries.id = countries_in_alliances.country_id inner join alliances
on countries_in_alliances.alliance_id = alliances.id
group by countries.id

Question 6 Correct (but check line 37)
with table_oldest_alliance as 
(
	select countries.id as countries_id, min(alliances.start) as oldest_alliance
	from countries inner join countries_in_alliances
	on countries.id = countries_in_alliances.country_id inner join alliances
	on countries_in_alliances.alliance_id = alliances.id
	group by countries.id
)
select countries.name,alliances.name,alliances.start
from countries inner join table_oldest_alliance
on countries.id = table_oldest_alliance.country_id inner join countries_in_alliances
on countries.id = countries_in_alliances.country_id inner join alliances
on countries_in_alliances.alliance_id = alliances.id
and alliances.start = table_oldest_alliance.oldest_alliance

Question 7 Correct
Either of the two alliances might appear to be the 

Question 8
select alliances.name,sum(countries.population) 
from countries inner join countries_in_alliances
on countries.id = countries_in_alliances.country_id inner join alliances
on countries_in_alliances.alliance_id = alliances.id
group by alliances.id

Question 9 Correct 
select *
from leaders 
where in_office_start is not null
and in_office_end is null


Question 10 Correct
select countries.name,count(distinct treaties.id) as number_of_treaties
from countries inner join treaties 
on countries.id = treaties.country_1_id
or countries.id = treaties.country_2_id
group by countries.id


Question 11 Correct
with row_in_office_the_longest as 
(	select *
	from leaders 
	where in_office_start is not null
	and in_office_end is null
	order by in_office_start
	limit 1 
),
row_most_titles as 
(
	select *,count(*) 
	from leaders inner join given_titles
	on leaders.id = given_titles.leader_id
	where in_office_start is not null
	and in_office_end is null
	group by leaders.id
	order by count(*) desc 
	limit 1
)
select 
(
	(select leader.id from row_in_office_the_longest) = (select leader.id from row_most_titles) 
) 

Question 12 Correct
select treaties.*,c1.name,c2.name,count(*) over (order by treaties.date)
treaties inner join countries as c1
on c1.id = treaties.country_1_id  inner join countries as c2
on c2.id = treaties.country_2_id 
order by date 





