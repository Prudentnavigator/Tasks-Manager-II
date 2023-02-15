# Lesson SE-T21
# Task CapstoneProject III - Lists, Functions and String Handling


# task_manager.py--a program for a small business that manages tasks
#                  assigned to each member of a team.


#=====importing libraries=====

import datetime

import os.path

#=====Define Functions=====

# Login function for users.
def user_login():

    while True:
        user_name = input("\t\t\tPlease enter your username: ")
        user_passwd = input("\t\t\tPlease enter your password: ")
    
        # Open user.txt file and until username and password entered match one of the
        #   username  and corresponding password in the file, keep requesting to login.
        #   Once there is match, quit loop.
    
        with open('user.txt', 'r') as user_data:
            u_name = ""
            passwd = ""
            for line in user_data:
                user_credentials = line.split(",")
                for name in user_credentials[ :1]:
                    if user_name == name:
                        u_name = name 
                        for passw in user_credentials[1: ]:
                            passwd = passw.strip()
        
        if user_name == u_name and user_passwd == passwd:
            return u_name             
            break


# A function to register a user
def reg_user() :
    
    # Check if user has permission to add a new user and request new user data.
    if user_name == "admin" :
        new_user = input("\n\t\t\tPlease enter a username for the new user: ")
        name = new_user

        # If username for a new user already exists, keep prompting for a different 
        #   username until there's no match.
        while new_user == name :
            with open('user.txt', 'r') as user_data:
                for line in user_data:
                    user_credentials = line.split(",")
                    for name in user_credentials[ :1]:
                        if new_user == name:
                            print("\n\t\t\t*** User name already exists! ***\n")
                            new_user = input("\t\t\tPlease enter a different username: ")
                        else :
                            break

        # Confirm password
        while True:
            new_passwd = input("\n\t\t\tPlease enter a password: ")
            repeat_passwd = input("\n\t\t\tConfirm password: ")
        
            # Check if the provided password matches the confirmed password
            if new_passwd == repeat_passwd:
                passwd = new_passwd
    
                # If passwords match, append data of the added user to the user.txt file.
                with open("user.txt", "a") as user_data: 
                    user_data.write( new_user + ", " + passwd + "\n")
                    break
    
            # If passwords do not match, print an error message and request 
            #   the user to enter the passwords again.
            else:
                print("\n\t\t\t***Passwords do not match!***\n")

    else:
            print("\n\t\t\t***Must be an administrative user in order to add new users!***\n")


# A function to add a task 
def add_task() :

    # Get todays date from the datetime module and convert to 
    #   desired date format.
    from datetime import datetime
    date_today = datetime.today()
    current_date = date_today.strftime("%d %b %Y")
    
    # Display available users to assign a task.
    with open('user.txt', 'r') as user_data:
        members = []
        for line in user_data:
            user_credentials = line.split(",")
            members += [ name for name in user_credentials[ :1] ]
        print("\n\t\t\t*** Available users:", *members, " ***")
    
    # Request the user to enter data of the new task.
    while True:
        assign_user = input("\n\t\t\tPlease enter the user you wish to assign the task to: ")
        if assign_user in members:
            break
        else:
            print("\n\t\t\t*** No user with that username! ***")

    task = input("\t\t\tPlease enter the title of the task: ")
    description = input("\t\t\tEnter a description of the task: ")
    due_date = input("\t\t\tWhen is the task due (i.e. 20 Mar 2024): ")
    assign_date = current_date
    completion = "No"

    # Append data to tasks.txt file.
    with open("tasks.txt", "a") as user_tasks:
        first_part = (f"{assign_user}, {task}, {description},") 
        second_part= (f" {assign_date}, {due_date}, {completion}" ) 
        user_tasks.write( first_part + second_part + "\n")


# A function to view all tasks
def view_all() :

    with open('tasks.txt', 'r') as user_tasks:
        for line in user_tasks:
            line = line.split(",")
            for value in line[1:2]:
                task = value 
            for name in line[:1]:
                user = name 
            for date in line[3:4]:
                assign_date = date 
            for due in line[4:5]:
                due_date = due 
            for status in line[5:6]:
                completion = status
            for value in line[2:3]:
                description = value

            print(f"""

            _______________________________________________________________


                    Task:                           {task}
                    Assigned to:                     {user}
                    Assign date:                    {assign_date}
                    Due date:                       {due_date}
                    Task Complete?                  {completion}
                    Task description:   
                     {description[0:50]}
                      {description[50:100]}
                       {description[100:150]}
            _______________________________________________________________

            """)


