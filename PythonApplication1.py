
note_list={}
while True:
    print("choose number for following action \n")
    print("choose 1 for creating a new file\n")
    print("choose 2 for show the created file\n")
    print("choose 3 for deleting a file\n")
    print("choose 4 to edit a file\n")
    print("choose 5 to exit the app")
    user_input=input("choose an option ")
    
    if user_input=="1":

        title=input("input title: ")
        note=input("write your note: ")
        storage={title:note}
        note_list.update(storage)

    elif user_input=="2":
        print (note_list.keys())

        lists=input("write which title you want to see: ")
        print(note_list.get(lists))

        
    elif user_input=="3":
        print(note_list.keys())
        lists1=input("choose which title you want to delete: ")
        print("you have deleted the following content: ",note_list.pop(lists1))
        
    elif user_input=="4":
        pass
    elif user_input=="5":
        break
    else:
        print("inpt a valid option") 

    
     
    
