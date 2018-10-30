

def top_bottom(stop_num, change):
    i = 0
    numbers = []
    while i < stop_num:
        print(f"At the top i is {i}")
        numbers.append(i)
        
        i = i + change
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    
    
    print("The numbers: ")

    for num in numbers:
        print(num)
        
def top_bottom_loop(stop_num, change):
    i = 0
    numbers = []
    for i in range(0, stop_num, change):
        print(f"At the top i is {i}")
        numbers.append(i)
        
        i = i + change
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    
    
    print("The numbers: ")

    for num in numbers:
        print(num)
