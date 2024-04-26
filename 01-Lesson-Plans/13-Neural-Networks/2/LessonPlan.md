## 13.2 Lesson Plan: Deep Neural Networks

### Overview

This class continues the journey into neural networks by introducing students to the concept and code behind deep neural networks. Deep neural networks are exciting models to deploy because of their power to solve problems in many applications.

### Class Objectives

By the end of this lesson, the students will be able to:

* Explain the difference between neural networks and deep neural networks.

* Build deep learning models using Keras.

### Instructor Notes

* **Important:** Slack out the [Deep Learning Installation Guide Folder](../../13-Neural-Networks/Supplemental/Deep_Learning_Installation_Guide) for installing Tensorflow before today's class. The students need to install these tools before class to conserve time for lessons and activities.

* **VERY Important:** Some machines will not install or run Tensorflow due to hardware incompatibilities. This is most prevalent for Apple Silicon M1 computers. The simplest solution is to have these students run their notebooks in [Google Colab](https://colab.research.google.com/) which comes with support for TensorFlow. Generally, the notebook can be uploaded and run in Colab without any changes. Where changes are necessitated, specific Colab compatible notebooks have been included in the activity files.

* Allow the class to ask questions, but when necessary, ask the students to save their questions for the review sessions or office hours.

### Class Slides and Time Tracker

You can view the slides for this lesson on Google Drive here: [Lesson 13.2 slides](https://docs.google.com/presentation/d/1yIRKFo0Gq5OiSpYVrRBkI0Dy4O132SSaC223IuIyUpY/edit?usp=sharing).

To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

Note: Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy."

You can view the time tracker for this lesson here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome the Class (5 min)

Welcome the students to the second day of the deep learning unit, and explain the following:

* Today, we will dive into constructing deep learning models with real-world data.

* Generally speaking, deep learning models are neural networks with more than one hidden layer.

  ![hidden_layers](./Images/multiple-hidden-layers.png)

* Deep neural networks are much more effective than traditional machine-learning approaches at discovering nonlinear relationships among data. They are often the best choice for complex or unstructured data like images, text, and voice.

* Deep neural networks are computational models composed of multiple layers that can learn complex relationships in the data.

* For example, in image recognition, each layer can identify different image features in the process of defining or identifying the image.

  ![deep_learning_layers](./Images/deep-learning-layers.png)

Answer any questions before moving on.

---

### 2. Instructor Do: Introduction to Deep Learning (15 min)

Explain that neural networks calculate the weights of various input data and pass them to the next layer of neurons. This process continues until the data reaches the output layer, which makes the final decision on the predicted category or numerical value of an instance.

* While definitions vary, we can consider neural networks with more than one hidden layer (as shown by the model depicted in the slide) to be deep learning models. The decreasing cost and greater availability of computing power has increased our ability to create and use these models.

* Each additional layer of neurons makes it possible to model more complex relationships and concepts.

  * Imagine that we are trying to classify whether a picture contains a cat. The first step in solving this problem might be to find any animal in the picture. Drilling deeper, the model might detect the presence of paws, pointed ears, etc. This breaking down of the problem continues until we reach the raw input of the model, which are the individual pixels in the picture. Each conceptual layer (where the model works on understanding a concept) needs its own layer of neurons.

* Deep learning models can solve very complex problems that cannot be handled by classical models (such as linear regression). Deep learning makes it possible to solve difficult problems with high accuracy, such as image classification or natural language processing.

Open the [TensorFlow playground](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=spiral&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=8&seed=0.14370&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=true&xSquared=true&ySquared=true&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false). Click the Play button to run the simulation, and then use the model to demonstrate the effects of adding layers of neurons to a neural network.

Tell the students that the benefits of adding additional layers in the TensorFlow playground are obvious when we observe more complex classification datasets like _spiral_. The following image shows a lack of convergence when we have only one layer of neurons:

![playground_1_layers](./Images/playground_1_layers.PNG)

Add a second hidden layer with six neurons to the model. Now the model converges to a much lower loss metric:

![playground_2_layers](./Images/playground_2_layers.PNG)

Add a third hidden layer with four neurons to the model and highlight the following information.

* Adding layers does not always guarantee better performance. If the problem isn't very complex, additional layers can be redundant. Because there isn't an easy analytical way of determining how many layers are needed, our only solution is through trial and error.

  ![playground_3_layers](./Images/playground_3_layers.PNG)

* Adding too many layers can cause overfitting. This happens when the model fits a far more complex function than the one that actually generated the data.

To check for understanding, ask for volunteers to answer the following questions.

* What are some examples of classification or regression problems that might benefit from a deep learning model?

    **Sample Answer**: Facial recognition, medical diagnoses, natural language generation for chatbots.

* How can we observe if a neural network has too many layers of neurons?

    **Sample Answer**: We can watch for signs of overfitting. For example, test accuracy is far lower than training accuracy.

Answer any questions before moving on.

---

### 3. Instructor Do: Deep Learning with Keras (15 min)

**Corresponding Activity:** [01-Ins_Deep_Learning](./Activities/01-Ins_Deep_Learning)

This instructor demo will lead the students through a deep learning model to predict the credit quality of different student loans.

**Files:**

* Solved:
  * [deeplearning.ipynb](./Activities/01-Ins_Deep_Learning/Solved/deeplearning.ipynb)
  * [Colab_deeplearning.ipynb](./Activities/01-Ins_Deep_Learning/Solved/Colab_deeplearning.ipynb)

* Unsolved:
  * [deeplearning.ipynb](./Activities/01-Ins_Deep_Learning/Unsolved/deeplearning.ipynb)
  * [Colab_deeplearning.ipynb](./Activities/01-Ins_Deep_Learning/Solved/Colab_deeplearning.ipynb)

If you feel confident, open the unsolved notebook and have the class follow along while you live-code the demo. Otherwise, go through the solved notebook and explain the following points.

* In this activity, we will use a deep neural network to predict credit quality ("credit_ranking") of various student loans. Our scenario involves building a model for a company that specializes in student loan refinancing. If the company can predict whether a borrower will pay their loan in full, it can provide a more accurate interest rate for the borrower.

* We assign the features to `X` and the target labels to `y`:

  ```python
  # Read in data
  data = Path("../Resources/student_loans.csv")
  df = pd.read_csv(data, delimiter=";")
  df.head()

  # Create the features (X) and target (y) sets
  X = df.iloc[:, 0:11].values
  y = df["credit_ranking"].values
  ```

* As always, we first need to scale the data:

  ```python
  # Scale the data
  from sklearn.preprocessing import StandardScaler

  scaler = StandardScaler().fit(X)
  X = scaler.transform(X)
  ```

* First, we'll create a shallow network with one hidden layer to accomplish the task. Note that we set the activation function in the output layer to `linear`.

  ```python
  # Define the model - shallow neural net
  number_hidden_nodes = 8
  number_input_features = 11

  nn = Sequential()
  # Hidden layer
  nn.add(
      Dense(units=number_hidden_nodes, input_dim=number_input_features, activation="relu")
  )
  # Output layer
  nn.add(Dense(units=1, activation="linear"))
  ```

* Then we compile and train the model.

  ```python
  # Compile the model
  nn.compile(loss="mean_squared_error", optimizer="adam", metrics=["mse"])

  # Train the model
  model_1 = nn.fit(X, y, validation_split=0.3, epochs=200)
  ```

* This is a regression model, so we use the `mean_squared_error` loss function because the output is continuous. We define `mse` as an additional metric.

* Note that we use the `validation_split` parameter in the `fit()` method. This parameter is a float number between `0` and `1` that reserves a fraction of the data for validation; it can be used as an alternative to the `train_test_split` method of sklearn.

* When we use the `validation_split` parameter, the model sets aside a fraction of the training data and will not train on it. The model will evaluate the loss and any metrics on this data portion at the end of each epoch.

* By plotting the loss function, we can observe that the model seems to quickly converge to a very small number. Can a deeper network do better?

  ![deep1](./Images/deep1.PNG)

* Defining a deep neural network is very easy. All we do is add another layer of hidden neurons with the same activation function as the first layer. This next layer normally has fewer neurons than the first hidden layer. Of course, we can and should experiment with different potential architectures if our goal is to minimize the loss metric.

  ```python
  # Define the model - deep neural net
  number_input_features = 11
  hidden_nodes_layer1 = 8
  hidden_nodes_layer2 = 4

  nn = Sequential()
  # First hidden layer
  nn.add(
      Dense(units=hidden_nodes_layer1, input_dim=number_input_features, activation="relu")
  )
  # Second hidden layer
  nn.add(Dense(units=hidden_nodes_layer2, activation="relu"))
  # Output layer
  nn.add(Dense(units=1, activation="linear"))

  # Compile model
  nn.compile(loss="mean_squared_error", optimizer="adam", metrics=["mse"])

  # Fit the model
  model_2 = nn.fit(X, y, validation_split=0.3, epochs=200)
  ```

* After defining and overlaying the results of the deep learning model on the shallow model, we observe that adding a layer increases the training speed (as measured by the slope of the loss metric over epochs) and slightly decreases the loss metric that the model converges to.

  ```python
  plt.plot(model_1.history["loss"])
  plt.plot(model_2.history["loss"])
  plt.title("loss_function - Training")
  plt.legend(["1 hidden layer", "2 hidden layers"])
  plt.show()
  ```

  ![deep2](./Images/deep2.PNG)

* This does not appear to create overfitting because both models perform equally well on validation data, which is unseen during training.

  ```python
  # Train vs test for shallow net
  plt.plot(model_1.history["loss"])
  plt.plot(model_1.history["val_loss"])
  plt.title("loss_function - Training Vs. Validation - 1 hidden layer")
  plt.legend(["train", "test"])
  plt.show()
  ```

  ![deep3](./Images/deep3.PNG)

* **Note**: If the students ask about the difference between "loss" and "val_loss", explain that loss is the value of the cost function for the training data, while val_loss is the value of the cost function for the testing data (cross-validation data). The model handles neurons differently in the training and testing phases.

  ```python
  # Train vs test for deep net
  plt.plot(model_2.history["loss"])
  plt.plot(model_2.history["val_loss"])
  plt.title("loss_function - Training Vs. Validation - 2 hidden layers")
  plt.legend(["train", "test"])
  plt.show()
  ```

  ![deep4](./Images/deep4.PNG)

Answer any questions before moving on.

---

### 4. Student Do: Predicting Fraudulent Transactions (20 min)

**Corresponding Activity:** [04-Predicting-Fraudulent-Transactions](Activities/02-Stu_Fraudulent_Transactions/)

In this activity, the students will build a deep learning model that can predict financial fraud.

**Instructions:**

* [README.md](Activities/02-Stu_Fraudulent_Transactions/README.md)

**Files:**

* [fraudulent-transactions.ipynb (Unsolved)](Activities/02-Stu_Fraudulent_Transactions/Unsolved/fraudulent_transactions.ipynb)
* [Colab_fraudulent-transactions.ipynb (Unsolved)](Activities/02-Stu_Fraudulent_Transactions/Unsolved/Colab_fraudulent_transactions.ipynb)

---

### 5. Instructor Do: Review Predicting Fraudulent Transactions (10 min)

**Files:**

* [fraudulent-transactions.ipynb](Activities/02-Stu_Fraudulent_Transactions/Solved/fraudulent_transactions.ipynb)
* [Colab_fraudulent-transactions.ipynb](Activities/02-Stu_Fraudulent_Transactions/Solved/Colab_fraudulent_transactions.ipynb)

Detecting fraudulent transactions is a major concern of big banks. In this activity, we'll predict fraudulent credit card transactions by training a neural network model on a collection of historical transaction data.

* If the students were able to follow the previous activity, live-code the solutions from the starter code.

* If they had trouble following the previous activity and need more in-depth explanations, go through the solution file, as follows:

* We first read the data from the CSV file into a Pandas DataFrame.

  ```python
  cc_transactions_df = pd.read_csv(
      Path("../Resources/credit_card_transactions.csv")
  )
  ```

* Next, we create the target variable `y` by assigning the values of the “isFraud” column of the DataFrame. The feature set `X` includes all the columns of the DataFrame except the “isFraud” column.

  ```python
  # Define the target set by selecting the isFraud column
  y = cc_transactions_df["isFraud"]
  # Define features set X by selecting all columns but the isFraud
  X = cc_transactions_df.drop(columns=["isFraud"])
  ```

* We create the training and testing sets using the `train_test_split` function from scikit-learn.

  ```python
  X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
  ```

* As we do in most ML models, we scale the features data by using the `StandardScaler` from scikit-learn.

  ```python
  # Create the StandardScaler instance
  X_scaler = StandardScaler()
  # Fit the scaler to the features training dataset
  X_scaler.fit(X_train)
  # Scale both the training and testing data from the features dataset
  X_train_scaled = X_scaler.transform(X_train)
  X_test_scaled = X_scaler.transform(X_test)
  ```

* Our deep neural network model will contain the following structure:

  * There are 9 inputs.
  * The first hidden layer has 18 neurons.
  * The second hidden layer has 8 neurons.
  * The output layer has a single output.
  * Hidden layers use the ReLU activation function, and the output layer uses the sigmoid activation function.

  ```python
  # Define the number of inputs to the model
  number_inputs = 9

  # Define the number of hidden nodes for the first hidden layer
  hidden_nodes_layer1 = 18

  # Define the number of hidden nodes for the second hidden layer
  hidden_nodes_layer2 = 8

  # Create the Sequential model instance
  nn = Sequential()

  # Add the first Dense layer specifying the number of inputs, the number of hidden nodes, and the activation function
  nn.add(Dense(units=hidden_nodes_layer1, input_dim=number_inputs, activation="relu"))

  # Add the second Dense layer specifying the number of hidden nodes and the activation function
  nn.add(Dense(units=hidden_nodes_layer2, activation="relu"))

  # Add the output layer to the model specifying the number of output neurons and activation function
  nn.add(Dense(1, activation="sigmoid"))
  ```

* We display the model structure by using the `summary` function:

  ```python
  # Display the Sequential model summary
  nn.summary()
  ```

* Finally, we compile the neural network model using the `binary_crossentropy` loss function, the `adam` optimizer, and `accuracy` as an additional metric.

  ```python
  # Compile the Sequential model
  nn.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
  ```

* Once we've compiled the model, we fit it with the training data, using 100 epochs.

  ```python
  # Fit the model using 100 epochs and the training data
  model = nn.fit(X_train_scaled, y_train, epochs=100)
  ```

* Finally, we evaluate the model by using testing data and the `evaluate` method.

  ```python
  # Evaluate the model loss and accuracy metrics using the evaluate method and the test data
  model_loss, model_accuracy = nn.evaluate(X_test_scaled, y_test, verbose=2)

  # Display the evaluation results
  print(f"Loss: {model_loss}, Accuracy: {model_accuracy}")
  ```

Congratulate the students on building their first deep learning model!

* Point out that creating deep learning models with Keras requires only a few lines of code.

* This is one advantage of using specialized frameworks. The framework simplifies the coding process, so you have more time to focus on the underlying business problem that you are trying to solve.

* Tuning a neural network model requires experience and an understanding of the context where the model will be used. It’s always a good idea to learn from the experiences of others who have addressed similar business problems with the same type of machine learning model.

* In the next lesson, we will learn some additional techniques for optimizing neural network models.

Ask if there are any questions before moving to the break.

---

### 6. Break (15 min)

---

### 7. Everyone Do: Deep Learning with Nonlinear Data (20 min)

**Corresponding Activity:** [Non-linear_Data](./Activities/03-Evr_Nonlinear_Data)

In this activity, the students will learn how neural networks can be used to predict outputs for complex nonlinear data.

**Files:**

* [Solution file](./Activities/03-Evr_Nonlinear_Data/Solved/nonlinear_data.ipynb)

* [Starter file](./Activities/03-Evr_Nonlinear_Data/Unsolved/nonlinear_data.ipynb)

Explain to the students that this demo will show how neural networks can adapt to nonlinear data.

Slack the following notebook out to the students:

* [Starter file](./Activities/03-Evr_Nonlinear_Data/Unsolved/nonlinear_data.ipynb)

Open the unsolved version of the Jupyter notebook and then live-code the demo while emphasizing the following information. Encourage the class to replicate your live-coding.

* First, we create some nonlinear dummy data by using the `make_moons()` function from sklearn.

  ```python
  # Creating dummy nonlinear data
  X_moons, y_moons = make_moons(n_samples=1000, noise=0.08, random_state=78)

  # Transforming y_moons to a vertical vector
  y_moons = y_moons.reshape(-1, 1)
  ```

* We create a DataFrame to plot the dummy data using `hvplot`.

  ```python
  # Creating a DataFrame to plot the nonlinear dummy data
  df_moons = pd.DataFrame(X_moons, columns=["Feature 1", "Feature 2"])
  df_moons["Target"] = y_moons
  df_moons.head()

  # Plotting the non-linear dummy data
  df_moons.plot.scatter(x="Feature 1", y="Feature 2", c="Target", colormap="winter")
  ```

  ![Non-linear data plot](Images/nn_1.png)

* We split the data into training and testing sets, and then we scale the data before building and testing the neural network:

  ```python
  # Create training and testing sets
  X_moon_train, X_moon_test, y_moon_train, y_moon_test = train_test_split(
      X_moons, y_moons, random_state=1
  )

  # Create the scaler instance
  X_moon_scaler = StandardScaler()

  # Fit the scaler
  X_moon_scaler.fit(X_moon_train)

  # Scale the data
  X_moon_train_scaled = X_moon_scaler.transform(X_moon_train)
  X_moon_test_scaled = X_moon_scaler.transform(X_moon_test)
  ```

Start building the neural network and highlight the following information.

* We’ll now create a neural network with two inputs and a hidden layer with six neurons.

  ![Neural net sample](./Images/simple-nn.png)

* We create a Sequential model to define the neural network.

  ```python
  nn = Sequential()
  ```

* We add the first layer by defining two input features and six hidden nodes. We'll use ReLU as our activation function:

  ![First layer in the neural network](./Images/simple-nn-layer-1.png)

  ```python
  # First layer
  number_inputs = 2
  number_hidden_nodes = 6

  nn.add(Dense(units=number_hidden_nodes, activation="relu", input_dim=number_inputs))
  ```

* We add the output layer by defining one unit to predict the target output:

  ![Second layer in the neural network](./Images/simple-nn-layer-2.png)

  ```python
  # Output layer
  number_classes = 1

  nn.add(Dense(units=number_classes, activation="sigmoid"))
  ```

* After checking the model summary, we compile and train it with 100 epochs so we can compare the results with our one-neuron model.

  ```python
  # Compile model
  nn.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

  # Training the model with the nonlinear data
  model_moon = nn.fit(X_moon_train_scaled, y_moon_train, epochs=100)
  ```

* The final step is to evaluate the model:

  ```python
  # Evaluate the model using nonlinear testing data
  model_moon_loss, model_moon_accuracy = nn.evaluate(
      X_moon_test_scaled, y_moon_test, verbose=2
  )
  print(f"Loss: {model_moon_loss}, Accuracy: {model_moon_accuracy}")
  ```

* We can observe that accuracy improves. This means that the neural network is capable of learning this complex, nonlinear dataset.

  ![Neural network evaluation](./Images/nn_2.png)

Ask students the following question.

* How can we improve the model accuracy?

  * **Sample Answer:** We can add more neurons to the hidden layer.

  * **Sample Answer:** We can add a second hidden layer.

  * **Sample Answer:**  We can test with different activation functions.

Collect a couple of answers from the class and highlight the following points.

* Adding more neurons to the model is a possible solution, but we might overfit the model.

* We could add a second layer to the model. This is a good solution that is part of deep learning. The next class will cover this topic.

* We can test with different activation functions. This is typically the first thing to try, especially when dealing with nonlinear data.

* Using more epochs for training is another strategy to improve the model's accuracy.

Encourage the students to spend some time modifying the code to use a different number of hidden layer nodes and observe how the model accuracy changes.

Modelling neural networks is a mix of science and art. You'll find the best model through playing around with the number of neurons and testing different activation functions.

---

### 8. Instructor Do: Encoding Categorical Variables (15 min)

**Corresponding Activity:** [04-Ins_Deep_Learning](./Activities/04-Ins_Encoding_Categoricals/)

In this activity, you will lead the students through a deep learning model to predict the credit quality of different student loans.

**Files:**

* Solved:
  * [one_hot_encoder.ipynb](./Activities/04-Ins_Encoding_Categoricals/Solved/one_hot_encoder.ipynb)
  * [Colab_one_hot_encoder.ipynb](./Activities/04-Ins_Encoding_Categoricals/Solved/Colab_one_hot_encoder.ipynb)

* Unsolved:
  * [one_hot_encoder.ipynb](./Activities/04-Ins_Encoding_Categoricals/Unsolved/one_hot_encoder.ipynb)
  * [Colab_one_hot_encoder.ipynb](./Activities/04-Ins_Encoding_Categoricals/Solved/Colab_one_hot_encoder.ipynb)

For all machine learning models (including neural networks), our first step is to preprocess the data.

* Neural networks often have difficulty training on numerical variables that are represented in different units or that have different scales of magnitude.

  * We previously used the `StandardScaler` module from scikit-learn to mitigate this problem for numerical variables. This module scales the values of different variables by normalizing data to centre around the mean.

* In addition, neural networks cannot process **categorical variables** in their raw forms.

* As the name implies, categorical variables represent categories, like a person's city of residence, or different industries of companies in a stock portfolio, in their raw forms.

* Remind students that we previously used the Pandas `get_dummies()` function to solve this problem for categorical variables. However, `get_dummies` can run into trouble if the testing dataset contains categories that are not present in the training dataset.

* To account for this potential `get_dummies` issue, we will use `OneHotEncoder`. OneHotEncoder is a scikit-learn module that allows us to specify what happens when a new category appears in testing data.

Open up the instructor starter notebook. Explain that you will demonstrate how OneHotEncoder works by building a deep neural classifier model that analyzes [bank loan data](https://www.kaggle.com/zaurbegiev/my-dataset#credit_train.csv) to predict whether a loan will be paid in full.

* The starter notebook contains the required module imports. Note that we’ll import OneHotEncoder from `sklearn.preprocessing`, just like we did with StandardScaler:

  ```python
  import pandas as pd
  from pathlib import Path
  from sklearn.preprocessing import OneHotEncoder
  from sklearn.preprocessing import StandardScaler
  from sklearn.model_selection import train_test_split
  ```

Next, we load the data into a Pandas DataFrame, which is already in the starter code:

```python
# Read the CSV file from the Resources folder into a Pandas DataFrame
df = pd.read_csv(
    Path("Resources/loan_status.csv")
)

# Review the DataFrame
df.head()
```

With the DataFrame previewed, point out to students that we have both numerical (“Current_Loan_Amount”, “Credit_Score”, “Annual_Income”, etc.) and categorical (“Loan_Status”, “Term”, “Home_Ownership”, etc.) variables, as shown in the following image:

![A screenshot depicts the head of the DataFrame.](Images/13-3-loading-loan-data.png)

* We can verify each column's contents by using the `info` method on the DataFrame:

  ```python
  df.info()
  ```

* In our case, we want our model to predict whether a loan will be paid. So, the target variable is the “Loan_Status” column. However, this column also is categorical.

  * So before creating the features (`X`) and target (`y`) datasets, we’ll use the OneHotEncoder module to numerically encode all the dataset’s categorical data, including "Loan_Status".

* First, we create an instance of OneHotEncoder. (We set the parameter `sparse=False` to fetch a NumPy array):

  ```python
  # Create a OneHotEncoder instance
  enc = OneHotEncoder(sparse=False)
  ```

Next, we want to list all the columns in our original dataset that have categorical variables. We will use this list later to filter the DataFrame to contain only categorical data.

```python
list(df.dtypes[df.dtypes == "object"].index)
```

The following code creates a list of the columns with only those categorical variables:

```python
# Create a list of the columns with categorical variables
categorical_variables = ["Loan_Status", "Term", "Years_in_current_job", "Home_Ownership", "Purpose"]
```

* Next, we need to train our encoder (OneHotEncoder) to transform our categorical data.

* We use the encoder’s `fit_transform()` function to train it with those variables included in the `categorical_variables` list.

* This same function transforms the data once the encoder has been trained. We pass the original DataFrame, filtered using the `categorical_variables` list, to the function. We do all of this in one step, as the following code shows:

  ```python
  # Use the fit_transform function from the OneHotEncoder to encode the data
  encoded_data = enc.fit_transform(df[categorical_variables])
  ```

* Next, we create a new DataFrame. This DataFrame will contain the encoded data returned by OneHotEncoder. We can use the encoder’s `get_feature_names()` function to set the DataFrame’s column names.

* We use our list of categorical variables as the function’s parameter. This enables the encoder to determine values for the categorical variables and fetch the correct name for each column. The following code shows this step:

  ```python
  # Create a DataFrame with the encoded variables
  encoded_df = pd.DataFrame(
      encoded_data,
      columns = enc.get_feature_names(categorical_variables)
  )

  # Display sample data
  encoded_df.head()
  ```

The following image shows the resulting DataFrame with the encoded variables:

![A screenshot depicts the DataFrame.](Images/13-3-categorical-variables-encoder.png)

Explain to the students that OneHotEncoder works similarly to the `get_dummies` function that they used previously.

* For example, the original categorical variable “Home_Ownership” has four values: Home_Mortgage, Rent, Own_Home, and HaveMortgage. OneHotEncoder will create the following four new columns for this categorical variable: “Home_Ownership_Home_Mortgage”, “Home_Ownership_Rent”, “Home_Ownership_Own_Home”, and “Home_Ownership_HaveMortgage”.

  * If the original "Home_Ownership" column has a row that contains "Own_Home", that row will now have a value of 1.0 in the newly created “Home_Ownership_Own_Home” column. The other new columns in that row will have a value of 0.0.

Finally, we'll need to concatenate the DataFrame with the encoded information with a version of the original DataFrame that has the categorical variable columns dropped.

We use StandardScaler to scale the remaining numerical variables to a similar range.

Answer any questions before moving on.

---

### 9. Student Do: Encoding Categorical Variables (20 min)

**Corresponding Activity:** [05-Stu_Predicting_Turnover](Activities/05-Stu_Predicting_Turnover/)

In this activity, the students will build a deep learning model that can predict employee attrition. In doing so, they'll have to use `onehotencoder` to construct their categorical predictor variables.

**Instructions:**

* [README.md](Activities/05-Stu_Predicting_Turnover/README.md)

**Files:**

* [predicting_turnover.ipynb (Starter Code)](Activities/05-Stu_Predicting_Turnover/Unsolved/predicting_employee_attrition.ipynb)
* [Colab_predicting_turnover.ipynb (Starter Code)](Activities/05-Stu_Predicting_Turnover/Unsolved/Colab_predicting_employee_attrition.ipynb)

---

### 10. Instructor Do: Review Encoding Categorical Variables (10 min)

**Files:**

* Solved:
  * [predicting_employee_attrition.ipynb (Solved)](Activities/05-Stu_Predicting_Turnover/Solved/predicting_employee_attrition.ipynb)
  * [Colab_predicting_employee_attrition.ipynb (Solved)](Activities/05-Stu_Predicting_Turnover/Solved/Colab_predicting_employee_attrition.ipynb)

* Unsolved:

  * [predicting_employee_attrition.ipynb (Starter Code)](Activities/05-Stu_Predicting_Turnover/Unsolved/predicting_employee_attrition.ipynb)
  * [Colab_predicting_employee_attrition.ipynb (Starter Code)](Activities/05-Stu_Predicting_Turnover/Unsolved/Colab_predicting_employee_attrition.ipynb)

In this activity, we'll apply our knowledge of deep learning models to predict whether an employee is likely to depart from a company.

Before going through the code, tell the students that our work will be broken into three sections:

* Preprocess the data.

* Create a neural network model to predict employee attrition.

* Train and evaluate the neural network model.

#### Preprocess the Data

First, we read in `HR-Employee-Attrition.csv` and review the resulting DataFrame.

```python
employee_df = pd.read_csv(
    Path("../Resources/HR-Employee-Attrition.csv")
    employee_df.head()
)
```

An important task is identifying categorical and non-categorical variables. Categorical variables have an `object` data type.

```python
# Review the data types associated with the columns
employee_df.dtypes
```

![Preview of DataFrame data types](Images/dtypes_preview.png)

After inspecting the data, we create a list of categorical variables.

```python
# Create a list of categorical variables
categorical_variables = list(employee_df.dtypes[employee_df.dtypes == "object"].index)
```

We use OneHotEncoder to encode the dataset's categorical variables.

```python
from sklearn.preprocessing import OneHotEncoder
# Create a OneHotEncoder instance
enc = OneHotEncoder(sparse=False)

# Encode categorical variables using OneHotEncoder
encoded_data = enc.fit_transform(employee_df[categorical_variables])
```

We'll then construct a Dataframe of this encoded categorical data:

```python
# Create a DataFrame with the encoded variables
# The column names should match those of the encoded variables
encoded_df = pd.DataFrame(
    encoded_data,
    columns = enc.get_feature_names(categorical_variables)
)
# Display the DataFrame
encoded_df.head()
```

We also create a separate DataFrame for only the numerical variables:

```python
# Create a DataFrame with the columns containing numerical variables from the original dataset
numerical_variables_df = employee_df.drop(columns = categorical_variables)
# Review the DataFrame
numerical_variables_df.head()
```

![Preview of Numerical Variables DataFrame](Images/numerical_variables_dataframe_preview.png)

A new DataFrame named `attrition_df` will contain both the encoded categorical variables and the numerical variables from the original dataset.

```python
attrition_df = pd.concat(
    [
        numerical_variables_df,
        encoded_df
    ],
    axis=1
)
```

From this `attrition_df`, we create the features (`X`) and target (`y`) sets.

```python
# Define the target set y using the Attrition_Yes column
y = attrition_df["Attrition_Yes"]
# Define features set X by selecting all columns but Attrition_Yes and Attrition_No
X = attrition_df.drop(columns=["Attrition_Yes", "Attrition_No"])
```

We create training and testing sets using the `train_test_split` function and use StandardScaler to standardize the numerical features.

```python
# Split the data into training and testing datasets
# Assign the function a random_state equal to 1
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# Create a StandardScaler instance
scaler = StandardScaler()

# Fit the scaler to the features training dataset
X_scaler = scaler.fit(X_train)

# Fit the scaler to the features training dataset
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)
```

#### Create a Neural Network Model to Predict Employee Attrition

Explain that, to predict employee attrition, we'll create a deep neural network model with two hidden layers. Cover the following points:

* We set a variable of `number_input_features` that is equal to the number of input features.

* We'll create a first hidden layer named hidden_nodes_layer1.

* There are many possible rules of thumb for selecting the number of nodes in each layer.

* For instance, one approach is to take the mean of the number of input features and the number of neurons in the output layer.

* Similarly, we can create a second hidden layer, `hidden_nodes_layer2`, where this time we take the mean of the number of hidden nodes defined for the first layer and the number of neurons in the output layer.

* Rules of thumb like these are a good place to start. From there, we can later fine-tune the performance of our model by making incremental adjustments to these values.

* Each hidden layer will contain the `relu` activation function.

* The model will predict a binary output (whether or not an employee leaves). That's why our output layer will have one neuron and use the sigmoid activation function.

  ```python
  # Define the the number of inputs (features) to the model
  number_input_features = len(X_train.iloc[0])

  # Define the number of hidden nodes for the first hidden layer
  # Use the mean of the number of input features and the number of output neurons
  # Use the Python floor division (//) to round down to the nearest integer
  hidden_nodes_layer1 =  (number_input_features + 1) // 2

  # Define the number of hidden nodes for the second hidden layer
  # Use the mean of the number of hidden nodes in the first hidden layer and the number of output neurons
  # Use the Python floor division (//) to round down to the nearest integer
  hidden_nodes_layer2 = (hidden_nodes_layer1 + 1) // 2

  # Create the Sequential model instance
  nn = Sequential()

  # Add the first hidden layer specifying the number of inputs, the number of hidden nodes, and the activation function
  nn.add(Dense(units=hidden_nodes_layer1, input_dim=number_input_features, activation="relu"))

  # Add the second hidden layer specifying the number of hidden nodes and the activation function
  nn.add(Dense(units=hidden_nodes_layer2, activation="relu"))

  # Add the output layer to the model specifying the number of output neurons and activation function
  nn.add(Dense(units=1, activation="sigmoid"))
  ```

* We display the structure of the model using the `summary` function.

  ```python
  # Display the Sequential model summary
  nn.summary()
  ```

  ![Preview of the neural network architecture](Images/nn_summary_turnover.png)

We compile the model using the  `binary_crossentropy` loss function, the `adam` optimizer, and the `accuracy` metric.

```python
# Compile the Sequential model
nn.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
```

#### Train and Evaluate the Neural Network Model

Finally, we train (fit) the neural network model with the training data and set the number of epochs to 100 (you could select a different number to start).

With the model fit, we evaluate it using the test data to determine its loss and accuracy.

```python
# Fit the model using 100 epochs and the training data
fit_model = nn.fit(X_train_scaled, y_train, epochs=100)

# Evaluate the model loss and accuracy metrics using the evaluate method and the test data
model_loss, model_accuracy = nn.evaluate(X_test_scaled,y_test,verbose=2)

# Display the model loss and accuracy results
print(f"Loss: {model_loss}, Accuracy: {model_accuracy}")
```

![Resulting test dataset accuracy](Images/accuracy_result_turnover.png)

Based on the preceding information, accuracy in the test dataset is at 0.837. This is lower than our training dataset accuracy levels which range from 85% to above 90%, depending on the epochs.

* Remind the students that we should expect somewhat lower test dataset performance because our model hasn't encountered or learned from this data before.

Ensure that there are no remaining questions about the code before moving on to the next activity.

---

### 11. Instructor Do: Multiclass Prediction in Deep Learning (15 min)

Use the slides as you explain to students that the very first step of building deep neural networks—or any machine learning model—is understanding what we're trying to predict. So far, we've covered how to predict two things:

* **Continuous variables**: When `y` is something like a stock return, the growth rate of a company, or other wide-ranging continuous number, our target variable is continuous.

  * We typically use regression-based approaches to predict variables which are continuous.

* **Binary variables**: In finance, there are many "Yes or No" type events that we want to predict. Will this customer default? Will the stock market crash next month? These answers are binary in nature: they either will or won't happen. We can even convert continuous variables to binary ones: the forecast of the percentage return on a stock for a month (a continuous variable) could be translated to a forecast of whether the market will go up or down (a binary variable).

  * Note that our models that try to predict `0` or `1` outcomes produce a probability of that event occurring, ranging from 0% to 100%. If the probability is greater than 50%, a model will categorize that row as a 1, or yes.

  * In some ML models, we use logistic regression to make predictions using **binary variables**. In deep neural networks, we use the softmax layer at the end of the model, which "squashes" the output to be within a range of 0 to 1. The probability of a particular observation then becomes either a 0 or a 1.

* **Categorical variables**: While a binary variable is technical a categorical variable with two possibilities, non-binary categorical variables are a more general concept. When `y` is a categorical variable, we're trying to predict among many outcomes. For example, we might try to predict the credit score ranking ("Bad", "Okay", "Good", "Great") to which a consumer belongs, or we might try to predict whether a public company's quarterly earnings will meet, beat, or "undershoot" what analysts and other stock market investors were predicting.

* To summarize, we have three types of models that correlate to three types of outcomes we're trying to predict: continuous, binary, or categorical.

Explain to the students that we'll build models for categorical outcomes next.

---

### 12. Everyone Do: Multiclass Prediction in Deep Learning Models (15 min)

Explain that we’ll now work together with a real life example of how to apply a multi-class neural network for predicting financial data.

**Corresponding Activity:** [06-Evr_Regression_And_Multiclass](Activities/06-Evr_Regression_And_Multiclass/)

**Files:**

* Unsolved:
  * [multiclass_in_deep_learning.ipynb (Unsolved)](Activities/06-Evr_Regression_And_Multiclass/Unsolved/multiclass_in_deep_learning.ipynb)
  * [Colab_multiclass_in_deep_learning.ipynb (Unsolved)](Activities/06-Evr_Regression_And_Multiclass/Unsolved/Colab_multiclass_in_deep_learning.ipynb)

* Solved:
  * [multiclass_in_deep_learning.ipynb (Solved)](Activities/06-Evr_Regression_And_Multiclass/Solved/multiclass_in_deep_learning.ipynb)
  * [Colab_multiclass_in_deep_learning.ipynb (Solved)](Activities/06-Evr_Regression_And_Multiclass/Solved/Colab_multiclass_in_deep_learning.ipynb)

* [meet_or_beat.csv (Company Earnings Data)](Activities/06-Evr_Regression_And_Multiclass/Resources/meet_or_beat.csv)

#### Preparing the Data

Explain that, In the world of public equity, companies must report their financial results to public investors every quarter. Because public investors are so interested in knowing financial results in advance, an industry of analysts specializes in making forecasts about future quarterly results.

* The above dataset, “meet_or_beat.csv”, includes information on the average analyst's quarterly earnings forecast (column name: 'forecasted_eps') plus the two-week total return prior to the announced earnings (column name: 'before_total_returns'). The latter might provide us with updated expectations that is priced in by the market prior to the earnings announcement (e.g. earnings released by other companies in the same industry are all lower than expected might put pressure on the stock price of this company in the 2 weeks prior to the announcement).

* Using historical data on approximately 5,000 stocks for quarterly earnings from 2016–2021, we'll construct a deep neural network to see if we can use this information to predict the actual earnings results.

* The difference here is that our `y` variable will be categorical with three categories:

  * The company had earnings equal to the average analyst forecast (meet)
  * It had results that were better than forecast (beat)
  * It has results that were worse than forecast (lose)

    ```python
    df['earnings_outcome'] = np.nan
    df.loc[(df['EPS']==df['forecasted_eps']), 'earnings_outcome'] = 'meet'
    df.loc[(df['EPS']>df['forecasted_eps']), 'earnings_outcome'] = 'beat'
    df.loc[(df['EPS']<df['forecasted_eps']), 'earnings_outcome'] = 'lose'
    ```

* This outcome variable, `earnings_outcome`, will be the categorical variable that we're trying to predict:

  ```python
  # Preview the output variable
  y = df['earnings_outcome']
  y
  ```

  ![meet_beat_lose_y_preview](Images/meet_beat_lose_y_preview.png)

Point out to students that this variable takes on three unique possibilities, instead of just the `0` or `1` they're used to seeing previously.

* Keras has some special fixes to deal with this type of categorical outcome, including a built-in method to explicitly declare our `y` data to be categorical.

* To start, we encode our data into labels:

  ```python
  # Encode earnings labels to integers
  from sklearn.preprocessing import LabelEncoder
  encoder = LabelEncoder()
  encoder.fit(y)
  encoded_y = encoder.transform(y)
  encoded_y
  ```

* Label encoding tells Keras that it's working with a certain type of data object, but we still need to explicitly convert our `y` variable to categorical.

* It helps if we keep track of the number of unique categories for our categorical `y` variable:

  ```python
  # Save the unique number of labels for future use
  number_of_classes = len(list(y.drop_duplicates()))
  number_of_classes
  ```

* With the "number_of_classes" saved (`3`), we can explicitly convert our `y` variable to a category variable:

  ```python
  # Convert labeled integers to a Keras `categorical` data type
  from keras.utils.np_utils import to_categorical
  y_categorical = to_categorical(encoded_y, num_classes=number_of_classes)
  ```

* We're done with `y`, and now we can set up our `X` data. We'll skip standardization for the moment. Because none of the `X` variables are categorical, we don't need to use `OneHotEncoder` on the `X` data.

  ```python
  # Specify X (predictor) variables
  X = df[['forecasted_eps',
                'before_total_returns','noOfEsts']]
  X.head(3)
  ```

  ![Preview of the X DataFrame](Images/x_dataframe_preview.png)

* With `X` and `y` (or rather, `y_categorical`) defined, we `train_test_split` our data:

  ```python
  # Split into training and testing windows
  from sklearn.model_selection import train_test_split
  X_train, X_test, y_train, y_test = train_test_split(X, y_categorical, random_state=1)
  ```

* After previewing the result and checking the frequency count of each category, we notice a class imbalance. (We'll look at some ways to correct for class imbalance on this dataset in future activities, but for now we'll let it be).

  ```python
  # Preview the encoded data we're trying to predict
  pd.DataFrame(y_train).head(5)

  # Check for class balance
  pd.DataFrame(y_train).sum()
  ```

* We're almost ready to build the neural network. But first, we should save the number of initial target features as a variable:

  ```python
  # Save the count of unique predictor variables for use in model
  number_of_predictors = len(X.columns)
  len(X.columns)
  ```

#### Building, Fitting, and Predicting with Multiple Classes

* Now we can build the model. We'll make two intermediate layers, both with ReLU activation layers. The first layer has an input dimension equal to the number of target features:

  ```python
  # Build the neural network layers
  model = Sequential()
  model.add(Dense(9, input_dim=number_of_predictors, activation='relu'))
  model.add(Dense(6, activation='relu'))
  ```

* This is similar to what we've seen for previous neural networks. But with multi-class predictions, the final activation layer in a neural network will be different.

* Instead of sigmoid, which condenses the final layer into a 0 or 1 choice, we will use `softmax`, which is specifically designed for classification problems with many labels.

* In addition, we set the number of output possibilities equal to the number of possible classes.

  ```python
  # Add the final output layer
  # With the # of possible outputs equal to the number classes
  model.add(Dense(number_of_classes, activation='softmax'))
  ```

* In previous models, we used either `binary_crossentropy` as our loss function (for binary outcomes) or `mean_squared_error`(for continuous outcomes). Explain to students that whenever we have multiple categories to predict, we also need to change our loss function to `categorical_crossentropy`.

  * **Categorical cross-entropy** is a way for the model to better distinguish differences between the different categorical outcomes.

* As with previous models, we can use the same optimizer (`adam`) and view the same metrics (`accuracy`).

  ```python
  # Compile the model (with multi-class specific parameters)
  model.compile(loss="categorical_crossentropy",
                optimizer= "adam",
                metrics=['categorical_accuracy'])

  # Summarize the structure of the model
  model.summary()
  ```

* The fit and evaluate aspects of the neural networks remain the same, regardless of whether we're working with binary or multi-class outcomes:

  ```python
  # Fit the model
  model.fit(X_train,y_train,
                      epochs=20,
                      batch_size=1000,
                      shuffle=True)

  # Evaluate model on the test data
  model.evaluate(X_test,y_test, verbose=2)
  ```

* However, another difference in multi-class predictions occurs in the form of the output from the `predict` method.

* Here, calling `predict` to make predictions using the `X_test` data results in a probability for  a specific observation to fall into one of the  classes (meet, beat, or lose).

  ```python
  # Save predictions on the test data
  predictions = model.predict(X_test)
  predictions
  ```

  ![Preview of predictions of probability for each category](Images/categ_prob_test_predictions.png)

* The preceding output shows an array, with three predictions for each single row of data—the probability of beat, meet, or lose, respectively. What we really care about is the highest probability prediction for each earnings release. NumPy's `argmax` function will do that for us by retrieving the array index for each row that contains the maximum value:

  ```python
  # Get the most likely prediction for each observation
  most_likely = np.argmax(predictions, axis=1)
  most_likely
  ```

* Our `most_likely` array contains the most likely outcome for each row. But it's a little hard to read because the label is still encoded. For example, a `beat` label is represented by a 0. We can use `inverse_transform` to make our label predictions more reader-friendly:

  ```python
  # Convert most likely category back to original labels
  most_likely = encoder.inverse_transform((most_likely))
  most_likely
  ```

  ![Labeled Predictions Displayed](Images/categorical_predictions_labeled.png)

* And if we convert these label predictions into a DataFrame, we can do useful things with them, like tabulate our predictions by category:

  ```python
  # Evaluate prediction balance
  pd.DataFrame(most_likely).value_counts()
  ```

* Based on the predictions in the preceding image, we apparently have a rather optimistic neural network. Most of the time, it predicts that the company will beat the analysts' forecasts. This may have something to do with our class imbalance, but we'll leave that issue for future work. For now, the focus is on making multi-category prediction models.

---

### 13. Wrap-Up (5 min)

This lesson may have been challenging for the students because they were presented with several new concepts. Spend a few minutes reflecting on what they've learned.

The students have now experienced how Keras empowers them to create deep learning models using relatively few lines of code. Because the framework simplifies the coding process, we'll have more time to understand the underlying business problem that we're solving with a neural network.

Using neural networks to solve real business problems is a process of iteration where we deploy these models and continually improve them. In the next class, we will learn how to save our models both for practical deployment as well as for future iterative improvements.

---

### End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
