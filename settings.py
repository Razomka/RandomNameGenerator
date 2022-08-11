# ScriptName: settings.py
# Author: <add your name here>

# settings for your tests

# ===================================================
# functions to call
test_func = ["print_function", # print_function example
             "print_function2", # print_function 2 example
             # "", # your function name
            ]

# ===================================================
# input parameter(s) and values to pass to the functions
param_name = [
              # print_function example
              ["input_string"], 
              # print_function 2 example
              ["input_string", "added_string"], 
              # your function parameter name(s) - list of String list(s) - with one name per parameter
              # [""],
             ]

input_vals = [
              # print_function example with one param
              [ ["I'm in another file"], ["Really, in another file"], [7], [True], ["Oops"], ["this won't work"], # [], [], [], [] 
              ],
              # print_function 2 example, with 2 params
              [ ["I'm in another file", ":)"], ["Really, in another file"], [7, ":)"], [True, ":)"], ["Oops", ":)"], ["this won't work", ":o)"], # [], [], [], [] 
              ],
              # your function parameter inout values - list of String list(s) - with one value per parameter
              # [ [], [], [], [], [], 
              #   [], [], [], [], [] 
              # ],
             ]

# ===================================================
# output values I must test against for this function
outputlist = [
              # print_function example
              [ "I'm in another file :)", "Really, in another file :)", "Oops", "Oops", "Oops :)", "this won't work", #
              ],
              # print_function 2 example
              [ "I'm in another file :)", "Really, in another file", "Oops", "Oops", "Oops :)", "this won't work ;)", #
              ],
              # your function return values to be tested against
              # [ , , , , , , 
              # ],
             ]
