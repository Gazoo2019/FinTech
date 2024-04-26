# Module 12 Credit Risk Report

## Overview of the Analysis

* **Purpose of the analysis** - The goal of this analysis to determine if the Logistic Regression machine learning model can more accurately predict healthy loans versus high-risk loans using the original dataset or a dataset that is resampled to increase the size of the minority class.

* **The Dataset** - The dataset used to perform the analysis consists of information on 77,536 loans. The data includes columns for  loan_size, interest_rate, borrower_income, debt_to_income ratio, number_of_accounts, derotatory_marks, total_debt, and loan_status. The category that we are attempting to predict with our analysis is **loan_status**. The data provided in the remaining columns will be used as features to train the data and inform the predictions. 


* **Class Distribution** - Based on the information provided from the value_count function, of the 77,536 total loans, 75,036 are categorized as healthy (Class 0), and 2500 are categorized as unhealthy (Class 1). This is a very imbalanced distribution, which is why we will use the RandomOverSampler in one of the machine learning models.

* **Stages of the Machine Learning Process** - The stages of the machine learning process are very scripted. If followed in order, they provide you with an accurate assessment of the model's ability to make predictions. The stages of the machine learning process are as follows:

    - Prepare the data - Import the file, establish the DataFrame, evaluate the class counts. If necessary, as in this case, resample the data. We will be using RandomOverSampler from imbalanced-learn to increase the size of our minority class.
    
    - Separate the data into features and labels - The labels are what you are attempting to predict, is the status of the loan healthy (0) or high-risk (1). The features are all of the remaining data you will use to train and test the model.
    
    - Use the train_test_split function to separate the features and labels data into training and testing datasets. 
    
    - Import the machine learning model from the library - In this instance, we will be importing LogisticRegression from SKLearn. 
    
    - Instantiate the model.
    
    - Fit the model using the training data.
    
    - Use the model to make predictions using the features test data.
    
    - Evaluate the predictions - Evaluations are done by calculating and comparing metrics like accuracy score, a confusion matrix, and a classification report.
    
* **Machine Learning Methods Utilized** - 

    The primary models used in this analysis are:

    - LogisticRegression model from SKLearn
    - RandomOverSampler from imbalanced-learn
    
    Supporting functions used in this analysis are:
    
    - train_test_split from SKLearn
    
    Models are evaluated using the following 3 functions:
    
    - balanced_accuracy_score from SKLearn
    - confustion_matrix from SKLearn
    - classification_report_imbalanced from imbalanced-learn

## Results

Using bulleted lists, describe the balanced accuracy scores and the precision and recall scores of all six machine learning models.

* Machine Learning Model 1 - Logistic Regression on the original data:
  
  - Accuracy score: 0.952048
  - Precision: Class 0: 1.00 Class 1: 0.85
  - Recall: Class 0: 0.99 Class 1: 0.91
  
* Machine Learning Model 2 - Logistic Regression on the resampled data:

  - Accuracy score: 0.993678
  - Precision: Class 0: 1.00 Class 1: 0.84
  - Recall: Class 0: 0.99 Class 1: 0.99

## Summary

Overall, both Logistic Regression models performed well, especially regarding predicting the outcomes for Class 0 (healthy loans). For the 0 class, both the precision and the recall were extremely close to perfect under both the original and oversampled data models.

For the 1 class (high-risk loans), the value associated with the model's precision is virtually identical between the model using oversampled data (0.84) and the original data (0.85). The recall number, however, is much higher for the logistic regression model using oversampled data at 0.99 versus the model using the original data at 0.91. 

Given this information, it appears that the Logistic Regression model created using oversampled data does a great job at predicting both healthy and high-risk loans, given the features that are used to train the data. 

Although the logistic regression model trained on the oversampled data appears to be promising, it would need to be evaluated against different data sets to confirm that it should be put into use for predicting the health status of loans.