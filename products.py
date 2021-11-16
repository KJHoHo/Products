import os # operating system

# 读取档案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,价格' in line:
                continue # 继续 跳到下一回
            name, price = line.strip().split(',')
            products.append([name, price])
    return products

# 让使用者输入
def user_input(products):
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
    return products

# 印出所有购买记录
def print_products(products):
    for product in products:
        print(product[0], '的价格是', str(product[1]))

# 写入档案
def write_file(filename, products):
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write('商品,价格\n')
        for product in products:
            f.write(product[0] + ',' + str(product[1]) + '\n')

def main():
    filename = 'products.csv'
    if os.path.isfile(filename): # 检查档案在不在    
        print('yeah!找到档案了！')
        products = read_file(filename)
    else:
        print('找不到档案......')
    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()