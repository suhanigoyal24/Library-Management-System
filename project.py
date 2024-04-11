import pickle
import os
def databases():
    f=open('library.dat','wb')
    header=["Book code","Book name","Author name","Book price"]
    pickle.dump(header,f)
    fields=[[1,'Klara And The Sun','Kazuo Ishiguro ',455],
            [2,'Rich Dad Poor Dad','Robert Kiyosaki',568],
            [3,'The Butterfield ',' Rosaria Buterld',667],
            [4,'Geography Of India','Majid Hussain ',445],
            [5,'Man Who Counted  ','Malba  Tahan   ',325],
            [6,'One Indian Girl  ','Chetan  Bhagat ',567],
            [7,'Guns Of  August ',' Barbara Tuchman',456],
            [8,'Trans Atlantic  ',' Colum  McCannon',234],
            [9,'Tortoise And Hare','Eric Ham Carle ',123]]
    for i in fields:   
        pickle.dump(i,f)
    f.close()
#function calling
databases()
def borrow_lend():
    f=open('dates.dat','wb')
    header=["Book code","Book name","Borrow Date","Return Date",'No of days book lent for',"Book Returned"]
    pickle.dump(header,f)
    fields=[[1,'Klara And The Sun','1 janaury 2022','15 janaury 2022',15,'Yes'],
            [2,'Rich Dad Poor Dad','12 febraury 2022','27 febraury 2022',15,'Yes'],
            [4,'Geography Of India','1 september 2022','-',20,'No'],
            [8,'Trans Atlantic','12 janaury 2023','-',15,'No']]
    for i in fields:   
        pickle.dump(i,f)
    f.close()
#function calling
borrow_lend()
def user_offer():
    print('Read the following menu and enter your choice')
    print('\n')
    print('Press 1 to add records')
    print('Press 2 to display all book records')
    print('Press 3 to search a record by book code no.')
    print('Press 4 to search a record by book name')
    print('Press 5 to update a record without considering lending')
    print('Press 6 to delete a record by book code no.')
    print('Press 7 to search by code no. the details of lending the book')
    print('Press 8 to calculate and display interest due on the book lended')
    print('Press 9 to update details on return of the book lended')
    print('Press 10 to exit')
user_offer()
print('\n')
c=int(input('Enter your choice here:'))
if c==1:
    def add_record():
        try:
            f=open('library.dat','ab')
            z=0
            while True:
                cn=int(input("Enter book code no:"))
                name=input("Enter the book name:")
                author=input("Enter name of the author:")
                pr=float(input('Enter price of the book:'))
                borrow=0
                name=name.title()
                author=author.title()
                rec=[cn,name,author, pr,borrow]
                pickle.dump(rec,f)
                z+=1
                print("Record added in file")
                ch=input('Do you want to add more records? if yes press y or Y')
                if ch=='y'or ch=='Y':
                  continue
                else:
                  break
        except EOFError:
            f.close()
            if z==0:
                print('Problem occured.Please restart')      
    add_record()
elif c==2:
    def displayrecords():
        try:
            f=open("library.dat","rb")
            print('='*66)
            i=0
            while True:
                rec=pickle.load(f)
                if not rec:
                    break
                print(rec[0],' '*7,rec[1],' '*5,rec[2],' '*7,rec[3],end='\n')
                if i==0:
                    print('='*66)
                    i+=1
            f.close()
        except EOFError:
            print('='*66)
            f.close()
        except IOError:
            print("Unable to open the file")
    displayrecords()
elif c==3:
    def search_bycode():
        try:
            z=0
            s=int(input("Enter code no to search:"))
            f=open("library.dat","rb")
            while True:
                rec=pickle.load(f)
                if rec[0]==s:
                    z+=1
                    print('Book found')
                    print('='*77)
                    print("Book code",' '*9,"Book name",' '*13,"Author name",' '*9,"Book price")
                    print('='*77)
                    print(rec[0],' '*15,rec[1],' '*6,rec[2],' '*7,rec[3])
                    print('='*77)
            f.close()
        except EOFError:
            f.close()
            if z==0:
                print("Book not found")
        except IOError:
            print("Unable to open the file.Please restart.")
    search_bycode()
elif c==4:
    def search_byname():
        try:
            z=0
            s=input("Enter book name to search:")
            s=s.title()
            f=open("library.dat","rb")
            while True:
                rec=pickle.load(f)
                if rec[1]==s:
                    z+=1
                    print('Book found')
                    print('='*77)
                    print("Book code",' '*9,"Book name",' '*13,"Author name",' '*9,"Book price")
                    print('='*77)
                    print(rec[0],' '*15,rec[1],' '*6,rec[2],' '*7,rec[3])
                    print('='*77)
                    
            f.close()
        except EOFError:
            f.close()
            if z==0:
                print("Record not found")
        except IOError:
            print("Unable to open the file")
    search_byname()
