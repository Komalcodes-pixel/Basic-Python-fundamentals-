#Program to check if a line starts with vowel
with open("/data/user/0/com.markodevcic.python_code_pad/cache/file_picker/1767348900114/genrators.py","r") as u:
    for i in u:
        if i.startswith("aeiou"):
            print(i)
        else:
             print(False)
