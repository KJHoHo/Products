import os # operating system

products = []
if os.path.isfile('products.csv'):
	print('yeah!找到档案了！')
	# 读取档案
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,价格' in line:
				continue # 继续 跳到下一回
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('找不到档案......')

# 让使用者输入
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

# 印出所有购买记录
for product in products:
	print(product[0], '的价格是', str(product[1]))

# 写入档案
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,价格\n')
	for product in products:
		f.write(product[0] + ',' + str(product[1]) + '\n')