# ScriptName: my_functions.py
# Author: James Goring - 121127318

# template for calling functions in another file
from random import *


# I left these in...Not sure what they do tbh. Uncomment if you want them. Cheers.
# def print_function(input_string:str) -> str:
#     '''
#     input_string - string input\n
#     return input_string with a nice happy face
#     '''
#     try:
#         return input_string+" :)"
#     except:
#         return "Oops"


# def print_function2(input_string:str, added_string:str = ":(") -> str:
#     '''
#     input_string - string input\n
#     return input_string with added_string added to it
#     '''
#     try:
#         return input_string+" "+added_string
#     except:
#         return "Oops"

'''
Intro speech.
The problem is that a game creator wants to generate random names but instead of getting things like Gum Gix, they wants things like Ted Smith etc. 
He also wants an easy file to manage if they desires to remove names or add names.
This function reads in a curated and special file that contains names of various size and gender. It also contains surnames.

The function and test framework:
It starts by asking the user for input. This is asking for size of the first name, size of the surname and if you want a male or female first name.
There are a few checks here. Because we know that input always gives back a string and they can type anything they want. We apply the ideology of try/expect. 
We attempt to cast the inputted string into a number and if it doesn't work, we inform the user that we can only take whole numbers. This is quite simple but really works.
If it isn't a whole number then it just fails and cue returned message of please only whole numbers. 
Granted, we could attempt to accept "one","two" etc. but I've asked politely to use a whole number, if you avoid it then error message.

The gender part is slightly worse. I am only checking the first letter of the string. So I've asked the user to put in Male/M/Female/F etc. But they want to fool around and put in MEAT then I'll accept it as Male. 
This is good and bad cause obviously MEAT isn't Male but I've asked them not to fool around and I want my code to work despite their fooling.

After that, it gets sent to some functions to pick a random letter and starts breaking up the masterfile into dictionaries within dictionaries within dictionaries. 
It works pretty well after that. As long the input is proper then it will work.

It is hard to fool around input because Sure you can type in "     3     " but I've included strip to remove those spaces.
Alright, how about "      3     3   " then it fails the casting and says whole numbers only. Which is fair.
Okay then "       16   ", That is over 6 so it will report that you are out of bounds. 
How about "True" - not a number etc.

The gender check is the vaguest and weakest check but it has a try/except if it fails to get grab the 0th index other than that it just checks if it is a M or F.
Anything else doesn't work, so instantly vetted.

Please note there is 2 global variables. I think they should work when you attempt to run this code. 
Please change the open file to Mac/Linux or whatever you are running on. Thank you!
Please don't change the format unless you want to add a name and see if it appears. 
The format for adding a name is simple enough. Find the length - 3/4/5/6 then gender/surname then after the last choice add a space " " then the name "Caelen" with no space after.

Example: c:{6:...Collin Caelen-S:...}. Done. Find the last choice, add a space then your name. 
That is it inserted into the file, it will be randomly picked.

I created an infite while loop with the correct parameters and it gave me random names forever. It is pretty good, it never found an error.
Yes it returned a few empty strings but that is good because not all characters have a name of that length and if we get an empty string then we rerun the function.

i = 0
while i < 1:
    print(consonant_curation(choice(["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z","a","e","i","o","u"]),6,"M"))

Thank you for reading and enjoy. Hopefully you get the white whale of names. Mrs Winter Wipple.


'''




# Global Variables that get used. Vaguely obsolete but I still use them so they are kept
g_consonant = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
g_vowel = ["a","e","i","o","u"]

