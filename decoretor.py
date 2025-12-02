#step 1 : define a decoraterie funtion

def my_decorater(func):
    
     # inner funtion (wraper) tht add exctra functionality
    
    def wrapper():
        print("before the function runs ") # code to run before
        
        func() # calling the orignial function
        print("after the code runs") # code to run after
        
        #return the wrapper funtion
    return wrapper

#step 2 use the decorater on another function

@my_decorater  # this apply the decorator to the function below

def say_hello ():
    print("hello world")
    
# step 3 call the decorated function

say_hello()


