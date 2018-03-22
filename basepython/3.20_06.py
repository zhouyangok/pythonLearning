
def open_file(file_name):
    try:
        with open("C:/Users/medo_zy/Desktop/"+file_name) as file_object:
            bw = file_object.read().strip()
            print(bw)
    except FileNotFoundError as e:
        print(e)

file_names = ['test.txt','testPython.txt','testJava.txt']
for file_name in file_names:
    open_file(file_name)
