## 13.3 Lesson Plan: Advanced Topics in Neural Networks

### Overview

Today's class completes the students' journey into neural networks by introducing them to more advanced concepts around model development and management. We will first examine the problem of overfitting and steps for identifying and preventing it. The class also provides an overview of next steps for students who want to further explore neural networks.

This lesson begins with more advanced, but essential, concepts in neural networks and machine learning. During the section on overfitting, the students will be introduced to ROC/AUC (receiver operating characteristics/area under the curve), evaluation methods that are appropriate for binary classifier neural networks. ROC/AUC usually involve comparisons of multiple models or variations of one model, so the students will learn how to save different iterations of models locally, for later use. Finally, they’ll learn about a concept called transfer learning, which builds upon model saving. The students will learn to load save models and selectively re-train only certain components of that existing neural network on new data.

### Class Objectives

By the end of this lesson, the students will be able to:

* Save and redeploy previously fit models.

* Describe the problem of overfitting and implement code that can mitigate it.

* Acquire resources for more advanced aspects of deep learning that are beyond the scope of today's class.

### Instructor Notes

* **Important:** Slack out the [Deep Learning Installation Guide Folder](../../13-Neural-Networks/Supplemental/Deep_Learning_Installation_Guide) for installing Tensorflow prior to today's class. The students should install these tools before class to conserve time for lessons and activities.

