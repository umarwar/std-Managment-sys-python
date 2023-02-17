import csv
import os
import pandas as pd

class student_Interface():
    
    def __init__(self,roll_no,name,father_name,section,course,batch,Dob,address,gender):      #declare variables in constructor to use through-out the class
        self.roll_no = roll_no
        self.name = name
        self.father_name = father_name
        self.section = section
        self.course = course
        self.batch = batch
        self.Dob = Dob
        self.address = address
        self.gender = gender
    
    #All menu's    
    def wellcome_Menu(self):
        print("\t\t\tWellcome to\n\t\tStudent Management System\n\t\t\tBy Umar-139")
    def home_Menu(self):
        print("\n\t\t\t1)Display Record\n\t\t\t2)Add Record\n\t\t\t3)Del Record\n\t\t\t4)Update Record\n\t\t\t0)Terminate")
    def display_Menu(self):
        print("\n\t\t\t1)Display All\n\t\t\t2)Find by Roll.\n\t\t\t3)Find by Name\n\t\t\t4)Find by Father-name\n\t\t\t5)Find by Section\n\t\t\t0)Back")    
    def update_Menu(self):
        print("\n\t\t\t1)update all record\n\t\t\t2)Update Roll.\n\t\t\t3)Update Name\n\t\t\t4)Update Father-name\n\t\t\t5)Update Section\n\t\t\t0)Back")    
        
    #Add record Section   
    def add_Record(self):
         with open("record.csv",mode='a',newline='') as file:     
            if os.stat('record.csv').st_size == 0:  #checking if file is empty add this section
                writer = csv.writer(file)
                writer.writerow(["Roll","Name","Father-Name","Section","Course","Batch","DOB","Address","Gender"])
                ch = int(input("How many record enter: "))
                for i in range(ch):
                    self.roll_no = int(input("Enter Roll_no: "))
                    self.name = input("Enter Name: ")
                    self.father_name = input("Enter Father-name: ")
                    self.section = input("Enter Section: ")
                    self.course = input("Enter Course: ")
                    self.batch = int(input("Enter Batch: "))
                    self.Dob = input("Enter DOB(dd\mm\yy): ")
                    self.address = input("Enter Address: ")
                    self.gender = input("Enter Gender: ")
                    print("********************")
                    writer.writerow([self.roll_no,self.name,self.father_name,self.section,self.course,
                             self.batch,self.Dob,self.address,self.gender])      
            else:                            #if file has some data than append this section
                writer = csv.writer(file)
                ch = int(input("How many record enter: "))
                for i in range(ch):
                    self.roll_no = int(input("Enter Roll_no: "))
                    self.name = input("Enter Name: ")
                    self.father_name = input("Enter Father-name: ")
                    self.section = input("Enter Section: ")
                    self.course = input("Enter Course: ")
                    self.batch = int(input("Enter Batch: "))
                    self.Dob = input("Enter DOB(dd/mm/yy): ")
                    self.address = input("Enter Address: ")
                    self.gender = input("Enter Gender: ")
                    print("********************")
                    writer.writerow([self.roll_no,self.name,self.father_name,self.section,self.course,
                             self.batch,self.Dob,self.address,self.gender])    
                         
    #Display section
    def display_Record(self):
            self.display_Menu()
            ch = input("Enter choice: ")
            print("********************")
            try:
                ch = int(ch)   
            except ValueError:
                print("Only <Int> input allowed")
            if ch == 1:       #display all record
                try:
                    data = pd.read_csv("record.csv")
                    print(data)
                except pd.errors.EmptyDataError:
                    print("File is empty")
                    
            elif ch == 2:     #display by search roll number
                roll = input("Enter Roll: ")
                print("********************")
                try:
                    with open('record.csv','r') as file:
                        read_list = list(csv.reader(file, delimiter=','))
                    print("Roll\tName\tF-Name\tSection\tCourse\tBatch\tDOB\t\tAddress\tGender")    
                    for row in read_list:
                        if row[0] == roll:
                            for i in row:
                                print(i,end="\t")            
                            print("\n")      
                except pd.errors.EmptyDataError:
                    print("File is empty")
                    
            elif ch == 3:    #display by search name
                name = input("Enter Name: ")
                print("********************")
                try:
                    with open('record.csv','r') as file:
                        read_list = list(csv.reader(file, delimiter=','))
                    print("Roll\tName\tF-Name\tSection\tCourse\tBatch\tDOB\t\tAddress\tGender")     
                    for row in read_list:
                        if row[1] == name:
                            for i in row:
                                print(i,end="\t")
                            print("\n")      
                except pd.errors.EmptyDataError:
                    print("File is empty")             
                        
            elif ch == 4:          #display by search father name
                f_Name = input("Enter Father-Name: ")
                print("********************")
                try:
                    with open('record.csv','r') as file:
                        read_list = list(csv.reader(file, delimiter=','))
                    print("Roll\tName\tF-Name\tSection\tCourse\tBatch\tDOB\t\tAddress\tGender")    
                    for row in read_list:
                        if row[2] == f_Name:
                            for i in row:
                                print(i,end="\t")
                            print("\n")      
                except pd.errors.EmptyDataError:
                    print("File is empty")     
                 
            elif ch == 5:         #display by search section
                sec = input("Enter Section: ")
                print("********************")
                try:
                    with open('record.csv','r') as file:
                        read_list = list(csv.reader(file, delimiter=','))
                    print("Roll\tName\tF-Name\tSection\tCourse\tBatch\tDOB\t\tAddress\tGender")    
                    for row in read_list:
                        if row[3] == sec:
                            for i in row:
                                print(i,end="\t")
                            print("\n")            
                except pd.errors.EmptyDataError:
                    print("File is empty") 
              
            elif ch == 0:         #return to main menu
                pass                               
    
            else:
                print("Enter right choice")       
             
    #Delete section            
    def delete_Record(self):
        try:                  #if file not empty than delete record
            file = open('record.csv','r')
            read_list = csv.reader(file)
            self.temp_list = []
            del_key = int(input("Enter the Roll to del: "))
            print("********************")
            Found = False
            for row in read_list:
                if row[0] == str(del_key):
                    Found = True
                    print('Record deleted successfully')
                    print("***************************")
                else:
                    self.temp_list.append(row)
            file.close()        
            if Found == False:
                print("Student not found")
            else:
                file = open('record.csv' ,"w+", newline='')
                writer = csv.writer(file)
                writer.writerows(self.temp_list)
                file.seek(0)
                read_list = csv.reader(file)
                for row in read_list:
                    for i in row:
                        print(i,end="\t")
                    print("\n")               
                file.close()     
        except pd.errors.EmptyDataError:      #if file empty
            print("File is empty")   
            
    def write_update_data(self): #write the updated data in file
        file = open('record.csv','w+',newline='')
        writer = csv.writer(file)
        writer.writerows(self.my_list)
        file.close()         
        
    #Update Section:
    def update_Record(self):
        self.update_Menu()
        ch = input("Enter choice: ")
        print("********************")
        try:
            ch = int(ch)   
        except ValueError:
            print("Only <Int> input allowed")
        self.my_list = []    
        if ch == 1:           #update all record 
            try:
                with open('record.csv','r') as file:
                    read_list = csv.reader(file)
                    for row in read_list:
                        self.my_list.append(row)
                print("Detail of CSV file below:")
                for i in range(len(self.my_list)):
                    print('Row'+ str(i)+':'+str(self.my_list[i]))
                edit = int(input("\nWhich record would you like to update? Enter Row: "))
                print("\nPlease enter new details of following:\n")
                for i in range(len(self.my_list[0])):
                    new_data = input("Enter new " + str(self.my_list[0][i])+ ":")
                    self.my_list[edit][i] = new_data
                print("Record Updated Successfully...!!!New detail of CSV file below:")
                for i in range(len(self.my_list)):
                    print(str(self.my_list[i]))
                with open('record.csv','w+',newline='') as file:
                    writer = csv.writer(file)
                    for i in range(len(self.my_list)):
                        writer.writerow(self.my_list[i])        
            except pd.errors.EmptyDataError:
                print("File is empty")
                   
          
        elif ch ==2:          #update roll number by search roll number
            try:
                file = open('record.csv','r')
                read_list = csv.reader(file)
                self.u_key = int(input("Enter the Roll to update: "))
                print("********************")
                Found = False
                for row in read_list:
                    if row[0] == str(self.u_key):
                        Found = True
                        new_roll = input("Enter new Roll: ")
                        row[0] = new_roll
                        print("\nRecord updated successfully")
                    self.my_list.append(row)
                file.close()        
                if Found == False:
                    print("Student not found")
                else:
                    self.write_update_data()
            except pd.errors.EmptyDataError:
                print("File is empty")
                
        elif ch ==3:             #update name by search roll number
            try:
                file = open('record.csv','r')
                read_list = csv.reader(file)
                self.u_key = int(input("Enter the Roll to update: "))
                print("********************")
                Found = False
                for row in read_list:
                    if row[0] == str(self.u_key):
                        Found = True
                        new_name = input("Enter new Name: ")
                        row[1] = new_name
                        print("\nRecord updated successfully")
                    self.my_list.append(row)
                file.close()        
                if Found == False:
                    print("Student not found")
                else:
                    self.write_update_data()    
            except pd.errors.EmptyDataError:
                print("File is empty") 
                
        elif ch ==4:           #update father name by search roll number
            try:
                file = open('record.csv','r')
                read_list = csv.reader(file)
                self.u_key = int(input("Enter the Roll to update: "))
                print("********************")
                Found = False
                for row in read_list:
                    if row[0] == str(self.u_key):
                        Found = True
                        new_fname = input("Enter new f-Name: ")
                        row[2] = new_fname
                        print("\nRecord updated successfully")
                    self.my_list.append(row)
                file.close()        
                if Found == False:
                    print("Student not found")
                else:
                    self.write_update_data()  
            except pd.errors.EmptyDataError:
                print("File is empty")       
                
        elif ch ==5:          #update section by search roll number
            try:
                file = open('record.csv','r')
                read_list = csv.reader(file)
                self.u_key = int(input("Enter the Roll to update: "))
                print("********************")
                Found = False
                for row in read_list:
                    if row[0] == str(self.u_key):
                        Found = True
                        new_sec = input("Enter new Section: ")
                        row[3] = new_sec
                        print("\nRecord updated successfully")
                    self.my_list.append(row)
                file.close()        
                if Found == False:
                    print("Student not found")
                else:
                    self.write_update_data()    
            except pd.errors.EmptyDataError:
                print("File is empty")                          
                
        elif ch == 0:              #return to main menu
            pass                               
    
        else:
            print("Enter right choice")         
                
        
        
#main class     
class main():
    s = student_Interface(1001,"umar","waris","c","apt",20,"4/10/2002","gujranwala","male")

    while True:
        s.wellcome_Menu()
        s.home_Menu()
        ch = input("Enter choice: ")
        print("********************")
        try:
            ch = int(ch)   
        except ValueError:
            print("Only <Int> input allowed")
        #calling All funtion   
        if ch == 1:
            s.display_Record()    
            print("\n********************")
        elif ch == 2:
            s.add_Record()    
            print("********************")
        elif ch == 3:
            s.delete_Record()
            print("********************")
        elif ch == 4:
            s.update_Record()
            print("********************")
        elif ch == 0:
            break
        else:
            print("Please Enter Correct Choice")
            print("***************************")   
            
m = main()                   