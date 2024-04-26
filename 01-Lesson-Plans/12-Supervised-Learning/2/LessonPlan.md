## 12.2 Lesson Plan: Trees and Ensemble Learning

### Overview

In this class, the students will gain hands-on experience with random forests and ensemble methods such as bagging and boosting. They will also learn the benefits of using tree-based algorithms for classification problems.

This lesson also teaches students how to identify when they should use categorical data as a feature in a model.

### Class Objectives

By the end of the class, students will be able to:

* Deploy various machine learning models for classification, such as support vector machines (SVM), k-nearest neighbours, and random forests.

* Identify when categorical variables are useful for a machine learning algorithm.

* Perform feature engineering on categorical features and convert labels to numerical class representations.

* Recognise the type of business cases where decision trees and random forests are a suitable solution for classification problems.

* Demonstrate how random forests avoid overfitting and perform better than decision trees.

* Identify the pros and cons of tree-based algorithms.

* Understand the implications of overfitting and how boosting and bagging can help to deal with it.

* Apply Gradient Tree Boosting models in classification problems.

---

### Instructor Notes

* Today's class is focused primarily on teaching students how to use tree-based algorithms for classification problems. You'll start with an introduction to support vector machines (SVMs) but then shift to decision trees. You will then introduce students to ensemble Learning algorithms such as random forests and gradient boosted trees.

* Tree-based algorithms have a wide range of applications, but here we'll use them primarily for risk analysis scenarios.

* Some of the demos in this class will use a lot of memory to train the models, which may result in Jupyter throwing warning messages. Reassure the students that these warnings are typically not critical and can mostly be ignored.

* Overfitting is a common problem in machine learning. Cover this topic thoroughly to ensure that students understand its implications. The techniques they'll learn in this class will help students avoid overfitting.

### Slideshow and Time Tracker

