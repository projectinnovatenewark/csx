# csx

1. Download Python -> https://www.python.org/downloads/
  a. IMPORTANT: Check off the "Add to Path" box when installing

2. Create a Github Account -> github.com
  a. Download Git -> https://git-scm.com/downloads
  
3. Download VS Code -> https://code.visualstudio.com/download
      VS Code Extensions to Download:
        Python
        
4. Create a foder named 'Programming'
  a. Inside 'Programming' - create a folder named 'python-work'
  
5. To open a terminal in VS Code:
        Use 'Shift + Ctrl + `'
        
6. Create a repository in Github -> https://help.github.com/en/enterprise/2.13/user/articles/creating-a-new-repository
      Then copy this set of commands into your terminal after creating repository:
          echo "# INSERT REPOSITORY NAME" >> README.md
          git init
          git add README.md
          git commit -m "first commit"
          git remote add origin REPOSITORY URL
          git push -u origin master
          
7. To check what your working directory is enter 'pwd' into your terminal

8. When you want to go up a level in your directory, enter 'cd ..' into your terminal
    ex: if you are in '/Users/christiantavares/Desktop/Programming/python-work'
        Enter in the Terminal: 'cd ..'
        your working directory will then be ''/Users/christiantavares/Desktop/Programming'

9. When you want to chamge your working directory, enter 'cd "directory name"'
        if you are in '/Users/christiantavares/Desktop/Programming'
        Enter in the Terminal: 'cd python-work' (If you begin to type the name of the desired directory,
                                                 you can hit the tab button and the directory should fill in)
        your working directory will then be ''/Users/christiantavares/Desktop/Programming/python-work'
        
10. The steps to commit code to Github are:
        'git add .'
        'git commit -m "commit message"
        'git push'
        
11. To pull code from the master branch of a repository:
        'git pull origin master'
        
12. Next you should copy and paste the todos (file ends in 'todo') into VS Code
 a. Go to -> https://github.com/projectinnovatenewark/csx/tree/master/lesons/marking_period_1
 b. Create a file in your 'python-work' folder in VS Code:
          right click on 'python-work' folder
          click 'new file'
          name the new file 'currentlesson.py' (.py tells VS Code that it is a pthon file)
 c. Copy the lesson in your new file and learn!
 
13. When you are finished with the lesson and complete the corresponding todo
          (todo's are meant to test what you learned from the lesson)
 a. repeat step 12.b but instead name the file 'currentlessontodo.py'
 b. try to complete the todo and then peer review


