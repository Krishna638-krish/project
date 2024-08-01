print("quiz game")
def fst():
    print("1.what is the name of capital of india?")
    a='''1.Delhi
2.mumbai
3.Tamilnadu'''
    print(a)
    c=int(input("enter the choise:"))
    if c==1:
        print("correct")
    else:
        print("worng")
    sec()
def sec():
    print("2.who is the India prime minister?")
    a='''1.giri
2.kishore 
3.modi'''
    print(a)
    c=int(input("enter the choise:"))
    if c==3:
        print("correct")
    else:
        print("worng")
    third()
def third ():
    print("3.how many states in India")
    a='''1.28
2.27
3.32'''
    print(a)
    c=int(input("enter the choise:"))
    if c==1:
        print("correct")
    else:
        print("wrong")
fst()
