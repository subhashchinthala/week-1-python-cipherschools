# 1to 3 (free)
# 4 to 10 (150)
# 11 to 60 (250)
# above 60 (200)


age = int(input("please input your age : "))

if age == 0 or age < 0:
    print("you can't watch")
elif 0<age<=3:
    print("ticket price : free")
elif 3<age<=10:
    print("ticket price : 150")
elif 10<age<=60:
    print("ticket price : 200")
else:
    print("ticket price : 250")        