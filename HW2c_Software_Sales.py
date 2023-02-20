quantity = int(input('Enter number of packages purchased: '))

subtotal = float(quantity * 99)

if quantity >= 0 and quantity < 10:
    discount = 0
elif quantity >= 10 and quantity <= 19:
    discount = subtotal * 0.1
elif quantity >= 20 and quantity <= 49:
    discount = subtotal * 0.2
elif quantity >= 50 and quantity <= 99:
    discount = subtotal * 0.3
elif quantity >= 100:
    discount = subtotal * 0.4

total = subtotal - discount

print(f'Discount: ${discount: .2f}')
print(f'Total of purchase: ${total: .2f}')