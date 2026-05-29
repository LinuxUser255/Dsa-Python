# O(n^2) - Order “N Squared”
def does_name_exist(first_names, last_names, full_name):
    for first in first_names:
        for last in last_names:
            try:
                if first + " " + last == full_name:
                    return True
            except Exception as e:
                print(f'''An Error occurred 
                while checking the name: {e}''')
    return False


