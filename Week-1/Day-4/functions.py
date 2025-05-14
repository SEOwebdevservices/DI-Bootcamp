#functions
#syntax

#def func_name():
 #   '''prints a phrase on the console''' #doc strings
 #   print("I am a function")

#func_name()
#print(print.__doc__)


#def greeting(language):
   # '''prints a phrase on the console'''
  #  if language == "PT":
 #      print("Ola") 
 #   elif language == "EN":    
 #       print("Hello")

#greeting("PT")
greeting(user_name = "Steve", language = "EN")

def greeting(language, user_name):
    '''prints a phrase on the console'''
    if language == "ES":
       print(f"Ola {user_name} ") 
    elif language == "RU":    
        print(f"Previet {user_name} ") 
    elif language == "PT":    
        print(f"Ola {user_name} ") 
    elif language == "EN":    
        print(f"Sup {user_name} ")    
    else:
       print("undefined language")




#create a function called country_info that receoves a country name as argument
# and prints the capital of that country. make the ecountry name argument default
#Naboo's capital is Theed

#def country_info(country_name = Naboo)
#if country_name == "France":
   # print("The capital of {country_name} is Paris")
#elif country_name == "Italy":
    #print(f"The capital of {} is Rome")
   # elif country_name == "Naboo":
   # print(f"The capital of {} is Theed")
#else:
   # print("country name not found")   
#country_info("patati")

#def calculation(num1, num2):
    #result = num1 + num2
    #return result
#print(calculation(5, 4))


