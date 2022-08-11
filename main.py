# ScriptName: main.py
# Author: <add your name here>

# template for calling functions in another file

# import my_functions from other files - different options
# from my_functions import print_function
# import my_functions - when you use this you need to call the function using 'my_functions.<function_name>'
# this option imports all my_functions, using '*'
from my_functions import *
from settings import *

# # helper function...
# def create_kwargs(param_name_r: str, input_vals_r: list) -> list:
#     '''
#     create a list of dictionaries to pass to our functions
#     '''
#     return_list = []
#     # for every value in the input list - create a dictionary
#     for _, value_r in enumerate(input_vals_r):
#         dict_r ={}
#         # for every parameter, create a key,value pair
#         for key_index, key in enumerate(param_name_r):
#             try:
#                 dict_r[key]=value_r[key_index]
#             except:
#                 continue
#         # append the newly created dictionary to the return list
#         return_list.append(dict_r)

#     return return_list

# # our main function
# def main():
#     """
#     Call the functions defined in the my_functions.py file
#     """
#     print("\nprint_function examples")
#     # these are the 6 calls I have created in the settings file
#     print(print_function("I'm in another file"))
#     print(print_function("Really, in another file"))
#     print(print_function(7))
#     print(print_function(True))
#     print(print_function("Oops"))
#     print(print_function("this won't work")) # this is there to show what happens when the resutls is not correct

#     print("\nprint_function2 examples")
#     # this is an example where we have 2 parameters and one has a default value
#     print(print_function2("I'm in another file", ":)"))
#     print(print_function2("Really, in another file")) # we use the default value here
#     print(print_function2(7, ":)"))
#     print(print_function2(True, ":)"))
#     print(print_function2("Oops", ":)"))
#     print(print_function2("this won't work", ":)"))

#     print("\nnow lets see if we can get the same results using what we have learned in class :)\n")

#     try:
#         # get all the function names from your my_functions file
#         mod_r = importlib.import_module("my_functions")
        
#         # loop over each of the functions to be tested
#         for index, _ in enumerate(test_func):
#             print("test "+ str(index+1)+":")
#             # create a test output list
#             test_output = []
#             # for each parameter - link it to its parameter input values
#             for val in create_kwargs(param_name[index], input_vals[index]):
#                 try:
#                     # test the functions
#                     test_output.append(getattr(mod_r, test_func[index])(**val))
#                 except Exception as e:
#                     return "Seems to be a problem in the code: "+str(e)

#             # now lets check if the values in the outputlist for this function
#             # is the same as the content of the test_output list
#             test_counter = 0
#             for _, test in enumerate(test_output):
#                 # grade the function calls
#                 if test == outputlist[index][test_counter]:
#                     print("\""+test +"\""+ "  equals " + "\""+outputlist[index][test_counter]+"\"", " - well done!!!")
#                 else:
#                     print("\""+test +"\""+ " does not equal " + "\""+outputlist[index][test_counter]+"\"", " - awww!!!")
#                 # increment our test counter
#                 test_counter += 1

#             # just add a blank line printed to terminal
#             print()

#     except:
#         return "Something strange happened..."

# if __name__ == "__main__":
#     ''' call the main() function in this file '''
#     print(main())
# i= 0
# while i < 1:
# print(false_random_name_generator()) 

print(false_random_name_generator())