## program that keeps in check stock details using functions
## define the functions

store = []

def import_data(filname):
    with open(filname,'r') as f:
        s = f.read().splitlines()
    for item in s:
        temp = item.split(',')
        x = []
        x.append(temp[0])
        x.append(int(temp[1]))
        x.append(float(temp[2]))
        store.append(x)
import_data('store.csv')


def my_print():
    table_head = '{:<4}{:<25}{:^10}{:^10}'.format('S/N','Item Names','Quantity','Price')
    print(table_head)
    f = '{:<4d}{:<25}{:^10d}{:^10,.1f}'
    for i in range(len(store)):
        print(f.format(i+1,*store[i]))

def change_price():
    try:
        id = int(input('Enter the s/n of the item: ')) - 1
        if id in range(len(store)):
            new_p = float(input('Enter the new price: '))
            store[id][2] = new_p
            print('%s price is now %.1f' %(store[id][0],new_p))
        else:
            print('no item with such s/n !')
    except ValueError:
                print('wrong input')
    finally:
        if input('do you need to change the price of another item? (y/n) ')[0] == 'y':
                change_price()


##take input from the operator
print("Hello, welcome to Mr Adamu Retail Market")
print("1.Admin")
print("2.User")
print("3.Exit")
choice = input("Enter choice 1/2/3:")

if choice == '1':
    print("ADMIN MENU")
    print("1.Display items")
    print("2.Set item price")
    print("3.Update quantities")
    print("4.Add new item")
    print("5.View Sales Record")
    print("6.Return")
    choice = int(input("Enter choice 1/2/3/4/5/6:"))

    if choice == 1:
        my_print()

    elif choice == 2:
        change_price()

elif choice == '2':
    print("USER MENU")
    print("1.Display")
    print("2.Buy Items")
    print("3.Return")
    choice = input("Enter choice 1/2/3:")

    if choice == 1:
        my_print()

elif choice == '3':
     print("Do you want to perform another transaction?")

else:
     print("Invalid input")




