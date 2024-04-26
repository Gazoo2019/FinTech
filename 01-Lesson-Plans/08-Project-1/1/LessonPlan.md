## 8.1 Lesson Plan—Projects & Collaboration with Git

#### Overview

This week, students will begin work on their first project of the boot camp: Use Python to deliver an in-depth analysis of a financial data source of their choosing.

#### Instructor Notes

The instructional staff should work together prior to class to identify the groups for this project. It often works best to pair students with similar skill levels, so everyone can contribute equally to the project.

It is highly recommended that students submit their project proposals ahead of time, especially as some may struggle to find data sources and set realistic goals. Use this as an opportunity to guide them to unique, interesting, and achievable projects.

Install the appropriate extension to your text editer to help visualize Git histories, for example: [Git History](https://github.com/DonJayamanne/gitHistoryVSCode) in VS Code or [git-time-machine](https://atom.io/packages/git-time-machine) for Atom.

Be sure to slack out the [Git Branching Workflow](http://nvie.com/posts/a-successful-git-branching-model/) before the end of class.

Slack out the [Visual Introduction to Git](https://medium.com/@ashk3l/a-visual-introduction-to-git-9fdca5d3b43a).

* If possible, share the above links both _before_ today's class, and again at the end of it.

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1f2z6AY8QHB0QsHsDLHfcV3tYse4hU1B-K8cKPE4LG9E/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/presentation/d/1UEkj7rFjMwpNr4eVXyArTdaq3FbhPabwJRRpxlPriZw/edit#slide=id.g473a132ac1_0_7).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The Time Tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### Class Objectives

Students must be able to:
* Articulate the requirements for Project 1.
* Draw and interpret diagrams of Git branching workflows.
* Create new branches with Git.
* Push local branches to GitHub.

---

### 1. Instructor Do: Welcome Students (5 min)

Greet the class, and welcome everyone to the first day of Project 1!

Congratulate students on having made it this far, and explain that over the next two class weeks, students will work in groups to complete a FinTech Python Project.

Point out that this provides students an opportunity to practice both programming and collaborative workflows.

Using the slides, review today's class objectives, then provide a high-level overview of what project week looks like. 

Explain that the first half of today's class will focus on using Git for collaboration, while the second half will give students the opportunity to start thinking about projects with their groups.

At this point, break students into their project groups then move on to the next activity.

### 2. Student Do: Create a Repository (10 min)

In this activity, each project group will create a project repo and invite all group members as collaborators.

**File:** [README.md](01-Lesson-Plans/08-Project-1/1/Activities/01-Stu_Create-Repository/README.md)

Slack out the [README.md](01-Lesson-Plans/08-Project-1/1/Activities/01-Stu_Create-Repository/README.md) file to the class and have students complete this activity with their groups. This will be the first time most students have created a collaborative repo, so instructional staff should check-in with groups often to offer assistance. 

### 3. Instructor Do: Pull Requests and Code Review (5 min)

Explain that when working with others on the same repo, it's important to make sure that all of the new code gets reviewed by at least one other team member before getting merged into the main branch.

Assure the class that we'll go into further detail about how this is done, but ask the class: "Why would we want to get code reviewed before merging it into the main?"

> Reviewing new code decreases the chances that broken code will accidentally be introduced into the main branch.

> Code review helps group members who didn't write the code understand how it works.

Explain that the next step of setting up our project repos for group collaboration is to protect the main branch.

* Protecting the main branch means we will configure the repo to prohibit any team members from pushing code up into the main directly, or merging it in without another team member's review.

### 4. Student Do: Protect Main Branch (5 min)

In this activity, groups will protect their main branches.

**File:** [README.md](01-Lesson-Plans/08-Project-1/1/Activities/02-Stu_Protect-Main/README.md)

Slack out the [README.md](01-Lesson-Plans/08-Project-1/1/Activities/02-Stu_Protect-Main/README.md) file to the class and have students complete this activity with their groups. 

### 5. Instructor Do: Branching (10 min)

Note: For now, we just want to give students a high-level conceptual understanding of branching.

Continuing with the slides, explain the following points about branching:

* Every Git repo starts off with a main branch, which is there to hold the production version of the repo's code. But when we want to work on the code, we start by creating a new feature branch off the main.

* If we create a new branch from the main, we essentially create a self-contained copy of all of the main branch's code for us to work in.

* When we're satisfied with our work in the new feature branch, we submit a pull request from the feature branch to the main branch.

* A pull request is a request to merge the **diffs** or changes from the source branch (the feature branch) to the target branch (main).

* With the way our repos are set up now, another group member must look at and approve the pull request before its changes can be merged into the main.

* Once a feature branch has been merged into the main, we delete it and then check back out to the main branch. From there, we'd check back out to a new feature branch, and repeat the process for each feature we add.

Slack out the following image for students to have as a visual aid:

  ![Git Branching](Images/01-Git-Branching.png)

Take a moment to answer any questions, but avoid going too in depth. Students will utilize branches in the next activity.

### 6. Student Do: Git Branching, Pushing (15 min)

In this activity, students will create branches, submit pull requests, and perform code reviews before merging.

**File:** [README.md](01-Lesson-Plans/08-Project-1/1/Activities/0--Stu_Branching-Pushing/README.md)

Slack out the [README.md](01-Lesson-Plans/08-Project-1/1/Activities/0--Stu_Branching-Pushing/README.md) file to the class and have students complete this activity with their groups. 

Instructional staff should be walking around the class making themselves available for assistance, and ensuring students understand the instructions.

### 7. Instructor Do: Introduce Projects (10 min)

Point out that students will need a project to work on if they're to be able to practice Git.

Utilize the slideshow to explain the requirements for Project 1.

* Be sure to slack out the Project's [Technical Requirements](../../../03-Projects/Project-01/TechnicalRequirements.md); the [Project Guidelines](../../../03-Projects/Project-01/ProjectGuidelines.md); the [Presentation Requirements](../../../03-Projects/Project-01/PresentationRequirements.md); the [Presentation Guidelines](../../../03-Projects/Project-01/PresentationGuidelines.md) after going through the slides.

Take a moment to address any remaining questions before dismissing the class for break.

---

### 8. BREAK (15 min)

---

### 9. Student Do: Project Work (1 hr, 45 min)

Students should spend the remainder of class working with their groups to develop a project proposal.

Walk around and offer advice on project scope, finding data sources, and potential questions that could be interesting and feasible for students to investigate.

---

### End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
