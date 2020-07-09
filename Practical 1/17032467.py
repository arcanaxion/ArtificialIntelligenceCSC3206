friends = [["Dale", "US", "Georgia"], ["Rodolfo", "US", "Illinois"], 
           ["Kristina", "US", "Texas"], ["Evan", "Greenland", "Danmarkshavn"],
           ["Rosario", "UK", "Garthbrengy"], ["Denise", "UK", "Popeswood"],
           ["Thomas", "UK", "Black Heddon"], ["Elaine", "UK", "Old Swarland"],
           ["Abigail", "New Zealand", "Auckland"], 
           ["Evan", "Australia", "Victoria"]]

def filterFriend(name='', home_country='', home_state=''):
    filtered = []
    for x in friends:
        if x[0] == name and home_country == '' and home_state == '':
            filtered.append(x)
        elif name == '' and x[1] == home_country and home_state == '':
            filtered.append(x)
        elif name == '' and home_country == '' and x[2] == home_state:
            filtered.append(x)
        elif x[0] == name and x[1] == home_country and home_state == '':
            filtered.append(x)
        elif x[0] == name and home_country == '' and x[2] == home_state:
            filtered.append(x)
        elif name == '' and x[1] == home_country and x[2] == home_state:
            filtered.append(x)
        elif x[0] == name and x[1] == home_country and x[2] == home_state:
            filtered.append(x)
        elif name == '' and home_country == '' and home_state == '':
            filtered.append(x)
    return filtered

print(filterFriend(home_country='UK'))