# ChapterThree/Order-1/main.py

"""
make faster by accessing the value directly from the dictionary using get() method
No for loop, no if statement, no recursion..
Just return the value directly from the dictionary using get() method
"""

def find_last_name(names_dict, first_name):
    try:
        return names_dict[first_name]
    except KeyError:
        return None



#def find_last_name(names_dict, first_name):
#    for current_first_name, last_name in names_dict.items():
#        if current_first_name == first_name:
#            return last_name
#
#
#def find_last_name(names_dict, first_name):
#    """accessing names_dict directly using get() """
#    return names_dict.get(first_name)
#
#
#def find_last_name(names_dict, first_name):
#    try:
#        return names_dict[first_name]
#    except KeyError:
#        return None
