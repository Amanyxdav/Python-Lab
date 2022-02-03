x=int(input("Enter the value of 1st variable:"))
y=int(input("Enter the value of 2nd variable:"))

def swap(x,y):
    print('Value of 1st variable before swapping:', x)
    print('Value of 2nd variable before swapping', y)
    x , y = y , x
    return x, y

x,y = swap(x,y)

print('Value of 1st variable after swapping:', x)
print('Value of 2nd variable after swapping', y)