elif c==5:
   def update_record():
      try:
         z=0
         s=int(input('Enter book code:'))
         f=open('library.dat','rb')
         tf=open('temp.dat','wb')
         while True:
             rec=pickle.load(f)
             if not rec:
                 break
             if rec[0]==s:
                 z+=1
                 print('Old record')
                 print('='*77)
                 print("Book code",' '*9,"Book name",' '*13,"Author name",' '*9,"Book price")
                 print('='*77)
                 print(rec[0],' '*15,rec[1],' '*6,rec[2],' '*7,rec[3])
                 print('='*77)
                 print('\n')
                 print('Enter new data')
                 book_code=int(input('Book Code:'))
                 book_name=input('Book Name:')
                 author_name=input('Author Name:')
                 book_price=int(input('Book Price:'))
                 book_name=book_name.title()
                 author_name=author_name.title()
                 rec=[book_code,book_name,author_name,book_price]
                 pickle.dump(rec,tf)
      except EOFError:
          f.close()
          tf.close()
          if z==0:
              print('Book not found')
          else:
             print('Record has been updated')
             os.remove('library.dat')
             os.rename('temp.dat','library.dat')
      except IOError:
          print('Unable to find the file.Please restart')
#Function Calling
   update_record()
elif c==6:
    def delete_record():
        try:
            z=0
            s=int(input("Enter book code to delete:"))
            f=open('library.dat','rb')
            tf=open('temp.dat','wb')
            while True:
                rec=pickle.load(f)
                if rec[0]==s:
                    z+=1
                    print('The record being deleted is:')
                    print('='*77)
                    print("Book code",' '*9,"Book name",' '*13,"Author name",' '*9,"Book price")
                    print('='*77)
                    print(rec[0],' '*15,rec[1],' '*6,rec[2],' '*7,rec[3])
                    print('='*77)
                else:
                    pickle.dump(rec,tf)
        except EOFError:
            f.close()
            tf.close()
            if z==0:
                print("Record not found")
            else:
                print('Record deleted succesfully')
                os.remove('library.dat')
                os.rename('temp.dat','library.dat')
        except IOError:
            print("Unable to open the file")
    delete_record()
elif c==7:
    def search_bycodeno():
        try:
            z=0
            a=int(input("Enter code no of book to be searched:"))
            f=open("dates.dat","rb")
            while True:
                rec=pickle.load(f)
                if rec[0]==a:
                    z+=1
                    print('Book found')
                    if rec[5]=='no' or rec[5]=='No' or rec[5]=='NO':
                        print('The entered book has not been returned')
                        print("It's details are")
                    else:
                        print('The entered book has been returned')
                        print("It's details are")
                    print('='*77)
                    print("Book code",' '*9,"Book name",' '*13,"Issue date",' '*9,"Return date")
                    print('='*77)
                    print(rec[0],' '*15,rec[1],' '*6,rec[2],' '*7,rec[3])
                    print('='*77)
        except EOFError:
            f.close()
            if z==0:
                print("Record not found")
        except IOError:
            print("Unable to open the file")

    search_bycodeno()
elif c==8:
    def interest():
        try:
            z=0
            a=int(input("Enter code no of book to be searched:"))
            f=open("dates.dat","rb")
            while True:
                rec=pickle.load(f)
                if rec[0]==a:
                    z+=1
                    print('Book found')
                    print('='*115)
                    print("Book code",' '*3,"Book name",' '*11,"Issue date",' '*5,"Return date",' '*5,'No of days book was lent for')
                    print('='*115)
                    print(rec[0],' '*11,rec[1],' '*3,rec[2],' '*1,rec[3],' '*1,rec[4])
                    print('='*115)
                    print('\n')
                    if rec[5]=='no' or rec[5]=='No' or rec[5]=='NO':
                        t=rec[4]    
                        r=5
                        inst=r*t
                        print('The entered book has not beeen returned')
                        print('The book was to be returned in ',rec[4],'days')
                        print('Interest due till the required date of return is',inst)
                        print('There will be a penalty charge of 5rs each day till the book is returned for late return') 
                    else:
                        print('The entered book has been returned on',rec[3])
                    
        except EOFError:
            f.close()
            if z==0:
               print("The entered book has not been lent")
        except IOError:
            print("Unable to open the file")
    interest()
elif c==9:
   def update_byrecord():
      try:
         z=0
         s=int(input('Enter book code no: '))
         f=open('dates.dat','rb')
         tf=open('temp.dat','wb')
         while True:
             rec=pickle.load(f)
             if rec[0]==s:
                 z+=1
                 if rec[5]=='no' or rec[5]=='No' or rec[5]=='NO':
                     print('Book found')
                     print('='*120)
                     print("Book code",' '*9,"Book name",' '*13,"Issue date",' '*9,"Return date",' '*3,'No of days book was lent for')
                     print('='*120)
                     print(rec[0],' '*15,rec[1],' '*6,rec[2],' '*7,rec[3],' '*9,rec[4])
                     print('='*120)
                     print('\n')
                     rec[5]='Yes'
                     m=input('Enter month of return in words:')
                     d=input('Enter date of return:')
                     y=input('Enter year of return:')
                     rec[3]=d+' '+m+' '+y
                     print('The entered return date is',rec[3])
                     tp=[rec[0],rec[1],rec[2],rec[3],rec[4],rec[5]]
                     pickle.dump(rec,tf)
                     print('Return succesful')
                     ch=input('Do you want to enter more records of return ?If yes enter y')
                     if ch=='Y' or ch=='y':
                         continue
                     else:
                         break
                 else:
                     print('The entered book has been returned on',rec[3])
                     break
      except EOFError:
          f.close()
          tf.close()
          if z==0:
              print('The entered book has not been lended')
          else:
             os.remove('library.dat')
             os.rename('temp.dat','library.dat')
      except IOError:
          print('Unable to find the file')
#Function Calling
   update_byrecord()
elif c==10:
    print('You chose to exit')
else:
    print('Wrong choice entered.Please restart')

