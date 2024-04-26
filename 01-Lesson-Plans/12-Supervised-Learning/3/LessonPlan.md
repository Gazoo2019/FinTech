## 12.3 Lesson Plan: Imbalanced Classes

### Overview

This class focuses on a problem that the students will often encounter in classification: imbalanced data. This happens when the classes we are trying to predict are represented unequally in the data. For example, in most fraud-detection problems, transactions involving fraud are rare when compared to the number of legitimate transactions. We will approach this problem in two ways: first, through careful examination of how we use model evaluation metrics, and second, by deliberately undersampling or oversampling to make the training data more equally proportioned. The students will get the opportunity in this class to practice both theory and implementation.

### Class Objectives

By the end of class, the students will be able to:

* Define model evaluation metrics and understand the pros and cons of each metric as applied imbalanced classification problems.

* Define class imbalance and understand why it presents a problem for classification models.

* Demonstrate the ability to undersample and oversample data with imbalanced classes.

### Instructor Notes

* Today's class is relatively heavy on theory. The students must understand the reasons for using the sampling strategies demonstrated in the activities. Check for understanding by posing questions to the students about hypothetical use cases and datasets.

* Be sure to spend some time on the implementations of SMOTE and cluster centroids undersampling, and encourage students to read the documentation so that they understand the logic used within these modules.

