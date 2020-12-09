Question 3 Correct
select user.*,sum(*) as number_of_message 
from users inner join messages
on users.id = messages.user_id
group by users.id

Question 4 Correct
select chats.created_at,count(*) as number_of_messages
from chats inner join messages
on chats.user_id = messages.chat_id
group by chats.id
order by chats.created_at

Question 5 Correct
select users.id,max(messages.created_at)
from users inner join messages
on users.id = messages.user_id
group by users.id
 
Question 6 Correct, but recheck
with table_most_rencently_posed_message as 
(
	select users.id as user_id,max(messages.created_at) as most_rencently_posed_message
	from users inner join messages
	on users.id = messages.user_id
	group by users.id
)
select users.name,users.id,message.text
from users inner join messages
on users.id = messages.user_id inner join table_most_recently_posed_message
on table_most_rencently_posed_message.user_id = users.id
and table_most_rencently_posed_message.most_rencently_posed_message = messages.created_at

Question 7 Correct 
select users.name,users.email,sum(*)
from user inner join messages
on users.user_id = messages.user_id
group by users.id
order by sum(*) desc 
limit 1

Question 8 Correct 
select messages.*,length(messages.text),sum(length(message.text)) over (order by messages.created_at)
from users inner join messages
on users.id = messages.user_id
where users.id = 777
order by messages.created_at

Question 9 Correct 
select users.user_id,count(distinct opinions.id),count(distinct user_blocks.block_id)
from users inner join user_blocks
on users.id = user_blocks.user_id inner join opinions
on users.id = opinions.user_id 
group by users.id
where opinions.opinion is FALSE
