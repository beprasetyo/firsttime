#**kwargs = keyword argument
'''
def hello(first,last):
    print("Hello "+first+" "+last)

hello("Bro","Code")'''

def hello(**kwargs):
    #print("Hello "+kwargs['first']+" "+kwargs['last'])
    print("Hello ",end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")



hello(title="Mr.",first="Bro",middle="dude",last="code")