def consonant_curation(char:str,first_len:int,gender:str="S") -> str:
    ''' This function opens the master file containing all of our names under specific tags. \n
        The tags are "M", "F" and "S" - Male,Female and surname respectively. There is also size tags - 3,4,5,6. \n
        Because this function is being called on. The assumptions are that the user has inputted the correct parameters and if they don't pick a gender then it will default to Surname.\n
    '''
    try:
        # New dictionary to start adding our data
        new_dict = {}
        # Open the master file
        master_file = open("D:\\Projects\\RandomNameGenerator\\masterfile.txt","r")
        # Read each line in the master file
        for line in master_file:
            # Because I have "\n" spaces between each line in the master file, I don't want to include them. This if statement skips that.
            if line != "\n":
                # Remove the end carriage at the end of the statement
                line = line.strip("\n")
                # Remove any spaces if inputted incorrectly
                line = line.strip()
                # Split the key "a" from the rest of the data {3:etc.}. The 1 is specific in picking the very first : and no others.
                innards = line.split(":",1)
                # Take the data {3:etc,4:etc,5:etc,6:etc}, Remove the {} brackets and then split it into [3:etc],[4:etc],[5:etc]. This means we now have [a],[3:etc],[4:etc],[5:etc]
                innards[1] = innards[1][1:-1].split(",")
                # Set the a,b,c,d,e,f,g etc to be a key in our lovely new dictionary.
                new_dict[innards[0]] = ""
                # Go over each [3:etc],[4:etc],[5:etc] and split it into [3][etc]
                for item in innards[1]:
                    # and split it into [3][etc]
                    item = item.split(":",1)
                    # Create a new_dictionary each time
                    value_dict = {}
                    # Assign the [3] into a key in this dictionary and then add the etc.
                    value_dict[item[0]] = item[1]
                    # if that key is blank in our New_Dictionary then assign this value_dict to it.
                    if new_dict[innards[0]] == "":
                        new_dict[innards[0]] = value_dict
                    else:
                        # If that key isn't blank then update it with our value_dictionary
                        new_dict[innards[0]].update(value_dict)
                        # This means we end up with {a:{3:etc},{4:etc}.{5:etc},{6:etc}}

        # Time to break up our ETC because etc actually means {M:Ada,Ara,etc.} Loop over our New_dict
        for values in new_dict.values():
            # Check the Inner_key and it's values, so 3 and etc.
            for inner_key,inner_value in values.items():
                # Remove the {} brackets from etc
                inner_value = inner_value[1:-1]
                # Split etc into [M:etc],[F:etc],[S:etc]
                inner_value = inner_value.split("-")
                # Remove any white noise
                inner_value[0] = inner_value[0].strip()
                inner_value[1] = inner_value[1].strip()
                inner_value[2] = inner_value[2].strip()
                # Split those values so now they exist as [[M],[etc]]
                inner_value_1 = inner_value[0].split(":")
                inner_value_2 = inner_value[1].split(":")
                inner_value_3 = inner_value[2].split(":")
                # Create a further dictionary
                new_value = {}
                # Start adding those values so {M:etc},{F:etc},{M:etc}
                new_value[inner_value_1[0]] = inner_value_1[1]
                new_value[inner_value_2[0]] = inner_value_2[1]
                new_value[inner_value_3[0]] = inner_value_3[1]
                # Go the key 3 and add {M:etc},{F:etc},{M:etc}
                values[inner_key] = new_value
        # So we have our dictionary within a dictionary within another dictionary. But we need get those names randomised.
        for value in new_dict.values():
            for innervalue in value.values():
                for innerkey,furthervalue in innervalue.items():
                    # Split the Names apart so a:3:M:Adam Adra Aren because a:3:M:[Adam,Adra,Aren]
                    furthervalue = furthervalue.split(" ")
                    # Assign that value back in.
                    innervalue[innerkey] = furthervalue
        # Close our file
        master_file.close()
    except Exception as e:
        return "Oops, Sorry", e
    # Return a random name using our parameters.
    # So if Char = a and length = 3 and gender = M then we goto key "a" then key "3" then key "M"
    # and grab a list[Adam,Adra,Aran] then pick a random choice of that.
    return choice(new_dict[char][str(first_len)][gender])

def letter_dict() -> str:
    '''This kind of pointlessly just picks a random letter. I kind of forgot about it but it works grand. I'll leave it alone.'''
    # Roll up roll up! Pick a letter any letter!
    random_choice = choice([choice(g_consonant),choice(g_vowel)])
    # Return said choice of letter! You win! Congrats little girl/boy!
    return random_choice

