## 13.1 Lesson Plan: Neural Networks

### Overview

This class introduces the students to powerful machine learning algorithms called neural networks. Neural networks can learn to make predictions based on datasets that are too large and complex for other types of machine learning algorithms to process. The students will gain an understanding of neural networks and how they work. They will also learn how to fit a basic neural network to financial data. The other classes this week will cover the use of TensorFlow and Keras to produce deeper and more robust neural networks.

The original developers of the neural network concept were inspired by how neurons work in the human brain. Neural networks can also be made to scale based on the complexity of the calculations or environment, similar to how the brain engages different regions as needed.

Neural networks can be used for many applications, but they are not necessarily meant to be "plug and play." The students will learn the complete process of building and using neural networks, from preprocessing input data to constructing a neural network architecture.

### Class Objectives

By the end of this lesson, the students will be able to:

* Explain the concept of neural networks, including how a neuron is related to logistic regression.

* Explain the intuition of how weights of neurons are determined.

* Describe some of the differences between neural networks involving regression versus those involving classification.

* Preprocess data for neural network models.

* List the Python libraries available for building neural networks.

* Describe the pros and cons of using Keras for building neural networks.

* Implement neural networks with the TensorFlow Keras API.

### Instructor Notes

* **VERY Important:** Some machines will not install or run Tensorflow due to hardware incompatibilities. This is most prevalent for Apple Silicon M1 computers. The simplest solution is to have these students run their notebooks in [Google Colab](https://colab.research.google.com/) which comes with support for TensorFlow. Generally, the notebook can be uploaded and run in Colab without any changes. Where changes are necessitated, specific Colab compatible notebooks have been included in the activity files.

* **Important:** Slack out the [Deep Learning Installation Guide Folder](../Supplemental/Deep_Learning_Installation_Guide) for installing TensorFlow prior to today's class. The students need to install all components before class to conserve time for lessons and activities.

* In addition to teaching the steps for implementation, today's activities include concepts that the students should be prepared to think about and discuss.

* Let the students ask questions during activities, but you might need to defer some questions for the review sessions or office hours.

* This class should be fun because we will be playing with neural networks to experiment with input, architecture, and algorithms.

* A thorough understanding of neural networks requires math that is beyond the scope of this class. Luckily, the students can implement a neural network while only having an intuitive understanding of the underlying algorithms. You will need to skim or even skip certain details, but we will provide additional materials for students who want to dig deeper.

* In the introduction to neural networks, you'll go over a demo using the [Quick, Draw! web application](https://quickdraw.withgoogle.com). Practice the demo before class.

### Class Slides and Time Tracker

You can view the slides for this lesson on Google Drive here: [Lesson 13.1 slides](https://docs.google.com/presentation/d/1wPPpgdCUauk5-xls9YwlXe7UuLZcepyPlQbkdtFwyjw/edit?usp=sharing).

To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

**Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy."

You can view the time tracker for this lesson here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome the Class (5 min)

Open the lesson slides and welcome the students to the first day of deep learning! Indicate that today's class will begin with an introduction to the basic unit of neural networks before moving on to constructing simple neural nets.

To help the students get ready to learn, open the class by asking the following questions.

* **Question:** What do you think a neural network is?

  * **Sample Answer:** It's a computer representation of a human neuron.

  * **Sample Answer:** It's a method to create artificial intelligence software.

  * **Sample Answer:** Neural networks are machine learning algorithms that can learn to solve a problem.

* **Question:** Do you know some cool applications of neural networks?

  * **Sample Answer:** Autonomous (self-driving) cars.

  * **Sample Answer:** Image processing in cancer detection.

  * **Sample Answer:** Banning inappropriate content on social networks.

  * **Sample Answer:** Automated trading based on artificial intelligence.

Ask two or three students to share their insights, and explain that this class will answer these questions.

Ask the students if they have additional questions before moving on.

---

### 2. Instructor Do: Homework Preview (10 min)

In this activity, you will conduct a demonstration of the homework.

**Files:**

* [README.md](../../../02-Homework/13-Neural-Networks/README.md)

Open the lesson slides, go to the "Homework Demo" section, and highlight the following information.

* Explain to the students that the venture capital industry uses data and models to determine how to make investments.

* In this homework assignment, the students will take on the role of a venture capital analyst. They will use models to quantify the factors that lead to investing success and to evaluate future deals.

* Using data on more than 34,000 organizations that have received funding, the students will create a neural network model that will predict whether an applicant will become a successful business.

Open the homework solutions, and then explain to the students that they will learn how to build, evaluate, and optimize deep neural networks by using a "model-fit-predict" pattern.

Answer any questions before moving on.

---

### 3. Instructor Do: What Is a Neural Network? (10 min)

Use the slides as you go through the following background concepts in neural networks.

* Neural networks, also known as artificial neural networks (ANN), are a set of algorithms that are modelled after the human brain. They are an advanced form of machine learning that recognizes patterns and features of input data and provides a clear quantitative output.

* In its simplest form, a neural network contains layers of neurons that perform individual computations. These computations are connected and weighed against one another until the neurons reach the final layer. In the final layer, the neurons return either a numerical result or an encoded categorical result.

* Using a neural network instead of a traditional statistical or machine learning model provides many advantages:

  * Neural networks can detect complex relationships within datasets.

  * Neural networks are versatile. They can be used to predict future shopping behaviour based on credit card transactions or to assess a loan applicant's likelihood of defaulting on a loan based on their application.

  * Neural networks have a greater tolerance for messy data. They can learn to ignore noisy characteristics within a large dataset.

Explain to the students that there are two primary disadvantages to using a neural network.

* Neural network algorithms can be too complex for humans to understand. This is an example of something known as a "black box" problem, where the inputs are not visible to the user and the resulting output cannot be traced back to discover the logic that was used.

* Neural networks are more likely to overfit the data. Overfitting occurs when a model gives too much importance to patterns within the training data that are not found in the test data. This results in a model learning the training data so well that it cannot create generalizations about other data.

* Fortunately, we can use different model designs and optimization techniques to compensate for and negate both of these disadvantages. We will review how to do this later in the module.

Use the slides as you point out that neural networks serve multiple purposes in the finance industry.

* Fraud detection: According to [Javelin Strategy & Research](https://www.javelinstrategy.com/coverage-area/future-proofing-card-authorization), $118 billion worth of credit card transactions are incorrectly identified as fraud and declined every year. Neural networks can efficiently evaluate the characteristics of a credit card transaction or loan application, allowing financial firms to predict fraud with more accuracy. This saves time and money.

* Risk management: The banking sector, insurance industry, and stock exchanges are all building more robust and efficient techniques for credit management using neural networks.

* Money laundering prevention: A [United Nations study](https://www.unodc.org/unodc/en/money-laundering/overview.html#:~:text=The%20estimated%20amount%20of%20money,goes%20through%20the%20laundering%20cycle) estimates that money laundering activity around the world accounts for 2–5% of annual global GDP (gross domestic product). Financial institutions now use neural nets as a tool in their fight against financial crime.

* Algorithmic stock trading: Thanks to trading algorithms that incorporate neural networks, you can automate your trading strategies and increase your trading profits.

Explain that, before we start getting into the code, let's review the components of a neural network and how they work together to learn.

#### Perceptron, the Computational Neuron

Artificial neural networks have become popular in recent years, but the original design for a computational neuron, known as a **perceptron**, dates back to the late 1950s.

The perceptron model mimics a biological neuron by receiving input data, weighting the information, and producing a clear output.

Use the slides while explaining that the perceptron model has four major components:

* **Input values** that are typically labelled as **x**.

* A **weight coefficient** for each input value. This is typically labeled **w** or **&omega;** (omega). The weight coefficient determines the input value’s strength—the impact the input value has on the network.

* A constant value called **bias** that gets added to the inputs to help best fit the model for a given dataset. It is typically labeled **w<sub>0</sub>**.  Bias is an adjustment made to the model to make the model either more or less sensitive.

* A **net summary function** that aggregates all weighted inputs (note that the following diagram shows a weighted summation).

Explain that a modern neural network model is a structure composed of several connected perceptrons that learn from input data to produce an output.

Use the slides to explain how to combine perceptrons to form a neural network model. A basic neural network contains three layers:

* An input layer of input values transformed by weight coefficients.

* A hidden layer that can contain a single neuron or multiple neurons.

* An output layer that reports the outcome of the value.

  ![A diagram depicts three input nodes that connect to a hidden layer, which then connects to an output layer.](Images/13-1-simple-neural-network.png)

#### Activation Functions

Explain that neural networks link neurons that process input together to produce a clear, quantitative output. An **activation function** combines all these outputs into a single classifier or regression model.

* When building a model, we apply the activation function to the end of each neuron (each individual perceptron model). This mathematical function transforms each neuron’s output into a quantitative value.

* The quantitative output value becomes the input value for the next layer in the neural network model.

  ![A diagram depicts a perceptron model with an activation function.](Images/13-1-activation-function.png)

Explain that a wide variety of activation functions exist, and each has a specific purpose. However, most neural networks will use one of the following activation functions:

* The **linear function** returns the sum of the weighted inputs without transformation.

* The **sigmoid function** transforms the neuron’s output to a range between 0 and 1, which is especially useful for predicting probabilities. A neural network that uses the sigmoid function will output a model with a characteristic S-curve.

* The **tanh function** transforms the output to a range between -1 and 1. The output for a model using a tanh function also forms a characteristic S-curve. Its primary use is classifying data into one of two classes.

* The **rectified linear unit (ReLU) function** returns a value from 0 to infinity. This activation function transforms any negative input to 0. It is the most commonly used activation function in neural networks due to its faster learning and simplified output. However, it is not always appropriate for simpler models.

* The **leaky ReLU function** is an alternative to the ReLU function, which can sometimes work better Instead of transforming negative input values to 0, it transforms them into much smaller negative values.

> **Deep Dive** When designing a neural network, developers usually test different activation function combinations. You can learn more about the formulas and the mathematical fundamentals behind each function from this [Wikipedia article](https://en.wikipedia.org/wiki/Activation_function) and from the [ML Glossary’s “Activation Function” sections](https://ml-cheatsheet.readthedocs.io/en/latest/activation_functions.html).

---

### 4. Instructor Do: Neural Networks Are Cool! (30 min)

In this section, you will introduce students to neural networks and some of their applications.

**Instructor Note** This section will incorporate Google's [Quick, Draw! web application](https://quickdraw.withgoogle.com) and the [Google AI Experiments website](https://experiments.withgoogle.com/collection/ai). Depending on the available time, you should give the students 5–10 minutes to play with the Google AI Experiments website as part of the following discussion. The students do not need to work in groups for this activity.

Start the presentation by displaying the following image from the [Rorschach Inkblot Test](https://en.wikipedia.org/wiki/Rorschach_test) and asking the students what they think it looks like.

  ![Rorschach Test Card](./Images/Rorschach_blot_05.jpg)

Allow the class to play around for a few seconds as they share their answers, then continue the presentation by noting that there is no precise answer to this question. Cover the following points:

* We can find similarities between this image and a real object because our brain uses thousands of neuron connections to find a match between the visual input and a mental representation of an object.

  ![How the brain works](./Images/how-the-brain-works.png)

* The ability of the brain to process information and make predictions or interpretations is what inspired neurophysiologists and mathematicians to start the development of artificial neural networks (ANN).

  ![a neuron](./Images/a-neuron.png)

* In the same way that biological neurons receive input signals through the dendrites, an ANN receives input variables and processes them using an activation function. The output of an ANN is similar to the neuron nucleus in the brain.

* [Warren McCulloch and Walter Pitts presented](https://doi.org/10.1007/BF02478259) the concept of ANNs for the first time in 1943 when they created a computational model for neural networks using electrical circuits.

* From that initial idea of a single neuron, the concept evolved in the last decades into more complex models that create connections between neurons—what we know today as neural networks.

Highlight the following points.

  ![neural network history](./Images/history-nn-1982-present.png)

* Neural networks are here to stay, and their applications become more common every day.

* Companies like Google (Waymo) and Tesla are using neural networks to develop self-driving cars.

* The power of neural networks allows you to communicate in any language thanks to automated tools that can perform real-time translation (Google Translate, Skype, etc.).

* Black and white photos can gain a new context through automatic image colourization.

* Neural networks are also used to help create a better world, not only for humans but for wildlife. For example, the U.S. National Oceanic and Atmospheric Administration is helping to save Right whales (a species of whale) by tracking their North Atlantic population using neural networks for image recognition.

Explain to the students that the financial sector is a leader in the use of neural networks.
Let the students know that they will be introduced to the components that comprise a neural network and how they work together to learn. The deep mathematical concepts behind neural networks are beyond the scope of today's class.

Next, open the [Quick, Draw! Web application](https://quickdraw.withgoogle.com) in your browser and slack out the URL to the students. Explain that they are going to play a short game powered by neural networks to illustrate how clever such models can be.

* _Quick, Draw!_ is an application that can identify an image from a trace.

* The game asks you to draw something in less than 20 seconds while the machine learning algorithm tries to guess what the trace could be.

  ![Quick,Draw! demo](./Images/quick-draw.gif)

Draw a couple of traces in the game, and tell the students that this is an example of the power of neural networks in real time. Even though this example is only a game, neural networks and machine learning have transformed fintech. Advances in machine learning are powering applications that were once considered to be science fiction.

Ask the students to visit the [Google AI Experiments website](https://experiments.withgoogle.com/collection/ai) and then select an experiment to try. After 5–10 minutes, ask for volunteers to share what they discovered with the class.

Answer any questions before moving on.

---

### 5. Instructor Do: Creating a Neural Network in Keras (15 min)

**Corresponding Activity:** [01-Evr_Keras_Intro](Activities/01-Evr_Keras_Intro)

In this section, the students will be introduced to the Keras library and learn how to build neural networks with it.

**Files:**

* [artificial-neuron.ipynb](Activities/01-Evr_Keras_Intro/Solved/artificial-neuron.ipynb)

Use the slides to explain the following points.

* There are two ways to code a neuron:

  * You can do all the math and code it from scratch using Python, Pandas, and NumPy.

  * Or, you can use an industry-standard API or framework to speed up your implementation and focus your efforts on improving your model. This allows you to spend more time learning about the business problem you want to solve.

* We are going to use [TensorFlow](https://www.tensorflow.org/) and [Keras](https://keras.io/) to build our neural networks.

* TensorFlow is an open-source platform for machine learning that allows us to run our code across multiple platforms in a highly efficient way.

* Keras is an abstraction layer on top of TensorFlow that makes it easier to build models. You can relate this to using Plotly Express to create charts instead of using the more verbose Matplotlib library.

* With Keras and TensorFlow, we can use the standard `model -> fit -> predict` interface.

Verify that the students have already installed TensorFlow. If some have not, slack out the [Deep Learning Installation Guide](../Supplemental/Deep_Learning_Installation_Guide/deep_learning_installation_guide.md) and ask your TAs to assist students while you start the demonstration.

Open the unsolved version of the Jupyter Notebook, then explain to the students that you are going to demo how to create a neural network with a single neuron using Keras. Slack out the unsolved version of the Jupyter notebook and encourage the class to follow along as you live-code.

* We will use Keras through TensorFlow, so our first step is to import the Keras modules:

  ```python
  from tensorflow.keras.models import Sequential
  from tensorflow.keras.layers import Dense
  ```

* There are two types of models in Keras.

  * The `Sequential` model is a linear stack of layers in which data flows from one layer to the next.

  * The functional `Model` class allows us to create sophisticated and more customizable models.

* Today, we'll use the `Sequential` model with the `Dense` class to add layers to the neural network.

Explain that we will start by coding a neural network with a single neuron to solve a binary classification problem.

* First, we create a dummy dataset using the `make_blobs` function from `sklearn`.

  ```python
  X, y = make_blobs(n_samples=1000, centers=2, n_features=2, random_state=78)
  ```

* This dummy dataset contains 1000 samples with two features that are split into two groups.

* As part of our data preprocessing, we transform `y` into a vertical vector.

  ```python
  # Transforming y to a vertical vector
  y = y.reshape(-1, 1)
  y.shape
  ```

* We create a DataFrame with the dummy data to generate a plot using Pandas' `plot()` method.

  ```python
  # Creating a DataFrame with the dummy data
  df = pd.DataFrame(X, columns=["Feature 1", "Feature 2"])
  df["Target"] = y

  # Plotting the dummy data
  df.plot.scatter(x="Feature 1", y="Feature 2", c="Target", colormap="winter")
  ```

  ![Two blobs dummy data](Images/neuron-two-blobs.png)

* As we do with other machine learning algorithms, we split the data into training and testing datasets.

  ```python
  X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=78)
  ```

Explain to the students that we must normalize or standardize the data before using a neural network.

* Neural networks typically perform better when each of the input features are on the same scale. This makes it easier for the network to stabilize and adjust the weights of the data.

* We can use scikit-Learn's `MinMaxScaler` or `StandardScaler` to scale and normalize input features. Here, we'll use StandardScaler to scale the features data. There is no need to scale the target data (`y`) because it's already encoded as 0 and 1.

  ```python
  # Create scaler instance
  X_scaler = StandardScaler()

  # Fit the scaler
  X_scaler.fit(X_train)

  # Scale the data
  X_train_scaled = X_scaler.transform(X_train)
  X_test_scaled = X_scaler.transform(X_test)
  ```

Explain that after we have scaled the data, we can create our first neural network.

* First, we create an instance of the Sequential model in the `neuron` variable.

  ```python
  neuron = Sequential()
  ```

* The neuron variable will store the architecture of our model.

* The next step is to add the first layer of our neural network using the `add()` method and the `Dense()` class.

  * **Note**: The following graph is for illustrative purposes only and does not match the number of inputs in our code.

  ![First Layer](Images/tensorflow-neuron-layer-1.png)

  ```python
  # First layer
  number_inputs = 2
  number_hidden_nodes = 1

  neuron.add(Dense(units=number_hidden_nodes, activation="relu", input_dim=number_inputs))
  ```

Explain to the students that we use the `Dense()` class to add layers to the neural networks. Because this is the first layer, we define the number of inputs in the `input_dim` parameter and the number of neurons in the first hidden layer in the `units` parameter.

* The `activation` parameter defines the activation function that will process the values of the input features as they are passed to the first hidden layer. In this demo, we are using the [rectified linear unit (ReLU) function](https://keras.io/activations/#relu).

* By adding an activation function in this first layer, we introduce nonlinearity and enable our neural network to learn about nonlinear relationships as it trains on the data.

* We complete the construction of our neural network by adding the output layer:

  ![Output layer](Images/tensorflow-neuron-output-layer.png)

  ```python
  # Output layer
  number_classes = 1

  neuron.add(Dense(units=number_classes, activation="sigmoid"))
  ```

* We use the `sigmoid` activation function for the output layer. There are no inputs to define, and we only specify the number of units that we want.

* The `summary()` method shows the architecture of the neural network model:

  ![Neuron summary](Images/tf_neuro_summary.png)

Explain to the students that after we define the structure of the model, we will compile it using a loss function and optimizer. But first, let's practice building a neural network for some consumer credit card data.

Answer any questions before moving on.

---

### 6. Student Do: Preventing Credit Card Defaults, Part 1 (20 min)

**Corresponding Activity:** [02-Stu_CC_Default](Activities/02-Stu_CC_Default)

In this activity, the students will use Keras and several features (variables) to build a neural network model that predicts whether a credit card customer will default on their debt.

**Instructions:**

* [README.md](Activities/02-Stu_CC_Default/README.md)

**Files:**

* [preventing_credit_card_defaults_part1.ipynb](Activities/02-Stu_CC_Default/Unsolved/preventing_credit_card_defaults_part1.ipynb)

* [Colab_preventing_credit_card_defaults_part1.ipynb](Activities/02-Stu_CC_Default/Unsolved/Colab_preventing_credit_card_defaults_part1.ipynb)

---

### 7. Instructor Do: Review Preventing Credit Card Defaults, Part 1 Solutions (10 min)

**Files:**

* [preventing_credit_card_defaults_part1.ipynb](Activities/02-Stu_CC_Default/Solved/preventing_credit_card_defaults_part1.ipynb)

* [Colab_preventing_credit_card_defaults_part1.ipynb](Activities/02-Stu_CC_Default/Solved/Colab_preventing_credit_card_defaults_part1.ipynb)

Go through the solution and highlight the following points.

* After we read in the data, we create `X` by using every column except the `y` variable ("DEFAULT"):

  ```python
  # Define features set X by selecting all columns but DEFAULT
  X = cc_df.drop(columns=["DEFAULT"]).copy()
  ```

* We use `DEFAULT` to create the `y` target variable:

  ```python
  # Define target set by selecting the DEFAULT column
  y = cc_df["DEFAULT"]
  ```

* With `X` and `y` built, we can use `train_test_split` from scikit-learn to automatically build training and testing datasets:

  * **Note**: To create a repeatable result, we set `random_state to`1`. The students may get slightly different results if they didn't set this value.

  ```python
  # Create training and testing datasets using train_test_split
  # Assign the function a random_state equal to 1
  X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
  ```

* After we create the training and test datasets, we scale them using the `StandardScaler()` function.

* Point out that we fit the scaler on the `X` training data only, but we transform both the training and test `X` data. This approach prevents us from accidentally using information from the test data when building our model on the training data. StandardScaler scales values by the standard deviation of the data, so using `fit` on only the training data prevents information from the test dataset to leak in.

* Next, we can define our neural network model. This neural network has two layers: an intermediate layer and a final sigmoid layer to produce an output that ranges from `0` to `1`, representing the probability of default:

  ```python
  # Define the number of inputs to the model
  number_inputs = 22

  # Define the number of hidden nodes for the model
  number_hidden_nodes = 12

  # Create the Sequential model instance
  neuron = Sequential()

  # Add a Dense layer specifying the number of inputs, the number of hidden nodes, and the activation function
  neuron.add(Dense(units=number_hidden_nodes, input_dim=number_inputs, activation="relu"))

  # Add the output layer to the model specifying the number of output neurons and activation function
  neuron.add(Dense(1, activation="sigmoid"))
  ```

* Finally, we can use the `summary` function to see a summary of our model, including the number of layers, the output shape of each layer, and the total number of parameters.

  ```python
  # Display the Sequential model summary
  neuron.summary()
  ```

Answer any questions before moving on.

---

### 8. Break (15 min)

---

### 9. Instructor Do: Building, Fitting, and Predicting a Neural Network Model (20 min)

**Corresponding Activity:** [03-Ins_Fit_Predict](Activities/03-Ins_Fit_Predict)

In this activity, the students will learn about Keras and how they can use this library to start building neural networks.

**Files:**

* [Fit_Predict_Network.ipynb](Activities/03-Ins_Fit_Predict/Solved/Fit_Predict_Network.ipynb)

#### Compiling a Neural Network Model

Explain to the students that the next step is compiling the model.

* Here is an analogy: Defining the neural network’s structure is like designing blueprints for a house, and compiling the model is like building the house.

Use the slides as you explain the following concepts.

To compile and fit a model, we need to specify **loss** and **optimization** functions.

* When we train our neural network model on a dataset, we pass our training dataset through the model multiple times. The loss function allows us to observe how the model’s performance changes over each iteration. We can then determine when the model reaches maximum performance (after a specific number of iterations).

* The optimization function shapes and moulds a neural network model while the model is trained on the data. This ensures that the model performs to the best of its ability. An optimization function reduces the model’s losses and provides the most accurate output possible.

When we fit the model, we also want to keep track of two evaluation metrics: **accuracy** and **mean squared error (MSE)**.

* We use model predictive accuracy (`accuracy`) for classification models that are designed to answer "whether or not" questions. A higher accuracy value indicates more accurate predictions, and the highest possible accuracy value is 1. We would use a classification model to predict if a borrower is likely to default on a loan.

* We use MSE (`mse`) for regression models in which we're trying to predict some continuous outcome, like the percentage stock return for the next day. As the MSE gets closer to 0, the model’s predictions become increasingly accurate.

* Open up the Instructor Do notebook, which continues from where the previous instructor activity ended.

* Remind the students that we defined a variable called `neuron` to store our initial neural network model. To compile the model, we use the `compile()` function provided by Keras, as the following code shows:

  ```python
  neuron.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
  ```

Explain that we’ll now examine the three parameters we pass to the `compile()` function.

* In this demonstration, we use the `binary_crossentropy` loss function because it is designed to deal with binary (yes or no) classification problems.

* We use the `adam` optimizer because it usually finds a good balance between speed and quality when it's searching for the best model fit.

We have created and compiled our neural network model, and that completes the “model” step in our model-fit-predict pattern. So, let’s move on to “fit.”

* To fit our Keras model, we'll use the `fit` function and provide the `X` and `y` training values and the number of **epochs**.

* In machine learning, an epoch is a single pass of the entire training dataset through the model. Sometimes an epoch is loosely defined as an iteration of a model.

* When we fit (train) a neural network model, we use the optimizer and loss functions to adjust the weights of each input during each epoch of the training cycle. In the following code, we fit our model using 50 epochs:

  ```python
  # Fitting the model
  model = neuron.fit(X_train_scaled, y_train, epochs=100)
  ```

The next image shows the results of the model fitting process:

![Screenshot depicts the optimizer, loss, and accuracy results from the first 10 epochs of a training cycle.](Images/13-1-fitting-a-neural-network.png)

* Note that we store the training results on the `model` variable.

While the model is running (it may take a minute or two), explain to the students that it is common to evaluate a neural network model after it’s fit but before using it to make predictions. This still matches our model-fit-predict pattern. Next, we will learn some techniques to assess the accuracy of a model.

After the training cycle ends, we can evaluate the model by plotting the loss function and the accuracy across all epochs.

* To create the plots, we first create a DataFrame using the `history` dictionary of the training results stored on the model variable. (This is a dictionary that gets automatically created when we fit a neural network).

* The `history` dictionary stores the loss and accuracy results of all epochs. The following code creates the DataFrame and the two plots:

  ```python
  # Create a DataFrame with the history dictionary
  df = pd.DataFrame(model.history, index=range(1, len(model.history["loss"]) + 1))

  # Plot the loss
  df.plot(y="loss")

  # Plot the accuracy
  df.plot(y="accuracy")
  ```

As the following image of the resulting plots shows, the loss function decreases and the accuracy increases as the model progresses through more epochs:

![ A screenshot depicts the resulting loss function and accuracy plots.](Images/13-1-plotting-loss-and-accuracy.png)

* Explain to the students that we can use loss and accuracy plots to assess how a model’s performance changes as the number of epochs increases. If a model’s performance improves as it progresses through more epochs, its accuracy should trend toward 1, and the loss should trend toward 0.

* These types of loss and accuracy plots (shown above) compare how well different models perform when solving the same problem.

Explain that now that we have trained our model and assessed its loss and accuracy, we can evaluate its performance using the test data. Ultimately, performance on test or otherwise new and unseen data is what really matters.

* Testing a neural network model in TensorFlow is similar to testing a machine learning model in scikit-learn.

* For this demonstration, we'll use the `evaluate` function. Then, we’ll print the testing loss and accuracy values, as shown in the code that follows:

  ```python
  # Evaluate the model using testing data
  model_loss, model_accuracy = neuron.evaluate(X_test_scaled, y_test, verbose=2)

  # Display evaluation results
  print(f"Loss: {model_loss}, Accuracy: {model_accuracy}")
  ```

This code returns the following results:

![A screenshot depicts the returned testing loss and accuracy values.](Images/13-1-evaluating-a-neural-network.png)

Explain to the students that they now know how to create a neural network model, train it, and evaluate its accuracy. They'll put all of this into practice in the next activity.

---

### 10. Student Do: Preventing Credit Card Defaults, Part 2 (Building, Fitting, and Predicting a Neural Network Model) (20 min)

In this activity, the students will continue working on the neural network model that they created in the previous activity. They will compile, fit, and evaluate their model that predicts credit card defaults.

**Instructions:**

* [README.md](Activities/04-Stu_CC_Default_Part_2/README.md)

**Files:**

* [preventing_credit_card_defaults_part2.ipynb](Activities/04-Stu_CC_Default_Part_2/Unsolved/preventing_credit_card_defaults_part2.ipynb)

* [Colab_preventing_credit_card_defaults_part2.ipynb](Activities/04-Stu_CC_Default_Part_2/Unsolved/Colab_preventing_credit_card_defaults_part2.ipynb)

---

### 11. Instructor Do: Review Preventing Credit Card Defaults, Part 2 Solutions (15 min)

**Files:**

* [preventing_credit_card_defaults_part2.ipynb](Activities/04-Stu_CC_Default_Part_2/Solved/preventing_credit_card_defaults_part2.ipynb)

* [Colab_preventing_credit_card_defaults_part2.ipynb](Activities/04-Stu_CC_Default_Part_2/Solved/Colab_preventing_credit_card_defaults_part2.ipynb)

Go through the solution and highlight the following information.

* The dataset consists of 22 features about each borrower and a column corresponding to whether they have defaulted on their credit card payments.

* We reviewed Part 1 of the notebook in the previous activity, so we can run these cells now and skip to Part 2.

* The first line of code in Part 2 compiles and builds the model and prepares it for fitting.

  ```python
  # Compile the Sequential model
  neuron.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
  ```

* Now that the model is built, we fit it using the data:

  ```python
  # Fit the model using 100 epochs and the training data
  model = neuron.fit(X_train_scaled, y_train, epochs=100)
  ```

* It will take a minute or two for the model to finish running. Use this time to remind students about what's currently happening:

* The model adjusts itself to best learn the data during the fitting process.

* The model uses only a portion of the training dataset during each run. Each time the model finishes cycling through the entire training dataset is known as an epoch.

* As each epoch completes, the model finds more parameters which best explain what's going on in the data. That's why we usually observe that loss decreases and accuracy steadily increases—up to a point—as the model runs.

* We can check the model's performance as it goes through these epochs using the `model.history` attribute. Converting that data to a `DataFrame` makes it easier to plot.

  * Because a `loss` value is generated each time an epoch occurs, we can use the `len` of those recorded losses to create an index with the correct number of entries for the plot.

  ```python
  # Create a DataFrame using the model history and an index parameter
  model_plot = pd.DataFrame(model.history, index=range(1, len(model.history["loss"]) + 1))
  ```

* With the `DataFrame` built, we can easily plot and label it, starting with just the `loss` column:

  ```python
  # Vizualize the model plot where the y-axis displays the loss metric
  model_plot.plot(y="loss")
  ```

* We can plot the `accuracy` column separately. Note that the accuracy levels off after a certain number of epochs, similar to the loss plot. When we decide on a final model, we should set the number of epochs near to where this levelling off starts.

  ```python
  # Visualize the model plot where the y-axis displays the accuracy metric
  model_plot.plot(y="accuracy")
  ```

* Explain to the students that we've examined performance on the training data, but what we ultimately care about is how well the model works on data it hasn't seen before: How well can it generalize "in the wild?"

* To learn this, we can use the evaluate method on our model, making sure to specify our test data.

  ```python
  # Evaluate the model loss and accuracy metrics using the evaluate method and the test data
  model_loss, model_accuracy = neuron.evaluate(X_test_scaled, y_test, verbose=2)

  # Display the evaluation results
  print(f"Loss: {model_loss}, Accuracy: {model_accuracy}")
  ```

* In reviewing the results on the test data, we observe that our model appears to perform fairly well out-of-sample, with a maintained accuracy of over 80%.

Answer any questions before moving on.

---

### 12. Instructor Do: Reflect (10 min)

This unit may have been challenging because it presented several new concepts. Be sure to spend a few minutes with the class reflecting on what they've learned:

* Modeling neural networks is part art and part science. Be patient while defining models.

* There are several frameworks for implementing neural networks. Keras is a business-class framework that students can use for prototyping or deploying production models.

* Mastering neural networks takes time. However, thanks to frameworks like Keras, you don't need a PhD to start using neural networks to solve real-world problems.

* Neural networks are not a universal best solution. You should always test and benchmark different machine learning algorithms.

Congratulate the students on learning a new skill that will add value to their professional portfolio, and answer any questions before ending the class.

---

### End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
