## 12.1 Lesson Plan: Supervised Learning

### Unit Overview

In this unit, the students will dive deeper into statistics and machine learning by working with supervised learning algorithms. This unit focuses on algorithms used for classification. **Classification** is the act of discovering whether a specific feature or element belongs to a feature class/group. Classification derives categorical conclusions (e.g., “Yes” or “No”, or “Great Credit” or “Bad Credit”) based on classified/modelled data.

**Supervised learning** connects the observable information in a system or scenario to the outcomes we want to predict. This involves using historical data of different outcomes (e.g., "Loan Defaulted" or "Loan Still Current") with the historical information connected to those outcomes (e.g., borrower has a credit score of 740+, or borrower has low existing debt). By the end of this unit, the students will be competent in the execution and evaluation of classification models, including logistic regression and decision trees. They will become proficient users of supervised learning approaches for predicting categorical conclusions and outcomes.

### Lesson Overview

Today's class will introduce the students to linear regression. In the latter part of the lesson, you'll demonstrate using a supervised learning model for classification (logistic regression), and how to evaluate whether a classification model is producing adequate results. In the process, the students will also learn how to use scikit-learn, a Python data science package, to train and evaluate models and make them more efficient and effective in determining probability/outcome predictions.

Before the end of class, encourage the students to continue researching and learning more about the various ways to implement classification models, especially models we couldn't cover here, such as neural networks. Be sure to slack out the following links as supplementary resources:

