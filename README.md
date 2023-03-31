# Welcome to the CSX After School Program!

### This semester we will be building a web application called "The Todo App". It will track personal tasks and
categorize them as either "Not Started", "In Progress", or "Completed". You can also assign due dates and different
categories (i.e. school, fun, family, etc.) to your todos. Since we prepared this course to accommodate all levels
of students, we will start assuming the student has no knowledge of programming. We will teach the basics of programming in Python, functions and classes, object oriented programming, followed by a bit of HTML/CSS and Javascript. Our final project will use Python, HTML/CSS, and Javascript. We look forward to embarking on this journey with you to learning programming and app development!

0. Here are some conventions we use in our documentation.

- Text wrapped in backticks `` (they are generally found in the top left of a keyboard along with the tilda "~")
should be directly copied and pasted. For example, `mkdir programming` as shown below would be directly copied and
pasted into your terminal window.

- Text wrapped in square brackets [] are meant to be replaced with text specific to the user. That text will be
described in the brackets. For example, if you wanted to change directories using the "cd" command, you could
enter the following `cd [directory name]`. If that directory was named "py-files", your command would look like
this- `cd py-files`. As you can see, the brackets are removed when you are inserting your own text.

- Text wrapped in double quotes is a reference to some text, or an action that should be taken by the user. These
are typically self-explanatory.

1. Download the latest version available for Python -> https://www.python.org/downloads/
        a. IMPORTANT: Check off the "Add to Path" box when installing
        b. If the installer does not pop-up, click on it in your downloads to begin the installation process

2. Create a Github Account -> github.com
        a. Download Git -> https://git-scm.com/downloads
        b. If the installer does not pop-up, click on it in your downloads to begin the installation process
        c. Leave all of the default installation steps and "Next" your way through the process.
  
3. Download VS Code -> https://code.visualstudio.com/download
        
4. Create a folder named "programming" in your computer's "Documents" directory.
  
5. Open a new window in VS Code. Click "Open Folder". Find your programming folder. Click it once then click "Open".
        a. To open a terminal in VS Code click "Shift + Ctrl + ~"
        b. If at any point in your terminal entries the beginning line of your terminal starts with ">>", ">>>", or is
           seemingly unable to enter your commands, click "Ctrl + C". That will quit any process running in your terminal.Sidebar- three arrows probably means you start a Python shell in your terminal! Another way to quit this type of process would be to type "quit()" and then enter.
        c. Enter the command `pwd` into your terminal then click enter. Your "working directory" should
           be in the "programming" folder, and the path response you get from the pwd command should end in "programming"
           (i.e. user/Documents/programming)
        d. Create a folder called "python-work" by entering the command `mkdir python-work`
        e. If you want to have these lessons stored locally on your computer and/or your mentor advises you to do so, type 
           `git clone https://github.com/projectinnovatenewark/csx.git` into your command terminal.
        f. Download the following VS Code extensions- Python and Highlight. You can find the extensions tab in VS
           Code by clicking "Shift + Ctrl + X" (windows) or "Shift + Command + X" (mac). Once there, search for those exact extensions and download the first result for each of them. Once you are done downloading those extensions, return back to the main "Explorer" page where you will be viewing your folders/files by clicking "Shift + Ctrl + E" (windows) or "Shift + Command + E" (mac). There are icons on the left panel of your VS Code to navigate through these different pages as well. You will see how these extensions are to be used at the bottom of this README
        
6. Create a repository in Github -> https://help.github.com/en/enterprise/2.13/user/articles/creating-a-new-repository
        Then after creating the repository, you should have some commands to choose from on the repository page. The top block of commands will look a bit like the following:

Copy the code block from the "...or create a new repository from the command line" section. You will paste it into your terminal momentarily - we will instruct you when to do that.

7. To check what your working directory is once again, enter `pwd` into your VS Code terminal.

8. When you want to go up a level in your directory, enter `cd ..` into your terminal
    ex: if you are in "/Users/username/Documents/programming/python-work"
        Enter in the Terminal: `cd ..`
        your working directory will then be "/Users/username/Documents/programming"

