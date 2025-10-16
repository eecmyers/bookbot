def get_book_text(file_path):
# read file text into a string
  with open(file_path) as f:
    file_contents = f.read()
    return file_contents

def countwords(book_text):
    #get number of words
    list_of_words = book_text.split() 
    return len(list_of_words) 

def unique_char_cnt(book_text):
    # input is string, returns dictionary
    # {'p': 6121, 'r': 20818, 'o': 25225, ..

    lowercase_str = book_text.lower()
    #lower case only

    my_char_set = set()
    my_dict = {} 

    for i in range(0,len(lowercase_str),1):
       my_char_set.add(lowercase_str[i])
       #remove duplicates

    for i in my_char_set:
        my_dict[i] = 0
        #set all char counts to 0

    for i in range(0,len(lowercase_str),1):
        for letter in my_dict:
            if letter == lowercase_str[i]:
                my_dict[letter] = my_dict[letter] + 1
    #iterate through eatch letter in string, increase count of a key value if found.

    return my_dict
  
def sort_my_dict(my_dict):
 #creates a list of dictionaries in char, num pairs
    my_list_of_dict = [] 
    tmp_dict = {}
   
    for pair in my_dict:
        tmp_dict = { "char": pair, "num": my_dict[pair]}
        my_list_of_dict.append(tmp_dict)
    return my_list_of_dict

#helper function for sorting the dictionary
def sort_on(items):
        return items["num"]

def print_my_list(my_list):
    for dicts in my_list:
        if dicts["char"].isalpha():
            print(f"{dicts["char"]}: {dicts["num"]}")