* You can view the slides for this lesson on Google Drive here: [Lesson 12.2 slides](https://docs.google.com/presentation/d/1IlaZAsdiCexUa4ZiyduQBv99t9Nm7WfiKAIV0yHdvQk/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. [View instructions for these instructions](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 minutes)

This lesson introduces the students to tree-based algorithms and ensemble learners such as random forests and gradient boosted trees. The students will gain experience in applying this new family of machine learning algorithms to a variety of classification problems. They will also learn about the difficulties presented with imbalance classes and a solution to this problem, which will be explored further in the next class.

Open the slides and welcome the students to the class, and then highlight what they’ll learn today.

* Today, the students will learn about several new machine learning models, such as support vector machines (SVM), k-nearest neighbours, and random forests.

* The students will also be introduced to a new family of machine learning algorithms: tree-based algorithms. **Tree-based algorithms** are supervised learning methods that programmers and analysts mostly use for classifications and regression problems.

* This class will cover the following algorithms and methods:

  * Decision trees
  * Random forests
  * Weak learners
  * Ensemble methods

Answer any questions before moving on.

---

### 2. Instructor Do: Support Vector Machines (10 minutes)

This section introduces students to **support vector machines**.

**Files:**

[support_vector_machine.ipynb](./Activities/01-Ins_SVM/Solved/support_vector_machine.ipynb)

sklearn follows a common pattern of model-fit-predict, which allows machine learning engineers to train, test, and evaluate a variety of machine learning models. To illustrate this, we will look at a new model called a support vector machine, or SVM.

Use the following points to introduce SVMs to the students:

* **Support vector machines** are a widely applied model in fintech, especially for assessing credit risk and fraud detection. They are robust and have applications across many industries.

* An SVM takes a unique approach to classification by trying to find the best boundary that separates the data points. It can assign a class to the points on one side of the boundary and another class to the points on the other side of the boundary.

* The idea behind SVMs is that a dataset and its labels are projected into a higher dimensional space.

* You might be familiar with how a globe is projected onto a flat surface to create a map. SVMs do this in reverse. They take a flat map and project a globe.

* In this higher dimensional projection, we hope to find that the labels and features are clearly separated. This boundary's projection is called a **hyperplane**, and we can use it to classify the points.

* A hyperplane is a line that charts data points into their corresponding classes. All items to the left of the line belong to class A. Items to the right belong to class B.

* The goal with hyperplanes is to get the margin of the hyperplane equidistant to the data points for all classes. This distance is considered the margin of separation.

![margin_of_separation.png](Images/margin_of_separation.png)

* The data closest to/within the margin of the hyperplane are called support vectors, and they are used to define boundaries of the hyperplane.

* These points are sometimes the most difficult to classify because they live closest to the margin and could belong to either class.

![support_vectors.png](Images/support_vectors.png)

Open the provided notebook and import the following modules:

 ```python
  # Import Modules
  import pandas as pd
  import matplotlib.pyplot as plt
  from sklearn.model_selection import train_test_split
  from sklearn.datasets import make_blobs
  from sklearn.preprocessing import StandardScaler

* We will use a synthetic dataset generated by `make_blobs()`. Then, we’ll plot the features of this synthetic data in a scatter plot, varying the colour of each observation according to its `y` label value.

* With a low standard deviation value of `1.25` the clusters will have no overlap.

   ```

  ```python
  # Generate a test dataset
  X, y = make_blobs(
      n_samples = 500,
      centers = 2,
      random_state = 1,
      cluster_std = 1.25)

  # Convert ndarray to pandas datatypes
  X = pd.DataFrame(X)
  y = pd.Series(y)

  # Plot test data
  plt.scatter(
      x=X[0],
      y=X[1],
      c=y,
      cmap="bwr")

  plt.show()
  ```

Now, demonstrate the `SVC` model from `sklearn`.

* The SVC constructor supports a number of arguments, with the `kernel` argument being the most important. Provide students with a brief overview of the `kernel` argument and what kernelling is.

  * The `kernel` argument expresses the degree of dimensionality needed to separate the data into classes.

  * Communicate to students that we should use a linear `kernel` value for datasets with two classes. This will create a hyperplane that is a line. Non-linear data will result in a hyperplane that is an actual plane.

  * The `kernel` argument accepts a number of values. These are listed and explained below. Advise students to consult the [documentation](https://scikit-learn.org/stable/modules/svm.html#svm-kernels) on kernels to get additional detail on these parameter values.

    * **rbf** creates a non-linear hyperplane.

    * **linear** creates a linear, 2D hyperplane.

Using the `linear` kernel for this demonstration, we import the SVM classifier and declare a model, entitled `svm`:

  ```python
  # Instantiate a linear SVM model
  from sklearn.svm import SVC
  svm = SVC(kernel='linear')
  svm
  ```

* We can then split the dataset into testing and training sets before fitting the model.

* Once we have fit the model, we can use it to generate a set of predicted values.

  ```python
  # Split Data
  X_train, X_test, y_train, y_test = train_test_split(X, y)
  X_train.shape

  # Scale the data
  scaler = StandardScaler()
  X_scaler = scaler.fit(X_train)
  X_train_scaled = X_scaler.transform(X_train)
  X_test_scaled = X_scaler.transform(X_test)

  # Fit the data
  svm.fit(X_train_scaled, y_train)

  # Make predictions using the test data
  y_pred = svm.predict(X_test_scaled)
  ```

* The classification report shows that the model fits perfectly. We should expect this because the clusters did not overlap.

  ```python
  # Import Module
  from sklearn.metrics import classification_report

  # Print classification report
  print(classification_report(y_test, y_pred))
  ```

* We can generate a new synthetic dataset using a higher value for standard deviation. This results in a dataset that is not as easy for the model to classify.

* This new dataset will have one cluster with 1000 instances and another with only 100. This is an example of class imbalance since we have many more observations of one class compared to the other.

  ```python
  # Generate dataset with overlap by increasing standard deviation
  X, y = make_blobs(
      n_samples=[1000, 100],
      random_state=1,
      cluster_std=5)

  # Convert ndarray to Pandas datatypes
  X = pd.DataFrame(X)
  y = pd.Series(y)

  # Plot dataset
  plt.scatter(
      x=X[0],
      y=X[1],
      c=y,
      cmap="bwr")

  plt.show()
  ```

* Following the same pattern as before, we can split the dataset, fit the model, and generate a set of predicted values.

* The classification report shows that our SVM again performed well, but it had more trouble classifying this second dataset.

  ```python
  # Split data
  X_train, X_test, y_train, y_test = train_test_split(X, y)
  X_train.shape

  # Scale the data
  scaler = StandardScaler()
  X_scaler = scaler.fit(X_train)
  X_train_scaled = X_scaler.transform(X_train)
  X_test_scaled = X_scaler.transform(X_test)

  # Fit the data
  svm.fit(X_train_scaled, y_train)

  # Make predictions using the test data
  y_pred = svm.predict(X_test_scaled)

  # Print classification report
  print(classification_report(y_test, y_pred))
  ```

Ask students if they have any questions and then move on to the student activity.

### 3. Students Do: Support Vector Machines (15 min)

In this activity, students will build an SVM classifier to predict the loan status (approve or deny) for a set of input features.

Slack out the following files to the students.

**Files:**

[loans.csv](./Activities/02-Stu_SVM/Resources/loans.csv)

[Starter Code](./Activities/02-Stu_SVM/Unsolved/svm_loan_approver.ipynb)

**Instructions:**

[Instructions](./Activities/02-Stu_SVM/README.md)

### 4. Instructor Do: Review Support Vector Machines (15 min)

**Files:**

[Solution code](./Activities/02-Stu_SVM/Solved/svm_loan_approver.ipynb)

Open the solution and explain the following points.

* The SVM algorithm is an alternative to the logistic regression model for running classification engines. The SVM algorithm is often more accurate than other models.

* SVM models can be either 2D (linear) or multi-dimensional (poly). The `kernel` argument defines the dimension of the model.

  ```python
  # Instantiate a linear SVM model
  from sklearn.svm import SVC
  svm_model = SVC(kernel='linear')
  svm_model
  ```

* After we've created the model, we have to fit it with data.

  ```python
  # Fit the data
  svm_model.fit(X_train_scaled, y_train)
  ```

* The next step is scoring the model for accuracy.

  ```python
  # Score the accuracy
  print(f"Training Data Score: {svm_model.score(X_train_scaled, y_train)}")
  print(f"Testing Data Score: {svm_model.score(X_test_scaled, y_test)}")
  ```

* An accurate model can make precise predictions. We use the sklearn `predict` function to make predictions for the new data.

  ```python
  # Make predictions using the test data
  y_pred = svm_model.predict(X_test_scaled)

  results = pd.DataFrame({
      "Prediction": y_pred,
      "Actual": y_test
  }).reset_index(drop=True)

  results.head()
  ```

* The last step is to evaluate the model. As we did with the logistic regression model, we'll use the `confusion_matrix` and `classification_report` libraries to assess metrics and performance.

  ```python
  # Evaluate performance
  from sklearn.metrics import confusion_matrix
  confusion_matrix(y_test, y_pred)

  from sklearn.metrics import classification_report
  print(classification_report(y_test, y_pred))
  ```

**Bonus Question**: Ask students which model performed better in terms of accuracy, precision, and recall.

**Answer:** The SVM model performed better in terms of accuracy, precision, and recall.

Ask students if they have any remaining questions before moving on to the next section.

### 5. Instructor Do: Decision Trees (15 min)

This lesson introduces students to decision trees, which form the basis for the family of tree-based algorithms.

**Files:**

[credit_data.csv](./Activities/03-Ins_Decision_Trees/Resources/credit_data.csv)

[decision-trees.ipynb](./Activities/03-Ins_Decision_Trees/Solved/decision-trees.ipynb)

Explain to students that a family of supervised learning models, known as trees, provides an alternative to logistic regression and SVMs. To start, we will look at the basic tree model called a decision tree.

Introduce tree-based classifiers by covering the following points.

* Unlike logistic regression and support vector machines, decision trees are easy to audit, which is important for Finance applications. In other words, you can trace the decision logic throughout each step of the model to see how the model reached the final prediction. This may be critical if you need to justify a loan decision or other financial decision.

* In contrast to linear models, tree-based algorithms can map non-linear relationships in data. This is an important advantage of using trees.

* In linear models, the relationship among input variables can be represented as a straight line, while non-linear models have a different shape.

* Predicting the price of a house based on its size is an example of a linear problem. As a general rule, the size of the house is directly proportional to the price of the house.

* Predicting if a credit application is going to be fraudulent or not (i.e, an application created by someone other than the named applicant) is an example of a non-linear problem, due to the complex relationship between the input features and the output prediction.

* Decision trees encode a series of `True/False` questions.

* `True/False` questions can be represented with a series of if/else statements.

* There are some key terms/concepts that are important to know when working with decision trees:

  * **Root Node:** A node that is divided into two or more homogeneous sets and represents the entire population or sample data.
  * **Parent Node:** A node that is divided into sub-nodes.
  * **Child Node:** Sub-nodes of a parent node.
  * **Decision Node:** A sub-node that is split into further sub-nodes.
  * **Leaf or Terminal Node:** Nodes that do not split.
  * **Branch or Sub-Tree:** A subsection of the entire tree.
  * **Splitting:** The process of dividing a node into two or more sub-nodes.
  * **Pruning:** The process of removing sub-nodes of a decision node.
  * **Tree's Depth:** The number of decision nodes encountered before the algorithm makes a decision.

* Decision trees can become very complex and deep, depending on how many questions have to be answered. Deep and complex trees tend to overfit to the training data and do not generalise well to new data.

Open the provided notebook and live-code the following activity:

* We import the `tree` module from `sklearn` into the initial import cell because this module offers a decision tree implementation for classification problems.

  ```python
  from sklearn import tree
  ```

* One interesting way to analyse a decision tree is to visualise it. We import the following libraries to create a visual representation of the decision tree.

  ```python
  import pydotplus
  from IPython.display import Image
  ```

* Students should have already installed the [`pydotplus` package](https://anaconda.org/conda-forge/pydotplus). If not, they can install it in their virtual environments by executing the following command in the terminal. (Students who are having issues with the installation can skip this visualisation step.)

  ```bash
  conda install -c conda-forge pydotplus
  ```

* We load the `credit_data.csv` into a DataFrame called `df`.

  ```python
  # Loading data
  file_path = Path("../Resources/credit_data.csv")
  df = pd.read_csv(file_path)
  ```

* Once we've loaded the data into the `df` DataFrame, we then create the features and target sets. The features set `X` contains all the columns except the `credit_risk` column. The `credit_risk` column is stored in the target variable `y`. We set the index to be the `id` column.

  ```python
  # Split target column from dataset
  y = df['credit_risk']
  X = df.drop(columns='credit_risk')

  # Set Index
  X = X.set_index('id')
  ```

* Next, we need to one-hot encode the categorical variables with `get_dummies`.

  ```python
  # Encode the categorical variables using get_dummies
  X = pd.get_dummies(X)

  X.head()
  ```

Explain to students that to train and validate the decision tree model, we'll need to split the data into training and testing sets.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
```

To improve the algorithm's performance, we'll scale the features data using the `StandardScaler`. There is no need to scale the target data, since it contains the labels that we want to predict using the decision tree.

```python
# Creating StandardScaler instance
scaler = StandardScaler()

# Fitting Standard Scaler with the training data
X_scaler = scaler.fit(X_train)

# Scaling data
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)
```

* After we scale the features data, we can create and train the decision tree model.

  ```python
  # Creating the decision tree classifier instance
  model = tree.DecisionTreeClassifier()
  ```

* We train the model with the scaled training data.

  ```python
  model = model.fit(X_train_scaled, y_train)
  ```

* After fitting the model, we can make predictions by using the scaled testing data.

  ```python
  predictions = model.predict(X_test_scaled)
  ```

An interesting way to analyse a decision tree is to visualise it. We'll use the `pydotplus` library to create a visual representation of the final decision tree.

  ![Decision tree visualization](./Images/decision-trees-2.png)

* We can visualise the graph by using `export_graphiz`.

  ```python
  # Create DOT data
  dot_data = tree.export_graphviz(
      model, out_file=None, feature_names=X.columns, class_names=["0", "1"], filled=True
  )

  # Draw graph
  graph = pydotplus.graph_from_dot_data(dot_data)

  # Show graph
  Image(graph.create_png())
  ```

* We can save the image as a `PDF` or `PNG` for viewing or editing later.

  ```python
  # Saving the tree as PDF
  file_path = "../Resources/credit_tree.pdf"
  graph.write_pdf(file_path)

  # Saving the tree as PNG
  file_path = "../Resources/credit_tree.png"
  graph.write_png(file_path)
  ```

Explain that the size and shape of the tree indicates the complexity in the decision logic needed to solve the problem. For very complex data, decision trees can become very large and nested. This often leads to overfitting to the training data. In other words, the tree is very good at predicting classes for data it has seen, but not good at predicting classes for new data points.

However, there are tree-based models that are robust against overfitting. One of the most popular types is random forests, and we will cover those next.

Answer any questions before moving on.

---

### 6. Students Do: Predicting Fraudulent Loan Applications (10 min)

**Corresponding Activity:** [04-Stu_Predicting_Fraud](Activities/04-Stu_Predicting_Fraud)

In this activity, students will create a decision tree model to predict fraudulent loan applications.

**Files:**

* [preventing-fraud.ipynb](Activities/04-Stu_Predicting_Fraud/Unsolved/preventing-fraud.ipynb)

* [sba_loans_encoded.csv](Activities/04-Stu_Predicting_Fraud/Resources/sba_loans_encoded.csv)

**Instructions:**

* [README.md](Activities/04-Stu_Predicting_Fraud/README.md)

---

### 7. Instructor Do: Review Predicting Fraudulent Loan Applications (10 min)

**Files:**

* [preventing-fraud.ipynb (Solved)](Activities/04-Stu_Predicting_Fraud/Solved/preventing-fraud.ipynb)

As you live-code the solution, highlight the following details:

* We import the `tree` module from `sklearn` to create a decision tree model instance.

  ```python
  from sklearn import tree
  ```

* We import the following libraries to create the decision tree graph.

  ```python
  import pydotplus
  from IPython.display import Image
  ```

* Next, we load the data from the `sba_loans_encoded.csv` file into a Pandas DataFrame called `df_loans`.

  ```python
  file_path = Path("../Resources/sba_loans_encoded.csv")
  df_loans = pd.read_csv(file_path)
  ```

* After loading the data, we define the features and target sets.

  ```python
  # Define features set
  X = df_loans.copy()
  X.drop("Default", axis=1, inplace=True)

  # Define target vector
  y = df_loans["Default"].values.reshape(-1, 1)
  ```

* We split the data into training and testing sets using the `train_test_split` method from `sklearn`.

  ```python
  X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=78)
  ```

* To improve the algorithm's performance, we scale the features data using the `StandardScaler` method from `sklearn`.

  ```python
  # Create the StandardScaler instance
  scaler = StandardScaler()

  # Fit the Standard Scaler with the training data
  X_scaler = scaler.fit(X_train)

  # Scale the training data
  X_train_scaled = X_scaler.transform(X_train)
  X_test_scaled = X_scaler.transform(X_test)
  ```

Remind students that we don't scale the target data because it contains the classes that we want to predict with the decision tree.

* Once the data is scaled, we create the decision tree model and fit it with the training data.

  ```python
  # Create the decision tree classifier instance
  model = tree.DecisionTreeClassifier()

  # Fit the model
  model = model.fit(X_train_scaled, y_train)
  ```

* After fitting the model, we make some predictions using the testing data.

  ```python
  # Making predictions using the testing data
  predictions = model.predict(X_test_scaled)
  ```

* We can use the confusion matrix, accuracy score, and classification report to evaluate the model.

  ![Model's evaluation results](Images/preventing_fraud_review_1.png)

Explain to students that despite the model's high accuracy, this model is not predicting all the fraudulent loan applications, as can be seen from the precision and recall values. This is why it is important to include the classification report when evaluating a classification model.

Continue live-coding the review by creating the model graph using the `pydotplus` library. Highlight the following information.

```python
# Create DOT data
dot_data = tree.export_graphviz(
    model, out_file=None, feature_names=X.columns, class_names=["0", "1"], filled=True
)

# Draw graph
graph = pydotplus.graph_from_dot_data(dot_data)

# Show graph
Image(graph.create_png())
```

![Transaction tree graph](Images/transactions_tree.png)

* The tree is too deep, yet we can observe that only one subtree branches out.

* This phenomenon occurs when the target classes are imbalanced—there are too many examples of only one type of target class in the dataset.

* Having imbalanced target classes is a common problem in classification machine learning algorithms when there is a disproportionate ratio of observations in each class.

Explain to students that the next session will cover the use of other tree algorithms, such as ensemble learners, that are better at modelling imbalanced classes.

Answer any questions before moving on.

---

### 8. BREAK (15 min)

---

### 9. Instructor Do: Introduction to Ensemble Learning (10 min)

In this activity, students will be introduced to ensemble learning, weak learners, and random forests.

Navigate to the _Introduction to Ensemble Learning_ section of the slides. Highlight the following details.

* If we were to compare all the classification models we've used up to now, we'd find that some algorithms performed better than others, as expected.

  * Although some of the other algorithms performed worse, they were able to execute independently and classify labels with some degree of accuracy.

  * Explain to students that they will encounter algorithms that actually fail at learning adequately. These algorithms/classifiers are considered **weak learners**.

Communicate that weak learners are a consequence of limited data to learn from. This may mean there are too few features, or that the data provided does not allow for data points to be classified.

* Weak learners make predictions that are only a little better than random chance. Individually, their predictions of the relationship between inputs and targets are not very accurate.

Explain to the students that weak learners, despite their flaws, are still valuable in machine learning.

* Ask the students if they can guess how to make a weak learner perform more accurately?

  * **Answer:** We can boost weak learners with other algorithms for an ensemble learning approach.

* Tell the students that a decision tree can sometimes be classified as a weak learner. Ask students what the reason might be.

  * **Answer:** This happens when a decision tree has only one split (i.e., a stump).

* Some models combine many weak learners to create a more accurate and robust prediction engine. A single weak learner will make inaccurate and imprecise predictions. Combined weak learners can perform just as well as any other strong learner.

  * This type of learning is an example of ensemble learning. Ensemble models help improve accuracy and robustness and they decrease variance.

* Emphasize that weak learners need to be combined using a specific algorithm. Example algorithms include **GradientBoostedTree** , **XGBoost**, and **Random Forests**.

Continue the presentation by introducing the random forest algorithm. Highlight the following points.

* Instead of having a single, complex tree, a random forest algorithm will sample the data and build several smaller, simpler decision trees.

* In a random forest, each tree is much simpler because it is built from a subset of the data.

* These simple trees are created by randomly sampling the data and creating a decision tree for only that small portion of data. Each simple tree is a weak classifier because it is only trained on a small piece of the original data.

* By itself, any single tree is only slightly better than a random guess. However, many _slightly better than average_ small decision trees can be combined to create a strong classifier, which has much better decision-making power.

* Let's examine some of the benefits of the random forest algorithm.

  * It is robust against overfitting because each weak classifier is trained on different pieces of the data.

  * It is robust to outliers and non-linear data.

  * It runs efficiently on large databases.

Answer any questions before moving on.

---

### 10. Instructor Do: Random Forest (10 minutes)

**Corresponding Activity:** [05-Ins_Random_Forest](Activities/05-Ins_Random_Forest)

In this activity, students will learn how to implement a random forest using `sklearn`.

**Files:**

* [random-forest.ipynb](Activities/05-Ins_Random_Forest/Solved/random-forest.ipynb)

* [loans_data_encoded.csv](Activities/05-Ins_Random_Forest/Resources/loans_data_encoded.csv)

Explain to students that in this demo, you will use the loan applications encoded dataset presented previously. The goal of this demo is to predict fraudulent loan applications using a random forest.

Use the unsolved Jupyter notebook to live-code the solution while highlighting the following details.

* First, we import the `RandomForestClassifier` class from the `ensemble` module so we can use the random forest implementation from `sklearn`.

  ```python
  from sklearn.ensemble import RandomForestClassifier
  ```

* We load the data into a Pandas DataFrame, and then scale and split the data into training and testing sets.

Briefly review this code and continue to live-code the random forest implementation by highlighting the following points.

* To create the target vector `y` before scaling the data, we use the `ravel` method instead of `reshape` (as we did in the decision tree demo).

  ```python
  y = df_loans["bad"].ravel()
  ```

* When we create the random forest instance, we need to set two important parameters:

  ```python
  rf_model = RandomForestClassifier(n_estimators=500, random_state=78)
  ```

  * `n_estimators`: This tells the algorithm how many random forests to create. In general, a larger number makes the predictions stronger and more stable. However, a very large number can result in longer training time. A good approach is to start low and increase the number if the model performance isn't adequate.

    * A [research study](https://doi.org/10.1007/978-3-642-31537-4_13) suggests that we might use a range between `64` and `128` trees in a forest for initial modelling.

  * `random_state`: This parameter defines the seed used by the random number generator. It is important to define a random state when comparing multiple models.

* Once we create the random forest model, we fit it with the training data.

  ```python
  rf_model = rf_model.fit(X_train_scaled, y_train)
  ```

* Next, we make some predictions using the scaled testing data.

  ```python
  predictions = rf_model.predict(X_test_scaled)
  ```

* We evaluate the model by using a confusion matrix, the `accuracy_score`, and the `classification_report` from `sklearn.metrics`.

* The confusion matrix is composed of the `y_test` and the `results` vectors. The matrix shows how well the model predicts fraudulent loan applications.

  ```python
  # Calculating the confusion matrix
  cm = confusion_matrix(y_test, predictions)
  cm_df = pd.DataFrame(
      cm, index=["Actual 0", "Actual 1"], columns=["Predicted 0", "Predicted 1"]
  )

  # Calculating the accuracy score
  acc_score = accuracy_score(y_test, predictions)
  ```

  ![Random forest evaluation results](Images/random-forest-1.png)

After observing the results, we can conclude that this model may not be the best one for preventing fraudulent loan applications. Explain to students that there are several strategies that may improve this model, such as:

* Reducing the number of features
* Creating new features based on new data
* Increasing the number of estimators

Finally, explain to the students that a byproduct of the random forest algorithm is a ranking of feature importance (i.e., which features have the most impact on the decision).

* The `RandomForestClassifier` of `sklearn` provides an attribute called `feature_importances_`, where you can observe which features were the most significant.

  ![Feature importance](Images/random-forest-2.png)

* In this demo, we notice that the `age` of the person and the `month` of the loan application are the more relevant features.

* If we need to drop some features, analysing feature importance could help us to decide which features can be removed.

Answer any questions before moving on.

---

### 10. Students Do: Predicting Fraud with Random Forests (15 minutes)

**Corresponding Activity:** [06-Stu_Random_Forests](Activities/06-Stu_Random_Forests)

In this activity, the students will explore how to use the random forest algorithm to identify fraudulent loan applications. Students will use the `sba_loans_encoded.csv` file that they created previously to train the model.

**Instructions:**

* [README.md](Activities/06-Stu_Random_Forests/README.md)

**Files:**

* [fraud-random-forest.ipynb](Activities/06-Stu_Random_Forests/Unsolved/fraud-random-forest.ipynb)

* [sba_loans_encoded.csv](Activities/06-Stu_Random_Forests/Resources/sba_loans_encoded.csv)

---

### 11. Instructor Do: Review Predicting Fraud with Random Forests (10 minutes)

**Files:**

* [fraud-random-forest.ipynb](Activities/06-Stu_Random_Forests/Solved/fraud-random-forest.ipynb)

* [sba_loans_encoded.csv](Activities/06-Stu_Random_Forests/Resources/sba_loans_encoded.csv)

Go through the solution and highlight the following information.

* The data for this activity is the data that students used in the decision tree exercise. The preprocessing is the same.

* We create the random forest model instance and define `n_estimators = 500` and `random_state = 78`.

Explain to the students that defining the `random_state` parameter is important for comparing different models.

* Next, we train the random forest model with the training data.

  ```python
  rf_model = rf_model.fit(X_train_scaled, y_train)
  ```

* Once the model is trained and fit, we validate it by using the testing data.

  ```python
  predictions = rf_model.predict(X_test_scaled)
  ```

* We can evaluate the model using the confusion matrix, the `accuracy_score`, and the `classification_report` from `sklearn`.

  ![Random forest evaluation results](Images/stu-random-forest-1.png)

Explain to the students that this model´s accuracy is better than the accuracy of the decision tree model from the previous activity (`0.89`). By observing the improved accuracy, confusion matrix results, and the precision and recall values, we can conclude random forests are better for predicting fraudulent loan applications.

* We retrieve a measurement of each feature’s importance to the model by using the `feature_importances_` attribute, which displays the top 10 most important features.

  ![Top 10 important features](Images/stu-random-forest-2.png)

Finally, ask one or two students for their insights in the Analysis Questions sections. You can comment on the following for each question.

* **Question 1:** Would you trust this model enough to deploy it as a fraud detection solution in a bank?

  * **Sample Answer:** This model's accuracy is better if we used decision trees. If we want to deploy a fraud detection solution for bank loans, we would trust in random forests more than in decision trees.

* **Question 2:** What are your insights about the top 10 most important features?

  * **Sample Answer:** The term of the loan, the year it originated, and the total size of the loan seem to be the top three features when it comes to predicting the probability of default. Other factors also matter, including the location (ZIP code), the number of employees in the business, and whether or not the loan proceeds were used to create new jobs within the company.

Answer any questions before moving on.

---

### 12. Instructor Do: K-Nearest Neighbours (10 minutes)

**Files:**

[credit_data.csv](./Activities/07-Ins_KNN/Resources/credit_data.csv)

[knn.ipynb](./Activities/07-Ins_KNN/Solved/knn.ipynb)

In this section, you will introduce the **k-nearest neighbours** (KNN) algorithm for the purpose of supervised learning. This final activity for the day is part review and part new material. Highlight the following points:

* The k-nearest neighbors algorithm, which is often also referred to as k-NN or KNN, is a non-parametric supervised learning algorithm that classifies datapoints. 

  * We can choose to classify an unknown point by averaging the known label values around it.

  * Closer points are weighted so that they contribute more to the average than distant points.

Point out to students that the general idea behinb KNN bears some similarities to the k-means algorithm but that both approaches are different from each other (and the letter 'k' is coincidentally in both algorithms but has a different meanings in each one).

Open a new notebook and import the following modules:

 ```python
  # Import Modules
  import pandas as pd
  from pathlib import Path
  from sklearn.neighbors import KNeighborsClassifier
  from sklearn.model_selection import train_test_split
  from sklearn.metrics import confusion_matrix
  from sklearn.preprocessing import StandardScaler

We can apply this concept by using the labels of grouped data with the dataset containing credit application data and a bank's decision regarding the lending outcome. The target of the analysis is predicting `credit_risk`, a marker which indicates that a specific loan ended in default.


  # Read the CSV file into a Pandas DataFrame
  df = pd.read_csv(
      Path('../Resources/credit_data.csv')
  )
  df.head()
  ```

We split the target column from the dataset and then encode the categorical values.

  ```python
  # Split target column from dataset
  y = df['credit_risk']
  X = df.drop(columns='credit_risk')

  # Preview the data
  X[:5]

  # Print first five entries for target
  y[:5]
  ```

* Many of the columns contain categorical values that we will need to one-hot encode before we fit the model. We will again use Pandas `get_dummies()` to encode the values.

  * **Note**: We must use `get_dummies()` before the data is split into training and testing sets. Since one-hot encoding produces a vector that is the same size as the distinct categorical values, we can run into a problem if we encode after splitting.

```python
# Encode the categorical variables using get_dummies
X = pd.get_dummies(X)

# Preview the data
X.head()
```

* Tell the students that whenever we create dummy variables, we need to be careful about something known as the "dummy variable trap." If two variables are perfectly correlated, the algorithm can't tell which one of the variables caused the change in the dependent variable. You can use the two examples below to illustrate this problem.

  * **Perfect Positive Correlation**: Let's say that a person is lactose intolerant but is not aware of this condition. They eat cereal with milk every morning and then start to have digestive issues. Here, it would be impossible for a machine learning algorithm to identify milk as the culprit because the milk and cereal are always consumed together. We could run additional tests to disentangle the two variables by having the person consume only cereal (maybe with oat milk) on some days and only cow's milk on others. But with a given dataset, we often don't have the ability to run additional tests.

  * **Perfect Negative Correlation**: If a person loses weight by skipping lunch on alternate days and using that time to work out at a gym, our algorithm won't be able to tell whether the weight loss was caused by working out or by not eating lunch. Whenever the person worked out, they skipped lunch, and whenever the person didn't work out, they ate lunch.

* We can avoid this problem by dropping one of the variables, making that variable the reference or base case, and then estimating the effect when the other variables return 1.

* Mention to students that the `get_dummies` function has an argument specifically created for this purpose, which is 'False' by default: 'drop_first'.

Now, we split the data into the testing and training sets, and then check that the shapes are the same between the testing and training sets.

```python
# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

X_train.shape

X_test.shape
```

As we've experienced before, the `StandardScaler` available in `sklearn` provides an easy way to scale the data. We must first fit the scaler, and then use it to transform our datasets.

```python
# Scale the data
scaler = StandardScaler()
X_scaler = scaler.fit(X_train)
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)
```

Import the `KNeighborsClassifier` model, fit it, and generate the predicted labels.

* The `KNeighborsClassifier` model accepts the parameter `n_neighbors` which defines how many neighbours should be used in the averaging calculation. This is similar to setting the value of lowercase-k, where `k` identifies the number of segments in the dataset.

```python
# Instantiate the model with k = 3 neighbors
model = KNeighborsClassifier(n_neighbors=3)