9. When you want to change your working directory, enter `cd [directory name]`
        For example, if you are in "/Users/username/Documents/programming"
        Enter in the Terminal: `cd python-work`
        TIP: If you begin to type the name of the desired directory, 
        you can hit the tab button to autocomplete, then the directory should fill in. If you
        are using Windows, clicking tab will be a requirement. That means, after typing in `cd python-work`, you will have to click tab on a Windows computer
        before clicking enter. Your working directory will then be "/Users/username/Documents/programming/python-work"
        
    Your working directory should now end in /python-work, which you can confirm using the `pwd` command. If that is the case, go ahead and paste in the block of commands from your Github repository page. Wait till all of the commands run, then click enter in your terminal. This connects your current working directory to the Github repository you just created.
        
10. The steps to commit code to Github are:
```
git add .
git commit -m "commit here"
git push
```
Run those commands one-by-one in order in your terminal. Following `git push` you might see an output in your terminal with instructions (i.e. "Run this command to do X", you should go ahead and follow those instructions. Some of these instructions have included commands to set your Github email or set the origin for different users. After, if everything worked, when you refresh your Github repository page you should have a file in the repository called README.md. Then, once you make new files in your "python-work" folder and want to put them on Github, you can simply run those 3 git commands to push up code to your repository.
   
11. If you are collaborating with someone else on a repository and you want to pull changes on to your computer, you would run this command. :
        `git pull origin master`

12. We will now include steps so that your files are formatted appropriately with the extensions you installed. Here are the different conventions we use

        a. Comment Blocks. Sections of code from a lesson are meant to be run in isolation. If a line in the file is completely composed of pound signs, it is a divider between sections. Each of these sections that are comment blocked should be ran one-by-one so you can observe their outputs and understand the content.

        b. Before reviewing the following, make sure that the Highlight extension by "Fabio Spampinato" is installed in your VS Code application as well as the "Python" extension by Microsoft. You should also have the VS Code "settings.json" file that comes with the csx repository copied and pasted into your own "settings.json" file. To access your own settings.json file click "Shift + Control (Command for Mac) + P" and type in "Open Settings (JSON)" and click on the option of the same name. That file should be scrapped and replaced entirely with the settings.json file that comes with the csx repository that is stored in the folder called ".vscode".

        c. ## FIXME's: callout questions and in-class demonstrations. FIXME's are meant to catch the teacher and students attention to do something. The FIXME will include items such as callout questions (questions to randomly choose a student from the class to solve), or in-class demonstrations (i.e. change a variable to show a different output). FIXME's will be highlighted red if you have the Highlight extension installed in your VS Code window.

        d. ## TODO's: working as a class. When you see a TODO in a lesson, it means that the class should pause the lesson and begin working on a problem. Nearly all TODO's in our lessons would lead to a question in the student_repository. There are often several TODO's per lesson and it is very important that you stop teaching and give the students time to solve each problem. After a reasonable amount of time (and drop-by support to students that need help), the teacher can then demo the solution on either the whiteboard or the projector with your computer connected. TODO's will be highlighted yellow if you have the Highlight extension installed in your VS Code window.

        e. ## TITLE: is what will be placed at the top of each section.

        f. ## HINT: is what will be used to give some tips or tricks to our students.

        g. ## TAKEAWAY: you will see this after an important lesson/todo to highlight what you should takeaway from it. These statements are crucial to summarize what you've learned.

        h. ## IMPORTANT: an important statement will be used to emphasize a section of the lesson. There will only be a handful of these throughout the curriculum- so make sure to read into these statements!
        
13. Next you should copy and paste the todos (file ends in "todo") into VS Code
        a. If you are accessing the repository through the browser -> https://github.com/projectinnovatenewark/csx/tree/master/lessons/students
           to see the lesson files separated by section.
                - Create a new file in your "python-work" folder in VS Code.
                        - right click on "python-work" folder
                        - click "new file"
                        - name the new file "currentlesson.ipynb" 
                                - the ".ipynb" extension tells your computer that it is a Jupyter notebook file running Python
                                - normal python files have just a ".py" extension
                        - replace the "currentlesson" with the name of the current lesson that you are on
                - Copy the first lesson from week one in your new file follow the instructions. 
                - To run your code, simply click on the green arrow at the top right of your VS Code window.
        b. If you are accessing the repository locally on your computer.
                - `cd` into your programming folder.
                - Enter the following command in your terminal `cp csx/lessons/students/[insert section]/[insert lesson folder]/[insertfile name] ./python-work` 
                - This should have copied the file in the first path into the location of the second path.
        