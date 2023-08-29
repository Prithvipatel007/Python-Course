# functions with outputs

# Takes first name and last name and change it into title case (First letter is capitalized in each word)
def format_name(f_name, l_name):
    """
    Take first and last name and format it  
    to return the title case version of the name
    """
    if(f_name == "" or l_name == ""):
        return  "You didn't provide valid inputs"     # terminate the function

    result = f_name.title() + " " + l_name.title()
    return result # defines the end of function
    print("This nerver gets executed")


first = "prithvi"
last = "patel"

res = format_name(first, last)

print(res)