**Note**: Concepts like confusion matrixes or the precision-recall curve may be easier for many students to understand visually, so be sure to use the slides that illustrate these concepts.

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 12.3 slides](https://docs.google.com/presentation/d/1JFKq-HIPuMhA0xYVChkvJGwFmwMyeSXCWb28sLDhk74/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. [View the instructions here].(<https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing>).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and then selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome the Class (5 minutes)

Open the [Lesson 12.3 slides](https://docs.google.com/presentation/d/1JFKq-HIPuMhA0xYVChkvJGwFmwMyeSXCWb28sLDhk74/edit?usp=sharing) and welcome the students back to the third day of classification and machine learning. Explain that now that we’ve discussed some techniques to create classification models, we are ready to take the next step and apply those techniques to real-world problems. Provide the following context:

* One prominent problem in many classification tasks is class imbalance, which occurs when the training data you use to build your classification model is unevenly split. Some examples include fraud detection, churn prediction, and medical diagnoses. (Ask the students if they can think of additional examples.)

* In this lesson, we’ll discuss the challenges this creates for model creation and evaluation, and then cover techniques for dealing with these challenges.

Explain that before diving in, we’ll briefly review some concepts from Day 1 of this unit, specifically, confusion matrixes and some metrics for evaluating models.

### 2. Instructor Do: Review Model Evaluation (10 minutes)

**Corresponding Activity:** [01-Ins_Review_Eval_Metrics](Activities/01-Ins_Review_Eval_Metrics)

This activity will give the students a chance to reinforce the concepts of model evaluation.

**Files:**

* [review_model_eval.ipynb (Solved)](Activities/01-Ins_Review_Eval_Metrics/Solved/review_model_eval.ipynb)

Slack out the solved version of this notebook above. Then, go through the first few blocks of the notebook, highlighting the following points:

* We created two classes in this data, and these classes have two important characteristics.

  * One class is much larger than the other.

  * The classes have significant variation, so one cannot be easily distinguished from the other.

   ![eval_1.png](Images/eval_1.PNG)

* Using a logistic regression model, we try to predict the class, purple or yellow, with the coordinates of a point.

Ask a student to help you interpret the output of the confusion matrix, and then reveal the correct answer.

![eval_2png](Images/eval_2.PNG)

* When we only look at this matrix, it seems that the model does reasonably well. While there are some false positives, the model has classified the vast majority of data points correctly.

Move on to the next block, and ask a student to define the three metrics that are shown here. Then reveal the correct answer.

![eval_3png](Images/eval_3.PNG)

* Precision is the proportion of predicted positives that are accurate. Recall is the proportion of actual positives that were predicted as positive. The F1 metric is a blended average of the two.

Ask students to evaluate the performance of this model. How do they think it did?

* While the confusion matrix and evaluation metrics give us some insight into performance, this is a trick question because what is considered "good" or "bad" depends on the context. What are we trying to predict? What are the costs of false positives or false negatives?

### 3. Students Do: Hypothetical Models (15 minutes)

**Corresponding Activity:** [02-Stu_Do_Hypothetical_Models](Activities/02-Stu_Do_Hypothetical_Models)

In this activity, the students will work in groups of two or three to discuss the relative importance of false positives and negatives. They’ll also weigh the pros and cons of using each evaluation metric for a set of hypothetical classification models.

**Instructions:**

* [README.md](Activities/02-Stu_Do_Hypothetical_Models/README.md)

### 4. Instructor Do: Review Hypothetical Models (10 minutes)

Open the slides and go through each scenario with the students.

Ask a student volunteer to lead the class through each scenario, and then review the answers.

* In the first case, if we define spam emails as positives, false positives are more costly than false negatives. A spam email getting through is not the end of the world, but an important email that gets flagged as spam might be disastrous for the user. We should review precision and specificity for this reason. Spam emails probably make up a relatively small (but not tiny) proportion of all emails. Because of this, a high accuracy or F1 score might be misleading.

* Here, we should be weighting false positives and false negatives evenly, but true positives are likely to be small, relative to the amount of true negatives. In this situation, high accuracy may still be misleading, and we should examine all other evaluation metrics for different models to understand their relative strengths and weaknesses.

* For the third example, there does not seem to be any obvious reason why false negatives or positives should be weighted more than the other. Assuming a random, representative sample, we would expect the two classes to be roughly equal in size. Therefore, accuracy or the F1 score would likely be an effective summary metric to compare models.

* In the fourth example, if we define rain as positive, false negatives are likely to be more costly than false positives. (The cost of being without an umbrella in the rain is a lot higher than the cost of carrying one when it’s not needed.) This makes recall a metric of special interest because the classes are likely to be imbalanced, but not overwhelmingly so. The F1 score is probably a useful measure for comparing metrics.

* For the final example, venture capitalists (VCs) will probably view false negatives as more costly than false positives. VCs invest with the knowledge that the majority of companies will fail, and they get large returns from those that don't. Recall is likely to be the metric of most interest in this case.

Remind the class that we will always benefit from looking at the confusion matrix and all the metrics to understand the strengths and weaknesses of any particular model, even if some models may be more useful than others for any given data.

### 5. Instructor Do: Imbalanced Data (5 minutes)

Use the slides as you discuss the following points:

* **Imbalanced data** describes cases when one or more classes in the data are much more or less frequent than the other class(es). We will be working with binary (two-class) classification tasks for simplicity, but imbalanced data is a problem in multi-class tasks as well.

* Imbalanced data is problematic for two main reasons. First, it can cause your model to be biased toward the majority class. Basically, the model will be better at predicting the majority class compared to the minority class because model fitting algorithms are designed to minimise the number of total incorrect classifications.

  * For a concrete example, imagine a dataset with two classes, A and B. There are 90 instances of A in the training sample, and only 10 instances of B. Imagine an unsophisticated model that always predicts an observation as A. If the data were perfectly balanced—that is, if the data had 50 of A and 50 of B—this unsophisticated model would result in an accuracy of 50%. However, because this data is imbalanced, this model would achieve an accuracy of 90/100, or 90%! If the data is imbalanced, accuracy scores can be a misleading indicator of model quality.

* As demonstrated in the previous activity, imbalanced classes like cancer/non-cancer can cause metrics like accuracy to be unreliable as a proxy for the "goodness" of a model. The preceding example illustrates why.

* The rest of the class will cover strategies for dealing with imbalanced classes. We will work mostly with oversampling and undersampling methods.

  * Oversampling is when we sample the minority class with greater-than-random chance.

  * Undersampling is when we sample the majority class with less-than-random chance.

* We will also explain why ensemble methods may be more suitable for imbalanced data than other classification methods, and we'll introduce a classification report specifically created for imbalanced data.

### 6. Instructor Do: Random Sampling (10 minutes)

**Corresponding Activity:** [03-Ins_Random_Resampling](Activities/03-Ins_Random_Resampling)

**Files:**

[random_resampling.ipynb](Activities/03-Ins_Random_Resampling/Solved/random_resampling.ipynb)

Introduce the problem of class imbalance and resampling methods.

* **Class imbalance** refers to a situation in which the existing classes in a dataset aren't equally represented.

  * Consider a fraud detection scenario with a large number of legitimate credit card transactions and only a small number of fraudulent ones. Let's say that out of 100,000 transactions, 50 are fraudulent and the rest are legitimate. The pronounced imbalance between the two classes (fraudulent and non-fraudulent) can cause machine learning models to be biased toward the majority class.

  * The model will be much better at predicting non-fraudulent transactions than fraudulent ones—and this is a problem if the goal is to detect fraudulent transactions!

  > **Note**: In the machine learning field, people often refer to the larger class as the majority class and to the smaller class as the minority class.

Most of these techniques for dealing with class imbalance fall into the following two categories:

* **Oversampling**: Creating more instances of a class label, usually for the smaller class.

Share the following image illustrating oversampling:

![oversampling](./Images/oversampling.png)

* **Undersampling**: Creating fewer instances of a class label, usually for the larger class. Undersampling is practical only when enough data exists in the training dataset. The undersampled majority class must have enough usable data for a model to prove useful.

Share the following image illustrating undersampling:

![undersampling](./Images/undersampling.png)

Highlight that oversampling addresses imbalanced classes by duplicating existing data. Undersampling uses only existing data.

* Oversampling and undersampling can be combined into **combination sampling**.

Next, cover two methods that are commonly used to obtain new samples.

* With **random sampling** our algorithm chooses random instances from the existing dataset. We can use either oversampling or undersampling when sampling randomly, but we are using existing instances in our dataset and not creating new ones.

* With **synthetic sampling, our algorithm generates new instances from observations about existing data. For example, in a dataset on loan defaults, if we wanted to simulate a new “did default” observation, we could use k-nearest neighbours to approximate the characteristics of a borrower who defaulted. We would then generate a point synthetically that was not in our original dataset.

Share the following image that shows the set of sampling techniques that we’ll learn in this lesson, categorised by type:

![resampling](./Images/resampling_tree.png)

The material that follows will cover these techniques.

* Oversampling techniques:

  * Random oversampling

  * Synthetic minority oversampling technique (SMOTE)

* Undersampling techniques:

  * Random undersampling

  * Cluster centroid

* Combination sampling technique:

  * SMOTE and edited nearest neighbours (ENN), or SMOTEENN

Open a new notebook and import the following modules:

```python
# Import modules
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

* We will use `make_blobs()` to generate a dataset with extreme class imbalance. This will exaggerate the effects of the resampling methods. Real-world datasets will usually not have such an extreme case, but it's useful for the demonstration.

* The dataset has two clusters: one has 5000 instances and the other has 50. A large standard deviation provides lots of overlap.

* We will plot the target labels by passing in the target column for the `c` parameter in the scatter plot.

* We will then compare the random forest on each resampled dataset.

# Generate Data
X, y = make_blobs(n_samples=[5000, 50], random_state=1, cluster_std=7)

# Convert ndarray to Pandas data types
X = pd.DataFrame(X)
y = pd.Series(y)

# Plot data
plt.scatter(
    x=X[0],
    y=X[1],
    c=y)
plt.show()

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# Count distinct values
y_train.value_counts()
```

> **Note**: We don't need to scale and normalise the data from `make_blobs`. The dataset is returned normalised.

![cluster_plot](./Images/cluster_plot.png)

* Highlight that the values of the target dataset are quite imbalanced, with 3753 observations in the majority class and only 34 in the minority class.

 ```text
 0   3753
 1     34
 dtype: int64
 ```

With the features and targets datasets in place, we can begin to address our sampling issues.

#### Random Undersampling

Explain to the class that random undersampling removes randomly selected instances from the majority class until the size of that class is reduced, typically to the size of the minority class. In class imbalance problems, we can measure the success of a model by how well it found instances of the minority class.

* Remind the students that precision calculates the number of false positives that the model produced relative to the total number of instances.

* The recall calculates the ratio of the known values from the testing dataset to the values that the model failed to predict.

Add the following code to the notebook:

  ```python
  # Import RandomUnderSampler from imblearn
  from imblearn.under_sampling import RandomUnderSampler

  # Instantiate the RandomUnderSampler instance
  rus = RandomUnderSampler(random_state=1)

  # Fit the data to the model
  X_resampled, y_resampled = rus.fit_resample(X_train, y_train)

  # Count distinct values
  y_resampled.value_counts()
  ```

* We import the `RandomUnderSampler` from `imblearn.under_sampling`. You can read more about RandomUnderSampler on the [documentation page](https://imbalanced-learn.org/stable/references/generated/imblearn.under_sampling.RandomUnderSampler.html).

* The minority class is value 1. In the original dataset, we had 3753 versus 34 instances in the training set. We can observe with `value_counts` that the resampled sets are equal at 34 observations each.

* The `RandomUnderSampler` model randomly chose which of the majority class labels not to keep until it was the same size as the minority class.

Now explain the following points, and add the code that follows.

* We fit a random forest classifier to the resampled dataset. Then we generate a set of test predictions for the original training set.

* Looking at the plots of the `y_pred` and `y_pred_resampled`, we notice that `y_pred_resampled` identified many more points as being part of the minority class. Looking at the two classification reports, the recall has gone up considerably for the minority class. By allowing more false positives, we went from capturing 6% of the known minority class labels to 81%.

* This may seem counterintuitive, but the calculations used for scoring and accuracy metrics may not apply to the business need.

  * Consider a bank that wants to automate a text verification system that asks customers if the last transaction made was truly theirs. The best scenario for the bank is to send the front line text to more people because this increases the chances of catching the fraudulent transactions. If a customer responds yes, then a human can intervene.

  ```python
  # Instantiate an initial RandomForestClassifier instance
  model = RandomForestClassifier()

  # Fit the initial model based the training data
  model.fit(X_train, y_train)
  ```

  ```python
  # Instantiate a second RandomForestClassifier instance
  model_resampled = RandomForestClassifier()

  # Fit the second model based the resampled data
  model_resampled.fit(X_resampled, y_resampled)
  ```

  ```python
  # Make predictions using the initial model
  y_pred = model.predict(X_test)

  # Make predictions using the model based on the resampled data
  y_pred_resampled = model_resampled.predict(X_test)

  # Plot the data using the original y_test information
  plt.scatter(
      x=X_test[0],
      y=X_test[1],
      c=y_test)
  plt.show()

  # Plot the data using the predictions based on the original test data
  plt.scatter(
      x=X_test[0],
      y=X_test[1],
      c=y_pred)
  plt.show()

  # Plot the data using the predictions based on the resampled test data
  plt.scatter(
      x=X_test[0],
      y=X_test[1],
      c=y_pred_resampled)
  plt.show()
  ```

The following image shows the plot based on the resampled data:

![false_positives](Images/rus_false_positives.png)

We'll print the classification reports:

  ```python
  # Print classification report
  print(classification_report(y_test, y_pred))
  print(classification_report(y_test, y_pred_resampled))
  ```

![classification_report](Images/rus_classification_report.png)

* **Note:** Your notebook output may vary from the preceding image. When describing the classification report output, use the following statement as a guide, but tailor your description according to your actual results:

  * We found 81% of the minority labels, but we were right only 5% of the time. This is definitely not the best outcome.

Explain that we can contrast the outcome from random undersampling with random oversampling by generating and evaluating observations using that methodology.

#### Random Oversampling

Now we will review **random oversampling**:

* In random oversampling, our algorithm randomly selects instances of the minority class and adds them to the training set until the majority and minority classes are balanced.

* We might need to test different resampling methods and model combinations for a dataset.

* We will use the `RandomOverSampler` from `imblearn.over_sampling`. You can read more about `RandomOverSampler` on the [imblearn documentation page](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.RandomOverSampler.html).

Explain the following points and add the code that follows:

* When we observe the value counts, we notice that the minority class instance had lower recall compared to random undersampling, but it was more precise.

* We didn't catch as many of the minority class, but we didn't get as many false positives, and we were more precise.

* Determining which resampler performs better can be very dependent on the business case.

  ```python
  # Import RandomOverSampler from imblearn
  from imblearn.over_sampling import RandomOverSampler

  # Instantiate the RandomOverSampler instance
  random_oversampler = RandomOverSampler(random_state=1)

  # Fit the data to the model
  X_resampled, y_resampled = random_oversampler.fit_resample(X_train, y_train)

  # Count distinct values
  y_resampled.value_counts()
  ```

Note that, after oversampling, the result of the value counts is still equal between the majority and minority class, but the values are vastly different.

  ```text
  1  3753
  0  3753
  dtype: int64
  ```

As with undersampling, create two RandomForestClassifier models, one using the original data and the other using the oversampled data. Then, generate the predictions and compare the results.

```python
# Create a RandomForestClassifier instance and fit it to the original data
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Create a RandomForestClassifier instance and fit it to the resampled data
model_resampled = RandomForestClassifier()
model_resampled.fit(X_resampled, y_resampled)

# Make predictions for testing features
y_pred = model.predict(X_test)
y_pred_resampled = model_resampled.predict(X_test)

# Print the classification reports for the two models
print(classification_report(y_test, y_pred))
print(classification_report(y_test, y_pred_resampled))
```

![ros_classification_report](Images/ros_classification_report.png)

* **Note:** Your notebook output may vary from the preceding image. When describing the classification report output, use the following statement as a guide, but tailor your description according to your actual results:

  * Using oversampling to correct the imbalance, we found only 19% of the minority class instances, but we were correct 43% of the time. Compare this to the predictions using undersampling: We found 81% of the minority class instances but were correct only 5% of the time. Regardless of the different outcomes, both undersampling and oversampling improved the results over the original data.

Answer any questions before moving on.

### 7. Students Do: Random Resampling (20 minutes)

In this activity, the students will use the provided dataset of a bank's telemarketing campaign. They will compare the effectiveness of random resampling methods using a random forest. They will then measure the random forest's recall of the minority class for both a random forest fitted to the resampled data and to the original dataset.

Slack out the following files to the students.

**Instructions:**

[Instructions](./Activities/04-Stu_Random_Resampling/README.md)

**Files:**

[bank.csv](./Activities/04-Stu_Random_Resampling/Resources/bank.csv)

[Starter Code](./Activities/04-Stu_Random_Resampling/Unsolved/random_resampling.ipynb)

### 8. Instructor Do: Review Random Resampling (10 minutes)

Review the following solution file with the students:

**Files:**

[Solution code](./Activities/04-Stu_Random_Resampling/Solved/random_resampling.ipynb)

Start the review of this activity by asking the following question:

**Question**: What is a categorical variable, and what must we do before fitting a model to a dataset with categorical variables?

**Answer**: Categorical variables are discrete variable types. They have a fixed number of indivisible values. In the bank dataset, `default` and `housing` are examples of categorical variables. We need to one-hot encode any categorical variable before fitting a model. Once we create the features and target datasets, we can update the categorical variables in the features dataset using the Pandas `get_dummies` function.

  ```python
  # Encode the features dataset's categorical variables using get_dummies
  X = pd.get_dummies(X)

  # Review the features DataFrame
  X.head()
  ```

After we've handled the categorical variables and split the data into testing and training datasets, we'll scale the data using `StandardScaler`.

  ```python
  # Split data into training and testing datasets
  X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

  # Review the distinct values from y
  y_train.value_counts()

  # Instantiate a StandardScaler instance
  scaler = StandardScaler()

  # Fit the training data to the standard scaler
  X_scaler = scaler.fit(X_train)

  # Transform the training data using the scaler
  X_train_scaled = X_scaler.transform(X_train)

  # Transform the testing data using the scaler
  X_test_scaled = X_scaler.transform(X_test)
  ```

Finally, we can generate a RandomForestClassifier model and make predictions based on the original data.

  ```python
  # Import the RandomForestClassifier from sklearn
  from sklearn.ensemble import RandomForestClassifier

  # Instantiate a RandomForestClassifier instance
  model = RandomForestClassifier()

  # Fit the training data to the model
  model.fit(X_train_scaled, y_train)

  # Predict labels for original scaled testing features
  y_pred = model.predict(X_test_scaled)
  ```

Next, we'll create random undersampling and random oversampling models that will resample the datasets. We will then use these resampled datasets to fit another instance of the random forest classifier for making predictions.

* The code to make predictions using RandomUnderSampler follows. Note that the distinct value counts associated with the target have changed.

  ```python
  # Import RandomUnderSampler from imblearn
  from imblearn.under_sampling import RandomUnderSampler

  # Instantiate a RandomUnderSampler instance
  rus = RandomUnderSampler(random_state=1)

  # Fit the training data to the random undersampler model
  X_undersampled, y_undersampled = rus.fit_resample(X_train_scaled, y_train)

  # Count distinct values for the resampled target data
  y_undersampled.value_counts()

  # Instantiate a new RandomForestClassier model to the undersampled data
  model_undersampled = RandomForestClassifier()

  # Fit the undersampled data the new model
  model_undersampled.fit(X_undersampled, y_undersampled)
  ```

  * In both resampling instances, there was an increase in the recall for the minority class. This is the result that we wanted. (Your output may vary from the following image.)

![stu_random_undersample](./Images/stu_random_undersample.png)

* Show the class that the code to resample the data using random oversampling is quite similar. Point out how the distinct value counts associated with the target have changed once again.

  ```python
  # Import RandomOverSampler from imblearn
  from imblearn.over_sampling import RandomOverSampler

  # Instantiate a RandomOversampler instance
  ros = RandomOverSampler(random_state=1)

  # Fit the model to the training data
  X_oversampled, y_oversampled = ros.fit_resample(X_train_scaled, y_train)

  # Count distinct values
  y_oversampled.value_counts()

  # Instantiate a new RandomForestClassier model to the oversampled data
  model_oversampled = RandomForestClassifier()

  # Fit the oversampled data the new model
  model_oversampled.fit(X_oversampled, y_oversampled)

  # Predict labels for oversampled testing features
  y_pred_oversampled = model_oversampled.predict(X_test_scaled)
  ```

* Similar to our demo, random oversampling proved better for one metric, but was not as strong for another. (Your output may vary from the image that follows.)

  ![stu_random_oversample](./Images/stu_random_oversample.png)

Ask students if they have any questions about random oversampling and random undersampling before moving on to the next activity.

---

### 9. Break (15 minutes)

---

### 10. Instructor Do: Synthetic Resampling (10 minutes)

In this activity, you will demo the following synthetic resampling methods:

* Cluster Centroids

* SMOTE (Synthetic Minority Oversampling Technique)

* SMOTEENN (SMOTE + Edited Nearest Neighbors)

**Files:**

* [synthetic_resampling.ipynb](./Activities/05-Ins_Synthetic_Resampling/Solved/synthetic_resampling.ipynb)

Explain the following:

* Synthetic sampling creates new data points from existing observations. There are several ways to do this, but the most common approach is to use K-nearest neighbours (KNN) to generate the new points.

* The general idea is that the algorithm will identify clusters of points that are near a mean value. This is similar to k-means (that was covered in the lessons on unsupervised learning). Once the cluster is identified, we use KNN to generate new points in the cluster.

Open a notebook and create a dataset using `make_blobs`:

  ```python
  # Import modules
  import Pandas as pd
  import matplotlib.pyplot as plt
  from sklearn.datasets import make_blobs
  from sklearn.model_selection import train_test_split
  from sklearn.ensemble import RandomForestClassifier
  from sklearn.metrics import classification_report

  # Generate Data
  X, y = make_blobs(n_samples=[5000, 50], random_state=1, cluster_std=7)

  # Convert ndarray to pandas datatypes
  X = pd.DataFrame(X)
  y = pd.Series(y)

  # Plot data
  plt.scatter(
      x=X[0],
      y=X[1],
      c=y)
  plt.show()

  # Split data
  X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

  # Count distinct values
  y_train.value_counts()
  ```

The resulting plot and data point should illustrate an imbalanced data set in favour of the 0 class:

  ```text
  0    3753
  1      34
  dtype: int64
  ```

#### Cluster Centroids

Explain the following points about cluster centroids.

* In both of the random sampling methods discussed in the prior section, we randomly chose points to add or remove.

* **Cluster centroids** is a synthetic method of resampling the data to achieve a balance between what started as the majority and minority classes.

* We identify the centre of a cluster of the majority class, and then generate points in that cluster using k-nearest neighbours.

* These generated points are then undersampled until there are an equivalent number of instances as the minority class.

> **Note:** `imblearn.under_sampling` provides the `ClusterCentroids` model for this task. You can read more about this model on the [documentation page](https://imbalanced-learn.org/stable/references/generated/imblearn.under_sampling.ClusterCentroids.html).

Add the following lines of code:

  ```python
  # Import ClusterCentroids from imblearn
  from imblearn.under_sampling import ClusterCentroids

  # Create an instance of ClusterCentroids
  cc = ClusterCentroids(random_state=1)

  # Fit the cluster centroids model to the traning data
  X_resampled, y_resampled = cc.fit_resample(X_train, y_train)

  # Count resampled values
  y_resampled.value_counts()
  ```

The output is as follows:

  ![cc-value-counts](Images/cc_value_counts.png)

Once we have our resampled data, our next step is to instantiate the RandomForestClassifier model, fit the models, and analyse the classification reports on the predicted values:

  ```python
  # Fit the RandomForestClassifier on the original data
  model = RandomForestClassifier()
  model.fit(X_train, y_train)

  # Fit the RandomForestClassifier on the resampled data
  model_resampled = RandomForestClassifier()
  model_resampled.fit(X_resampled, y_resampled)

  # Generate predictions based on the original data model
  y_pred = model.predict(X_test)

  # Generate predictions based on the resampled data model
  y_pred_resampled = model_resampled.predict(X_test)

  # Print classification reports
  print(classification_report(y_test, y_pred))
  print(classification_report(y_test, y_pred_resampled))
  ```

* Although the accuracy with the resampled data was not improved, the resampled model using cluster centroids improved in making predictions regarding the 1 class. (Your output may vary from the following image.)

  ![cc_classification_report](Images/cc_classification_report.png)

* The performance of CentroidClusters looks very similar to that of the RandomUnderSampler.

* Keep in mind that our synthetic data generated make_blobs is derived from a normal distribution. Real world datasets may NOT be normally distributed, so the performance of different resampling methods will vary.

#### SMOTE

Slack out the following research paper on SMOTE, as you introduce the high-level points behind this algorithm.

[SMOTE.pdf](./Activities/05-Ins_Synthetic_Resampling/Resources/SMOTE.pdf)

* **SMOTE**, the **Synthetic Minority Oversampling Technique**, is another synthetic resampling technique. It also works by using K-nearest neighbours to generate synthetic data. Only this time, the synthetic points are from the minority class.

* The set of synthetic points from the minority class is oversampled until it is the same size as the majority class.

* You can read more about implementing SMOTE on the [documentation page](https://imbalanced-learn.org/stable/over_sampling.html#from-random-over-sampling-to-smote-and-adasyn).

Add the following code:

```python
# Import SMOTE from imblearn
from imblearn.over_sampling import SMOTE

# Instantiate the SMOTE model instance
smote_sampler = SMOTE(random_state=1, sampling_strategy='auto')

# Fit the SMOTE model to the training data
X_resampled, y_resampled = smote_sampler.fit_resample(X_train, y_train)

# Count resampled values
y_resampled.value_counts()
```

* Note that we add the parameter `sampling_strategy='auto'` when instantiating the SMOTE instance. This allows the algorithm to automatically re-sample the training dataset. This is in contrast to specifying the number of elements in each class.

* We can observe from the value counts that SMOTE is an oversampling method, as shown in the following image:

  ![smote_value_counts](Images/smote_value_counts.png)

  ```python
  # Fit the RandomForestClassifier on the original data
  model = RandomForestClassifier()
  model.fit(X_train, y_train)

  # Fit the RandomForestClassifier on the resampled data
  model_resampled = RandomForestClassifier()
  model_resampled.fit(X_resampled, y_resampled)

  # Generate predictions based on the original data model
  y_pred = model.predict(X_test)

  # Generate predictions based on the resampled data model
  y_pred_resampled = model_resampled.predict(X_test)

  # Print classification reports
  print(classification_report(y_test, y_pred))
  print(classification_report(y_test, y_pred_resampled))
  ```

The output is shown in the following image. (Your output may vary from what is shown here.)

  ![smote_classification_report](Images/smote_classification_report.png)

* SMOTE improved the results, but they were not the best that we have observed for this dataset. This does not mean that, on average, SMOTE performs worse. It simply means that for this specific synthetic dataset, it did not perform as well as undersampling with cluster centroids or, in terms of precision, as the RandomOverSampler model.

#### SMOTEENN

* **SMOTEENN** is a combination of SMOTE oversampling and undersampling by removing misclassified points using edited nearest neighbours (ENN).

* **Edited nearest neighbours** is a rule that uses the three nearest neighbours to find a misclassified point and then remove it. You can read more about imblearn's `EditedNearestNeighbors` implementation on the [documentation page](https://imbalanced-learn.org/stable/references/generated/imblearn.under_sampling.EditedNearestNeighbours.html).

* You can read more about `SMOTEENN` on the [documentation page](https://imbalanced-learn.org/stable/references/generated/imblearn.combine.SMOTEENN.html).

Add the following code to resample the dataset by using SMOTEENN:

  ```python
  # Import SMOTEENN from imblearn
  from imblearn.combine import SMOTEENN

  # Instantiate an instance of the SMOTEENN model
  smote_enn = SMOTEENN(random_state=0)

  # Fit the SMOTEENN model to the training data
  X_resampled, y_resampled = smote_enn.fit_resample(X_train, y_train)

  # Count distinct values
  y_resampled.value_counts()
  ```

* Notice that the value counts are not the same because we applied edited nearest neighbours to remove misclassified points.

![smoteen_value_counts](Images/smoteenn_value_counts.png)

Fit the model and then compare the predicted values of the resampled and original training set.

  ```python
  # Fit random forest on data
  model = RandomForestClassifier()
  model.fit(X_train, y_train)

  # Fit random forest on resampled data
  model_resampled = RandomForestClassifier()
  model_resampled.fit(X_resampled, y_resampled)

  # Generate predictions based on the original data model
  y_pred = model.predict(X_test)

  # Generate predictions based on the resampled data model
  y_pred_resampled = model_resampled.predict(X_test)

  # Print classification reports
  print(classification_report(y_test, y_pred))
  print(classification_report(y_test, y_pred_resampled))
  ```

  ![smoteenn_classification_report](Images/smoteenn_classification_report.png)

* As we can observe in the classification report, SMOTEEN's model performed better than the SMOTE model alone, but SMOTEEN did not do as well as the cluster centroids. (Your output may vary from the preceding image.)

Explain to the students that the key to selecting the best resampling technique is understanding how they generally perform. Through the process of resampling the data, fitting the classifier model, making predictions, and evaluating the results, you can determine the technique that works best for the current dataset.

Answer any questions before moving on.

### 11. Students Do: Synthetic Resampling (20 minutes)

In this activity, the students will use the provided dataset of a bank's telemarketing campaign. They will compare the effectiveness of synthetic resampling methods by using a random forest. They will measure the random forest's recall of the minority class for both a random forest fitted to the resampled data and the original data.

Slack out the following files to the students:

**Files:**

[bank.csv](./Activities/06-Stu_Synthetic_Resampling/Resources/bank.csv)

[Starter code](./Activities/06-Stu_Synthetic_Resampling/Unsolved/synthetic_resampling.ipynb)

[Instructions](./Activities/06-Stu_Synthetic_Resampling/README.md)

### 12. Instructor Do: Review Synthetic Resampling (10 minutes)

Review the solution with the students:

**Files:**

[Solution code](./Activities/06-Stu_Synthetic_Resampling/Solved/synthetic_resampling.ipynb)

* The solution code is very similar to the previous activity, with the only exception being the resamplers used.

Ask the students the following question and call on a volunteer to share the answer. If no one volunteers, provide the students with the answer.

* **Question:** What are the high-level steps in the process for making predictions with resampled data?

* **Answer:**

  * Import the data.
  * Separate the data into target and feature datasets.
  * Encode the data.
  * Split the data into training and testing datasets.
  * Scale the data.
  * Import the resampling technique (random oversampling, cluster centroids, SMOTE, etc.)
  * Resample the X and y training sets to make the value counts between classes approximately equal.
  * Instantiate the classifier model.
  * Fit the model with the resampled data
  * Generate the predictions.
  * Review the results.

Because this process is identical across the board, review the code for just the cluster centroids resampling technique.

  ```python
  # Import ClusterCentroids from imblearn
  from imblearn.under_sampling import ClusterCentroids

  # Instantiate a ClusterCentroids instance
  cc_sampler = ClusterCentroids(random_state=1)

  # Fit the training data to the cluster centroids model
  X_resampled, y_resampled = cc_sampler.fit_resample(X_train_scaled, y_train)

  # Count distinct values for the resampled target data
  y_resampled.value_counts()

  # Instantiate a new RandomForestClassier model
  cc_model = RandomForestClassifier()

  # Fit the resampled data to the new model
  cc_model.fit(X_resampled, y_resampled)

  # Predict labels for resampled testing features
  cc_y_pred = cc_model.predict(X_test_scaled)

  # Print classification reports
  print(f"Classifiction Report - Original Data")
  print(classification_report(y_test, y_pred))
  print("---------")
  print(f"Classifiction Report - Redsampled Data - CentroidClusters")
  print(classification_report(y_test, cc_y_pred))
  ```

  ![activity_cc_classification_report](./Images/activity-cc-classification-report.png)

Ask the students if they have any questions about the process for either the SMOTE or SMOTEENN techniques before moving on to the following questions.

The students’ results may vary slightly from the preceding image. Use the following answers as a guide, and tailor your responses appropriately.

* **Question:** Which model that we fit to the resampled datasets had the best recall for the minority class?

  * **Answer:** Cluster centroids had a recall of 0.99, though the precision was 0.16.

Explain the following:

* When we think about a bank that wants to send automated texts to catch fraudulent transactions, this is the best model/resampler combination for predicting the minority class label.

* The bank's business case may not care so much about precision, because the bank wants to catch fraudulent transactions, which are expensive. Even if five out of six emails sent are in reference to non-fraudulent transactions, this solution will make business sense if it catches 99% of actual fraud cases.

* Keep in mind that in the real world, the models receive new data and are updated as more cases are discovered. Over time, we would expect precision to increase once a feedback loop is established.

Note to the students that cluster centroids would work best for the fraudulent transaction business case, but our dataset was for targeted marketing campaigns. We would not want this low precision value because calling all the customers would yield a high recall rate.

* **Question**: Which model, when fit to the resampled datasets, would be the best for a targeted marketing campaign?

  * **Answer:** SMOTEENN had the best precision and recall combination overall. It would be the best for pre-screening potential customers for a targeted marketing campaign.

* **Question:** Which resampler technique/classifier model combination will work best?

  * **Answer:** Most of the time, we won't be able to identify the optimal combination from the start. You will need to experiment and try different combinations to determine what works for a given dataset. The best combination will also depend on the business case. A resampler technique/classifier model combo for one business case may not be acceptable for something else.

Explain that it's important to know all the available techniques and classifier models. Then you can test different combinations and evaluate their performance to find the optimal solution and save it for reuse.

Ask the students if they have any questions about resampling techniques and how they work in conjunction with classifier models. Next, we'll cover the `BalancedRandomForestClassifier` model.

### 13. Instructor Do: Balanced Random Forest (10 minutes)

In this section, you will demonstrate the balanced random forest classifier.

`imblearn` contains a class that implements random undersampling in addition to a random forest classifier called `BalancedRandomForestClassifier`.

* You can read more about it on the [documentation page](https://imbalanced-learn.org/stable/references/generated/imblearn.ensemble.BalancedRandomForestClassifier.html).

**Files:**

[credit_data.csv](./Activities/07-Ins_Balanced_Random_Forest/Resources/credit_data.csv)

[balanced_random_forest.ipynb](./Activities/07-Ins_Balanced_Random_Forest/Solved/balanced_random_forest.ipynb)

Open a new notebook and demonstrate the following code:

```python
# Prepare the data
# Import modules
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Read dataset
df = pd.read_csv('../Resources/credit_data.csv')
df.head()

# Split target column from dataset
y = df['credit_risk']
X = df.drop(columns='credit_risk')

# Encode the categorical variables using get_dummies
X = pd.get_dummies(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# Count distinct values
y_train.value_counts()

# Scale the data
scaler = StandardScaler()
X_scaler = scaler.fit(X_train)
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)
```

* We can create an instance of the classifier, fit it to the data, and then use it to predict labels from our scaled test dataset. The classifier will randomly undersample for us when it is fit.

```python
# Import BalancedRandomForestClassifier from imblearn
from imblearn.ensemble import BalancedRandomForestClassifier

# Instantiate a Balanced Random Forest Classifier instance
brf = BalancedRandomForestClassifier()

# Fit the model to the training data
brf.fit(X_train_scaled, y_train)

# Predict labels for testing features
y_pred = brf.predict(X_test_scaled)

# Print classification report
print(classification_report(y_test, y_pred))
```

Reinforce that the process for utilising a classifier model is the same (model-fit-predict), but the balanced random forest classifier incorporates random undersampling into the algorithm, so we don't need to perform a separate step for this.

* The classification report indicates that the accuracy, precision and recall for both class labels is very good. These are the best results observed so far for this dataset.

!['balanced_random_forest_classification](./Images/balanced_random_forest_classification_report.png)

Answer any questions before moving on.

---

### 14. Students Do: Comparing Imbalanced Classifiers (20 minutes)

**Corresponding Activity:** [08-Stu_Balanced_Random_Forest](Activities/08-Stu_Balanced_Random_Forest)

In this activity, the students will apply the balanced random forest model that they just learned. To understand the tradeoffs and determine which model performs best, they'll also deploy a regular random forest and an additional imbalanced model of their choosing.

Slack out the following files to the students:

**Instructions:**

* [README.md](Activities/08-Stu_Balanced_Random_Forest/README.md)

**Files:**

* [comparing_sampling_methods.ipynb](Activities/08-Stu_Balanced_Random_Forest/Unsolved/comparing_sampling_methods.ipynb)

* [sba_loans.csv](Activities/08-Stu_Balanced_Random_Forest/Resources/sba_loans.csv)

---

### 15. Instructor Do: Review Comparing Imbalanced Classifiers (10 minutes)

**Files:**

* [comparing_sampling_methods.ipynb (Solved)](Activities/08-Stu_Balanced_Random_Forest/Solved/comparing_sampling_methods.ipynb)

Go through the solution and highlight the following points.

* We first read in the data on SBA loans from the `Resources` folder into a Pandas DataFrame.

```python
# Read the sba_loans.csv file from the Resources folder into a Pandas DataFrame
loans_df = pd.read_csv(
    Path('../Resources/sba_loans.csv')
)

# Review the DataFrame
loans_df.head()
```

* Then, we create a Series named `y` that contains the data from the "Default" column of the original DataFrame. Note that this Series will contain the labels. Next, we create a new DataFrame named `X` that contains the remaining columns from the original DataFrame. Note that this DataFrame will contain the features.

```python
# Split the data into X (features) and y (labels)

# The y variable should focus on the Default column
y = loans_df['Default']

# The X variable should include all features except the Default column
X = loans_df.drop(columns=['Default'])
```

* We split the features and labels into training and testing sets.

```python
# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
```

* Then we scale the `X` data.

```python
# Scale the data
scaler = StandardScaler()
X_scaler = scaler.fit(X_train)
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)
```

* We check the magnitude of imbalance in the dataset by viewing the number of distinct values (`value_counts`) for the labels. Based on this, the dataset appears to be imbalanced, with loan defaults representing roughly 10% of the dataset.

```python
# Count the distinct values in the original labels data
y_train.value_counts()
```

* Then, we fit two versions of a random forest model to the data: the first is a regular `RandomForest` classifier:

```python
from sklearn.ensemble import RandomForestClassifier

# Create a random forest classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=1)

# Fitting the model
rf_model = rf_model.fit(X_train_scaled, y_train)

# Making predictions using the testing data
rf_predictions = rf_model.predict(X_test_scaled)
```

* Then, we add our a second model, a `BalancedRandomForest` classifier:

```python
# Import BalancedRandomForestClassifier from imblearn
from imblearn.ensemble import BalancedRandomForestClassifier

# Instantiate a BalancedRandomForestClassifier instance
brf = BalancedRandomForestClassifier()

# Fit the model to the training data
brf.fit(X_train_scaled, y_train)

# Predict labels for testing features
brf_predictions = brf.predict(X_test_scaled)
```

* We resample and fit the training data by one additional method for imbalanced data, such as `RandomOverSampler`, undersampling, or a synthetic technique. Here, we use `SMOTE` to resample the data, and then fit a random forest model to that resample data. (The students may have chosen any number of alternative models or resampling techniques).

```python
# Import SMOTE from imblearn
from imblearn.over_sampling import SMOTE

# Instantiate the SMOTE model instance
smote_sampler = SMOTE(random_state=1, sampling_strategy='auto')

# Fit the SMOTE model to the training data
X_resampled, y_resampled = smote_sampler.fit_resample(X_train, y_train)

# Fit the RandomForestClassifier on the resampled data
model_resampled_rf = RandomForestClassifier()
model_resampled_rf.fit(X_resampled, y_resampled)

# Generate predictions based on the resampled data model
rf_resampled_predictions = model_resampled_rf.predict(X_test)
```

Explain to the students that the next step is to print the confusion matrixes, accuracy scores, and classification reports for the three different models.

* Print the confusion matrixes:

```python
# Print the confusion matrix for RandomForest on the original data
confusion_matrix(y_test, rf_predictions)

# Print the confusion matrix for balanced random forest data
confusion_matrix(y_test, brf_predictions)

# Print the confusion matrix for RandomForest on the resampled data
confusion_matrix(y_test, rf_resampled_predictions)
```

* Then we print the accuracy scores:

```python
# Print the accuracy score for the original data
baso = balanced_accuracy_score(y_test, rf_predictions)
print(baso)

# Print the accuracy score for the resampled data
basr = balanced_accuracy_score(y_test, brf_predictions)
print(basr)

# Print the accuracy score for the resampled data
basrs = balanced_accuracy_score(y_test, rf_resampled_predictions)
print(basrs)
```

* And finally, we print the classification reports for the three different models.

```python
# Print the classification report for the original data
print(classification_report_imbalanced(y_test, rf_predictions))

# Print the classification report for the resampled data
print(classification_report_imbalanced(y_test, brf_predictions))

# Print the classification report for the resampled data
print(classification_report_imbalanced(y_test, rf_resampled_predictions))
```

Explain to the students that the final step in this exercise is to answer the following question:

* Does the model generated by using one of the imbalanced methods more accurately flag all the loans that eventually defaulted?

In your answer, explain the following points:

* Overall, both resampled models in this example perform better at identifying more of the eventual loan defaults.

* We can observe this by the increased recall for the “default” or “`1`” category in the two imbalanced models as compared to the original random forest model.

* Recall refers to how many loans that were actually in default that the model caught.

* A higher recall for this category means that the model will do a better job at making sure no potential defaults are missed.

 However, the higher recall for these two imbalanced models comes at a cost: a greater tendency to incorrectly flag a loan as a potential default. We can observe this through a lower precision for these two models.

* Precision answers the following question: of all those loans the model predicted as in default, how many of them actually were defaults?

* A lower precision value means that the model is making a lot of false positives—predicting a default when there isn’t one.

Highlight that this illustrates the critical decision point when using imbalanced versions of machine learning models.

* If you really care about identifying those faulty loans (or whatever you’re trying to predict), and the cost of failing to identify a faulty loan is very high, then an imbalanced model with lower precision might be best.

  * A bank can always find another business to lend to, but banks can lose a lot of money when a business defaults on a loan.

* If, on the other hand, you have a situation in which the costs of misclassification are the same either way—if failing to correctly identify a `1` has the same practical cost as failing to correctly identify a `0`—then we may be better off with the overall higher accuracy of a standard machine learning model.

Answer any questions before ending the class.

---

### End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
