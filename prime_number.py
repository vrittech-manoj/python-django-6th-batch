number = int(input("Enter any number#>>>"))
count = 1
divisible_count = 0
while count <= number:
    
    if number%count == 0:
        divisible_count = divisible_count+1

    count = count + 1


print("divisible count ",divisible_count)

if divisible_count<=2:
    print(number, f" is prime number with divisible count {divisible_count}")
else:
    print(number,f" is not prime number because it is divisible_count {divisible_count}")