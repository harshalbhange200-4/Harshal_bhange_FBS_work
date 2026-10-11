# write a program to input any alphabet and cheak whether it is vowel or consonant .
# take values 
alphabet = input('Enter the alphabet :')
# if condition 
vowel ='A','a','E','e','I','i','O','o','U','u' 

if(alphabet in vowel):
    #display result
    print('the alphabet is vowel.')
else :
    print('the alphabet is consonant .')