* **VERY Important:** Some machines will not install or run Tensorflow due to hardware incompatibilities. This is most prevalent for Apple Silicon M1 computers. The simplest solution is to have these students run their notebooks in [Google Colab](https://colab.research.google.com/) which comes with support for TensorFlow. Generally, the notebook can be uploaded and run in Colab without any changes. Where changes are necessitated, specific Colab compatible notebooks have been included in the activity files.

* Allow the students to ask questions, and when necessary, ask them to save questions for the review sessions or office hours.

### Class Slides and Time Tracker

You can view the slides for this lesson on Google Drive here: [Lesson 13.3 slides](https://docs.google.com/presentation/d/1hrzNfSY0o9QexeaZ2ywsCre3kbLqNZSDvbrVO8p9ufk/edit?usp=sharing).

To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

Note: Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy."

You can view the time tracker for this lesson here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome the Class (5 min)

Welcome the students to the third day of the deep learning unit! Cover the following:

* In this lesson, we will explore some common techniques for optimizing neural network models. These techniques span all elements of building a neural network: data processing, model design and saving, and making models more robust by avoiding overfitting.

* The technology behind neural networks is relatively new, and techniques for optimizing neural network performance are evolving as data scientists conduct further research.

* There is no infallible approach to designing an optimal neural network, but we can apply some guidelines and best practices to find the most suitable model for a particular problem.

---

### 2. Instructor Do: Overfitting (10 min)

Use the slides and go through the following concepts related to overfitting.

#### What Is Overfitting?

Explain the following:

* **Overfitting** results from attempting to model the training data too precisely.

* Deep neural networks are beneficial because they can discover subtle, complex patterns in data that other models often can't find.

* However, there's a limit to what we can learn about the data. Random things that are unlikely to repeat—coincidences—can occur in the training data.

* If we have a model that perfectly fits the training data, the model probably won't perfectly fit any future data that it encounters.

* Sometimes, a complex model that is extremely well fit on the training data will perform worse on new data than a simpler model that used the same training data.

#### Techniques to Reduce Overfitting

* The most effective techniques to reduce overfitting in neural networks involve the following concepts:

  * Dropout
  * Regularization
  * Use of a Validation Set

* **Dropout** is when we cut connections at random in the neural network when it's training. This is similar to when we "forget on purpose." The model finds certain relationships but disregards them.

  * No one fully understands why this works. However, dropout has become a proven method across a wide variety of data to reduce overfitting.

* **Regularization** involves cutting or downplaying specific (not random) connections, depending on their importance. The less impact that a connection has, the greater chance it will be minimized or eliminated.

* A **validation set** is an additional dataset that we do not use for training the model. It’s similar to the test dataset. By monitoring the model's performance on the validation set as we continue to train the model, we can observe any increasing risk of overfitting.

Next, we’ll introduce each of these three concepts in more detail and demonstrate the code in Keras.

#### Dropout

* We add dropout as a layer, similar to other Sequential layers.

#### Regularization

* We add regularization as a parameter to any existing layers.

#### Validation Set

* We add a `validation_split` parameter when we `fit` our model, so we can track and save the performance on this additional dataset. Once we fit the model, we can then visualize performance differences between the validation and training datasets.

---

### 3. Instructor Do: Overfitting—Coding Demo (10 min)

**Corresponding Activity:** [01-Ins_Overfitting](./Activities/01-Ins_Overfitting)

Explain that, in many cases, and especially with financial data, models can overfit training data and end up with reduced performance in real life. This demonstration shows various techniques to help reduce overfitting and make models more robust.

**Files:**

* Solved:
  * [ins_overfitting.ipynb](./Activities/01-Ins_Overfitting/Solved/ins_overfitting.ipynb)
  * [Colab_ins_overfitting.ipynb](./Activities/01-Ins_Overfitting/Solved/Colab_ins_overfitting.ipynb)

* Unsolved:
  * [ins_overfitting.ipynb](./Activities/01-Ins_Overfitting/Solved/ins_overfitting.ipynb)
  * [Colab_ins_overfitting.ipynb](./Activities/01-Ins_Overfitting/Solved/Colab_ins_overfitting.ipynb)

#### Preparing the Data

Open the notebook and explain that we're going to revisit the data from the activity on predicting earnings.

* Our data for the quarterly earnings per share for US companies is continuous. To convert the data to categorical, we group it into buckets.

* This type of categorical conversion enables us to force the dependent variable to be balanced. Because the data is divided evenly into five groups, each category contains approximately the same number of observations (after accounting for ties).

* As you write the following code, point out to students that we could also use the `EPS` earnings data directly. Our "binning" approach is another method that is sometimes used to limit overfitting by reducing the impact of outliers.

  ```python
  # Create a balanced `y` categorical variable
  # Use qcut to group earnings results into 5 buckets
  df['earnings_quantile'] = (pd.qcut(df['EPS'], q=5, labels=False))+1
  # Verify buckets are approximately balanced
  # (Slight imbalance from ties is OK)
  df['earnings_quantile'].value_counts()
  ```

* The following code should be a refresher from the previous day, so it's OK to go through it quickly:

  ```python
  # Save bucket ("quantile") value as the new  `y` variable
  y_quantile = df['earnings_quantile']

  # Save the unique count of categories for later use
  number_of_classes = len(y_quantile.unique())

  # Encode quantiles into labels
  encoder = LabelEncoder()
  encoder.fit(y_quantile)
  encoded_y = encoder.transform(y_quantile)

  # Encode labels into categories
  y_categorical = to_categorical(encoded_y, num_classes=number_of_classes)

  # Split into training and testing windows
  X_train, X_test, y_train, y_test = train_test_split(X, y_categorical, random_state=1)

  # Preview the `y_train` values
  y_train

  # Save the count of unique predictor variables for use in model
  number_of_predictors = len(X.columns)
  len(X.columns)
  ```

#### Building the Model

The next step contains new material for the students. Start live-coding as you explain the following concepts.

* Building a model that can avoid overfitting is similar to building a regular model, with two additions.

  * We'll add a `Dropout` layer(s).

  * We'll also **regularize** existing layers, using `kernel_regularizer` and `bias_regularizer` as additional parameters into existing layer(s).

    ```python
    # Build the model
    # Import the Dropout layer
    from keras.layers import Dropout
    # Import regularizers
    from keras.regularizers import l1, l2

    # Build the Model
    model = Sequential()
    # Add a dense layer (as before)
    model.add(Dense(10, input_dim=number_of_predictors, activation='relu'))
    # Now add a Dropout layer
    model.add(Dropout(.2,input_shape=(10,)))
    # Add regularization to another dense layer
    model.add(Dense(5, activation='relu', kernel_regularizer=l2(0.01), bias_regularizer=l2(0.01)))
    # Add the final output layer
    # (Set the # of possible outputs equal to the number classes)
    model.add(Dense(number_of_classes, activation='softmax'))

    # Compile the model (as before)
    model.compile(loss="categorical_crossentropy",
                  optimizer= "adam",
                  metrics=['categorical_accuracy'])
    ```

* When we fit this model, we can also include a validation set to help avoid overfitting.

* We fit the model with a large number of epochs, and we observe the incremental performance on the validation set as the number of epochs increases.

  ```python
  # Add in validation loss to select the number of epochs
  # Fit the model
  number_of_epochs = 50
  model.fit(X_train,y_train,
                      epochs=number_of_epochs,
                      batch_size=1000,
                        validation_split=0.2,
                      shuffle=True)
  ```

* When performance on the validation set levels off, we stop the training, reduce the number of epochs to that specific leveling off point, and then refit the model.

* To check validation performance, we save the model's performance across epochs by recalling the model's `history`.

  * The `keys` attribute returns a dictionary:

    ```python
    # Save model history across epochs
    model_history = model.history.history
    model_history.keys()
    ```

    ![model_keys_preview.png](Images/model_keys_preview.png)

* Because our data is categorical, we'll measure performance by comparing `categorical_accuracy` between the training and validation datasets.

  ```python
  # View `categorical_accuracy` for the training dataset
  model_history['categorical_accuracy']
  ```

* If we save categorical accuracy for both the training and validation data to a DataFrame, it'll be easier to plot:

  ```python
  # Save accuracy for training and validation set across epochs
  training_results = pd.DataFrame(index=range(1,number_of_epochs+1))
  training_results['Training'] = model_history['categorical_accuracy']
  training_results['Validation'] = model_history['val_categorical_accuracy']
  training_results.plot(title = 'Performance Across Training and Validation')
  ```

  ![Plot of performance across training and validation.](Images/performance_across_training_validation.png)

Point out to students how accuracy continues to increase on the training dataset but flattens out on the validation set.

* Leveling off is an indication of overfitting. To prevent this, we should refit our model and then stop training after approximately 30 epochs instead of our original choice of 50.

---

### 4. Student Do: Overfitting (20 min)

**Corresponding Activity:** [02-Stu_Overfitting](Activities/02-Stu_Overfitting)

In this activity, the students will build a neural network and apply various techniques to prevent overfitting.

**Instructions:**

* [README.md](Activities/02-Stu_Overfitting/README.md)

**Files:**

* [Instructions](Activities/02-Stu_Overfitting/README.md)

* [overfitting.ipynb (Starter Code)](Activities/02-Stu_Overfitting/Unsolved/claims_overfitting.ipynb)
* [Colab_overfitting.ipynb (Starter Code)](Activities/02-Stu_Overfitting/Unsolved/Colab_claims_overfitting.ipynb)

---

### 5. Instructor Do: Review Overfitting (10 min)

**Files:**

* [Instructions](Activities/02-Stu_Overfitting/README.md)

* Solved:
  * [overfitting.ipynb (Solutions Code)](Activities/02-Stu_Overfitting/Solved/claims_overfitting.ipynb)
  * [Colab_overfitting.ipynb (Solutions Code)](Activities/02-Stu_Overfitting/Solved/Colab_claims_overfitting.ipynb)

* Unsolved:
  * [overfitting.ipynb (Starter Code)](Activities/02-Stu_Overfitting/Unsolved/claims_overfitting.ipynb)
  * [Colab_overfitting.ipynb (Starter Code)](Activities/02-Stu_Overfitting/Unsolved/Colab_claims_overfitting.ipynb)

Start this review by verifying how many students were able to finish the activity. If the majority of students are keeping up, recommend Office Hours for more in-depth discussions on specific topics. However, you might need to adjust your pace for the remainder of this module if many students are getting stuck.

* First, we import the necessary Keras functions. We use `set_random_seed` to ensure that we get the same results every time we run this notebook.

  ```python
  from keras.models import Sequential
  from keras.layers import Dense, Activation

  # This code is necessary to produce the same results every time
  import tensorflow as tf
  tf.keras.utils.set_random_seed(1)
  ```

* The data on insurance consists of various claim amounts and characteristics of the people who made those claims.

  ```python
  # Read in the data
  df = pd.read_csv('../Resources/insurance_claims.csv')
  df.head()
  ```

  ![Preview of the claims data DataFrame.](Images/claims_preview.png)

* Now we'll demonstrate categorical prediction again by grouping the dollar claim amounts into one of five equally allocated bins.

  ```python
  # Use qcut to group claims data ("charges") into 5 buckets
  df['charges_quantile'] = (pd.qcut(df['charges'], q=5, labels=False))+1
  # Verify buckets are approximately balanced
  # (Slight imbalance from ties is OK)
  df['charges_quantile'].value_counts()
  ```

* This is our new categorical variable to predict, so we'll use the code from the previous activity to tell Keras that this is a categorical dependent variable.

  ```python
  # Save bucket ("quantile") value as the new  `y` variable
  y_quantile = df['charges_quantile']
  # Save the unique count of categories for later use
  number_of_classes = len(y_quantile.unique())
  # Encode quantiles into labels
  from sklearn.preprocessing import LabelEncoder
  encoder = LabelEncoder()
  encoder.fit(y_quantile)
  encoded_y = encoder.transform(y_quantile)
  # Encode labels into categories
  from keras.utils.np_utils import to_categorical
  y_categorical = to_categorical(encoded_y, num_classes=number_of_classes)
  y_categorical
  ```

  ![Preview of y categorical values.](Images/y_categorical_overfitting.png)

* The `X` predictor data consists of four different variables:

  ```python
  # Specify X (predictor) variables
  X = df[['age','bmi','children', 'smoker']]
  ```

* As always, we first split the dataset into `train` and `test` datasets (“windows”).

  ```python
  # Split into training and testing windows
  from sklearn.model_selection import train_test_split
  X_train, X_test, y_train, y_test = train_test_split(X, y_categorical, random_state=1)
  # Preview the `y_train` values
  y_train
  ```

* The `number_of_predictors` is the number of independent variables. We should save this as a variable since we'll use that number in our first Keras layer.

  ```python
  # Save the count of unique predictor variables for use in model
  number_of_predictors = len(X.columns)
  len(X.columns)
  ```

* With the data ready to go, we construct the neural network architecture.

Point out to the students that one way to reduce overfitting is by introducing a dropout layer.

* Dropout layers use different input parameters, but the process of adding dropouts is the same.

  * For example, the `.2` indicates that this layer is randomly forgetting `20%` of the connections it has learned.

* In addition, we regularize the last layers by using `kernel_regularizer` and `bias_regularizer` as additional parameters.

  ```python
  # Import the `Dropout` layer
  from keras.layers import Dropout
  # Build the Model
  model = Sequential()
  # Add a dense layer
  model.add(Dense(10, input_dim=number_of_predictors, activation='relu'))
  # Now add a dropout layer
  model.add(Dropout(.2,input_shape=(10,)))
  # Add another dense layer, this one with regularization
  model.add(Dense(5, activation='relu', kernel_regularizer=l2(0.01), bias_regularizer=l2(0.01)))
  # Add the final output layer
  # (Set the # of possible outputs equal to the number classes)
  model.add(Dense(number_of_classes, activation='softmax'))
  ```

* Now that we've built the architecture, we can compile the model. Note that we use `categorical_crossentropy` because we're predicting the category (the bin) that each claim belongs to.

  ```python
  # Compile the model
  model.compile(loss="categorical_crossentropy",
                optimizer= "adam",
                metrics=['categorical_accuracy'])
  ```

* It's a good idea to review the summary of the model architecture to make sure everything seems sensible. You can do this before or after compiling the model.

  * For example, if we have more parameters than observations, we should scale our model architecture down.

    ```python
    # Summarize the model
    model.summary()
    ```

    ![Model summary](Images/overfitting_model_summary.png)

* After compiling the model, we fit it to our training data.

Explain to the students that in addition to using a dropout layer, we can prevent overfitting by controlling the amount of learning that takes place.

* An epoch in a neural network occurs when the entire training dataset has been fed through the model. The model re-learns each time it processes a portion (“batch”) of the dataset, so one epoch represents a lot of learning.

* We cycle through the dataset many times (the model completes many epochs) to learn as much as we can about it.

* If we pass the data through the model too many times, we'll get extremely good at learning about the training data, but we'll lose our ability to generalize about the testing data or any new, previously unseen data which might come in when the model is used in real life.

Explain that we can monitor this type of overfitting across each epoch by using a validation test dataset.

* During each epoch, we'll hold back a certain portion of the training data. This portion that we retain becomes our validation dataset, and we'll evaluate performance on both the training and validation datasets.

* We use the `validation_split` parameter when fitting our model to the training data, and then hold back `0.20` (20%) of our data from each epoch as a validation set.

  ```python
  # Add in validation loss to select the number of epochs
  # Fit the model
  number_of_epochs = 50
  model.fit(X_train,y_train,
                      epochs=number_of_epochs,
                      batch_size=10,
                        validation_split=0.2,
                      shuffle=True)
  ```

* After we fit the model, we can check its performance across the epochs.

  ```python
  # Save model history across epochs
  model_history = model.history.history
  model_history.keys()
  ```

  ```python
  # View `categorical_accuracy` for the training dataset
  model_history['categorical_accuracy']
  ```

* We save this history into a DataFrame for better visualization.

  * The plot indicates that performance levels off on the validation set after about 10 epochs.

  ```python
  # Save accuracy for training and validation set across epochs
  training_results = pd.DataFrame(index=range(1,number_of_epochs+1))
  training_results['Training'] = model_history['categorical_accuracy']
  training_results['Validation'] = model_history['val_categorical_accuracy']
  training_results.plot(title = 'Performance Across Training and Validation')
  ```

* Stopping training at about 10 epochs would make the model less prone to overfitting.

  ```python
  # Add in validation loss to select the number of epochs
  # Fit the model
  number_of_epochs = 10
  model.fit(X_train,y_train,
                      epochs=number_of_epochs,
                      batch_size=10,
                        validation_split=0.2,
                      shuffle=True)
  ```

Conclude the activity by noting how model building is not a "one and done" process. Instead, we will always need to iteratively adjust our model to find the version which best avoids overfitting and delivers great performance.

Explain that in the next activity, we'll cover one more metric for evaluating model performance that is very appropriate for classifier-based neural networks. We'll also show one more approach that can help us identify potential overfitting.

Answer any questions before moving on.

---

### 6. Instructor Do: Additional Methods for Model Performance Evaluation—ROC and AUC (10 min)

In this activity, you’ll demonstrate how to assess the performance of a binary classification model by interpreting the ROC curve and AUC. This will add to the students' knowledge of model metrics and overfitting.

Use the slides and highlight the following information:

* The confusion matrix is a method for assessing the performance of a binary classification model.

  ![Confusion matrix components](Images/confusion-matrix.png)

* Let's review the four components of this matrix:

  * TP (True Positives): Positive values that are correctly classified as positive.

  * TN (True Negatives): Negative values that are correctly classified as negative.

  * FP (False Positives): Negative values that are incorrectly classified as positive.

  * FN (False Negatives): Positive values that are incorrectly classified as negative.

* The ROC curve and AUC are two techniques that use the values from the confusion matrix to check and visualize the performance of a classification model.

* **ROC** stands for **Receiver Operating Characteristic**. **AUC** stands for **Area Under the Curve**.

* The ROC curve shows the performance of a classification model as its discrimination threshold is changed—how the model decides what is a 0 and what is a 1.

* By comparing ROC curves across training, test, and validation datasets, we can better understand whether our model is overfit.

* To plot a ROC curve, we use two parameters: true positive rate (`TPR` or "recall") and false positive rate (`FPR`).

* The following image shows the calculation for TPR:

  ![rnn-sentiment-6](Images/rnn-sentiment-6.png)

* The next image shows the calculation for FPR:

  ![rnn-sentiment-7](Images/rnn-sentiment-7.png)

* Every point in the ROC curve represents the TPR versus FPR at different thresholds. The following image is a typical ROC Curve.

  ![ROC Curve](Images/roc-curve.png)

* We might find that interpreting the ROC curve is challenging. The AUC can help us by measuring the area underneath the entire ROC curve, from (0,0) to (1,1).

  ![AUC](Images/auc.png)

* The AUC value ranges from 0 to 1. AUC = 0.0 for a model with predictions that are 100% wrong. AUC = 1.0 for a model that predicts everything correctly.

* AUC=1 is a paradox because it means that the model is perfect, but it also is likely to be overfit. A model with this AU value correctly distinguishes between positive and negative classes.

* AUC=0.50 means that the model is unable to distinguish between positive and negative classes. This model would produce results no different than random guessing (50% chance of either a 0 or 1).

* The higher the AUC, the better the model is at predicting zeros as zeros and ones as ones.

* So, a model with AUC=0.90 may be better than a model with AUC=0.65.

  ![Different AUC values](Images/auc-for-roc-curves.png)

Explain to the students that they will now learn how to perform this analysis using Python. Answer any questions before moving on.

---

### 7. Everyone Do: Additional Methods for Model Performance Evaluation—ROC and AUC (15 min)

**Corresponding Activity:** [03-Evr_ROC_AUC](Activities/03-Evr_ROC_AUC)

In this activity, the students will learn how to create the ROC curve and compute the AUC by using Python.

**Files:**

* Solved:
  * [roc_auc_fraud.ipynb](Activities/03-Evr_ROC_AUC/Solved/roc_auc_fraud.ipynb)
  * [Colab_roc_auc_fraud.ipynb](Activities/03-Evr_ROC_AUC/Solved/Colab_roc_auc_fraud.ipynb)
* Unsolved:
  * [roc_auc_fraud.ipynb](Activities/03-Evr_ROC_AUC/Unsolved/roc_auc_fraud.ipynb)
  * [Colab_roc_auc_fraud.ipynb](Activities/03-Evr_ROC_AUC/Unsolved/Colab_roc_auc_fraud.ipynb)

* [Dataset: transactions.csv](Activities/03-Evr_ROC_AUC/Resources/transactions.csv)

Explain that this is a collaborative activity where together we create the ROC curve and calculate the AUC of a deep learning model.

Slack out the unsolved version of the Jupyter notebook to the students, and ask them to follow you as you live-code the solution.

Open the unsolved version of the Jupyter notebook and highlight the following information.

* For this demo, we will create a fraud detection model using a deep neural network.

* We will use a dataset that contains anonymous information about 284,807 credit card transactions made by European credit cardholders in September 2013.

* The dataset contains nine numerical variables which are the result of PCA transformation to protect the confidentiality of credit cardholders. We can only see the transaction amount.

Import the dataset into a Pandas DataFrame called `transactions_df` and show the head.

![roc-auc-1](Images/roc-auc-1.png)

Continue the data preprocessing and highlight the following points.

* The features set `X` will contain all the variables, from `V1` to `V9` and the `Amount`.

* The target vector `y` will contain the values of the `Class` column. It's set to 0 for non-fraudulent transactions and to 1 for the fraudulent ones.

  ```python
  # Creating the X and y sets
  X = transactions_df.iloc[:, 0:10].values
  y = transactions_df["Class"].values
  ```

* Next, we create the training, validation, and testing sets using the `train_test_split` method from sklearn.

  ```python
  # Creating training, validation, and testing sets
  from sklearn.model_selection import train_test_split

  X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=78)

  X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, random_state=78)
  ```

* By splitting the initial training set, we create a new training set to fit the model and a validation test to verify the model's metrics during the training process.

* Now that the training, validation, and testing sets are ready, we can scale the data. The numerical features are on different scales, so we'll use StandardScaler to scale the data of `X_train`.

  ```python
  # Import the StandardScaler from sklearn
  from sklearn.preprocessing import StandardScaler

  # Scale the data
  scaler = StandardScaler().fit(X_train)
  X_train = scaler.transform(X_train)
  ```

* To define our deep neural network, we will use a Sequential model and two Dense layers.

* First, we define the number of inputs and the number of hidden nodes for each layer:

  ```python
  # Model set-up
  number_input_features = 10
  hidden_nodes_layer1 = 15
  hidden_nodes_layer2 = 5
  ```

* Next, we define the model structure:

  ```python
  # Define the LSTM RNN model
  model = Sequential()

  # Layer 1
  model.add(
    Dense(units=hidden_nodes_layer1, input_dim=number_input_features, activation="relu")
  )

  # Layer 2
  model.add(Dense(units=hidden_nodes_layer2, activation="relu"))

  # Output layer
  model.add(Dense(1, activation="sigmoid"))
  ```

Explain to students that we'll use the sigmoid activation function because we have a binary output: 1 for fraud or 0 for not fraud.

Next, we'll compile the model. We use the `binary_crossentropy` loss function to create a binary classification model.

Point out that we are also defining some metrics to assess the model. These metrics are part of [the Keras metrics module](https://www.tensorflow.org/api_docs/python/tf/keras/metrics?version=stable), and we already went over them in the introduction to binary classification. The only new metric is AUC, which you'll explain during the model evaluation.

We use the `name` parameter to quickly identify each metric during the training process and the model evaluation phase.

```python
# Compile the model
model.compile(
  loss="binary_crossentropy",
  optimizer="adam",
  metrics=[
    "accuracy",
    tf.keras.metrics.TruePositives(name="tp"),
    tf.keras.metrics.TrueNegatives(name="tn"),
    tf.keras.metrics.FalsePositives(name="fp"),
    tf.keras.metrics.FalseNegatives(name="fn"),
    tf.keras.metrics.Precision(name="precision"),
    tf.keras.metrics.Recall(name="recall"),
    tf.keras.metrics.AUC(name="auc"),
  ],
)
```

Now it's time to fit the model. We will use `batch_size = 1000` to speed up the training process for 50 epochs.

* Just like the previous activity on overfitting, we also include the `validation_data` parameter to the `fit` method.

  ```python
  # Training the model
  batch_size = 1000
  epochs = 50
  training_history = model.fit(
    X_train,
    y_train,
    validation_data=(X_val, y_val),
    epochs=epochs,
    batch_size=batch_size,
    verbose=1,
  )
  ```

Execute the compiled code and highlight the following points.

![roc-auc-2](Images/roc-auc-2.gif)

* Note that the training runs on 160,203 samples and the validation runs on 53,402 samples.

* We can observe that each epoch takes around two seconds, so running 50 epochs will take close to two minutes (so we wait).

* Also note that all the metrics are calculated on each epoch for the training and validation data. The validation metrics have the `val_` prefix.

* We'll save the model training results in the `training_history` variable for further analysis.

Continue the demo with the model performance assessment, and then explain to the students that you will start by plotting two metrics that they are already familiar with: `loss` and `accuracy`. Highlight the following information:

* We store the metrics results of the training process in the `history` dictionary of the `training_history` object.

* You can access each metric using the names we define when compiling the model.

* To plot the metrics results, we'll create a DataFrame using the `history` dictionary and plot using the `plot()` method of the Pandas DataFrame.

  ![roc-auc-3](Images/roc-auc-3.png)

  ![roc-auc-4](Images/roc-auc-4.png)

Explain to the students that the third metric that we'll plot is AUC.

![roc-auc-5](Images/roc-auc-5.png)

* As expected, the AUC value is better in the training data across epochs.

* In later epochs, AUC appears to show a very slight decline in the validation set but continues to increase for the training set. This indicates that we should stop training at this point to avoid the risk of overfitting.

* AUC is useful for quickly comparing the performance of many binary classification models because it is a standardized measure, always ranging between 0 and 1.

Continue to the ROC curve plot. Explain to the students that sklearn has a method in the `metrics` module called [`roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html) that calculates the values needed to plot the ROC curve for binary classification models.

* We will also use the `auc` method from sklearn in this part of the demo.

  ```python
  # Import the roc_curve and auc metrics from sklearn
  from sklearn.metrics import roc_curve, auc
  ```

Highlight the following as you continue live-coding the demo.

* To create the ROC curve, we must get the predictions from the training and test datasets.

  ```python
  # Making predictions to feed the roc_curve module
  train_predictions = model.predict(X_train, batch_size=1000)
  test_predictions = model.predict(X_test, batch_size=1000)
  ```

* The `roc_curve` method takes as parameters the actual labels and the predicted labels to then compute the false positive rate (`fpr`), true positive rate (`tpr`), and `thresholds`.

  ```python
  # Calculate the ROC curve and AUC for the training set
  fpr_train, tpr_train, thresholds_train = roc_curve(y_train, train_predictions)
  auc_train = auc(fpr_train, tpr_train)
  auc_train = round(auc_train, 4)

  # Calculate the ROC curve and AUC for the testing set
  fpr_test, tpr_test, thresholds_test = roc_curve(y_test, test_predictions)
  auc_test = auc(fpr_test, tpr_test)
  auc_test = round(auc_test, 4)
  ```

* Once we compute these values, we will use the `fpr` and `tpr` to create a pair of DataFrames to plot the ROC curve.

  ```python
  # Create a DataFrame with the fpr and tpr results
  roc_df_train = pd.DataFrame({"FPR Train": fpr_train, "TPR Train": tpr_train,})

  roc_df_test = pd.DataFrame({"FPR Test": fpr_test, "TPR Test": tpr_test,})
  ```

* We will plot the ROC curve using the `plot()` method from the Pandas DataFrame, and we'll also include the AUC value in the title for further analysis.

  ![roc-auc-6](Images/roc-auc-6.png)

* Plotting the training and testing data ROC curves is a visual technique to validate how the model behaves with different data.

* Plotting is also a way to observe if the test data results are relatively similar to the training data results. A small difference is probably OK, but a big divergence indicates overfitting.

Continue the demo by coding the model's evaluation using the `evaluate()` method. Explain to students that we'll store the evaluation results in the `scores` object. Then we'll create a `metrics` dictionary with the results.

![roc-auc-7](Images/roc-auc-7.png)

The preceding image shows the results from the model's evaluation. We'll use these values for further analysis.

We continue the model's evaluation by creating a confusion matrix using the metrics obtained from the validation. We'll use a Pandas DataFrame to display the matrix.

![roc-auc-8](Images/roc-auc-8.png)

Next, we create the classification report using the `classification_report` method from sklearn.

![roc-auc-9](Images/roc-auc-9.png)

We can also use these techniques to compare the performance of a single model using different hyperparameters, and to compare different models for the same problem.

Explain to the students that in the next activity, they'll learn how to save models for later analysis or comparison.

Answer any questions before moving on.

---

### 8. Instructor Do: Saving Models (10 min)

**Corresponding Activity:** [04-Ins_Saving_Models](./Activities/04-Ins_Saving_Models/)

After trying out various versions of a model, you might find one that delivers great performance and is also robust against overfitting. But how do you save that model to use again in the future? In this activity, the students will learn how to save the models that they build for future experimentation, sharing on GitHub, or deploying in a production environment.

**Files:**

* Solved:
  * [Saving_a_Neural_Network_Model.ipynb](./Activities/04-Ins_Saving_Models/Solved/Saving_a_Neural_Network_Model.ipynb)
  * [Colab_Saving_a_Neural_Network_Model.ipynb](./Activities/04-Ins_Saving_Models/Solved/Colab_Saving_a_Neural_Network_Model.ipynb)
* Unsolved:
  * [Saving_a_Neural_Network_Model.ipynb](./Activities/04-Ins_Saving_Models/Unsolved/Saving_a_Neural_Network_Model.ipynb)
  * [Colab_Saving_a_Neural_Network_Model.ipynb](./Activities/04-Ins_Saving_Models/Unsolved/Colab_Saving_a_Neural_Network_Model.ipynb)

Explain that neural networks, especially complex ones, may demand significant computational resources, including CPU memory and activity on the allotted server. Training a complex neural network on a medium or large dataset can take hours (or even days)!

* For simple modelling problems like the ones covered in this module, we can train a model in the same notebook where we analyze our data.

* However, for more formal applications of neural networks and deep learning models, data scientists don't have enough time or resources to build and train a model each time they analyze data. In these cases, they must store and access trained models outside of the training environment.

* Data scientists publish trained models in scientific papers, deploy them in software, share them on GitHub, and even pass them along to colleagues.

* Sharing only the weights, parameters, input weights, and biases for each layer of the model would result in frustration and confusion. Instead, we can use the Keras `Sequential` model's `save` function to export an entire model to a Hierarchical DataFormat [HDF5](https://en.wikipedia.org/wiki/Hierarchical_Data_Format) file. The HDF5 includes:

  * the configuration of the model layers
  * the weights associated with each layer
  * the activation functions
  * the optimizer
  * the set of losses and metrics

* Once we have created the HDF5, anyone can import the same trained model to their environment using the Keras `load_model` function. Then, they can use the model for analysis.

To demonstrate how to export and import a neural network model, we'll use a common machine learning [dataset](https://archive.ics.uci.edu/ml/datasets/wine+quality) on various factors which can be used to predict wine quality..

First, let’s review the code we used to create the deep neural network model with two hidden layers:

```python
# Define the model - deep neural net with two hidden layers
number_input_features = 11
hidden_nodes_layer1 = 8
hidden_nodes_layer2 = 4

# Create a Sequential neural network model
nn_1 = Sequential()

# Add the first hidden layer
nn_1.add(Dense(units=hidden_nodes_layer1, input_dim=number_input_features, activation="relu"))

# Add the second hidden layer
nn_1.add(Dense(units=hidden_nodes_layer2, activation="relu"))

# Add the output layer
nn_1.add(Dense(units=1, activation="linear"))

# Compile model
nn_1.compile(loss="mean_squared_error", optimizer="adam", metrics=["mse"])

# Fit the model
deep_net_model_1 = nn_1.fit(X_train_scaled, y_train, epochs=100)
```

* After training the model, let's say that we want to save the current model and share it with our colleagues.

* To export the trained model, we use the `save` function provided by Keras. This will save the model as an HDF5 file. The following code saves the file:

  ```python
  # Set the model's file path
  file_path = Path("Resources/wine_quality.h5")

  # Export your model to an HDF5 file
  nn_1.save(file_path)
  ```

* After running the code, we should see a file named `wine_quality.h5`, which contains the complete model and configuration.

* Now that we've saved the model, we can create it again at any time. Let's try loading the model into the notebook without providing any structure or context. To load the model, add and run the following code:

**Note**: Point out to students that we import the TensorFlow library as `tf` so we can use the `keras.models.load_model` function to import the model into the Jupyter notebook.

```python
# Import the required libraries
import tensorflow as tf

# Set the model's file path
file_path = Path("Resources/wine_quality.h5")

# Load the model to a new object
nn_imported = tf.keras.models.load_model(file_path)
```

Finally, we can test the performance of the imported model on our test dataset by running the following code:

```python
# Evaluate the model using the test data
model_loss, model_accuracy = nn_imported.evaluate(X_test_scaled, y_test, verbose=2)

# Display evaluation results
print(f"Loss: {model_loss}, Accuracy: {model_accuracy}")
```

The results, including both a loss and accuracy value of approximately 0.434, are shown in the following image:

![Screenshot depicting evaluation results.](Images/13-3-evaluating-imported-model.png)

Our imported model produces the same performance metrics as the original model. Using this procedure, we can import any Keras neural network model. Then, we can evaluate our imported model on any dataset that has the same features as the model’s original dataset.

The next activity provides the opportunity to practice your model-saving skills.

---

### 9. Student Do: Saving Models (20 min)

**Corresponding Activity:** [05-Stu_After_Training](./Activities/05-Stu_After_Training)

In this activity, the students will create a deep learning model from the credit score data, save it, and load it to evaluate its performance on unseen data.

**Files:**

* [Starter file](./Activities/05-Stu_After_Training/Unsolved/after_training.ipynb)
* [Colab Starter file](./Activities/05-Stu_After_Training/Unsolved/after_training.ipynb)

* [credit_scores.csv](./Activities/05-Stu_After_Training/Resources/credit_scores.csv)

**Instructions:**

* [Instructions](./Activities/05-Stu_After_Training/README.md)

---

### 10. Instructor Do: Review Saving Models (10 min)

**Files:**

* [Solution file](./Activities/05-Stu_After_Training/Solved/after_training.ipynb)
* [Colab Solution file](./Activities/05-Stu_After_Training/Solved/Colab_after_training.ipynb)

* [credit_scores.csv](./Activities/05-Stu_After_Training/Resources/credit_scores.csv)

Open the notebook and go through the code, but take time to answer any questions.

* After we load the data, we split it into training and testing sets.

  ```python
  from sklearn.model_selection import train_test_split

  X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
  ```

* We scale the data before creating the model.

  ```python
  # Scale the data for the features set X_tain and X_test

  # Fit the training data to a StandardScaler instance
  scaler = StandardScaler().fit(X_train)

  # Scale the training data
  X_train_scaled = scaler.transform(X_train)

  # Scale the testing data
  X_test_scaled = scaler.transform(X_test)
  ```

* We use a shallow neural net to predict the credit scores and limit overfitting.

  ```python
  # Create a shallow, 1 hidden layer, neural network

  # Instantiate an instance of the Sequential model
  nn = Sequential()

  # Create 1 hidden layer
  nn.add(Dense(units=8, input_dim=68, activation="relu"))

  # Create the output layer
  nn.add(Dense(units=2, activation="linear"))

  # Compile the model
  # Set the parameters as mean_squared_error, adam, and mse.
  nn.compile(loss="mean_squared_error", optimizer="adam", metrics=["mse"])

  # Fit the model using the training data
  model_1 = nn.fit(X_train_scaled, y_train, epochs=800, verbose=0)

  # Plot the train function
  plt.plot(model_1.history["loss"])
  plt.title("loss_function - training")
  plt.legend(["loss"])
  plt.show()
  ```

  ![Plot of Loss Function Across Epochs](Images/loss_function_plot.png)

* After compiling and fitting the model, we save it to a JSON file. We save the weights to an H5 store.

  ```python
  # Save model in JSON format
  nn_json = nn.to_json()

  # Define a relative path to save the model
  # The model should be saved with a .json file extension
  file_path = Path("../Resources/model.json")

  # Write the model to the the file
  with open(file_path, "w") as json_file:
      json_file.write(nn_json)

  # Define a relative path to save the model weights
  # The model weights should be saved with a .h5 file extension
  file_path = "../Resources/model.h5"

  # Save the weights to the file path
  nn.save_weights(file_path)
  ```

* To load the model, we first read the JSON file. Then, we use the model object to load the weights from its file path.

  ```python
  # Identify the relative path of the model's location
  file_path = Path("../Resources/model.json")

  # Read in the model and save it as the variable loaded_model
  with open(file_path, "r") as json_file:
      model_json = json_file.read()
  loaded_model = model_from_json(model_json)

  # Identify the relative path for the model's weights
  file_path = "../Resources/model.h5"

  # Load the model's weights to the variable loaded_model
  loaded_model.load_weights(file_path)
  ```

* All that's left to do is to use the model for prediction. After this, we can use sklearn's MSE metric function to calculate the difference between predicted and observed values for the test set.

  ```python
  # Predict values using the testing data
  y_pred = loaded_model.predict(X_test_scaled)

  # View the model's predictions
  y_pred[:5, :]

  # Import
  from sklearn.metrics import mean_squared_error

  # Evaluate the model with the MSE metric
  print(mean_squared_error(y_test, y_pred))
  ```

Explain that the mean squared error tells us how close the regression line is to a set of points. A higher number means a higher loss function.

Ask the students if they have any questions about how to create deep neural network models or how to save those models and weights for use with different datasets.

Next, the students will learn how to continue editing models after saving them.

---

### 11. Break (15 min)

---

### 12. Instructor Do: Transfer Learning (15 min)

**Corresponding Activity:** [06-Ins_Transfer_Learning](./Activities/06-Ins_Transfer_Learning)

We often will need to save a neural network model for future use in a production setting where it can predict outcomes on unseen data. In this demo, you will show the students how to persist a neural network model and apply it to different, yet similar, data.

**Files:**

* Solved:
  * [ins_transfer_learning.ipynb](./Activities/06-Ins_Transfer_Learning/Solved/ins_transfer_learning.ipynb)
  * [Colab_ins_transfer_learning.ipynb](./Activities/06-Ins_Transfer_Learning/Solved/Colab_ins_transfer_learning.ipynb)

* Unsolved:
  * [ins_transfer_learning.ipynb](./Activities/06-Ins_Transfer_Learning/Unsolved/ins_transfer_learning.ipynb)
  * [Colab_ins_transfer_learning.ipynb](./Activities/06-Ins_Transfer_Learning/Unsolved/Colab_ins_transfer_learning.ipynb)

If there’s enough time remaining, live-code the following activity. Otherwise, open the solved notebook and go through each cell while stopping to answer questions.

* Let's say that we have created a model on the training and test data. Now, we want to put it into production to make actual predictions. Our first step is to save the model somewhere so we can call it as needed.

* In the first few blocks of code, we have defined a model to predict the stock returns of US companies in the two weeks after their earnings results are announced. The model uses the earnings amount, the returns in the two weeks running up to the announcement date, and a couple of other independent variables.

**Note**: The model and data preparation steps have been done for you in the instructor code. Feel free to run and skim quickly through these, and then live-code only the steps the follow, beginning with the **Save the Model and its Weights** section of the notebook.

#### Save the Model and Its Weights

* To save the model, we use the `to_json()` function which represents the parameters and hyperparameters of the model in a `JSON` format. Students should be familiar with this format because it is a common API output standard.

  ```python
  # Save model as JSON
  nn_json = nn.to_json()

  file_path = Path("../Resources/model.json")
  with open(file_path, "w") as json_file:
      json_file.write(nn_json)
  ```

Be sure to cover the syntax associated with both defining the file path and the Python `with open` function in detail.

* Once we've saved the model, we can read and access it again by code. However, it is now also viewable by humans since JSON is human-readable. Open the saved JSON file and ask students to identify parameters.

  ![json_model](./Images/json_model.PNG)

Tell students that the model doesn't contain the training weights (the parameters within each neuron that dictate how variables are used to predict outcomes). So we also need to save the model weights in an HDF file.

* [Hierarchical Data Format (HDF or h5)](https://en.wikipedia.org/wiki/Hierarchical_Data_Format) files contain multidimensional arrays of data.

  ```python
  # Save weights
  file_path = "../Resources/model.h5"
  nn.save_weights(file_path)
  ```

**Note:** To save the model, we set a relative file path using a string variable because the `pathlib` library has some known issues when working with Keras functions to save and load models.

#### Read in the Model with Weights

* To load the models, we need to call the `model_from_json` function from Keras.

  ```python
  # Load the saved model to make predictions

  #Imports
  from tensorflow.keras.models import model_from_json

  # load json and create model
  file_path = Path("../Resources/model.json")
  with open("../Resources/model.json", "r") as json_file:
      model_json = json_file.read()
  loaded_model = model_from_json(model_json)

  # load weights into new model
  file_path = "../Resources/model.h5"
  loaded_model.load_weights(file_path)
  ```

Be sure to cover the syntax associated with both defining the file path and the Python `with open` function in detail.

#### Read in New Data and Work with Previously Saved Model

* Finally, we can use the loaded model's `predict()` function to make predictions on unseen, newly loaded data.

  ```python
  # Load in some new data
  X = pd.read_csv('../Resources/meet_or_beat_US_new_data.csv')

  # Make some predictions with the loaded model
  new_predictions = loaded_model.predict(X)
  new_predictions
  ```

  ![Predicted values](./Images/predicted_values.png)

Remind the students that we can use the model to predict new and previously unseen data or apply the model to a different dataset entirely. This is called **transfer learning**.

* For example, a fintech company might apply a model that was trained on one dataset to a new segment of customers in that same dataset.

* Or, it could use a model built on user engagement for one type of product, and apply that model to a newly launched product for which no data is yet available.

Demonstrate the idea of transfer learning by live-coding the following exercise. Explain that you're going to apply a saved model for predicting US equity returns to a dataset on Australian equity returns.

* First, we read in the new Australian data and train-test-split/standardize it.

  ```python
  new_data = pd.read_csv('../Resources/meet_or_beat_AU.csv')

  # Split into training and testing windows
  from sklearn.model_selection import train_test_split

  y_var = 'after_total_returns'
  x_vars = list(new_data.columns)
  x_vars.remove(y_var)

  X_train, X_test, y_train, y_test = train_test_split(new_data[x_vars], new_data[y_var], random_state=1)

  # Create the StandardScaler instance
  X_scaler = StandardScaler()

  # Fit the scaler to the features training dataset
  X_scaler.fit(X_train)

  # Scale both the training and testing data from the features dataset
  X_train_scaled = X_scaler.transform(X_train)
  X_test_scaled = X_scaler.transform(X_test)
  ```

* Sometimes we might want to tweak our model slightly.

  * For example, if we have a dataset that is too small to train on, we can use a model built previously on a larger dataset.

  * We might not be able to train a full model with the smaller dataset, but we might have enough data to train an additional layer or two.

  * If the new data differs slightly, we can adjust the old model to better predict this new data.

Explain to the students that model adjustments like this are common when conducting transfer learning.

* We start the adjustment process by "freezing" the original layers of the original model, which are all saved in the `layers` attribute of that model.

  * We'll freeze all but the last layer. The last layer is the final output layer to get the predictions, and we want to train the model a little bit more before getting to our final predictions.

  ```python
  # Freeze the existing layers of the loaded model
  for layer in loaded_model.layers[0:-1]:
      layer.trainable = False
  ```

* We can verify that the `loaded_model` is the same as the one used previously by using the `summary` function:

  ```python
  loaded_model.summary()
  ```

  ![frozen_layers_summary.png](Images/frozen_layers_summary.png)

Explain to the students that selecting layers to add or retrain is a flexible concept in transfer learning. You do what works best for your specific data and situation.

* Here, we'll keep all but the last layer of our existing model. Then, we'll train an additional layer and add a new final output layer.

* These two layers will be trained on this new data. The rest of the deep neural network (“DNN”) will stay the same (i.e., trained previously on the other data).

* We create a new `Sequential` DNN where we copy all layers except for the final one from our saved DNN:

  ```python
  # Create a new DNN to hold the old one
  transfer_model = Sequential()
  # We'll copy all but the last layer
  for layer in loaded_model.layers[:-1]:
      transfer_model.add(layer)
  ```

* By displaying this new DNN, we confirm that it has everything from the `loaded_model` DNN, minus the final layer.

  ```python
  transfer_model.summary()
  ```

Point out to the students that these layers were previously frozen, so nothing in this DNN is trainable. If we try to train at this point, the learning algorithm will pass over all these layers, and they will remain unchanged.

* Next, we add the two final layers which we'll train on the new data.

  ```python
  # Add an additional layer
  transfer_model.add(Dense(10, activation="relu"))
  # Add the final output layer
  transfer_model.add(Dense(1))
  ```

* By printing the `summary` of our final model, we can observe that the last two layers have been added.

* Within the two new layers, our DNN now has a few new trainable parameters.

  ```python
  transfer_model.summary()
  ```

  ![frozen_and_unfrozen_layers](Images/frozen_and_unfrozen_layers.png)

At this point, we have built and trained our transfer learning model. Creating predictions with it works the same as with any other deep learning model.

* **Note**: If you are running out of time, review these next steps briefly.

  ```python
  # Compile the Sequential model
  transfer_model.compile(loss="mean_absolute_error", optimizer="adam", metrics=["accuracy"])

  # Fit the model
  transfer_model.fit(X_train_scaled,y_train,
                      epochs=20,
                      batch_size=100,
                      shuffle=True)

    # Evaluate the model loss and accuracy metrics using the evaluate method and the test data
  model_loss, model_accuracy = nn.evaluate(X_test_scaled, y_test, verbose=2)

  # Display the evaluation results
  print(f"Loss: {model_loss}, Accuracy: {model_accuracy}")
  ```

  ```text
  43/43 - 0s - loss: 0.0086 - accuracy: 0.0073 - 185ms/epoch - 4ms/step
  Loss: 0.008577074855566025, Accuracy: 0.007342143915593624
  ```

Ask students for questions before moving on to the practice activity.

---

### 13. Student Do: Transfer Learning: "Model Homes" (15 min)

**Corresponding Activity:** [07-Stu_Transfer_Learning](./Activities/07-Stu_Transfer_Learning)

In this activity, the students will load a pre-existing deep neural network that was trained on one housing market area and apply it to another area.

**Instructions:**

* [Readme](./Activities/07-Stu_Transfer_Learning/README.md)

**Files:**

* [Starter file](./Activities/07-Stu_Transfer_Learning/Unsolved/model_homes.ipynb)
* [Colab Starter file](./Activities/07-Stu_Transfer_Learning/Unsolved/Colab_model_homes.ipynb)

---

### 14. Instructor Do: Review Transfer Learning: "Model Homes" (10 min)

* [Solution file](./Activities/07-Stu_Transfer_Learning/Solved/model_homes.ipynb)
* [Colab_Solution file](./Activities/07-Stu_Transfer_Learning/Solved/Colab_model_homes.ipynb)

Depending on the available time, either live-code the solution or go through the solution description that follows.

* The saved model is a JSON file, so we use `model_from_json` to import it. Separately, we also load the model's weights.

  ```python
  from tensorflow.keras.models import model_from_json

  file_path = ("../Resources/los_angeles_model.json")

  with open("../Resources/los_angeles_model.json", "r") as json_file:
      model_json = json_file.read()
  loaded_model = model_from_json(model_json)

  file_path = "../Resources/los_angeles_model.h5"
  loaded_model.load_weights(file_path)
  ```

* The `layers` attribute for this model reveals that there are five, including one Dropout layer.

  ```python
  # Use the `layers` attribute or `summary` function to count how many layers there are
  loaded_model.layers
  ```

* With the model loaded, our next step is to load some new data and observe how it performs.

  ```python
  df = pd.read_csv('../Resources/san_diego.csv')
  ```

* `y` is the data that we want to predict, and `X` is the data we'll use to make that prediction.

  ```python
  y = df['pricePerSquareFoot']
  X = df[['livingArea','bathrooms','bedrooms','garageSpaces']]
  ```

* As usual, we split the data into training and testing datasets:

  ```python
  from sklearn.model_selection import train_test_split
  X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
  ```

* We keep all but the last layer of our original model unchanged (freeze the layers):

  ```python
  # Freeze the existing layers of the loaded model
  for layer in loaded_model.layers[0:-1]:
      layer.trainable = False
  ```

* Reviewing the model with `summary` reveals that none of the parameters outside of the last layer are currently trainable. This means that these layers and their weights will be unchanged, even if we fit the model again.

  ```python
  # Verify all layers are frozen by printing the `summary` of the
  # model's architecture.
  loaded_model.summary()
  ```

* Our new model will contain these frozen layers and omit that final layer.

  ```python
  # Create a new network which is an exact copy of this loaded model,
  # except that the top layer of the original model is removed.
  transfer_model = Sequential()
  for layer in loaded_model.layers[:-1]:
      transfer_model.add(layer)
  ```

* In addition, we'll add a new trainable layer on top and a new (also trainable) final output layer. These new top layers will be trained and adapted for the specifics of the San Diego real estate data.

  * By only changing the top two layers, we're keeping the most important, core features of the model unchanged. However, we are adapting it for new predictions which will be more specific to this new, somewhat different data.

  * We're still predicting houses in either model; what's different is the county-specific factors.

* We'll now add those two layers:

  ```python
  # Replace those removed layers with one or two new layers
  # (including the final output layer).

  # Add an additional layer
  transfer_model.add(Dense(10, activation="relu"))
  # Add the final output layer
  transfer_model.add(Dense(1))
  ```

* Next, we'll review the network architecture to ensure that those layers are indeed showing up. Note that the number of trainable parameters has increased because of the new layers.

  ```python
  # Ensure that these new trainable layers are added by using
  # the `summary` function on this revised model.
  transfer_model.summary()
  ```

* Finally, we compile and then fit the model, just as we've done in previous activities.

  ```python
  # Compile the Sequential model
  transfer_model.compile(loss="mean_absolute_error", optimizer="adam", metrics=["accuracy"])
  ```

  ```python
  # Fit the model
  transfer_model.fit(X_train,y_train,
                      epochs=20,
                      batch_size=100,
                      shuffle=True)
  ```

Answer any questions before moving on.

---

### 15. Wrap-Up (5 min)

Close today's session by reminding students about all the skills that they've acquired. The students can now:

* Utilize a number of techniques to avoid overfitting, which is a critical skill for neural networks and ML in general.

* Build and interpret ROC curves and the AUC, which are common methods in the field for determining a model's goodness of fit.

* Save DNN models either for future use or for private or public collaboration with others.

* Use previously built models and tweak them according to the specific circumstances of the data.

Congratulate the students on learning advanced skills that build upon the core knowledge from the previous sessions. Now, the students can build neural networks with both great accuracy and good generalization to new datasets. Plus, they can share their networks with others and modify them as needed.

---

### 16. Instructor Do: Structured Review (35 min)

**Note:** If you are teaching this Lesson on a weeknight, please save this 35-minute review for the next Saturday class.

Please use the entire time to review questions with the students before officially ending class.

Suggested Format:

* Ask students for specific activities to revisit.

* Revisit key activities for the homework.

* Allow students to start the homework with extra TA support.

Take your time on these questions! This is a great time to reinforce concepts and address misunderstandings.

---

### End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
