# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = float(weight) / float(height) ** 2
print (round(BMI,3)) #四舍五入到小数点后第三位
