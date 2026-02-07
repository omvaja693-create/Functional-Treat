
print("Welcome to the Data Analyzer and Transformer Program")
print()

#.................................................UDF`s.........................................

# 1). For Facrorial
def factorial(n):
    """Calculates factorial using recursion"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
# 2). Ascending Sorting
def Ascending ():
    return (f"Sorted Data in Ascending Order: {sorted(array)}")
# 3). Decending Sorting
def Descending ():
     return (f"Sorted Data in Descending Order: {sorted(array, reverse=True)}")
# 4). For Sum
def total ():
    return len(array)
# 5). For Minium value
def smallest ():
    return min(array)
# 6). For Maximum value
def biggest ():
    return max(array)
# 7). For Addition
def add ():
    return sum(array)
# 8). For Division
def division():
    return sum(array)/len(array)
#..............................................Program....................................................
array = []
while True:
    print("Main Menu:")
    print('1. Input Data')
    print('2. Displat Data Summary (Built-in Functions)')
    print('3. Calculate Factorial (Recursion)')
    print('4. Filter Data by Threshold ')
    print('5. Sort Data')
    print('6. Display Dataset Statistics (Return Multiple values)')
    print('7. Exit Program')

    choise = int(input('Please enter your choise: '))

    match choise:
        case 1:
            size = int(input('Enter size of 1D array: '))
            print('Enter data for a 1D array :')
            
            for i in range(size):
                array.append(int(input('Enter elements: ')))
            print('Data Entered Sucessfully...')
            print()
        case 2:
            if len(array) == 0:
                print('Array is empty, press 1 to Input Data')
            else:
                print("Data Summary:")
                print(f"- Total elements:", total())
                print(f"- Minium value:", smallest())
                print(f"- Maximum value:", biggest())
                print(f"- Sum of all values:", add())
                print(f"- Average value:", division())
                print()
        case 3:
            a = int(input("Enter a number to calculate its factorial: "))
            factorial(a)
            print(f"Factorial of {a} is:", factorial(a))
        case 4: 
            a = int(input('Enter a threshold value to filter uot data above this value:'))
            f = []
            for i in array:
                if i >=a:
                    f.append(i)
            print(f"Filtered Data (values >={a}): {f}")
        case 5:
            if len(array) == 0:
                print('Array is empty, press 1 to Input Data')
            else:
                print('Choose sorting option:')
                print('1.Ascending')
                print('2.Decending')

                choise = int(input('Enter your choise:'))

                match choise:
                    case 1:
                        print(f"Sorted Data in Ascending Order:" , Ascending ())
                    case 2:
                        print(f"Sorted Data in Descending Order:" , Descending ())
        case 6:
            if len(array) == 0:
                print('Array is empty, press 1 to Input Data')
            else:
                print("Dataset Statistics:")
                print(f"- Total elements:", total())
                print(f"- Minium value:", smallest())
                print(f"- Maximum value:", biggest())
                print(f"- Sum of all values:", add())
                print(f"- Average value:", division())
                print()
        case 7:
            print('Thank you for using the Data Analyzer and Transformer Program. Goodbye!')
            break
    
            
