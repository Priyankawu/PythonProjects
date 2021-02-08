

num1 = 12 
num2 = 10 
results = num1 + num2 
if results == 12:
     print("Your number is twelve") 
else:
     print("Your number is {}".format(results))

colors = ['Red','Blue','Green','Yellow'] 
for i in colors:
   print(i)

num1 = 12 
num2 = 'two' 
try:
     results = num1 + num2
     if results > 12:
         print("Your number was {}".format(results))
     else:
         print("Your number was {}".format(results)) 
except TypeError:
     print("num2 was not a number")


def getNum():
     i = sum = 0
     while i <= 4:
         sum += i
         i = i+1
     print(sum)
getNum()