# Train the model
model.fit(X_train_scaled, y_train)

# Create predictions
y_pred = model.predict(X_test_scaled)

# Review the predictions
y_pred
```

Ask students the following review question:

**Question:** How can we determine how well this model performs at predicting this dataset?

**Answer:** We can count the number of times it predicted each one of the labels right or wrong. A confusion matrix summarises these counts in a table. We can also evaluate the accuracy, precision and recall using the classification report.

  ```python
  # Print confusion matrix
  confusion_matrix(y_pred,y_test)

  # Print classification report
  print(classification_report(y_pred,y_test))
  ```

Answer any questions before moving on.

### 13. Students Do: K Nearest Neighbors (20 minutes)

In this activity, the students will use the provided dataset of a bank's telemarketing campaign. The bank's marketing partner ran the campaign, and the bank has labelled the customers that opened an account after receiving a phone call. Now, they want a model that will help them to identify customers so they can provide the marketer with a better list of potential customers in the future.

Slack out the following files to the students:

**Files:**

[bank.csv](./Activities/08-Stu_KNN/Resources/bank.csv)

[Starter code](./Activities/08-Stu_KNN/Unsolved/knn.ipynb)

**Instructions:**

[Instructions](./Activities/08-Stu_KNN/README.md)

### 14. Instructor Do: Review K-Nearest Neighbors (10 minutes)

**Files:**

[Solution code](./Activities/08-Stu_KNN/Solved/knn.ipynb)

Review the solution while highlighting the following points.

* We must encode the categorical variables before we split the testing and training sets.

  ```python
  # Encode the categorical variables using get_dummies
  X = pd.get_dummies(X)

  # Split the dataset
  X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
  ```

* After splitting the data, we must scale it before fitting it to the KNN model.

  ```python
  # Instantiate a StandardScaler instance
  scaler = StandardScaler()

  # Fit the training data to the standard scaler
  X_scaler = scaler.fit(X_train)

  # Transform the training data using the scaler
  X_train_scaled = X_scaler.transform(X_train)

  # Transform the testing data using the scaler
  X_test_scaled = X_scaler.transform(X_test)
  ```

* Using the model-fit-predict pattern, we create an instance of the `KNeighborsClassifier` module with an `n_neighbors` value of 3. Next, we fit the model using the `X_train_scaled` and `y_train` data. Finally, we generate the predicted values. The classification report helps us analyze how well the model performed.

  ```python
  # Instantiate the model with k = 3 neighbors
  knn = KNeighborsClassifier(n_neighbors=3)

  # Train the model
  knn.fit(X_train_scaled, y_train)

  # Create predictions
  y_pred = knn.predict(X_test_scaled)

  # Model metrics
  print(classification_report(y_test, y_pred))
  ```

Ask students if they have any questions about the `KNeighborsClassifier` module, or any of the topics introduced today, before ending the class.

—

### End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
