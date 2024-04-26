# GitHub Practice

In this activity, you will create a new project in GitHub and practice commonly used Git commands.

Git is a great resource for managing your code and very convenient if you want to change computers. You'll become very familiar with git and GitHub over the course of this class.

## Instructions

1. Navigate to your GitHub page and create a new respository by clicking on the Repositories tab.

    ![Making a new repository](images/01.PNG)

2. Create a new project named `git-practice`. Add a short description to the project, such as "practicing with git." Then, initialize the repository with a README and create the repository.

    ![Creating a new respository](images/02.PNG)

3. Clone the repository by clicking the `Clone or download` button. Copy the link to your clipboard.

    ![Copying the clone url](images/03.PNG)

4. Navigate to the directory where you want to save your future coding drills––e.g., your desktop, root directory, or Documents folder. Open the command line in this folder, and run `git clone ` with the link you've copied. This will make a local copy of the repository.

    ![Cloning down a repository](images/04.PNG)

5. Check the current status of the repository by running the `git status` command, which should tell you that you're completely up to date.

    ![Checking the git status](images/05.PNG)

6. Create a new file named `test.md` and then check your `git status` again. Notice that git is now showing you have an untracked file.

    ![Adding a new file](images/06.PNG)

7. Use the  `git add .` command to add the contents of the current folder to be tracked by git. The period by itself references the current directory. Now git is waiting for those files to be committed.

    ![Tracking a new file](images/07.PNG)

8. Commit the changes to the repository along with a commit message using the `git commit -m "add test file"` command. This creates a new commit with the "add test file" commit message.

    ![Committing a new file](images/08.PNG)

9. Push the changes to GitHub to sync your machine with GitHub. Use the `git push origin main` command.

    ![Pushing up to GitHub](images/09.PNG)

10. If you made changes to the repository on another computer, you can pull down the changes you've committed with the `git pull origin main` command. But since you haven't made any changes yet, git will tell you that you're already up to date.

    ![Pulling down from Github](images/10.PNG)

11. If you want to work on your project on another computer or from a different location, you can clone the repository from GitHub as we did in Step 4.

    ![Cloning to another computer or location](images/11.PNG)

12. From the new location, you can make changes to the project and push those changes up to GitHub.

    ![Making changes in another location](images/12.PNG)

13. If you go back to your first directory, you can pull down the changes you made elsewhere. Navigate back to the directory you cloned in Step 4 and run `git pull origin main`.

    ![Pulling down changes from GitHub](images/13.PNG)

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
