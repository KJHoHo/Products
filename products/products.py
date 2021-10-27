products = []
while True:
	name = input('请输入商品名称：')
	if name == 'q':
		break
	price = input('请输入商品价格：')
	price = int(price)
	# p = [name, price]
	#p = []
	# p.append(name)
	# p.append(price)
	products.append([name, price])
print(products)

for product in products:
	print(product[0], '的价格是', str(product[1]))

with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,价格\n')
	for product in products:
		f.write(product[0] + ',' + str(product[1]) + '\n')