import webbrowser

def rename_files():
    file_names = os.listdir("C:\\Users\\Default\\Downloads\\prank\\prank")
    print (file_names)

    #print("A says ki.........")
    os.chdir("C:\\Users\\Default\\Downloads\\prank\\prank")
    current_working_directory = os.getcwd()
    print(current_working_directory)


    for filename in file_names:
        os.rename(filename,filename.translate(str.maketrans('','',"0123456789")))
    new_file_list = os.listdir("C:\\Users\\Default\\Downloads\\prank\\prank")
    print(new_file_list)


rename_files()