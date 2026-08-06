n = int(input())
rows = []
grant_total = 0

for _ in range(n):
    product, qty, price = input().split()
    qty = int(qty)
    price = int(price)
    total = qty * price
    grant_total += total
    rows.append((product, qty, price, total))

print(f"{'Product':<12} | {'Qty':>5} | {'Price':>7} | {'Total':>9}")
print("-" * 12 + "+" + "-" * 5 + "+" + "-" * 7 + "+" + "-" * 9)

for product, qty, price, total in rows:
    print(f"{product:<12} | {qty:>5} | {price:>7} | {total:>9}")
    
print(f"GRAND: {grant_total}")