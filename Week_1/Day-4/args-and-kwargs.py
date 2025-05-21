#*Args and **kwargs
def print_names(*args):
    for name in args:
        print(f"hello, {name}") 
    if not args:
        print ("please add a name to say hello") 
    print_names()

def user_info(**kwargs):

    user_info(name = "Juliana", age = 35, address = "Ramat Gan")   

def tasks_manager(*args):
    for tasks in args:
        print(f"today I need to {tasks}"):
tasks_manager("go shopping for Shabbat", "Get gas for car", "Finish Mini Project",)        



#

def party_planner(*args, **kwargs):
    if args:
        print('You need to buy: ')
        for arg in args:
            print(arg)
    else:
        print('there is no food to buy' )

    if kwargs:
        print('Party details: ')

        for key, value in kwargs.items():
            print(f' {key} : \n {value}')

            