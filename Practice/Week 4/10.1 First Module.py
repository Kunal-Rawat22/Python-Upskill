import Second_Module
# If the python file is directly running then __name__ will be equal to __main__
# else if the python module/file is imported then __name__ will be equal to name of the file

print(f"First Module's name: {__name__}")