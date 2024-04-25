### Assignment 7: Data Science 101

#### Title: Exploratory Data Analysis (EDA) and Hypothesis Testing

#### Objective:
The objective of this assignment is to encourage students to explore and analyze datasets, perform Exploratory Data Analysis (EDA), frame hypotheses, and use data visualization to prove or disprove their hypotheses. Students will create a Jupyter notebook for their analysis.
  
#### Datasets to Choose From:

1. **Student Performance Dataset:**
   - Dataset: [Student Performance Dataset](https://archive.ics.uci.edu/ml/datasets/Student+Performance)
   - Description: Includes data on student grades, demographic, social and school-related features from two Portuguese schools.

2. **Census Income Dataset:**
   - Dataset: [Census Income Dataset](https://archive.ics.uci.edu/ml/datasets/Census+Income)
   - Description: Focuses on predicting whether an individual's income exceeds $50K/yr based on census data.

3. **Wine Dataset:**
   - Dataset: [Wine Dataset](https://archive.ics.uci.edu/ml/datasets/Wine)
   - Description: Results of a chemical analysis of wines grown in the same region in Italy but derived from three different cultivars.

4. **German Credit Data Dataset:**
   - Dataset: [German Credit Data Dataset](https://archive.ics.uci.edu/ml/datasets/Statlog+(German+Credit+Data))
   - Description: Classifies people described by a set of attributes as good or bad credit risks.

5. **Wine Quality Dataset:**
   - Dataset: [Wine Quality Dataset](https://archive.ics.uci.edu/ml/datasets/wine+quality)
   - Description: Contains various physicochemical properties of red and white wine, and quality ratings.

#### Assignment Tasks:

1. **Importing Data and Libraries:**
   - Use Python and Jupyter notebook to import the chosen dataset and necessary libraries (Pandas, NumPy, Matplotlib, Seaborn).

2. **Exploratory Data Analysis (EDA):**
   - Explore the dataset's structure, summary statistics, and distributions.
   - Visualize key features using appropriate plots (scatter plots, histograms, etc.).

3. **Hypothesis Formulation:**
   - Frame at least two hypotheses related to the dataset. For example:
     - "There is a correlation between alcohol content and wine quality."
     - "The day of the week influences absenteeism at work."

4. **Hypothesis Testing:**
   - Use statistical tests or visualizations to test the formulated hypotheses.
   - Discuss the results and draw conclusions based on the analysis.

5. **Documentation and Reporting:**
   - Document the entire analysis process, including code, explanations, and interpretations.
   - Summarize key findings in a clear and concise report.

#### Sample Jupyter Notebook Template:

```python
# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Importing the dataset
# Replace 'your_dataset_url' with the actual URL or file path
url = 'your_dataset_url'
df = pd.read_csv(url)

# Exploratory Data Analysis (EDA)
# Explore the dataset's structure and summary statistics

# Visualize key features using plots

# Hypothesis Formulation
# Formulate at least two hypotheses related to the dataset

# Hypothesis Testing
# Test the formulated hypotheses using statistical tests or visualizations

# Documentation and Reporting
# Document the entire analysis process, including code and explanations
# Summarize key findings in a clear and concise report
```

**Note:** Students should replace `your_dataset_url` with the actual URL or file path of their chosen dataset. 
##### Extra Credit : Additional analyses and inferences beyond the outlined tasks for a more comprehensive understanding.


#### How to Submit:

Ensure that you are up to date with the upstream Github repo. Do the following before starting your assignment.

```
cd <to your github repo path>
git checkout main
git fetch upstream
git rebase upstream/main
git checkout -b [new branch] upstream/main
```

Create a folder here [https://github.com/DS219/spark-seprep/tree/main/assignments/assignment7/](https://github.com/DS219/spark-seprep/tree/main/assignments/assignment7/) with your name, and add the dataset you choose and jupyter notebook in this folder. After adding it your branch, make a pull request to the upstream repository.
