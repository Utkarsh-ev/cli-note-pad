from ast import Is
import json
try:
    with open("notes.json","r") as note_file:
        note_list=json.load(note_file)
except:
    note_list={}

def create_note ():
    title=input("input title: ").capitalize().strip()
    note_list[title]=input("write your note: ").capitalize().strip()

def note_iterate():
    for i in note_list.keys():
        print(i)

def show_note():
        if note_list=={}:
            print("the note is empty")
        else:
            note_iterate()

        ask=input("do you want to see your note Y/N: ").capitalize().strip()
        if ask=="Y":

            lists=input("write which title you want to see: ").capitalize().strip()
            if lists not in note_list.keys():
                 print("this title does not exist or incorrect")
            else:
                 print(f"\n{note_list.get(lists)}\n")
        else:
             pass

def delete_note():
     print(note_iterate())
     ask=input("do you want to delete your note Y/N: ").capitalize().strip()
     if ask=="Y":

            lists=input("choose which title you want to delete: ").capitalize().strip()
            if lists not in note_list:
                print("title in not in the list ")
            else:
                print("you have deleted the following content: ",note_list.pop(lists))
     else:
          pass
def edit_note():
    print(note_iterate())
    print( "which title you want to edit\n ")
    edit_title=input(":").capitalize().strip()
    print("write your new content\n")
    new_content=input(":").capitalize().strip()
    note_list[edit_title]=new_content
    print(note_list)

def json_method():
     with open("notes.json","w") as note_file:
         json.dump(note_list,note_file)

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
       json_method()
    elif user_input=="2":
        show_note()
    elif user_input=="3":
      delete_note()
      json_method()
    elif user_input=="4":
        edit_note()
        json_method()
    elif user_input=="5":
        break
    else:
        print("input a valid option")

    
