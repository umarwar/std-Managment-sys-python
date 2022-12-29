class student:
    
    roll_no_l = []
    name_l = []
    section_l = []
    course_l = []
    
    def __init__(self,roll_no,name,section,course):      #declare variables in constructor to use through-out the class
        self.roll_no = roll_no
        self.name = name
        self.section = section
        self.course = course
    
    #Function to add data in list
    def add_Data(self):                  
        roll_no = input("Enter Roll_no: ")
        check = False
        while check == False:      #exception
            try:
                roll_no = int(roll_no)   
                check = True
            except ValueError:
                print("**************************")
                print("Please enter numeric only ")
                print("**************************")
                roll_no = input("Enter Again: ")
        self.roll_no_l.append(roll_no)
        while True:
            try:
                name = input("Enter your name: ")
                if name.isalpha():
                    break
                else:
                    raise TypeError
            except TypeError:
                print("*************************")
                print("Please enter letters only")
                print("*************************")
        self.name_l.append(name)
        while True:
            try:
                section = input("Enter Section: ")
                if section.isalpha():
                    break
                else:
                    raise TypeError
            except TypeError:
                print("*************************")
                print("Please enter letters only")
                print("*************************")
        self.section_l.append(section)
        while True:
            try:
                course = input("Enter Course: ")
                if course.isalpha():
                    break
                else:
                    raise TypeError
            except TypeError:
                print("*************************")
                print("Please enter letters only")
                print("*************************")
        self.course_l.append(course)
        print("********************")
        print("Data Entered Successfully...")
        
    #Function to display data in list    
    def Display_Data(self):       
        if not self.roll_no_l:   #checking if list is empty
            print("No Record Found...\nEnter some Data")
        else:
            print("**********************\n----Student Record----\n**********************")         
            for i in range(len(self.roll_no_l)):
                print(f"Roll_no: {self.roll_no_l[i]}\nName: {self.name_l[i]}\nSection: {self.section_l[i]}\nCourse: {self.course_l[i]}")    
                print("*************************")
            
    #Function to search data in list          
    def search_Data(self):  
        s_key = input("Enter the roll_No u want to search: ")
        check = False
        while check == False:      #exception
            try:
                s_key = int(s_key)   
                check = True
            except ValueError:
                print("**************************")
                print("Please enter numeric only ")
                print("**************************")
                s_key = input("Enter Again: ")
        print("********************")   
        if not self.roll_no_l:  #checking if list is empty
            print("No Record Found...")
        for i in range(len(self.roll_no_l)):   #checking user entered roll_no availible in record or not
            if s_key != self.roll_no_l[i]:
                print("Alert: Please enter Valid Roll_no")
        else:
            for i in range(len(self.roll_no_l)):
                if s_key == self.roll_no_l[i]:
                    print(f"1-\nRoll_no: {self.roll_no_l[i]}\nName: {self.name_l[i]}\nSection: {self.section_l[i]}\nCourse: {self.course_l[i]}")
                    print("********************")
    
    #Function to del data in list       
    def del_Data(self):           
        d_key = input("Enter the roll_No u want to Del: ")
        check = False
        while check == False:      #exception
            try:
                d_key = int(d_key)   
                check = True
            except ValueError:
                print("**************************")
                print("Please enter numeric only ")
                print("**************************")
                d_key = input("Enter Again: ")
        print("********************")
        if not self.roll_no_l:    #checking if list is empty
            print("No Recored Found")
        for i in range(len(self.roll_no_l)):   #checking user entered roll_no availible in record or not
            if d_key != self.roll_no_l[i]:
                print("Alert: Please enter Valid Roll_no")
        else:              
            for i in range(len(self.roll_no_l)):
                if (d_key == self.roll_no_l[i]):
                    del self.roll_no_l[i]
                    del self.name_l[i]
                    del self.section_l[i]
                    del self.course_l[i]
                    print("Record Deleted successfully")
    
    #Function to update data in list               
    def update_Data(self):        
        u_key = input("Enter the roll_No u want to Update: ")
        check = False
        while check == False:      #exception
            try:
                u_key = int(u_key)   
                check = True
            except ValueError:
                print("**************************")
                print("Please enter numeric only ")
                print("**************************")
                u_key = input("Enter Again: ")
        print("********************")
        if not self.roll_no_l:     #checking if list is empty
            print("No Recored Found")
        for i in range(len(self.roll_no_l)):    #checking user entered roll_no availible in record or not
            if u_key != self.roll_no_l[i]:
                print("Alert: Please enter Valid Roll_no")
        else: 
            check = False                    
            for i in range(len(self.roll_no_l)):
                if u_key == self.roll_no_l[i]:
                    self.temp_roll = input("Enter your roll_no: ")
                    while check == False:
                        try:
                            self.temp_roll = int(self.temp_roll)
                            check = True
                        except:
                            print("**************************")
                            print("Please enter numeric only ")
                            print("**************************")
                            self.temp_roll = input("Enter again: ")    
                    self.roll_no_l[i] = self.temp_roll
                    while True:
                        try:
                            self.temp_name = input("Enter your Name: ")
                            if self.temp_name.isalpha():
                                break
                            else:
                                raise TypeError
                        except TypeError:
                            print("*************************")
                            print("Please enter letter only ")
                            print("*************************")                    
                    self.name_l[i] = self.temp_name
                    while True:
                        try:
                            self.temp_sec = input("Enter your Section: ")
                            if self.temp_sec.isalpha():
                                break
                            else:
                                raise TypeError
                        except TypeError:
                            print("*************************")
                            print("Please enter letter only ")
                            print("*************************")
                    self.section_l[i] = self.temp_sec
                    while True:
                        try:
                            self.temp_course = input("Enter your Course: ")
                            if self.temp_course.isalpha():
                                break
                            else:
                                raise TypeError
                        except TypeError:
                            print("*************************")
                            print("Please enter letter only ")
                            print("*************************")
                    self.course_l[i] = self.temp_course
                    print("***************************")
                    print("Record Updated successfully")
                        
                        
                        
            
s = student(1001,"name","section","course")       #creating object for class student
   
while True:
    print("\t\t\t****************************\n\t\t\t----OPERATIONS U PERFORM----\n\t\t\t****************************")
    print("\t\t\t1-Add_Data\n\t\t\t2-Display_Data\n\t\t\t3-Search-Data\n\t\t\t4-Del_Data\n\t\t\t5-Update_Data\n\t\t\t6-Terminate\n")
    ch = input("Enter choice: ")
    print("********************")
    try:
        ch = int(ch)   
    except ValueError:
        print("Only <Int> input allowed")
       
    #calling All funtion   
    if ch == 1:
        s.add_Data() 
        print("********************")
   
    elif ch == 2:
        s.Display_Data()
        print("********************")
             
    elif ch == 3:
        s.search_Data()
        print("********************")
    
    elif ch == 4:
        s.del_Data()
        print("********************")
    
    elif ch == 5:
        s.update_Data()
        print("********************")
    
    elif ch == 6:
        break
    
    else:
        print("Please Enter Correct Choice")
        print("***************************")