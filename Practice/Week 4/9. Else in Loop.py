my_list = [1,2,3,4,5]

for i in my_list:
    print(i)
    if i==3:
        break
else: 
    print("Hit the For/Else Statement")

# Here else is the no break statement i.e if the loop is completed without any break then this will print

def find_index(list, searchItem):
    for value in list:
        if value == searchItem:
            break
    else:
        return -1
    return 1

list = ['Kunal', 'Rawat', 'Singh', 'Kumar']
print(f"is Kunal present in list: {find_index(list, 'Kunal')}")
print(f"is Anil present in list: {find_index(list, 'Anil')}")
