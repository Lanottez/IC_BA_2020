Practice Exam 4


Question 3 Correct
select users.*,count(*)
from users inner join messages
on users.id = message.user_id
group by users.id


Question 4 Correct 
select chats.*,count(*) 
from chats inner join messages
on chats.id = messages.chat_id
order by chats.created_at


Question 5 Redo
select users.id,max(messages.created_at) 
from users inner join messages
on users.id = messages.user_id
group by users.id

Question 6 Redo
with table_time_of_most_recent_message as (select users.id,max(created_at) at time_of_most_recent_message 
from users inner join messages
on users.id = messages.user_id
group by users.id) 

select users.id, users.name, messages.created_at, messages.text
from users inner join time_of_most_recent_message 
on users.id = time_of_most_recent_message.user_id inner join messages
on messages.user_id = users.id 
and time_of_most_recent_message.created_at = messages.created_at


Question 7 Not sure
With user_with_number_of_message as 
(
select chats.*,count(*) as number_of_message
from chats inner join messages
on chats.id = messages.chat_id
order by chats.created_at
)
select users.id,users.name
from users inner join user_with_number_of_message
on users.id = user_with_number_of_message.user_id
order by number_of_message
limit 1

Question 8 Redo
select messages.*,length(messages.text),sum(length(text)) over (order by created_at)
from messages
where user_id = 777
order by created_at


Question 9 Redo
select users.users.id,count(distinct user_blocks.block_id),
count(distinct opinions.id)
users inner join user_blocks
on users.id = user_blocks.user_id inner join opinions
on users.id = opinions.user_id
where opinions.opinion is FALSE
group by users.id


Question 10 Incorrect