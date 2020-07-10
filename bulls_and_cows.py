import random

print("Welcome to the Bulls and Cow game!")

def random_numbers_generator():
    temp = []
    for x in range(4):
        temp.append(random.randint(0,9))
    return temp

def is_unique(l):
    temp = []
    for i in l:
        if i not in temp:
            temp.append(i)
    temp_length = len(temp)
    list_length = len(l)
    if(temp_length<list_length):
        return False
    elif(temp_length==list_length):
        return True

def secret_code_generator():
    secret_code = random_numbers_generator()
    if(is_unique(secret_code)):
       # final_code = sum(d * 10**i for i, d in enumerate(secret_code[::-1]))
        return(secret_code)
    else:
        return(secret_code_generator())

def user_input():
    guess = input("Enter you guess: ")
    guess_list = []
    while(guess>0):
        digit = guess%10
        guess_list.append(digit)
        guess=guess/10
    return guess_list[::-1]
    
def bulls(l1,l2): #correct in correct position
    bulls = 0
    for i in range(len(l1)):
        if(l1[i]==l2[i]):
            bulls=bulls+1
    return bulls

def cows_temp(l1, l2): #correct but may not be in correct place
    cows = 0
    for i in l1:
        if i in l2:
            cows=cows+1
    return cows

def main():
    flag = 1
    x = secret_code_generator()
    while(flag): 
        y = user_input()
        b = bulls(x,y)
        c = cows_temp(x,y)
        c_final = c - b
        print("Bulls: "+str(b))
        print("Cows: "+str(c_final))
        if(x==y):
            print("Congratulations! Your guess is correct.")
            flag = 0
        
if __name__=="__main__":
    main()