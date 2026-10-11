#Write a program calculate selling price of book based on cost price and discount .
# take vales
Cost_price = int(input('Enter book price :'))
Discount = int(input('Enter discount :'))
# apply condition 
# formula - cost price = Cost_price * Discount / 100
#formula - selling price = cost - discount 
Selling_price = Cost_price - (Cost_price * Discount / 100)
# dispaly result
print(f'the selling price is {Selling_price}.')
