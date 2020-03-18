Here we will cover different commands that you can use when working with Github! Anything in square
brackets means you would substitute that with your own input.
 
git add . = stages changes in code to be committed
 
git commit -m "[commit message here]" = creates the commit that previous command staged
 
git push = pushes your commits to the remote repository/branch (sends it to github)
 
git clone = copies the repository to a specific folder on your computer; copy and paste the URL right after typing this command.
 
git pull = pulls down the changes from the remote repository into the branch you're in (you can use git pull to access lessons)
 
git pull origin master = fetches a copy of the master branch from the original repository, then merges it with your current branch. 
 
git remote -v = tells whether or not your folder is a repository
 
git checkout [name-of-branch] = switches you to another branch (make sure not to put spaces in your branch name!)
 
git checkout -b [name-of-branch] = creates a new branch based on the code you're on (make sure not to put spaces in your branch name!)
 
git fetch = retrieves changes from Github for your computer to recognize.
 
git merge = merges specified branch with branch you're currently in.
 
git stash = temporarily saves any changes you make in your repository, and allows you to re-apply those changes later.

Pushing up assignments to your own repository:

Run the following commands in order-
    git add .
    git commit -m "completed ______ assignment"
    git push
