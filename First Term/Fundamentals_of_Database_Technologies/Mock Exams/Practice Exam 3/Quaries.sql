Practice Exam 3


Question B3 Correct 
select name,in_office_start
from leaders



Question B4 Redo For Practice
select leaders.*,count(*)
from leaders left outer join given_titles
on leaders.id = given_titles.title_id
group by leaders.id

Question B5 Correct
select countries.id,countries.name,min(alliances.start)
from countries inner join countries_in_alliances 
on countries.id = countries_in_alliances.country_id inner join alliances
on countries_in_alliances.alliances_id = alliances.id
group by countries.id

Question B6 Redo 
with (select countries.id,min(alliances.start) as date_of_oldest_alliance_enter_time
from alliances inner join countries_in_alliances
on alliances.id = countries_in_alliances.alliance_id inner join countries
on countries_in_alliances.country_id = countries.id)
as table_of_date_of_oldest_alliance_enter_time

select *
from countries inner join table_of_date_of_oldest_alliance_enter_time
on countries.country_id = table_of_date_of_oldest_alliance_enter_time.country_id inner join countries_in_alliances
on countries.country_id = countries_in_alliances.alliance_id inner join alliances
on countries_in_alliances.alliance_id = alliances.alliances_id
and alliances.date = table_of_date_of_oldest_alliance_enter_time.start


Question B8 Correct
Select alliances.name,sum(countries.population)
from alliances inner join countries_in_alliances
on alliances.id = countries_in_alliances.alliances_id inner join countries
on countries.id = countries_in_alliances.country_id
group by alliances.alliances_id

Question B9 Correct 
select * 
from leaders
where in_office_end is NULL 
and in_office_start is not NULL


Question B10 Redo
select countries.name,count(distinct treaties.id) from
countries inner join treaties
on countries.id = treaties.country_1_id 
or countries.id = treaties.country_2_id 
group by countries.id

Question B11 Redo
with leader_with_most_titles as 
(
	SELECT leaders.id, COUNT(*) AS title_count FROM
	leaders INNER JOIN given_titles
	ON leaders.id = given_titles.leader_id WHERE in_office_start IS NOT NULL
	AND in_office_end IS NULL
	GROUP BY leaders.id
	ORDER BY title_count DESC
	LIMIT 1
),
leader_in_offce_the_longest as 
(
	SELECT id FROM leaders
	WHERE in_office_start IS NOT NULL AND in_office_end IS NULL
	ORDER BY in_office_start ASC 
	LIMIT 1
)
select 
(
	(select id from leader_with_most_titles) = (select id from leader_in_offce_the_longest
)


Question B12 Redo
select treaties.id,c1.name,c2.name, count(*) over (order by date)
from treaties inner join countries as c1
on treaties.country_1_id = c1.id inner join countries as c2
on treaties.country_2_id = c2.id
order by date


