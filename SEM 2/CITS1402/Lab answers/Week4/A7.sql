select titles.title,people.name
from
titles join castmembers on titles.title_id=castmembers.title_id
join people on castmembers.person_id=people.person_id
join ratings on titles.title_id=ratings.title_id
where
ratings.rating>=9;