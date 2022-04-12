#Original code adapteed from Corey Schafer https://youtu.be/FsAPt_9Bf3U 
# Case 1
#msg=input('Enter your intended message
assert(1+1)
def outer_function(msg):
    assert(1+1)
    message=msg
    def inner_function():
        print(message)
    return inner_function

my_function=outer_function('First class function')
my_function()

# Case 2: Decorator functions "Long-cut"
def decorator_function(original_function):  
    def wrapper_function():
        print("Wrapper executed this")
        return original_function()
    return wrapper_function
def display():
    print("The display function ran")

decorated_display=decorator_function(display)
#decorator_function.display()
decorated_display()

# Case 3: Decorator functions "Long-cut"
# Note This part needs some modifications 

def decorator_function2(original_function2):
    def wrapper_function2(*args,**kwargs):
        print("Wrapper Executed this part")
        return original_function2()
    return wrapper_function2
@decorator_function2
def display_info(name,age):
    print("Display info ran with arguments({},{})".format(name,age))
#a=display_info("John",26)

