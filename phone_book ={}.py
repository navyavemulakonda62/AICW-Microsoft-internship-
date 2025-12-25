phone_book ={}
def add_contact():
     name=input("enter the name:").strip()
     phone_number=int(input("enter the phone number:").strip())
     phone_book[name]=phone_number
     print("contact saved successfuly")
     print("phone_book")
 

def read_contact():
    search_name=input("enter the name:").strip().lower()
    if search_name in phone_book.keys():
      print()
      print('-------------')
      print(f"the number for {search_name}:{phone_book[search_name]}")
    else:
       print("contact is not available")

 
def update_contact():
    update_contact=("enter the name:").strip().lower()
    update_number=int(input("enter new number to update"))
    phone_book[update_contact]=update_number
    print()
    print('-------------')
    print("----sucessfully updated-----")

def main():
    while(True):
         print("choose the task from below options")
         print("""
              1.Add contact
              2.Read contact
              3.update contact
              4.delete contact """)
         choice=int(input("enter the choice:"))
         if choice == 1:
           add_contact()
         elif choice == 2:
           read_contact()
         elif choice == 3:
           update_contact()
         else:
           break
if __name__=='__main__':
   main()