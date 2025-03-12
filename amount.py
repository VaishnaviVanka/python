amount = int(input("enter the amount:"))
five_hun =amount//500
print(f"five_hun(500): {five_hun}")
remaining = amount%500
one_hun = remaining//100
print(f"one_hun(100): {one_hun}")
fifty_rupees = 50//one_hun
print(f"fifty_rupees(50): {fifty_rupees}")
ten_rupees = 10//fifty_rupees
print(f"ten_rupees(10): {ten_rupees}")
