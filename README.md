# Tasks-Manager-II

Bootcamp Project

● Modify the code of Tasks-Manager-I so that functions are used. Your program should include at least the following functions:

o reg_user - that is called when the user selects 'r' to register a user.
o add_task - that is called when the user selects 'a' to add a new task.
o view_all - that is called when the user selects 'va' to view all the tasks.
o view_mine - that is called when the user selects 'vm' to view the tasks that have been assigned to them.

● Modify the function called reg_user to make sure you don't duplicate usernames when you add a new user to the user.txt file.
  If a username already exists, display a relevant error message and allow the user to add a different username.
    
● Add the following functionality when the user selects 'vm':

o Display all tasks in a maner that is easy to read. Make sure that each task is displayed with a corresponding number which
  can be used to identify the task.
o Allow the user to select either a specific task (by entering the number) or input '-1' to return to the main menu.
o If the user selects a task, they should be able to choose to either mark the task as complete or edit the task. If mark as 
  complete is chosen, the value that describes whether the task has been completed or not, should be changed to 'Yes' in the 
  tasks.txt file. When the user chooses to edit the task, the username of the person to whom the task is assigned or the due 
  date of the task can be edited. The task can only be edited if it has not yet been completed.

● Add an option to generate reports to the main menu of the application. (gr - generate reports)

● When the user chooses to generate reports, two text files, called tasks_overview.txt and user_overview.txt, should  be generated.
  Both these text files should output data in a user-friendly, easy to read manner.
  
● tasks_overview.txt should contain:
  o The total number of tasks that have been generated and tracked using the task_manager.py.
  o The total number of completed tasks.
  o The total number of uncompleted tasks.
  o The total number of incomplete tasks that are overdue.
  o The percentage of incomplete tasks.
  o The percentage of tasks overdue.
  
● user_overview.txt should contain:
  o The total number of users registered.
  o The total number of tasks that have been generated and tracked.
  o For each user also describe:
  o The total number of tasks assigned to that user.
  o The percentage of the total number of tasks that have been assigned to that user.
  o The percentage of the tasks assigned to that user that have been completed.
  o The percentage of the tasks assigned to that user that still must be completed.
  o The percentage of the tasks assigned to that user that have not yet been completed and are overdue.
  
● Modify the menu option that allows the admin to display statistics so that the reports generated are read from tasks_overview.txt
  and user_overview.txt and displayed on the screen in a user-friendly manner. If these files don't exist (because the user hasn't
  selected to generate them yet), first call the code to generate the text files.
