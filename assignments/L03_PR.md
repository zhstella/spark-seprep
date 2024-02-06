# Assignment 3

**Objective:**

This assignment aims to enhance your version control skills by guiding you through setting up GitHub repositories, creating folders, submitting pull requests, and establishing an upstream repository.

**Instructions:**

**1. GitHub Repository Setup:**

   - Work within the `DS219/spark-seprep/assignments/assignment3` directory structure on GitHub.

**3. Forking the Main Repository:**

   - Create a fork of the `DS219/spark-seprep` repository.

**4. Cloning your Fork:**

   - Clone your fork of the `DS219/spark-seprep` repository.

   ```bash
   mkdir -p ~/github
   cd ~/github/spark-seprep
   git clone git@github.com:yourgh-name/spark-seprep.git  # if your SSH key is set correctly in GH
   git clone https://github.com/yourgh-name/spark-seprep.git # if your SSH key is not set correctly in GH
   cd spark-seprep
   git remote show -v
   git remote add upstream git@github.com:DS219/spark-seprep.git  # if your SSH key is set correctly in GH
   git remote add upstream  https://github.com/DS219/spark-seprep.git # if your SSH key is not set correctly in GH
   ```

**5. Update your local main branch**

   - Ensure your main branch is in sync with upstream/main, both locally and on GitHub.
   - This step is crucial before starting any new work.

   ```bash
   git fetch --all
   git rebase upstream/main
   git push origin main
   ```

**File Creation:**

   - Create a markdown file in the `student-introduction/` folder with the following nomenclature: `yourname.md`. Take a look at the [example here.](https://github.com/DS219/spark-seprep/blob/main/student-introduction/aakanksha.md) 
   - Add a header using `#` and add your name.
   - Then in normal text add your introduction with your favorite programming language and why. 

   ```bash
   git checkout -b assignment-3-branch
   cd student-introduction/
   touch yourname.md
   # Open the document, add content, and save.

   git add .
   git commit -m "[your name]: Assignment 3"
   git push origin assignment-3-branch
   ```

**9. Final PR to Main Upstream:**

   - Submit a pull request to the main upstream repository (`DS219/spark-seprep`) containing the changes to `student-introduction/yourname.md`.

**Important Notes:**

- Maintain clear and descriptive commit messages.
- Communicate effectively with your teammate if applicable.
- Thoroughly review your work during the pull request phase.
- Seek assistance from your instructor if any issues arise.

**Submission:**

- Complete a series of pull requests within the GitHub repository.
- Ensure all steps are finished, including setting up upstream repositories, and submit the final pull request to the main upstream repository.

This assignment not only enhances GitHub collaboration skills but also emphasizes effective communication and teamwork. If you have questions or need clarification, contact your instructor. Good luck and happy collaborating!