# A function to view the logged in user's tasks
def view_mine() :

    with open("tasks.txt", "r") as user_tasks:
        count = 0
        task = []
        assign_date = []
        due_date = []
        completion = []
        description = []

        for line in user_tasks:
            line = line.split(",")
            for name in line[:1]:
                if user_name == name: 
                    user = user_name 
                    count += 1
                    for value in line[1:2]:
                        task += [value] 
                    for date in line[3:4]:
                        assign_date += [date]
                    for due in line[4:5]:
                        due_date += [due] 
                    for status in line[5:6]:
                        completion += [status]
                    for value in line[2:3]:
                        description += [value]
                        task_des = description[count-1]

                    print(f"""

            _______________________________________________________________


                    Task:                           {task[count -1]}
                    Assigned to:                     {user}
                    Assign date:                    {assign_date[count -1]}
                    Due date:                       {due_date[count -1]}
                    Task Complete?                  {completion[count -1]}
                Task description:   
                    {task_des[0:50]}
                     {task_des[50:100]}
                     {task_des[100:150]}
            _______________________________________________________________

            """)

        print("\n\t    _______________________________________________________________")        
        print(f"""

                            Tasks editing menu (for {user}):
                                                                                   """)

        for i, j in enumerate(task, 1):
            
            print(f"""                        {i} {j}
                           due date:{due_date[i-1]}      complete:{completion[i-1]}""")

        print("\t\t       -1  exit menu")
        
        print("\n\t    _______________________________________________________________")        


        # Ask the user to make a selection.
        choice = "" 

        while choice != "-1" :
            status = ""
            while True:
                choice = input("""
                        Please enter the number of the task you'd like
                        to edit or -1 to exit: """)

                if choice.isnumeric() and int(choice) <= i:
                    break
                elif choice == "-1" :
                    break
                            
            if choice == "-1" :
                break

            # If a task is complete display message
            with open("tasks.txt", "r") as in_file:
                choice = int(choice) 
                for line in in_file:
                    if task[choice-1] in line:
                        if user in line:
                            if "Yes\n" in line:
                                print("\n\t\t\tTask has been completed and can't be edited anymore!")
                                status = "no" 

            # Mark task as complete
            if status != "no":
                mark = input("\n\t\t\tWould you like to mark the task as completed (y/n): ")
    
                if mark.lower() == "y":
                    choice = int(choice) 
    
                    with open("tasks.txt", "r+") as in_file:
                        for line in in_file:
                            if task[choice-1] in line:
                                if " No\n" in line:
                                    in_file.write(line.replace(" No\n", " Yes\n"))
    
                    with open("tasks.txt", "r") as in_file:
                        with open("tmp.txt", "w") as out_temp:
                            for line in in_file:
                                out_temp.write(line)
    
                    with open("tasks.txt", "w") as out_file:
                        with open("tmp.txt", "r") as in_temp:
                            for line in in_temp:
                                if task[choice-1] not in line:
                                    out_file.write(line)
    
                                if task[choice-1] in line:
                                    if " Yes\n" in line:
                                        out_file.write(line)                 
                else:

                    # Re-assign task to another user
                    edit_uName = input("\n\t\t\tWould you like to edit the user name of the task (y/n):")
    
                    if edit_uName.lower() == "y":

                        # Display available users to re-assign task.
                        with open('user.txt', 'r') as user_data:
                            members = []
                            for line in user_data:
                                user_credentials = line.split(",")
                                members += [ name for name in user_credentials[ :1] ]
                            print("\n\t\t\t*** Available users:", *members, " ***")

                        # Keep asking for a username until there is match in the members list.
                        while True:
                            new_user = input("\n\t\t\tTo which user would you like reassign the task to: ")
                            if new_user in members:
                                break
                            else:
                                print("\n\t\t\t*** Username does not exist! ***")

                        choice = int(choice) 
    
                        with open("tasks.txt", "r+") as in_file:
                            for line in in_file:
                                if task[choice-1] in line:
                                    if user  in line:
                                        in_file.write(line.replace(user , new_user))
        
                        with open("tasks.txt", "r") as in_file:
                            with open("tmp.txt", "w") as out_temp:
                                for line in in_file:
                                    out_temp.write(line)
        
                        with open("tasks.txt", "w") as out_file:
                            with open("tmp.txt", "r") as in_temp:
                                for line in in_temp:
                                    if task[choice-1] not in line:
                                        out_file.write(line)
        
                                    if task[choice-1] in line:
                                        if new_user in line:
                                            out_file.write(line)                 
    
                    # Edit due date
                    edit_dueDate = input("\n\t\t\tWould you like to edit the due date of the task (y/n):")
    
                    if edit_dueDate.lower() == "y":
                        new_dueDate = input("\n\t\t\tPlease enter the new due date (i.e. 10 Jan 2028): ")
                        choice = int(choice) 
    
                        with open("tasks.txt", "r+") as in_file:
                            for line in in_file:
                                if task[choice-1] in line:
                                    if due_date[choice-1] in line:
                                        in_file.write(line.replace(due_date[choice-1] , " " + new_dueDate))
    
                        with open("tasks.txt", "r") as in_file:
                            with open("tmp.txt", "w") as out_temp:
                                for line in in_file:
                                    out_temp.write(line)
        
                        with open("tasks.txt", "w") as out_file:
                            with open("tmp.txt", "r") as in_temp:
                                for line in in_temp:
                                    if task[choice-1] in line:
                                        if new_dueDate in line:
                                            out_file.write(line) 
                                    if task[choice-1] not in line:
                                        out_file.write(line)


