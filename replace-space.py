# Write a method to replace all spaces in a string with '%20'.

def replace_space(string, length):
    # convert to list because python strings are immutable
    char_list = list(string)
    string = ""
    new_index = len(char_list)

    for i in reversed(range(length)):
        if char_list[i] == " ":
            char_list[new_index - 3: new_index] = "%20"
            new_index -= 3
        else:
            char_list[new_index - 1] = char_list[i]
            new_index -= 1
        
    return string.join(char_list)

string = "do nothing"
length = len(string)
print(replace_space(string, length))
