# #WAP to find out a given number is odd or even. if odd print "given number is odd" if even print "Even"
# odd = number / 2 = remainder = 1 -> odd else even(0)
# num%2

# #WAP to check given word is palindrome or not(LEVEL)(reverse)

# step-1: define any word
# step-2: reverse the word 
# step-3: compare both word (define word,reverse word)
# step-4: if compare true print "given word is palindrom"
# step-5: else print "given word is not palindrom"

word = "APPLE"
reverse_word = word[::-1]
if word == reverse_word:
    print(f"the given word {word} is palindrome word")
else:
    print(word, " is not palindrome")



# git add .
# git commit -m "any message"
# git push



