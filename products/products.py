products = []
while True:
	name = input('请输入商品名称：')
	if name == 'q':
		break
	price = input('请输入商品价格：')
	# p = [name, price]
	#p = []
	# p.append(name)
	# p.append(price)
	products.append([name, price])
print(products)

for product in products:
	print(product[0], '的价格是', product[1])