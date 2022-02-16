# 1
#   Order Number	Book Title and Author	              Quantity	   Price per Item
#   34587	        Learning Python, Mark Lutz	          4	           40.95
#   98762	        Programming Python, Mark Lutz	      5	           56.80
#   77226	        Head First Python, Paul Barry	      3	           32.95
#   88112	        Einführung in Python3, Bernd Klein	  3	           24.99

book_sales_list = [[34587, 'Learning Python, Mark Lutz', 4, 40.95], \
                   [98762, 'Programming Python, Mark Lutz', 5, 56.80],\
                   [77226, 'Head First Python, Paul Barry', 3, 32.95], \
                   [88112, 'Einführung in Python3, Bernd Klein', 3, 24.99]]

# 2
def total_cost(lst):
    return list(map(lambda order_num, price, quantity: (order_num, round(price*quantity, 2) + 10 if round(price*quantity, 2) < 100 else round(price*quantity, 2)), [row[0] for row in lst], [row[3] for row in lst], [row[2] for row in lst]))

print(total_cost(book_sales_list))

# 3
#   Order Number	Article Number	   Quantity	    Price per Unit
#   34587	        100	               4	        4.95
#   98762	        53	               5	        6.80
#   77226	        34	               3	        2.95
#   88112	        45	               2	        4.99

article_sales_list = [[34587, 100, 4, 4.95], \
                      [98762, 53, 5, 6.80],\
                      [77226, 34, 3, 2.95], \
                      [88112, 45, 2, 4.99]]

def order_total(lst):
    return list(zip([row[0] for row in lst], list(map(lambda price, quantity: round(price*quantity, 2) + 10 if round(price*quantity, 2) < 100 else round(price*quantity, 2), [row[3] for row in lst], [row[2] for row in lst]))))

print(order_total(article_sales_list))