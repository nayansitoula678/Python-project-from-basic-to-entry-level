def multiplication_table():
 
    number = int(input("Enter a number to generate its multiplication table: "))
    
    
    limit = int(input("Enter the range for the multiplication table: "))
    
    print("\nMultiplication Table of", number)
    print("-" * 30)

  
    print("Using a for loop:")
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")
    print("-" * 30)

   
    print("Using a while loop:")
    count = 1
    while count <= limit:
        print(f"{number} x {count} = {number * count}")
        count += 1
    print("-" * 30)

    print("Using break and continue:")
    for i in range(1, limit + 1):
        if i == limit + 1:  
            break
        if i % 2 == 0:  
            continue
        print(f"{number} x {i} = {number * i}")
    print("-" * 30)



multiplication_table()
