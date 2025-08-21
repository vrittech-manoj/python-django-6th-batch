#WAP to print 0 to 100 using while loop
#WAP to find odd and even number upto 0 10 100
#WAP to find prime number of user input number


# "6595" = "595"
# "8636" = "686"
# "9894" = "989"
# "36796" = "696"
# count = 0
# while True:
#     count = count+1
#     print(count)
#     if count == 100:
#         break

count = 0
while count<100:
    count = count + 1
    if count%2 == 0:
        print(count," is even")
    else:
        print(count," is odd")
    # print(count)