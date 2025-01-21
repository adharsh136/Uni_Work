select o.orderNumber as order_number,
p.productLine as product_line,
count(o.orderNumber) as number_of_line_items,
round(sum(o.quantityOrdered*o.priceEach),2) as total_cost 
from
orderdetails as o join products as p on o.productCode=p.productCode
group by order_number,product_line order by order_number;