def firstname(first_len,gender="S"):
    ''' This to create our name. \n
        Originally was going to surname and firstname but ended up using the same upper function to do both. Hence the weird varible names\n
        Assumes that the false_random_name_generator was filled out correctly.
    '''
    try:
        # Create an empty string, not really needed
        Firstname = ""
        # Grab a random letter
        Firstname = letter_dict()
        # Sends the random letter plus the size of the name wanted and it's gender.
        Firstname = consonant_curation(Firstname,first_len,gender)
        # If the circumstance of returning a "" because it was something like "u",3,"M" and this has no value then repeat it again until you get something
        while len(Firstname) == 0:
            # Generate another random letter cause "u" didn't work so lets try "t"
            Firstname = letter_dict()
            # Off we go again. Lets hope it brings back anything cause it's looking for a length > 0
            Firstname = consonant_curation(Firstname,first_len,gender)
        # Success, return the firstname
    except:
        return "Oops, Error"
    return Firstname



def false_random_name_generator() -> str:
    ''' This is the screening function.\n
        First, it will ask you how long you want your name to be? Seperately. \n
        Then it will ask for gender or surname. \n
        It will screen you answers to make sure they are valid. \n
    '''
    try:
        # Inputs. Generic enough. Answer the question please.
        first_len = input("How long would you like the first name to be? Use a whole number between 3-6:")
        second_len = input("How long would you like the surname to be? Use a whole number between 3-6:")
        gender = input("Male or Female first name? Please use the following format, Male or Female or M or F:")
        # The first catch. If you don't put in a whole number then when it goes to cast it to an integer. It will crash and inform you: please use a whole number.
        try:
            # cast the input to an int. This kindly stops any silly inputs like strings,Booleans(Kind of),lists etc. 
            first_len = int(first_len.strip())
            second_len = int(second_len.strip())
            # remove any whitenoise from gender.
            gender = gender.strip()
            # Checks to make sure you put in Male/Female/male/female/M/F.
            # Now this does work if they put in something like Meat/Fart. Cause it just takes the first letter but that's all it needs. So HAH. Jokes on you - Have a male/female name.
            # Actually. This works with any length of sentence, so long as they start with M or F.
            # Honestly. I'm fine with this. If you want to write ME SO STUPID. You'll get a male name. I'll kindly asked you not write nonsense at the input level. Haha
            try:
                if gender[0].capitalize() == "M" or gender[0].capitalize().strip() == "F":
                    # Continue wasn't allowed and I needed python to just move on with it's life. So i=0 it is.
                    i = ""
                else:
                    # If you didn't put in Male/Meat/Mark then please try again and use a better word containing our wanted letter. 
                    return "Sorry Only Male or Female or M or F will be accepted. Anything else will be rejected."
            except:
                return "Please type in Male/Female/M/F. Anything else will be rejected. Thank you"
        except:
            return "Sorry, you need to pick a whole number for both inputs. Anything else will not be accepted."
        # Checks your asked for lenghth. We are currently only doing 3-6. Anything else can be added but currently not in use.
        if first_len <= 2 or first_len > 6:
            return "Sorry, The first name cannot be less than 3 or greater than 6."
        # Checks your asked for lenghth. We are currently only doing 3-6. Anything else can be added but currently not in use.
        if second_len < 3 or second_len > 6:
            return "Sorry, the surname cannot be less than 3 or greater than 6. Strangely, 2 letter surnames were quite rare, so I cut them"
        # off we go! Here our length and the gender and lets get a NAME!
        FirstName = firstname(first_len,gender[0].capitalize())
        # Lets get the surname! The default for our name creation is surname, so we don't need gender here. 
        Surname = firstname(second_len)
    except:
        return "Oops, Error"
    # Return our newly created firstname and surname. Lets capitalize them cause we aren't animals and done.
    return FirstName.capitalize() + " "+ Surname.capitalize()