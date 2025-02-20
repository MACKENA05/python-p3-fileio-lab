def write_file(file_name, file_content):
    file_name = str(file_name) + ".txt"
    with open(file_name, 'w') as lf:
        lf.write(file_content)


def append_file(file_name, append_content):
    file_name = str(file_name) + ".txt"  
    with open(file_name, 'a') as lf:
        lf.write(append_content)

def read_file(file_name):
    file_name = str(file_name) + ".txt"  
    with open(file_name, 'r') as lf:
        return lf.read()

write_file(file_name="logfile", file_content="Log 1: 5 bananas added" )
append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")

read_file(file_name="logfile")