* [Ten Applications of AI to Fintech](https://towardsdatascience.com/ten-applications-of-ai-to-fintech-22d626c2fdac)

* [Types of Classification Algorithms](https://medium.com/@Mandysidana/machine-learning-types-of-classification-9497bd4f2e14)

* [FICO: Cognitive Fraud Analytics](https://www.fico.com/en/latest-thinking/product-sheet/fico-falcon-platform-cognitive-fraud-analytics-fraud-focused-machine-learning)

### Class Objectives

By the end of class, the students will be able to:

* Model and fit several supervised learning classification models (linear regression, logistic regression) using scikit-learn.

* Conceptualise and build training and test windows for supervised learning analysis.

* Define classification in the context of machine learning.

* Evaluate classification algorithms using a confusion matrix and classification report.

### Instructor Notes

* Today's class will require the students to train and evaluate multiple supervised learning models, including both continuous and classification-based problems. The content is heavy in statistical analysis and machine learning, so to keep the students engaged, you'll need to reinforce concepts with the provided fintech use cases. When appropriate, remind the students that classification models enable financial companies to make faster and smarter data-driven decisions and outcomes, such as:

  * Credit risk and worthiness

  * Money laundering and fraud identification

  * Investment returns

  * Loan recommendations

* The world of classification is vast, and we can't cover all forms and concepts in one class. Be aware of how long you are taking to explain concepts as you go through the lesson. The key is to stay rooted in real-world and practical examples of how classification can be used within fintech. Avoid getting bogged down in the statistical and mathematical detail for the algorithms. The focus should be on:

  * How each algorithm/model works and its fintech use case

  * How to train/enhance the algorithm/model

  * How to test algorithms/models and correctly handle false negatives and positives

* This unit’s activities use imbalance-learn and scikit-learn packages.

  * The students will need to install imbalanced-learn and scikit-learn to their Python environments before they attend class. There will be no time dedicated for in-class installation. The students can review the [classification ecosystem install guide](../Supplemental/Machine_Learning_Env_Setup_Guide.md) for steps on verifying that both packages have been installed correctly.

  * Slack out the following links for students to use as resources.

    * [imbalance-learn documentation](https://imbalanced-learn.org/stable/)

    * [scikit-learn documentation](https://scikit-learn.org/stable/)

    * [Classification ecosystem installation guide](../Supplemental/Machine_Learning_Env_Setup_Guide.md)

* Be sure to keep pace based on the times specified for each demonstration and activity. Invite the students to attend office hours if they need additional help. Due to their varying backgrounds, some students may be less familiar with statistical concepts, while others might have limited experience in the application of machine learning models.

  * Encourage the students to work with partners for all assignments to promote collaboration.

  * Remind the students that they must research and practice on their own to reinforce concepts and build competence in learning and evaluating trained models.

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 12.1 slides](https://docs.google.com/presentation/d/1OW1QeQruj6GUr3eKYc0vF3b5w3dLoxdpu3IXf9LqKm4/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to "File," selecting "Download," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. [Review the instructions for these steps.](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to "File" and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Introduction to Supervised Learning & Classification (15 minutes)

Begin this module with a brief introduction to Supervised Learning:

* In supervised learning, we take a set of known answers called labels and fit a model with a set of features (inputs) that corresponds to the labels. These models are called supervised learners.

* Supervised learning requires us to feed the correct answers to the model. The model learns from the data and the answers, and it becomes better at predicting the correct answer as we provide more data.

* Supervised learners generally fall into one of two broad categories: classification and regression.

Ask the class the following questions:

**Question**: What is regression?

**Answer**: Regression is a method for predicting a **continuous** valued variable. Continuous values are those that can always be divided into smaller pieces. Continuous variables, no matter how small, will have a middle that we can find. For example, a variable of distance is continuous. We can always find a smaller distance by dividing the current distance by half. In finance, prices and rates are usually continuous.

**Question**: What is classification?

**Answer**: Classification is a method to predict **discrete** valued variables. A discrete variable has no middle, and its values cannot be divided. For example, consider a loan application that asks if you own a car. The possible answers are yes or no. You either own a car or you don't. There is no middle value, so this type of variable, such as `car_ownership`, would be discrete.

Open the slideshow, and explain the following points:

* Explain that fintech analysts use classification to draw categorical conclusions about data. Instead of forecasting quantitative numbers, classification uses a binary (true-positive / true-negative) approach to predict membership in a category (i.e., will the outcome be of type A or type B).

  * For example, financial institutions can use classification models to identify a loan applicant as creditworthy or a credit risk.

* Tell the students that today they'll learn to perform classification using logistic regression. In the next class, they'll discover other tools for classification including support vector machines, decision trees, and random forests.

* Classification models have greatly improved the ability for organisations to properly classify applicants, predict market decline, and classify fraudulent transactions or suspicious activity.

  * Most large financial institutions use some form of machine learning to monitor and predict fraudulent activities. This is how banks know when to flag and decline transactions due to suspicion of fraud.

    * Ask the students if they have ever received a call from their bank because a transaction was flagged as fraudulent. Explain that the call was triggered by a probability prediction based on specific data that typically indicates fraud.

    * For example, FICO credit scoring currently uses a classification model for their cognitive fraud analytics platform. Classification models have allowed the financial industry to become more proactive. Outcomes can be predicted with a high degree of accuracy, which allows for more effective and efficient mitigation. Slack out the following link as an article of interest for students to review outside of class.

      * [FICO Falcon: Cognitive Fraud Analytics](https://www.fico.com/en/latest-thinking/product-sheet/fico-falcon-platform-cognitive-fraud-analytics-fraud-focused-machine-learning)

* Tell the students that their mission for the remainder of this week is to build and train robust classification models making predictions.

---

### 2. Instructor Do: Demo Homework (10 minutes)

This section introduces students to the Unit 12 homework. Allocate 5–7 minutes for an overview of the assignment and use the remaining time to answer any questions before moving on.

**Homework Instructions:** [README.md](../../../02-Homework/12-Supervised-Learning/Instructions/README.md)

Open the homework instructions and briefly review the subsections that comprise the assignment.

* Explain that this week's homework focuses on creating a classification model for predicting and categorising credit risk.

* The students will use multiple models to complete the homework, including linear regression and decision trees. Explain that these models are available in the `scikit-learn` package, which students used in Unit 10.

* The homework comprises two goals:

  * Create a classification model that will categorise credit risk.

  * Compare and contrast the various machine learning models for their ability to classify credit risk. Any model in the homework can generate a prediction, but we want to identify which model is more accurate and precise.

* Explain that data for this activity will be from a peer-to-peer lending service that is similar to [**Lending Club**](http://www.lendingclub.com). Peer-to-peer lending companies have large volumes of loan performance data that can be used to train machine learning algorithms for **classification**, and they use these models to help investors decide which loans to back, or guarantee. The students will use data points such as loan amount, interest rate, and loan balance to make predictions about credit risk.

* Note that the `imbalanced-learn` and `scikit-learn` tools are needed for completing the assignment. Emphasise that the students need to be sure that these tools are properly installed and functional.

Answer any questions about the assignment before moving on.

---

### 3. Instructor Do: Linear Regression (15 minutes)

**Corresponding Activity:** [01-Ins_Linear_Regression](Activities/01-Ins_Linear_Regression)

In this activity, the students will learn how to implement a linear regression model by using scikit-learn.

**Files:**

* [linear_regression.ipynb](Activities/01-Ins_Linear_Regression/Solved/linear_regression.ipynb)

* [salary_data.csv](Activities/01-Ins_Linear_Regression/Resources/salary_data.csv)

Open the lesson slides, and highlight the following information.

* **Linear regression** is a model for describing the relationship between a numerical response and one or more variables that explains that response.

* For example, if it's snowing outside, the amount of snow outside depends on factors such as the temperature, humidity, and geographical latitude and longitude of your house.

* In statistics and machine learning, the numerical response is known as the **dependent variable** because its value depends on other variables. These other variables that explain the dependent variable are known as **independent variables**.

  **Note:** In machine learning, we can use the term "features" for independent variables and the term "target variable" for the dependent variable.

* For now, we will explore simple linear regression, where we have one independent variable.

* The formula for a linear regression describes, or models, the relationship between variables `X` and `y`, where uppercase `X` represents the independent variable, and lowercase `y` represents the dependent variable.

* This linear relationship implies the following:

  * As `X` increases, `y` increases.

  * How fast `y` increases in relation to `X` is called the **slope**.

  * The slope is represented by the letter `b` in the formula.

  * The value of `y` when `X` is 0 is called the **y-intercept**. It is represented by the letter `a`.

* A linear regression is considered to be a supervised learning model because it can predict the value of `y` based on historical data.

Open the unsolved version of the provided Jupyter notebook, `linear_regression.ipynb`. Explain that you will demonstrate how to implement a simple linear regression model by using scikit-learn. Highlight the following points.

* For this demo, we will use a dataset on years of work experience and expected salary.

* Using the `LinearRegression` module of scikit-learn, we will predict the expected salary for a given number of years of experience.

* We start by importing the required libraries, as the following code shows:

  ```python
  # Import required libraries
  import numpy as np
  import pandas as pd
  import hvplot.pandas
  from pathlib import Path
  from sklearn.linear_model import LinearRegression
  ```

* Note that we have imported the `LinearRegression` module from scikit-learn in addition to the typical libraries that we use to import a CSV file into Pandas.

* Next, we load the salary data into a DataFrame and display some sample data, as the following code shows:

  ```python
  # Read salary data
  file_path = Path("../Resources/salary_data.csv")
  df_salary = pd.read_csv(file_path)

  # Display sample data
  df_salary.head()
  ```

  ![A screenshot shows the code followed by a DataFrame of salary data.](Images/12-1-salary-sample-data.png)

* Note that the DataFrame contains only two columns. The “years_experience” column represents the `X` (independent) variable, and the “salary” column represents the `y` (dependent) variable.

* Now we’ll plot the data by using the `scatter` function of hvPlot:

  ```python
  # Create a scatter plot with the salary information
  salary_plot = df_salary.hvplot.scatter(
      x="years_experience",
      y="salary",
      title="Expected Salary Based on Years of Experience"
  )
  salary_plot
  ```

  ![A scatter plot shows data about expected salary based on years of experience.](Images/12-1-salary-scatter-plot.png)

Ask the students the following question:

* **Question:** What is the relationship between these variables, based on the plot?

* **Answer:** There is a clear relationship between these variables. As the years of experience increase, the salary increases.

The plot contains a **best fit line** that depicts the trend of this relationship. Linear regression finds this line for us.

Explain to the students that you now will use scikit-learn to create a linear regression model to find the best fit line for this data. Highlight the following points.

* The linear regression model of scikit-learn can't take a Pandas Series directly as input data. We need to use the `reshape` Pandas function to reformat the independent `X` variable as a one-column array.

  ```python
  # Reformat data of the independent variable X as a single-column array
  X = df_salary["years_experience"].values.reshape(-1, 1)

  # Display sample data
  X[:5]
  ```

  ```text
  array([[1.1],
        [1.3],
        [1.5],
        [2. ],
        [2.2]])
  ```

* The `reshape` function receives as its parameters the number of rows and columns that we want to set. Using `-1` as the first parameter, we tell Pandas to reshape the data as an array with as many columns as there are elements in the Pandas Series. The second parameter, `1`, tells Pandas to reshape the data to a one-column array.

  ```python
  # The shape of X is 30 samples, with a single feature (column)
  X.shape
  ```

  ```text
  (30, 1)
  ```

* The dependent variable can remain a Pandas Series.

  ```python
  # Create an array for the dependent variable y
  y = df_salary["salary"]
  ```

* We can use the familiar model-fit-predict pipeline (that we used with other scikit-learn models) to create our linear regression model.

* We start by creating an instance of the `LinearRegression` model.

  ```python
  # Create a model with scikit-learn
  model = LinearRegression()
  ```

* Next, we fit the data into the model.

  ```python
  # Fit the data into the model
  model.fit(X, y)
  ```

  ```text
  LinearRegression()
  ```

* Once we fit the model, we can retrieve the slope and the y-intercept of the best fit line computed by the `LinearRegression` module.

  ```python
  # Display the slope
  print(f"Model's slope: {model.coef_}")
  ```

  ```text
  Model's slope: [9449.96232146]
  ```

  ```python
  # Display the y-intercept
  print(f"Model's y-intercept: {model.intercept_}")
  ```

  ```text
  Model's y-intercept: 25792.20019866871
  ```

* Using the regression model formula, we can predict the expected value for any given number of years of experience.

* For example, to predict the salary of a person with seven years of experience, our computation will be as follows:

  ```python
  # Display the formula to predict the salary for a person with 7 years of experience
  print(f"Model's formula: y = {model.intercept_} + {model.coef_[0]} * 7")

  # Predict the salary for a person with 7 years of experience
  y_7 = model.intercept_ + model.coef_[0] * 7

  # Display the prediction
  print(f"Predicted salary for a person with 7 years of experience: ${y_7:.2f}")
  ```

  ```text
  Model's formula: y = 25792.20019866871 + 9449.962321455074 * 7
  Predicted salary for a person with 7 years of experience: $91941.94
  ```

* Although it’s good to understand how to use the slope and the y-intercept to make predictions, making manual predictions can be tedious. A more efficient way is to use the `predict` function of the `LinearRegression` scikit-learn module.

* We’ll use the `predict` function of the linear regression model to make predictions by using the values of the `X` set.

```python
# Make predictions using the X set
predicted_y_values = model.predict(X)
```

* By using the `X` set to make salary predictions, we can test our model against the original data. We can also plot the best fit line that was computed by the `LinearRegression` module.

* Let's create a copy of the original data to create a new DataFrame that will contain the original and the predicted salaries:

  ```python
  # Create a copy of the original data
  df_salary_predicted = df_salary.copy()

  # Add a column with the predicted salary values
  df_salary_predicted["salary_predicted"] = predicted_y_values

  # Display sample data
  df_salary_predicted.head()
  ```

  ![An image shows the code and the new DataFrame of salary data.](Images/12-1-salary-predictions.png)

* Now, we can use hvPlot to create the best fit line plot.

  ```python
  # Create a line plot of the predicted salary values
  best_fit_line = df_salary_predicted.hvplot.line(
      x = "years_experience",
      y = "salary_predicted",
      color = "red"
  )
  best_fit_line
  ```

  ![An image shows the code and the best fit line plot](Images/12-1-salary-best-line.png)

* This line represents the predictions of the linear regression model for each value of years of experience. We'll overlay the best fit line on the scatter plot for further analysis.

  ```python
  # Superpose the original data and the best fit line
  salary_plot * best_fit_line
  ```

  ![An image shows the scatter plot and line plot.](Images/12-1-salary-scatter-line.png)

* The blue dots are a scatter plot of data points for the original data on years of experience versus salary.

* The red line is the best fit line. It represents the linear regression model.

* The distance between each data point and the best fit line is referred to as the **error**.

Use the slides to explain that the linear regression model is mathematically constructed to minimise the sum of all the errors after they have been squared.

Explain that one way to assess the accuracy of a linear regression model is to observe the errors. Highlight the following details.

* The **mean squared error**, or **MSE**, is the average of the square of the errors of the dataset. It is the variance of the errors in the dataset.

* The **root mean square error**, or **RMSE**, is the square root of the MSE. It is the standard deviation of the errors in the dataset.

* Low MSE and RMSE scores indicate a more accurate model.

* The correlation coefficient is a numerical description of the extent to which the two variables move together. It ranges from -1 to 1.

* **R2**, or **r-square value**, is the square of the correlation coefficient. It describes the extent to which a change in one variable is associated with the change in the other variable. It ranges from 0 to 1.

Return to the notebook to demonstrate how these metrics can be fetched from our linear model by using scikit-learn.

* scikit-learn provides these metrics as part of the `metrics` module. Let's import them into our notebook.

  ```python
  # Import relevant metrics from scikit-learn: score, r2, mse, rmse, std
  from sklearn.metrics import mean_squared_error, r2_score
  ```

* After importing the metrics from the `metrics` library, we can compute them for our model, as the following code shows:

  ```python
  # Compute the metrics for the linear regression model
  score = model.score(X, y, sample_weight=None)
  r2 = r2_score(y, predicted_y_values)
  mse = mean_squared_error(y, predicted_y_values)
  rmse = np.sqrt(mse)
  std = np.std(y)

  # Print relevant metrics.
  print(f"The score is {score}.")
  print(f"The r2 is {r2}.")
  print(f"The mean squared error is {mse}.")
  print(f"The root mean squared error is {rmse}.")
  print(f"The standard deviation is {std}.")
  ```

  ```text
  The score is 0.9569566641435086.
  The r2 is 0.9569566641435086.
  The mean squared error is 31270951.722280968.
  The root mean squared error is 5592.043608760662.
  The standard deviation is 26953.65024877583.
  ```

* For the linear regression model, the `score` and `r2_score` functions retrieve the same value. We can use either metric as a general measure of the model's accuracy—the closer to 1, the better.

* Remember that the RMSE is the square root of the mean squared error—the standard deviation of the errors. A low RMSE score means that the model fits well to the data.

* Ideally, the RMSE will not exceed the standard deviation of our salary data.

* The RMSE, or the standard deviation of the error, is 5592.04.

* The standard deviation of the salaries, calculated by `np.std()`, is 26953.65.

* The standard deviation exceeds the RMSE, indicating that the model may be useful. In other words, on average, there are smaller swings in the error than for the recorded salaries.

Summarise the key points of linear regression.

* It models data with a linear trend. Linear regression is not useful when the data does not follow a linear trend, e.g., exponential trends.

* Based on the `X` values, it predicts `y` values.

* Because linear regression doesn't do a good job of describing nonlinear patterns, we will cover techniques to model nonlinear data later in the course.

Answer any questions before moving on.

---

### 4. Students Do: Predicting Sales with Linear Regression (15 minutes)

**Corresponding Activity:** [02-Stu_Predicting_Sales](Activities/02-Stu_Predicting_Sales)

In this activity, the students will apply linear regression to predict sales based on historical data.

**Files:**

* [Instructions](Activities/02-Stu_Predicting_Sales/README.md)

* [predicting-sales.ipynb](Activities/02-Stu_Predicting_Sales/Unsolved/predicting-sales.ipynb)

* [sales.csv](Activities/02-Stu_Predicting_Sales/Resources/sales.csv)

---

### 5. Instructor Do: Review Predicting Sales with Linear Regression (10 minutes)

**Files:**

* [Instructions](Activities/02-Stu_Predicting_Sales/README.md)

* [predicting-sales.ipynb (Unsolved)](Activities/02-Stu_Predicting_Sales/Unsolved/predicting-sales.ipynb)

* [predicting-sales.ipynb (Solved)](Activities/02-Stu_Predicting_Sales/Solved/predicting-sales.ipynb)

* [sales.csv](Activities/02-Stu_Predicting_Sales/Resources/sales.csv)

Open the unsolved version of the provided Jupyter notebook. Live-code the solution and highlight the following information.

* After importing the required libraries, we load and plot the provided sales data, as the following code shows:

  ```python
  # Read the sales data
  file_path = Path("../Resources/sales.csv")
  df_sales = pd.read_csv(file_path)

  # Display sample data
  df_sales.head()

  # Create a scatter plot with the sales information
  sales_plot = df_sales.hvplot.scatter(
      x="ads",
      y="sales",
      title="Sales per Number of Ads"
  )
  sales_plot
  ```

  ![A screenshot shows the code and the resulting scatter plot.](Images/12-1-sales-data.png)

* By analysing the scatter plot, we can identify a linear trend between the number of ads and the sales. Let's use the linear regression model to find the best fit line and then make some predictions.

* The first step is to prepare the data. We’ll use the number of ads as our independent variable X. So, we use the `reshape` function to create the `X` set as a one-column array, as required by scikit-learn.

  ```python
  # Create the X set by using the `reshape` function to format the ads data as a single column array
  X = df_sales["ads"].values.reshape(-1, 1)
  ```

* Next, we use the sales data as our dependent variable to create the `y` set.

  ```python
  # Create an array for the dependent variable y with the sales data
  y = df_sales["sales"]
  ```

* After preparing the data, we use scikit-learn to build the linear regression model and display the model's formula.

  ```python
  # Create a model with scikit-learn
  model = LinearRegression()

  # Fit the data into the model
  model.fit(X, y)
  ```

  ```text
  LinearRegression()
  ```

  ```python
  # Display the slope
  print(f"Model's slope: {model.coef_}")
  ```

  ```text
  Model's slope: [81.34898394]
  ```

  ```python
  # Display the y-intercept
  print(f"Model's y-intercept: {model.intercept_}")
  ```

  ```text
  Model's y-intercept: 7764.796945240416
  ```

  ```python
  # Display the model's best fit line formula
  print(f"Model's formula: y = {model.intercept_} + {model.coef_[0]}X")
  ```

  ```text
  Model's formula: y = 7764.796945240416 + 81.34898393753775X
  ```

* Awesome! With a few lines of code, we created a model that we can make future sales predictions based on the number of ads.

Now, explain to the students that we’ll plot the best fit line for the sales prediction model, which will create a visual perspective of the model.

* First, we’ll use the `predict` function to make predictions by using the original data.

  ```python
  # Make predictions by using the X set
  predicted_y_values = model.predict(X)
  ```

* Next, to visualise the best fit line, we’ll create a new DataFrame with the original data and the predicted values.

  ```python
  # Create a copy of the original data
  df_sales_predicted = df_sales.copy()

  # Add a column with the predicted sales values
  df_sales_predicted["sales_predicted"] = predicted_y_values

  # Display sample data
  df_sales_predicted.head()
  ```

  ![A screenshot shows the code and the new DataFrame.](Images/12-1-sales-best-line-data.png)

* After creating the new DataFrame, we will use hvPlot to display the best fit line.

  ```python
  # Create a line plot of the predicted salary values
  best_fit_line = df_sales_predicted.hvplot.line(
      x = "ads",
      y = "sales_predicted",
      color = "red"
  )
  best_fit_line

  # Superpose the original data and the best fit line
  sales_plot * best_fit_line
  ```

  ![A screenshot shows the code and the best fit line.t](Images/12-1-sales-best-line-plot.png)

* We'll now use the model to predict the expected sales with 100 ads.

  ```python
  # Display the formula to predict the sales with 100 ads
  print(f"Model's formula: y = {model.intercept_} + {model.coef_[0]} * 100")

  # Predict the sales with 100 ads
  y_100 = model.intercept_ + model.coef_[0] * 100

  # Display the prediction
  print(f"Predicted sales with 100 ads: ${y_100:.2f}")
  ```

  ```predict
  Model's formula: y = 7764.796945240416 + 81.34898393753775 * 100
  Predicted sales with 100 ads: $15899.70
  ```

* Making manual predictions can be time-consuming, so we will use the `predict` function to make sales predictions for 100, 150, 200, 250, and 300 ads.

* By using NumPy, we’ll create a one-column array that contains the ad counts for which we're going to predict sales.

  ```python
  # Create an array to predict sales for 100, 150, 200, 250, and 300 ads
  X_ads = np.array([100, 150, 200, 250, 300])

  # Format the array as a one-column array
  X_ads = X_ads.reshape(-1,1)

  # Display sample data
  X_ads
  ```

  ```text
  array([[100],
        [150],
        [200],
        [250],
        [300]])
  ```

* Now, we will use the `predict` function to forecast the sales.

  ```python
  # Predict sales for 100, 150, 200, 250, and 300 ads
  predicted_sales = model.predict(X_ads)
  ```

* We'll create a DataFrame to visualise the forecasted sales. Note that we need to reshape the `X_ads` array as a one-row array. We do this using the `reshape` function, with `(1, -1)` as the parameters.

  ```python
  # Create a DataFrame for the predicted sales
  df_predicted_sales = pd.DataFrame(
      {
          "ads": X_ads.reshape(1, -1)[0],
          "predicted_sales": predicted_sales
      }
  )

  # Display data
  df_predicted_sales
  ```

  ![A screenshot shows the code and the DataFrame of predicted sales data.](Images/12-1-prediced-new-sales.png)

* Finally, we need to discover whether the model's predictions are trustworthy. We’ll use the `metrics` module from scikit-learn along with NumPy, as the following code shows:

  ```python
  # Import relevant metrics from scikit-learn: score, r2, mse, rmse, std
  from sklearn.metrics import mean_squared_error, r2_score

  # Compute the metrics for the linear regression model

  score = model.score(X, y, sample_weight=None)
  r2 = r2_score(y, predicted_y_values)
  mse = mean_squared_error(y, predicted_y_values)
  rmse = np.sqrt(mse)
  std = np.std(y)

  # Print relevant metrics

  print(f"The score is {score}.")
  print(f"The r2 is {r2}.")
  print(f"The mean squared error is {mse}.")
  print(f"The root mean squared error is {rmse}.")
  print(f"The standard deviation is {std}.")
  ```

  ```text
  The score is 0.9219961974942595.
  The r2 is 0.9219961974942595.
  The mean squared error is 1922652.7853956919.
  The root mean squared error is 1386.5975571144252.
  The standard deviation is 4964.6946616416735.
  ```

* After reviewing the metrics and observing that the score is `0.92`, we can initially trust the model. However, we should run the model for more data to observe if the model score increases.

Answer any questions before moving on.

---

### 6. Break (15 minutes)

---

### 7. Instructor Do: Making Predictions with Logistic Regression (15 min)

**Corresponding Activity:** [03-Ins_Logistic_Regression](Activities/03-Ins_Logistic_Regression)

In this activity, you will demonstrate the use of logistic regression to make linear predictions for categorical outcomes. Logistic regression will be new to the students, so this classification demo contains two parts: a brief explanation of training and testing datasets, and a more in-depth explanation of model fitting and execution.

#### Logistic Regression: Explanation

Go through the slideshow and highlight the following points.

* **Logistic regression** is a statistical method for predicting binary outcomes from data.

  * With linear regression, our linear model can provide a numerical output, such as a credit score ranging from 0 to 850. Logistic regression can translate that numerical value for credit score to a probability between 0 and 1. We could then label the two endpoints as “good credit” (a label of `1`) versus “bad credit” (a label of `0`). The logistic regression model can take in various data to predict how a borrower might be classified. Data related to credit risk could include the number of continuous on-time payments, number of accounts, and credit age.

* As shown in the following image, these predictions get converted into a probability of being “good credit.”

* For example, the model will classify a borrower as a "good credit" borrower when the probability, based on the data inputs, exceeds 50% (0.50).

* The range of probabilities, produced from these variables used for prediction, is shown by the black S-shaped curve in the image below. This is known as the prediction curve. Given information on any borrower, we can now make a prediction based on where their data sits upon this curve.

  ![logistic_1.png](Images/logistic_1.png)
  ![logistic_2.png](Images/logistic_2.png)

* How do we translate continuous data like payment history into a probability of “good credit” ranging from 0 to 1?

  *In any logistic regression model, a sigmoid function transforms our model’s predictions about the borrower into a single probability value. Here the probability ranges from 0% chance of good credit to 100% chance of good credit.

  * In short, a sigmoid function lets us put in any range of numbers, and the output will be a number which ranges only from `0` to `1` (i.e., the same range as a probability).

  ![sigmoid_1.png](Images/sigmoid_1.png)
  ![sigmoid_2.png](Images/sigmoid_2.png)

* Emphasize to the students that running a logistic regression model involves four steps, and we can apply these steps when running any machine learning model.

#### Steps in Logistic Regression Modeling

  1. Preprocess. This step consists of cleaning the data (such as removing rows with missing values) and splitting it into subsets for training and testing the model.

  2. Train. Training is when we use a large subset of our labelled data to teach the model to recognise classification patterns.

  3. Validate. In the validation step, we use a small subset of our labelled data to test how well the model is able to predict labels.

  4. Predict. Finally, we use our model to predict labels for unclassified data.

* We can use logistic regression to predict which category or class a new data point should go into.

Now, open the Jupyter notebook and go through the process of running logistic regression with scikit-learn (sklearn). Quickly review the following bullet points and emphasise that classification algorithms require data to be clustered into classes/groups.

#### Preprocessing

* Tell the students that to use a logistic regression model, the first step is always preparing the dataset for training the model. In order for a logistic regression model to learn on its own, you must give it data that is clustered in classes or groups.

  * For example, we can create two classes that represent credit risk: **low risk** (purple) and **high risk** (yellow). Then, we use logistic regression to classify new data points and credit applicants.

    ```python
    from sklearn.datasets import make_blobs

    X, y = make_blobs(centers=2, random_state=42)
    ```

    ![make-blobs.png](Images/make-blobs.png)

* Highlight to the students that we use the `random_state` parameter to preserve the state of the output from `make_blobs`. The value passed to `random_state` serves as a numerical bookmark for the dataset returned from `make_blobs`. The goal is to produce the same dataset, no matter how many times the code is re-ran. If `random_state` is not preserved, `make_blobs` would generate a new random dataset each time it is executed.

  * Reassure the students that the `random_state` argument will not prevent the `make_blobs` function from creating a randomised dataset. It just ensures that we can retrieve that same randomised dataset (using the parameter provided, e.g., 42).

  * This means that `X` and `y` will always be the same value as long as `random_state=42` is provided.

  * This helps ensure that we use the same dataset to train the model, even if the `make_blobs` function is re-executed.

  * If we don't provide the `random_state` parameter, our model will create a new randomised dataset every time that the process is run.

Explain to the students that, like all machine learning methods that we’ve seen so far, the first step in preprocessing involves cleaning the data, as well as (usually) standardising it. Point out that with this simulated data, these steps do not need to be done.

* Additionally, however, when it comes to supervised learning models, preprocessing the data involves splitting it  into **training** and **testing** datasets.

* We train the model and help it learn how to classify data by giving it the training subset. We then evaluate the models with the testing data.

* Doing this helps us make unbiased evaluations of the model, because we’ll find out how the model performs when classifying data that it’s never encountered before (the test data).

* The testing data should not be used in any way until after we have created and trained the model using the training data.

Introduce the `train_test_split` function from the scikit-learn library, and tell students that they will use it to automatically split data into training and testing data.

* The train_test_split function takes two parameters: the X data and the y data. The X data consists of the variables that the model will use to make predictions. The X variables are sometimes called the features. The y data is the variable that we want to predict, and it is sometimes called the target variable
.
The following code demonstrates how this works:

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    random_state=1,
    stratify=y
)
```

Run the code and explain each of the parameters in the train_test_split function:

* `X` corresponds to the data we are using to predict the classification, or the features.

* `y` corresponds to the labels or classifications or our data.

* The `random_state` parameter controls how the data are shuffled before the split. By setting this equal to a number, we can reproduce this exact shuffling process.

* Setting the `stratify` parameter equal to `y` will ensure that the proportions of our different labels will be the same in both our training and testing data subsets.

Now, preview one of the DataFrames, named `training_features`, that results from this function.

* Run the following code. Explain that we can check the index of this `X_train` DataFrame to verify that it only has some of the rows from the original `X` DataFrame. Later, we’ll use the `X_train` DataFrame to fit our model. Then, we'll then test how our model makes predictions by using the testing data that we kept separate.

```python
print(X_train.shape)
print(X_test.shape)
X_train
```

**Note**: If you have enough time, explain the following points to the students.

* Compare the number of rows in the `training_features` DataFrame, which should be 993, to the original number of rows, 1,324.

* Ask the students to explain the difference in the number of rows.

* **Answer** The scikit-learn `train_test_split` function used 75% of the original dataset for training the model (993 / 1,324 = 75%). Seventy-five percent is the `train_test_split` function's default setting.

* People commonly use 70 to 75% of the data for training. But by using the `train_size` parameter to `train_test_split`, you can set that proportion to anything from 0 to 1 (that is, 0% to 100%).

Ask a TA to slack out the following link to the `train_test_split` documentation:
[https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.htm](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)

#### Training the Model

As a transition to the next part of the demo, explain to students that after we've completed the preprocessing work, we can run the logistic regression model. Demonstrate and explain how logistic regression models are trained and executed.

* We implement a logistic regression by using the sklearn `LogisticRegression` class. This module is a part of the **linear model** package that developers often choose for running a linear regression. The object returned from the `LogisticRegression` class will be a **classifier** object, which is used to train, validate, and make predictions.

```python
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(solver='lbfgs', random_state=1)
classifier
```

  ![logistic_regression_class.png](Images/logistic_regression_class.png)

* After we create a logistic regression model, we can train and fit the model by using the `train` function provided by the `LogisticRegression` object.

* As we stated previously, classification is a form of supervised learning. The algorithm learns by processing the data we feed to it.

  ```python
  # Train the data
  classifier.fit(X_train, y_train)
  ```

  ![train_model.png](Images/train_model.png)

#### Validating the Model

After we train the model, we'll need to **validate** it by using both the training and the test datasets that we created earlier.

* However, we can't validate the model unless it has been given a numerical score.

* We use the sklearn `score` function to score the model based on how well it predicts outcomes in comparison to the actual outcomes (i.e., predicted y versus actual y). If the predictions are the same and the score is 1.0, the model is perfectly accurate. In general, the closer the score is to 1.0, the more accurate the model.

* Emphasize to students that we have to score the model using both the training data and the test data.

  * When we score with the training data, we compare the accuracy of the model against the data we used to create the model. In most cases, a model that has seen more training data will have a higher accuracy score.

  * When we score using the test data, we are giving the model data it has never encountered before. Testing using this test data is basically a trial run: it’s a way to gauge how accurately the model might make predictions in real life.

  * If the training score is significantly more accurate than the testing score (closer to 1.0), the model may be overtrained. Overtraining the model can result in **overfitting**, where the model has learned rules for predictions that apply mostly for the training dataset but not to the overall dataset. The goal is to have the scores as close to each other in accuracy as possible.

    ```python
    # Score the model
    print(f"Training Data Score: {classifier.score(X_train, y_train)}")
    print(f"Testing Data Score: {classifier.score(X_test, y_test)}")
    ```

    ![testing_model.png](Images/testing_model.png)

#### Predicting with the Model

Explain to the students how we can use the sklearn package to make logistic regression predictions.

* The **sklearn** `predict` function will, for the `X_test` data, predict which group these data points will fall into.

* We can save these test predictions to either a series or dataframe for further analysis.

* This allows us to see the actual predictions made from the data points in the test dataset.

```python
# Save a Series of these test predictions
predictions = classifier.predict(X_test)
# Display a Dataframe of test predictions and actual labels
pd.DataFrame({"Prediction": predictions, "Actual": y_test})
```

![predict_test.png](Images/predict_test.png)

* Another way to calculate the `score` for `LogisticRegression` is to use the `accuracy_score` function, as the following code shows.

```python
from sklearn.metrics import accuracy_score
# Display the accuracy score for the test dataset.
accuracy_score(y_test, predictions)
```

* The accuracy score tells us the model's percentage of correct predictions for the test data.

Once the model is proven to be accurate for both the training and test data, we can use it to make predictions using an entirely new dataset.

* Just as we can use `predict` to evaluate how well the model does on the test data, we can also use `predict` on any new data points which may be coming in.

* Here we generate a new data point to illustrate how `predict` can take in information about one new piece of data and produce a label for it.

  ```python
  # Generate a new data point (the red circle)
  import numpy as np
  new_data = np.array([[-2, 6]])
  plt.scatter(X[:, 0], X[:, 1], c=y)
  plt.scatter(new_data[0, 0], new_data[0, 1], c="r", marker="o", s=100)

  # Predict the class (purple or yellow) of the new data point
  predictions = classifier.predict(new_data)
  print("Classes are either 0 (purple) or 1 (yellow)")
  print(f"The new point was classified as: {predictions}")
  ```

  ![predict_new_data.png](Images/predict_new_data.png)

Ask the students if there are any questions before moving on. This was a heavy activity, so you should expect several questions. Try to answer one or two questions if time permits. Otherwise, ask students to save questions for review. Remind students that the steps for running a logistic regression model are as follows:

  1. Preprocess (i.e., centring)

  2. Train

  3. Validate

  4. Predict

After answering any remaining questions, explain that a common use in industry for these types of logistic regression models is in classifying potentially fraudulent transactions. Payment processors such as Visa regularly use such models to evaluate the likelihood that any given card swipe is unauthorised. Tell students that in the next activity, they’ll get a chance to practice building logistic regression models for just such a practical application.

---

### 8. Students Do: Predicting with Logistic Regression (20 minutes)

**Corresponding Activity:** [04-Stu_Logistic_Regression](Activities/04-Stu_Logistic_Regression)

In this activity, the students will see how logistic regression works on the real-world problem of fraud detection.

**Files:**

* [Instructions](Activities/04-Stu_Logistic_Regression/README.md)

* [predicting_fraudulent_transactions.ipynb (Unsolved)](Activities/04-Stu_Logistic_Regression/Unsolved/predicting_fraudulent_transactions.ipynb)

* [transaction_fraud_data.csv](Activities/04-Stu_Logistic_Regression/Resources/transaction_fraud_data.csv)

---

### 9. Instructor Do: Review Predicting with Logistic Regression (10 minutes)

**Files:**

* [Instructions](Activities/04-Stu_Logistic_Regression/README.md)

* [predicting_fraudulent_transactions.ipynb (Unsolved)](Activities/04-Stu_Logistic_Regression/Unsolved/predicting_fraudulent_transactions.ipynb)

* [predicting_fraudulent_transactions.ipynb (Solved)](Activities/04-Stu_Logistic_Regression/Solved/predicting_fraudulent_transactions.ipynb)

* [transaction_fraud_data.csv](Activities/04-Stu_Logistic_Regression/Resources/transaction_fraud_data.csv)

Open the unsolved version of the provided Jupyter notebook. Run the required imports and reading in of data, then live-code the remaining solution, beginning with the `value_counts` of the target variable:

```python

transaction_fraud_data["fraud"].value_counts()
```

Explain that the first step is to separate the data into training and testing data.

* We start the process of splitting the data by defining the `target` (the “fraud” column) and the `features` of the data (all the columns except “fraud”).

```python
# The target column should be the binary `fraud` column.
target = transaction_fraud_data["fraud"]

# The features column should be all of the features.
features = transaction_fraud_data.drop(columns="fraud")
```

* Next, we split the features and target data into `training_features`, `testing_features`, `training_targets`, and `testing_targets` datasets by using the `train_test_split` function:

* Note that since we didn’t specify a `train_size` or `test_size` parameter here, the default option is to use 75% of the data for training, and the remaining 25% for testing.

```python
training_features, testing_features, training_targets, testing_targets = train_test_split(features, target)
```

* With the train-test-split step completed, we declare a `LogisticRegression` model.

```python
logistic_regression_model = LogisticRegression(random_state=7)
```

* We fit the training data to the model, and then save the model.

```python
lr_model = logistic_regression_model.fit(training_features, training_targets)
```

* With the model now built, we make predictions about fraud by using the testing dataset, and save those predictions.

```python
testing_predictions = lr_model.predict(testing_features)

testing_predictions
```

* Finally, we evaluate model performance through the accuracy score.

* The accuracy score compares the percentage of loans in the test data which were correctly predicted by the model versus the actual values.

```python
accuracy_score(testing_targets, testing_predictions)
```

* For our test data, the accuracy looks extremely good: approximately 99% of the transactions in the test data (rounded to `1` here) were accurately categorized by the model.

Point out to students that based on `value_counts`, there were very few transactions in the data that were actually fraudulent. So, our model could have a high accuracy score by simply predicting all the transactions will be valid.

In future lessons, we'll discuss how to deal with this type of imbalanced class problem.

---

### 10. Instructor Do: Evaluating Logistic Regression Predictions (5 minutes)

In this activity, you will engage the students in a facilitated discussion for evaluating the results of logistic regression predictions. The focus of this activity will be the evaluation of diabetes predictions.

Open the slides, and highlight the following points.

* In this scenario, we have used a logistic regression model to predict if an individual has diabetes, based on a set of diagnostic metrics provided as a dataset. We evaluated the logistic regression model by using a scoring feature. This revealed that the model is somewhat accurate. However, can you trust that its predictions are correct?

  * Ask the students how sure they are that their models can actually predict diabetes.

    * **Answer** Seventy-five percent sure, as described by the scored accuracy.

  * Ask the students if anyone would feel comfortable giving the diagnosis of diabetes based on the predictions of the model. Why or why not?

    * **Answer** No. The prediction is not 100% accurate. There is room for error, as well as false positives.

  * Ask the students if they'd rather have a model that incorrectly flags diabetes for patients that didn't have the disease, or would you rather miss predicting the disease in some patients? What is better: the false-positive or false-negative?

    * **Answer** Neither option is preferred. Both leave opportunities for inaccuracy.

    * However, in the case of a model that incorrectly flags patients as having diabetes, we can use additional tests to refine the prediction and filter out individuals who do not have diabetes. This way, anyone with the potential of having the disease can be given the treatment and attention they need.

* The process of evaluating a model requires more than simply scoring/measuring the model for accuracy. In addition to **accuracy**, we must measure for **precision** and **recall**, both of which can be used to eliminate false positives and false negatives.

Answer any questions before moving on.

---

### 11. Instructor Do: Accuracy, Precision, Recall (10 minutes)

In this section, you will provide a formal lecture explaining how accuracy, precision, and recall relate to logistic regression models, as well as how to measure each metric.

Go to the section in the slides on accuracy, precision, and recall, and then highlight the following details:

* You should evaluate all statistical models for accuracy, precision, and recall. This is especially important for **classification** models because they are **binary decision problems**. Binary decision problems have two possible correct answers: True Positive and True Negative.

  * Inaccurate and imprecise models ultimately will return false positives and false negatives.

* Accuracy is a measure of how often the model is correct: the ratio of correctly predicted observations to the total number of observations. As stated earlier, we can evaluate the accuracy of a model by scoring the model using training and testing datasets. However, accuracy does not communicate how precise the model is.

  * Accuracy can be very susceptible to imbalanced classes. In the homework assignment, the number of good loans greatly outweighs the number of at-risk loans. In this case, it can be very easy for the model to only care about the good loans because that has the biggest impact on accuracy. However, we also care about at-risk loans, so we need a metric that can help us evaluate each class prediction.

  * **Calculation:** (TP + TN) / (TP + TN + FP + FN)

* Precision is the ratio of correctly predicted positive observations to the total predicted positive observations (i.e., of all the samples classified as having diabetes, how many actually have diabetes?).

  * Another example: For all the individuals who were classified by the model as being a credit risk, how many actually were a credit risk? Did we classify them comprehensively and correctly?

  * A similar example: For all the loans predicted to be in good standing, how many actually are? For the loans predicted to be at risk, are they actually at risk?

  * High precision relates to a low false-positive rate.

  * **Calculation:** TP / (TP + FP)

* Recall is the ratio of correctly predicted positive observations to all predicted observations for that class (i.e., of all of the actual diabetes samples, how many were correctly classified as having diabetes?). Did we classify all samples correctly, leaving little room for false negatives?

  * Another example: For all the individuals who are a credit risk, how many were classified by the model as being a credit risk?

  * High recall relates to a more comprehensive output and a low false-negative rate.

  * **Calculation:** TP / (TP + FN)

Encourage the students to consult the following [documentation](https://blog.exsilio.com/all/accuracy-precision-recall-f1-score-interpretation-of-performance-measures/) if they need any additional explanation of precision and recall and how they are calculated.

Use the remaining time to answer any questions about logistic regression models and evaluating predictions. Then, move on to the next activity.

---

### 12. Instructor Do: Confusion Matrix & Classification Report (10 minutes)

**Corresponding Activity:** [05-Ins_Classification_Models](Activities/05-Ins_Classification_Models)

In this section, you will provide students with a live demonstration of creating and using a confusion matrix and classification report to evaluate models for error.

**Files:** [confusion_matrix.ipynb](Activities/05-Ins_Classification_Models/Solved/confusion_matrix.ipynb)

Open the starter file, and then highlight the following discussion points while live-coding the steps of using a confusion matrix.

* We can use a confusion matrix to measure and gauge the success of a model. Confusion matrixes reveal the number of true negatives and true positives (actuals) for each categorical class and compare it to the number of predicted values for each class. These values are then individually summed by column and row. The aggregate sums are then compared to gauge accuracy and precision. If the aggregates match, the model can be considered accurate and precise.

  ![confusion_matrix_table.png](Images/confusion_matrix_table.png)

* Confusion matrixes are great because they describe the performance of the classification model. By looking at the confusion matrix, we can determine whether the model has been correctly trained to produce comprehensive, accurate, and precise predictions.

* For binary classifiers like the logistic regression classifier, a confusion matrix would measure the number of positive and negative predictions. These will then be compared to the actuals.

* So …  how do we get data loaded into a confusion matrix for model evaluation? Most models will come equipped with a confusion matrix module, like the sklearn `metrics.confusion_matrix` module. The function accepts two arguments, one dataset containing the predicted values and another containing the actual data points.

Transition to the live-coding part of the demo, and demonstrate how to use and interpret the sklearn `confusion_matrix` function.

* We import the `confusion_matrix` function into the Python environment from the `metrics` package.

* The output from analysing both datasets (predicted values and actual values) is a two-dimensional array. Columns reflect binary classes (high credit risk or low credit risk), and the rows represent the number of samples/data points that actually belong to that class.

  ```python
  from sklearn.metrics import confusion_matrix
  confusion_matrix(y_test, predictions)
  ```

  ![confusion_matrix.png](Images/confusion_matrix.png)

Let the students know that they can also use a ***classification report** to evaluate a model. A classification report holds the test results so we can assess and evaluate the number of predicted occurrences for each class. Remember that when we evaluate a model, we have to assess its accuracy, precision, and recall to ensure the rates of false-positives and false-negatives are minimal.

* Classification reports calculate the precision, recall, and f1 score (accuracy in relation to precision and recall). We can generate them using the sklearn `metrics.classification_report` module. All that we need to execute the `classification_report` function is the actual data points and predicted data points.

  * The classification report will automatically calculate precision, recall, and accuracy.

    ```python
    from sklearn.metrics import classification_report
    target_names = ["Class Purple", "Class Yellow"]
    print(classification_report(y_test, predictions, target_names=target_names))
    ```

    ![classification_report.png](Images/classification_report.png)

Answer any questions before moving on.

---

### 13. Students Do: Evaluating Classification Models (20 minutes)

In this activity, the students will practice building and interpreting classification reports and confusion matrixes on consumer usage data for a financial app.

**Instructions:**

* [Instructions](Activities/06-Stu_Classification_Models/README.md)

**Files:**

* [lets-get-this-snowball-rolling.ipynb (Unsolved)](Activities/06-Stu_Classification_Models/Unsolved/lets-get-this-snowball-rolling.ipynb)

* [usage_stats.csv](Activities/06-Stu_Classification_Models/Resources/usage_stats.csv)

---

### 14. Instructor Do: Review Evaluating Classification Models (10 minutes)

**Instructions:**

* [Instructions](Activities/06-Stu_Classification_Models/README.md)

**Files:**

* [lets-get-this-snowball-rolling.ipynb (Unsolved)](Activities/06-Stu_Classification_Models/Unsolved/lets-get-this-snowball-rolling.ipynb)

* [lets-get-this-snowball-rolling.ipynb (Solved)](Activities/06-Stu_Classification_Models/Solved/lets-get-this-snowball-rolling.ipynb)

* [usage_stats.csv](Activities/06-Stu_Classification_Models/Resources/usage_stats.csv)

Open the starter notebook, read in the data and import the required packages, and then live-code the solutions:

* The first step in any ML analysis is to split the data into X and y, and then create testing and training sets.

```python
y = customer_df['target']
X = customer_df.drop(columns=['target'])
X_train, X_test, y_train, y_test = train_test_split(X, y)
```

* Next, we fit a logistic regression classifier.

```python
logistic_regression_model = LogisticRegression(random_state=9)
lr_model = logistic_regression_model.fit(X_train, y_train)
```

* Now that we have fit the model, we create the predicted values for the testing and the training data.

```python
training_predictions = lr_model.predict(X_train)
testing_predictions = logistic_regression_model.predict(X_test)
```

* After saving the predictions, we can print a confusion matrix, starting with the training data:

```python
from sklearn.metrics import confusion_matrix
training_matrix = confusion_matrix(y_train, training_predictions)
print(training_matrix)
```

* Then, we can print a confusion matrix for the testing data.

```python
test_matrix = confusion_matrix(y_test, testing_predictions)
print(test_matrix)
```

* Next, we can generate a training classification report that tells us the accuracy, recall, and precision for the training dataset:

```python
training_report = classification_report(y_train, training_predictions)
print(training_report)
```

* We create a classification report on the test dataset the same way.

```python
testing_report = classification_report(y_test, testing_predictions)
print(testing_report)
```

* How does the model performance of the training data and the testing data compare?

* Here, it appears that model performance declined slightly on the test data.

Emphasise to students that this relative decline on the test dataset is to be expected in most ML models. Remember that the model is evaluating that it has not encountered previously. If we're still getting strong precision and recall on the test dataset, this is a good indication about how well the model is likely to perform in real life.

Answer any questions before ending the class.

---

### End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
