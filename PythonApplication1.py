def create_note ():
    title=input("input title: ")
    note_list[title]=input("write your note: ")

def show_note():
     print (note_list.keys())
     ask=input("do you want to see your note Y/N: ").capitalize
     if ask=="Y":

            lists=input("write which title you want to see: ")
            print(note_list.get(lists))
     else:
          pass

def delete_note():
     print(note_list.keys())
     ask=input("do you want to delete your note Y/N: ").capitalize
     if ask=="Y":

            lists=input("choose which title you want to delete: ")
            print("you have deleted the following content: ",note_list.pop(lists))
     else:
          pass

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
       create_note()
    elif user_input=="2":
        show_note()
    elif user_input=="3":
      delete_note()
    elif user_input=="4":
        pass
    elif user_input=="5":
        break
    else:
        print("inpt a valid option") 

    
     
    
