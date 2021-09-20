import os
import random
import string
letters_and_digits =string.ascii_lowercase + string.digits

# input 123456.png
# output R1R2R2R4R5R6.png
# R stands for a random number or a letter

for filename in os.listdir("torename"):
    filename_splitted = filename.split('.',1)
    filename_basename = filename_splitted[0]
    filename_extension = filename_splitted[1]
    filename_basename_list = list(filename_basename)

    random_chars = random.choices(letters_and_digits, k=len(filename_basename))

    newbasename_list = [x for y in zip(random_chars,filename_basename_list) for x in y]

    newbasename = ''.join(newbasename_list)

    new_name = newbasename + "." + filename_extension

    # renaming happens here
    os.rename(os.path.join("torename",filename), os.path.join("torename",new_name))
  
    # to decode
    print(new_name[1:-3:2])
