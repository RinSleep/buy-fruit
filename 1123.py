
fruit = [['apple','banana','wetermelon','orange','mango'],[20,30,100,40,50]]
d = {'apple':0,'banana':1,'wetermelon':2,'orange':3,'mango':4}
a = 0
e = 0
f = 0
z = 0
total = 0
print('welcome to my store!')
print('the store have sells some fruits! for example')
while  a<5:
 print(fruit[0][a])
 a = a+1
print('do you want to buy some?')
b = (input('yes or no?'))
if b == 'yes':
    while z == 0:
     c = (input('what kind od fruit do you want to buy?'))
     e = int(input('quantity?'))
     f = int(fruit[1][d[c]])*e
     total = total + f
     k = (input('whats more?(yes or no)'))
     if k == 'yes':
        z = z
     else :
        z = z+1
    print(total,'NTD')
else :
    print("bye~")     