# A function that writes a report to two external files.
def write_report():
 
    # total number of tasks
    with open("tasks.txt", "r") as in_file:
        task_count = 0
        for task in in_file:
            task_count += 1 

    # total number of complete tasks
    with open("tasks.txt", "r") as in_file:
        comp_tasks = 0
        for task in in_file:
            if " Yes\n" in task:
                comp_tasks += 1 

    # total number of incomplete tasks
    incom_tasks = task_count - comp_tasks

    # total number of overdue tasks
    with open("tasks.txt", "r") as in_file:
        from datetime import datetime
        date_today = datetime.today()
        over_dueTasks = 0
        for line in in_file:
            line = line.split(",")
            if " No\n" in line:
                for due in line[4:5]:
                    due_now = datetime.strptime(due, " %d %b %Y") 
                    if due_now < date_today:
                        over_dueTasks += 1

    # The percentage of incomplete tasks
    calculate = ( incom_tasks / task_count ) * 100
    per_incomTasks = round(calculate)

    # The percentage of overdue tasks
    calculate = ( over_dueTasks / task_count ) * 100
    per_overdueTasks = round(calculate)

    # Write report to task_overview.txt
    with open("task_overview.txt", "w") as out_file:
        part1 = (f"{task_count}, {comp_tasks}, {incom_tasks},")
        part2 = (f" {over_dueTasks}, {per_incomTasks}%, {per_overdueTasks}%")
        out_file.write(part1 + part2) 

    print("\n\n\t\t\t\t*** A Report has been Generated! ***\n")

    # Total number of tasks assigned to each user
    with open('user.txt', 'r') as user_data:
        users = []
        for line in user_data:
            user_credentials = line.split(",")
            users += [ name for name in user_credentials[ :1] ]

    with open("tasks.txt", "r") as user_tasks:
        user_count = {}
        for name in users:
            user_count[name] = 0
        for task in user_tasks:
            for name in users:
                if name in task:
                    user_count[name] = user_count[name] + 1 

    # The number of completed tasks of each user
    with open("tasks.txt", "r") as in_file:
        user_compTasks = {} 
        for name in users:
            user_compTasks[name] = 0
        for task in in_file:
            for name in users:
                if name in task:
                    if " Yes\n" in task:
                        user_compTasks[name] = user_compTasks[name] + 1 

    # The percentage of incomplete and overdue tasks of each user
    with open("tasks.txt", "r") as in_file:
        over_dueTask = {}
        for name in users:
            over_dueTask[name] = 0
        for line in in_file:
            line = line.split(",")
            for name in users:
                if name in line:
                    if " No\n" in line:
                        for due in line[4:5]:
                            due_now = datetime.strptime(due, " %d %b %Y") 
                            if due_now < date_today:
                                over_dueTask[name] = over_dueTask[name] + 1

    # Create text file
    with open("user_overview.txt", "w") as new_outFile:
        pass

    for user in users:
        if user_count[user] != 0:

            # The percentage of the total tasks assigned to each user
            calculation = (user_compTasks[user] / user_count[user]) * 100 
            comp_per = round(calculation)
        else:
            comp_per = 0
        
        if task_count != 0:
            calculation = (user_count[user] / task_count) * 100 
            of_allTasks = round(calculation)
        else:
            of_allTasks = 0

        # The percentage of incomplete task of each user
        incomp_per = 100 - comp_per

        if user_count[user] == 0:
            incomp_per = 0

        # The percentage of over-due task of each user
        if user_count[user] != 0:
            calculation = (over_dueTask[user] / user_count[user]) * 100
            per_overdue = round(calculation)
        else:
            per_overdue = 0

        # Write results to text file
        with open("user_overview.txt", "a+") as out_file:
            part1 = (f"{user}, {user_count[user]}, {of_allTasks}%, {comp_per}%,")
            part2 = (f" {incomp_per}%, {per_overdue}%\n")
            out_file.write(part1 + part2) 
 

