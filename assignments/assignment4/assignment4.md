# Assignment 4 - Collaborative GitHub Project - Creating Team PRs

## Deadline:

Feb 28th 2024, 4:00 PM

## Objective:

Enhance version control skills and teamwork by collaborating with assigned teammates to set up GitHub repositories, create folders, submit pull requests, and establish upstream repositories for P1 and P2.

## Instructions:

### 1. Team Pairings:

- Instructors have assigned pairs for all students, resulting in 15 teams for this assignment.
- Each team member is designated as either `P1` or `P2`.

### 2. GitHub Repository Setup:

- Work within the `DS219/spark-seprep/assignments/assignment4` directory structure on GitHub.
- Most students have cloned the class repository in their `$HOME` directory, so the following or something close to it should
  bring most students to the root of the class repository:

  ```bash
  cd ~/github/spark-seprep
  ```

### 3. Update your local main branch (both P1 and P2):

- Ensure your local main branch is in sync with upstream/main before starting any new work.
- The following assumes you are currently working within the locally cloned spark-seprep repository.
  
```bash
git checkout main
git fetch --all
git rebase upstream/main
git push origin main
```

### 4. Set up working branches (Both P1 and P2):

- The following assumes you are currently working within the locally cloned spark-seprep repository.
- **Both** P1 and P2 create a new branch named `assignment4`

  ```
  git checkout -b assignment4
  git push origin assignment4
  ```

### 5. P1 initiate PR to P2's fork:

- P1 will create a folder with their team name in `assignments/assignment4` directory. Name the directory with your team number.
  For example, P1 from Team3 should run the following:
  
  ```bash
  mkdir assignments/assignment4/Team3  <-Replace "3" with your team number!
  ```
  
- With the folder structure in place, P1 will add a new document to the team folder named `<Their Name>.md`.
  For instance, if P1 is Alice, the document should be named `Alice.md`. **This file should be inside the team directory**
- After creating the document, P1 will submit a pull request to P2's fork against P2's assignment4 branch.
  For example, P1 from Team3 will do the following to push their new file to their fork:
  
  ```
  git add assignments/assignment4/Team3
  git commit -m "adding new file here"
  git push origin assignment4
  ```
-  P1, after pushing the assignment4 branch to GitHub, and from the GitHub UI, choose P2's **assignment4** branch to contribute a PR against.
  
### 6. P2 reviews and merges P1's PR on their fork:

- P2 should check if P1 has correctly created the folder with the suggested nomenclature.
- **P2, Make sure P1 submitted the PR against the assignment4 branch, not your main branch!** If necessary, P2 can close the PR and tell P1 to
  open a new PR against the correct branch.
- Once everything looks good, P2 will merge the PR that P1 submitted against the `assignment4` branch.

### 7. P2 initiates Pull Request (PR) to P1's Fork:

- The following assumes you are currently working within the locally cloned spark-seprep repository.
- First, P2 must fetch and rebase locally (from the terminal) to pick up the changes that were merged in GitHub.
  P2 do the following:
  
  ```
  git branch <-confirm that you are still in assignment4 branch, if not, then run 'git checkout assignment4'
  git fetch --all
  git rebase origin/assignment4
  ```
  
  Now, P2, your local copy of your assignment4 branch matches the branch you have just merged P1s work into in GitHub.

- P2 will add a new document to the team folder named `assignments/assignment4/TeamX`. For example, if P2's name is Bob, the document should be `Bob.md`.
  **This file should be inside the team directory.**
- After creating the document, P2 will submit a pull request to P1's fork on their assignment4 branch.
  First, P2 will do the following to push their new file to their fork.
  For example, Bob, from P2 Team3, would do the following:
  
  ```
  git add assignments/assignment4/Team3/Bob.md
  git commit -m "adding new file here"
  git push origin assignment4
  ```
  
-  P2, after pushing the assignment4 branch to GitHub, and from the GitHub UI, choose P1's **assignment4** branch to contribute a PR against.
- **P1, make sure P2 submitted the PR against your assignment4 branch, not your main branch!** If necessary, P1 can close the PR and tell P2 to
  open a new PR against the correct branch.
-  P1 should review P2's pull request and merge it into their assignment4 branch in GitHub.

### 9. Final PR to Main Upstream:

- To complete the process, P1 will submit a pull request to the main upstream repository (`DS219/spark-seprep`) containing the changes 
  made by both teammates. From the GitHub UI, open a PR and choose the DS219/main branch to contribute to, from your `assignment4` branch, that contains both
  your commit as well as P2's commit.

## Important Notes:

- Maintain clear and descriptive commit messages.
- Communicate effectively with your teammate to coordinate the process.
- Review each other's work thoroughly during the pull request phase.
- If you encounter any issues or have questions, seek assistance from your instructor.

## Submission:

- This assignment involves a series of pull requests within the GitHub repository.
- Ensure that all steps are completed, including setting up upstream repositories for P1 and P2, and that the final pull request to the main upstream repository is made.

This assignment not only helps you practice GitHub collaboration but also emphasizes effective communication and teamwork. If you have any questions or need clarification on any step, please reach out to on piazza. Good luck, and happy collaborating!
