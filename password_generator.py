import string
import random

def pass_gen():
     l = string.ascii_lowercase
     u = string.ascii_uppercase
     d = string.digits
     p = string.punctuation
     # empty list
     pass_list = []
     # add chars to the list
     pass_list.extend(l)
     pass_list.extend(u)
     pass_list.extend(d)
     pass_list.extend(p)
     # shuffle password list chars (reorganize the order of the list items)
     random.shuffle(pass_list)
     # get password length from user input
     pass_length = int(input("Enter password length : "))
     # convert password list to string from index 0 to password length entered from user
     password = "".join(pass_list[0:pass_length])
     # print password generated 
     print(f"Password generated is : {password}")

if __name__=="__main__":
     pass_gen()