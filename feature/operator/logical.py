# 逻辑运算符

flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag0

print("flag3 =", flag3)  # flag3 = False
print("flag4 =", flag4)  # flag4 = True
print("flag5 =", flag5)  # flag5 = False
print(flag1 and not flag2)  # True
print(1 > 2 or 2 == 3)  # False