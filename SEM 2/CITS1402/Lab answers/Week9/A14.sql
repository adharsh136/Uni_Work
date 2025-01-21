select (premiered/10) || '0s' as name_of_the_decade, title, rating from
titles join ratings  using (title_id)
where (name_of_the_decade,rating) in
(select (premiered/10) || '0s' as a,max(rating) from titles join ratings using (title_id) group by a) 
order by name_of_the_decade;