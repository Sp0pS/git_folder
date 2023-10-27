## Chapter 4: Two New Different Features

In this chapter, we'll work on two different features for our Python program. Each feature will be developed in a separate Git branch.

We'll create the "feature/cheer-user-name" branch, where the program greets the user by name, and the "feature/question" branch, where the program asks the users how they are doing. 

Finally, we'll merge these branches into the master branch.

### 4.1 Feature: Cheer User Name

#### 4.1.1 Create and Switch to the Branch

1. In your terminal, navigate to the repository directory.

2. Create a new branch named "feature/cheer-user-name".

#### 4.1.2 Modify Python Program

1. Open `hello_world.py` in a text editor.

2. Add the following code to greet the user by name:
   ```python
   # hello_world.py
   user_name = input("Enter your name: ")
   print("Hello, " + user_name + "!")
   ```

#### 4.1.3 Commit and Push Changes

1. Stage the changes.

2. Commit the changes.

3. Push the changes to the remote repository. In the previous exericse, the working branch was never pushed to the remote repo. Hence, it remained local all along its lifecycle. Try with the following command, and edit it accordingly its output to make it work.
   ```bash
   git push
   ```

### 4.2 Feature: Ask a Question

#### 4.2.1 Create and Switch to the Branch

1. In your terminal, navigate to the repository directory.

2. Create a new branch named "feature/question" branched from **master**.

#### 4.2.2 Modify Python Program

1. Open `hello_world.py` in a text editor.

2. Add the following code to ask the user how they are doing:
   ```python
   # hello_world.py
   print("Hello, World!")
   print("How are you doing?")
   ```

#### 4.2.3 Commit and Push Changes

1. Stage the changes.

2. Commit the changes.

3. Push the changes to the remote repository.

### 4.3 Merge Branches into Master

#### 4.3.1 Merge "feature/cheer-user-name" into Master

1. Switch to the master branch.

2. Merge the "feature/cheer-user-name" branch into master.

#### 4.3.2 Merge "feature/question" into Master

1. Merge the "feature/question" branch into master.

2. If everything is ok, we should notice that the automatic merge has failed, since we have conflicts. We have now to proceed with a manual merge. But why do we have conflicts?

3. Think well on how apply modifications: which parts do we keep, and which do we discard?. After finishing the edit, our modification are not committed. Proceed now with the commit and remember to add a useful commit message.

4. Update the remote repo with the latest modifications.

Now, your master branch includes both features!

Take some minutes to analyze the branch graph. Do we still see all three branches? Are the branches still there, or were they deleted (locally and remotely)? Where is the first merge?