#====Login Section====

print()

# Call login function
if os.path.exists("user.txt"):
    user_name = user_login()
else:
    print("\n\t\t\t*** Input file 'user.txt' does not exist! ***\n")
    exit()
if os.path.exists("tasks.txt"):
    pass
else:
    print("\n\t\t\t*** Input file 'tasks.txt' does not exist! ***\n")
    exit()


#====Menu Section====


# Presenting the menu to the user and  making sure that
#   the user input is converted to lower case.
while True:

    if user_name == "admin":
        menu = input('''
                            
                                    Admin-menu

                        Select one of the following Options below:
                
                        r - Registering a user
                        a - Adding a task
                        va - View all tasks
                        vm - View my tasks
                        gr - Generate reports
                        ds - Display statistics
                        e - Exit
                        :  ''').lower()

    else:
        menu = input('''
                        Select one of the following Options below:
                
                        r - Registering a user
                        a - Adding a task
                        va - View all tasks
                        vm - View my tasks
                        e - Exit
                        :  ''').lower()



    #====Compute Selected====
    
    # Add a new user to the user.txt file with the reg_user function.
    if menu == 'r':
        reg_user()
        
    
    # Add a new task to tasks.txt file with the add_task function.
    elif menu == 'a':
        add_task()
    
    
    # Read the tasks from tasks.txt file and print *all tasks* to the console.  
    elif menu == 'va':
        view_all()
    
    
    # Read the tasks from tasks.txt file and print the *users tasks* (if assigned)     
    #   to the console and provides the user options to edit tasks.
    elif menu == 'vm':

        with open("tasks.txt", "r") as user_tasks:
            name_list = []
            for line in user_tasks:
                line = line.split(",")
                for name in line[:1]:
                    name_list.append(name)

            if not user_name in name_list:
                print("\n\t\t\t*** No Tasks assigned for", user_name, "***")
            else:
                view_mine()


    # Generate reports with the write_report function.
    elif menu == "gr":
        if user_name == "admin":
            write_report()
               

    # Compute and display user and tasks statistics.
    # This option is only available for admin users.
    elif menu == "ds":
        if user_name == "admin":
    
            # Verify that the text files exist, if not call write_report function to write the files.
            if not os.path.exists("task_overview.txt") and not os.path.exists("user_overview.txt"):
                write_report()

            # Read from the task report file.
            with open("task_overview.txt", "r") as task_report:
                for values in task_report:
                    value = values.split(",")
                    task_count = value[0:1] 
                    comp_tasks = value[1:2]
                    incom_tasks = value[2:3]
                    over_dueTasks = value[3:4]
                    per_incomTasks = value[4:5]
                    per_overdueTasks = value[5:6]

            # Display report
            print(f"""
    
    
                _______________________________________________________________
    
    
                        *** Task Manager Tasks Overview Report ***
    
    
                        Total Tasks:                        {task_count[0]}             
                        Completed Tasks:                    {comp_tasks[0]}
                        Incomplete Tasks:                   {incom_tasks[0]} 
                        Over-due Tasks:                     {over_dueTasks[0]}
                        Incomplete in %:                   {per_incomTasks[0]}
                        Over-due in %:                      {per_overdueTasks[0]}

                _______________________________________________________________
    
            """)

            # Read user report file
            with open("user_overview.txt", "r") as user_report:
                for values in user_report:
                    value = values.split(",")
                    user = value[0:1]
                    user_count = value[1:2] 
                    of_allTasks = value[2:3]
                    comp_per = value[3:4]
                    incomp_per = value[4:5]
                    per_overdue = value[5:6]

                    # Display report
                    print(f"""
    
    
                _______________________________________________________________
    
    
                        *** Task Manager User Report of {user[0]} ***
    
    
                        Total Tasks assigned:                {user_count[0]}             
                        Tasks of all Tasks in %:            {of_allTasks[0]}
                        Complete in %:                      {comp_per[0]}
                        Incomplete in %:                    {incomp_per[0]}    
                        Over-due Tasks in %:                 {per_overdue[0]}
                                       

                _______________________________________________________________
    
            """)

                
    # Option to exit the program
    elif menu == 'e':

        # Remove temp file.
        if os.path.exists("tmp.txt"):
            os.remove("tmp.txt")

        print('\n\t\t\tGoodbye!!!\n')
        exit()
    
    # When selected is not in the menu, display an error message.
    else:
        print("\n\t\t\t***You have made a wrong choice, Please Try again***\n")


