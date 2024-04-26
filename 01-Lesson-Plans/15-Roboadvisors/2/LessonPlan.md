## 15.2: Power Up Chatbots with AWS Lambda

### Overview

In today’s class, you’ll introduce the students to **AWS Lambda**, which is a service that AWS offers for remotely running code. Lambda uses a technology that’s known as a **serverless computing platform**, where you can upload your code. Furthermore, Lambda handles all the technical aspects for deploying your code as an application that others can use. This resembles what the students did before when using APIs.

In today’s class, the students will then learn how to use Lambda to add functionality to an Amazon Lex bot.

### Class Objectives

By the end of this class, the students will be able to:

* Describe how Lambda implements serverless applications.

* Apply their Python skills to building a Lambda function.

* Test and debug the code of a Lambda function.

* Use a Lambda function to add new features to an Amazon Lex bot.

---

### Instructor Notes

* The students will create and edit Lambda functions by using the online code editor that AWS provides. This editor has issues and sometimes stops working. So, tell the students to back up their code by using a local Python script.

* Testing Lambda functions can be intricate and frustrating. The names of intents and slots are case sensitive, so special attention should be paid to their spelling. Have the TAs help the students while they’re coding and testing them.

* What if an error occurs when you test your Amazon Lex bot after enabling Lambda initialisation and validation in the bot? You won't get much information in the Amazon Lex console. In most cases, the error results from a typo in an intent or slot name. Logic errors can also occur in the Python code. So, you can review the code and test the function in the Lambda console for debugging.

* In today's class, you and the students will add functionality to the bots that were created in an earlier class by using Lambda and Python code.

### Class Slides and Time Tracker

* You can review the slides for this lesson on Google Drive at [Lesson 15.2 Slides](https://docs.google.com/presentation/d/1mBqimlStlaCp_N7YJR5kROBW9J9PAN7Audv0y7O_xZI/edit?usp=sharing).

  * **Note:** If you want to modify the slides, create a copy as follows: on the File menu, select "Make a copy," and then select “Entire presentation.”

* To add the slides to the student-facing repository, first download the slides as a PDF. To do so, open the slide deck for this lesson. On the File menu, select Download, and then select "PDF Document (.pdf)." Then, add the PDF file and other necessary files to your class repository. This way, if the curriculum changes in the future, your students will always have the slides that align with the lesson you taught.

* You can review the Time Tracker for this lesson at [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome and Introduction to AWS Lambda (10 min)

In this activity, you’ll welcome the students to class. You’ll also introduce them to serverless applications.

Welcome the students to the second day of Module 15! Get the class excited about today's class, when they’ll learn how to add functionality to an Amazon Lex bot by using Python and Lambda.

In this module, the students will learn what a serverless application is, how to implement one by using Lambda, and how to later use Lambda to power up an Amazon Lex chatbot.

Explain to the students that with Lambda, we can deploy and run code in the cloud. Furthermore, we don’t need to concern ourselves with server configuration or administration, such as keeping servers up and running or handling security issues. This type of cloud application is known as a **serverless application**.

Use the lesson slides, and highlight the following talking points to explain how serverless applications work and how Lambda implements them:

* When we develop a software application, the ultimate goal is to make it available to anyone who’s interested in using it.

* Say that you want to create a chatbot to help customers make cryptocurrency trading decisions.

* To do so, you need to connect various components, like a chatbot development tool to define the dialogue’s interaction, a software application to fetch both historical and current crypto prices by using an API, a machine learning model that’s deployed to the cloud to aid trading decisions, and a database to store and manage all the information.

* Managing all these components poses a challenge. You need to be aware of software updates, diagnose hardware for potential failures, and secure your servers to prevent cyberattacks.

* This is where the power of serverless applications comes in. Using a serverless application means that you don’t need to worry about managing any servers.

* A serverless application is the glue that ties different services, tools, and devices together to ease the deployment of a software system to the cloud. You won’t need to maintain or manage any servers. For example, consider the following image of robo advisor architecture:

  ![A diagram depicts the architecture.](Images/15-2-robo-advisor-architecture.png)

  In the preceding image, notice that the client app interacts only with the serverless application. But, the serverless application also interacts with a cryptocurrency exchange service, a chatbots framework, and a database server.

Explain to the students that when we deploy a serverless application, it runs in the cloud on one or several servers, depending on the current user’s demand. The cloud services provider that hosts the serverless application will automatically scale the infrastructure depending on the demand. This ensures the optimal functioning of our software. Explain that Lambda is an AWS service that we can use to deploy serverless applications that can interact with other AWS services.

Mention that today, the students will learn how to use Lambda to create a serverless application that interacts with Amazon Lex.

Before moving on, answer any questions that the students might have.

---

### 2. Instructor Do: Creating Python Functions with AWS Lambda (20 min)

**Corresponding activity:** [01-Ins_Python_Functions_AWS_Lambda](Activities/01-Ins_Python_Functions_AWS_Lambda)

**File:**

* [lambda_function.py](Activities/01-Ins_Python_Functions_AWS_Lambda/Solved/lambda_function.py)

In this activity, you’ll demonstrate how to launch the Lambda console so that you can create a function by using Python. You'll then create a function that adds functionality to the crypto converter bot that you started in an earlier class.

Explain to the students that Lambda can run functions that are written in several programming languages, such as C#, Go, Java, Ruby, and Python. Mention that each language has its own particulars for remotely running functions with Lambda. And in this activity, they’ll learn how to run Python functions.

Explain that in this activity, you’ll extend the functionality of the crypto converter bot that was created in an earlier class. Highlight that specifically, you’ll use Lambda to add a Python function that gets the current bitcoin price in US dollars.

To create a Python function with Lambda, you’ll demonstrate the following high-level steps:

1. Open the Lambda console.

2. Create a Lambda function.

3. Open the Lambda function in the online code editor.

4. Organize the Lambda function code.

#### Open the AWS Lambda Console

Share your screen with the class.

**Important:** In this module, the screenshots and descriptions of the AWS user interface appear as they exist at the time of this writing. But, you might find slight differences because of updates.

To open the Lambda console, demonstrate the following steps:

1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/) with the administrator IAM user.

2. In the Find Services search box, type Lambda, and then in the resulting Services list, click Lambda (to open the Lambda console).

    ![“”](Images/15-2-launching-aws-lambda-console.png)

#### Create an AWS Lambda Function

To create a Lambda function, demonstrate the following steps:

1. In the Lambda console, in the navigation pane on the left side, click Functions, and then in the Functions pane on the right side, click the "Create function" button.

    ![“”](Images/15-2-create-aws-lambda-function.png)

2. On the “Create function” page, click “Author from scratch,” and then in the “Basic information” section, complete the following steps:

    * In the “Function name” box, type convertDollars.

    * In the Runtime drop-down list, click “Python 3.7.”

      **Important:** Although Lambda supports Python 3.8 and later versions, you need to choose version 3.7. This is to avoid version conflicts with the code in this lesson.

3. Click the “Create function” button.

    ![“”](Images/15-2-lambda-function-details.png)

4. Note that AWS creates the `convertDollars` Lambda function environment by provisioning the necessary infrastructure for running a serverless application. This process takes a few seconds.

    * Explain to the students that each time they create a new Lambda instance, several processes run behind the scenes. For one, AWS creates a new container to host the Lambda instance. They can think of this container as a computer that keeps their code up and running. AWS dynamically allocates each container with a RAM-and-CPU capacity according to its needs. AWS manages the entire infrastructure behind the scenes&mdash;so they don’t need to concern themselves with those details. By the end of each billing cycle, they just need to pay for any allocated resources that their function used beyond the limits of the free tier. Point out that during this module, no reason exists to exceed these limits.

    * Slack out to the class the following link to a video on the AWS YouTube channel: [Introduction to AWS Lambda & Serverless Applications](https://youtu.be/EBSdyoO3goc). Tell them that they can review the video to learn more about how Lambda works.

5. Note that once AWS creates the Lambda function, the convertDollars page displays with the following confirmation message:

    Successfully created the function **convertDollars**. You can now change its code and configuration. To invoke your function with a test event, choose "Test".

    ![“”](Images/15-2-lambda-function-created.png)

#### Open the Lambda Function in the Online Code Editor

To continue the demo and open the Lambda function in the online code editor, demonstrate the following steps:

1. Scroll down to the “Code source” section, and then in the Environment pane on the left side, point out that a Python program named `lambda_function.py` already exists.

2. Click this name, and then in the lambda_function pane on the right side, point out that starter code returning a greetings message already exists, as the following image shows:

    ![A screenshot depicts the online code editor with a sample Python program.](Images/15-2-initial-lambda-code.png)

Explain to the students that you’ve now successfully created the baseline for a Lambda function. In the forthcoming activities, the students will code new features in Python to extend the functionality of an Amazon Lex bot. But first, it’s important that they understand how to organise the code in a Lambda function that will connect with Amazon Lex.

#### Organise the AWS Lambda Function Code

Explain to the students that Lambda functions are designed to manage events that other AWS services can trigger. Such an event occurs when a slot gets filled in Amazon Lex, for example.

Point out that in the starter code of the `lambda_function.py` program, the `lambda_handler` function is the main event handler. Its goal is to manage all the incoming events and dispatch them depending on the defined business logic.

The following code shows the `lambda_handler` function (which also appears in the image in the preceding section):

```python
import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
```

Explain that we’ll use the `lambda_handler` function to route the incoming requests that are based on the user intents that the Amazon Lex bot captures. So, they'll now learn how to organise the code of a Lambda function to connect with Amazon Lex.

Explain that Lambda can interact with several AWS services to invoke functions. To do so, Lambda defines specific events for each service. In this lesson, the students will learn about the events that Lambda defines for Amazon Lex.

Encourage the students to learn more about the events that Lambda supports, Slack out the link to [Using AWS Lambda with other services](https://docs.aws.amazon.com/lambda/latest/dg/lambda-services.html) in the AWS Lambda Developer Guide.

The following image shows the anatomy of the Lambda function that we’ll use to communicate with Amazon Lex. Use the lesson slides to present this image to the class. And, explain that we can use this code as a boilerplate template to code business logic for extending the functionality of the Amazon Lex bot:

![A screenshot depicts the Lambda function and points out its main sections.](Images/15-2-lambda-function-anatomy.png)

Explain that as the preceding image shows, we can organise a Lambda function into six general building blocks. These will manage the interaction with Amazon Lex and implement the necessary business logic.

For a better understanding of each block, explain the following points:

1. **Required Libraries:** This section contains all the libraries that are needed for coding the business logic in the Lambda functions. Although Lambda supports Python, the Lambda runtime doesn't support some common packages, such as `pandas`, `numpy` and `requests`. So, we should use or install alternative packages.

    In this demo, you’ll get the current price of bitcoin by making an API call to the [alternative.me Crypto API](https://alternative.me/crypto/api/). So, the Requests library will be imported from the [botocore package](https://botocore.amazonaws.com/v1/documentation/api/latest/index.html).

2. **Functionality Helper Functions:** These functions implement business logic and data validation. In this demo, you’ll use four helper functions:

    * `parse_float`: Securely parses a non-numeric value into a `float`.

    * `get_btcprice`: Retrieves the current price of bitcoin in dollars from the alternative.me Crypto API.

    * `build_validation_result`: Defines an internal validation message that’s structured as a Python dictionary.

    * `validate_data`: According to the business logic, validates the data that the user provides in the intent's dialogue in Amazon Lex. In this demo, only two rules apply. First, the user should be at least 21 years old. Second, the amount to convert, in dollars, must be greater than zero.

      The `validate_data` function uses the `build_validation_result` function to return a validation result message. In this demo, if the user's age is less than 21, or if the amount to convert is less than zero, the function returns `False`. Otherwise, it returns `True`.

3. **Dialog Actions Helper Functions:** Handles the input and response events data from the conversation between Amazon Lex and Lambda. The `get_slots` function gets all the slots and their values from the current intent. The `elicit_slot`, `delegate` and `close` functions build response messages that are structured as a valid Amazon Lex event in the JavaScript Object Notation (JSON) format.

4. **Intents Handlers:** Implements the functionality to fulfil the user's intents. The core business logic is coded into the intents handlers. An **intent handler** is a function that implements the functionality to fulfil a user's intent.

    In this demo, the `convert_dollars` function contains all the logic to validate the user's input, which is stored in the Amazon Lex slots. This logic uses the `validate_data` helper function along with the conversation between the user and the bot. If any slot has invalid data, the `convert_dollars` function returns an `elicitSlot` dialogue to ask the user for the data again. Otherwise, it returns a `delegate` dialogue to direct Amazon Lex to choose the next course of action per the configuration of the bot.

    When the conversation between the user and the bot ends, `convert_dollars` gets the current price of the bitcoins in dollars by using the `get_btcprice` function. The conversion about going from dollars to bitcoins is done, and `convert_dollars` calls the `close` function to return a `Fulfilled` event message to Amazon Lex.

5. **Intents Dispatcher:** Checks that the current intent is valid and, if so, dispatches it to the correct intent handler. In this demo, the `dispatch` function does this. Note that an Amazon Lex bot can have one or more intents. But in this demo, we have only one intent. So we have only one intent handler call to the `convert_dollars` function.

6. **Main Handler:** Catches each event and returns a response for each to Amazon Lex. In this demo, the `lambda_handler` function does this, returning each response via the `dispatch` function. Note that each time a user sends a message to Amazon Lex (via either voice or text), an event gets sent to Lambda.

Slack out the provided code for the `lambda_function.py` Python script to the students.

Explain that getting started with coding Lambda functions might seem challenging. But, they already have the required Python skills to succeed!

Ask the students to open the Python script that you shared. Explain that a Lambda function resembles the Python code that they’re familiar with. But, they need to arrange it according to a special structure that allows Amazon Lex to communicate with Lambda.

Explain that they'll have time to explore this code and that they’ll use a similar approach to add more functionality to the Bitcoin Fear & Greed robo advisor that they started in an earlier class.

Before moving on, answer any questions that the students might have.

---

### 3. Student Do: Enhancing the Bitcoin Fear & Greed Robo Advisor (15 min)

**Corresponding activity:** [02-Stu_Enhancing_Robo_Advisor](Activities/02-Stu_Enhancing_Robo_Advisor)

**Files:**

* [Instructions](Activities/02-Stu_Enhancing_Robo_Advisor/README.md)

* [lambda_function.py](Activities/02-Stu_Enhancing_Robo_Advisor/Unsolved/lambda_function.py)

In this activity, the students will create a Lambda function that adds functionality to the Bitcoin Fear & Greed Robo Advisor that they started in an earlier class.

---

### 4. Instructor Do: Review Enhancing the Bitcoin Fear & Greed Robo Advisor (15 min)

Start this review activity by conducting a pulse check to find out how many students were able to create the Lambda function.

Ask the class to raise their hands if they were able to finish this activity. If you’re teaching an online class by using Zoom, remain in the [Gallery View](https://support.zoom.us/hc/en-us/articles/201362323-Changing-the-video-layout-Speaker-view-and-Gallery-view-) for this activity so that you can observe your class on one screen.

Ask the students to find the [Zoom Meeting Reactions](https://support.zoom.us/hc/en-us/articles/115001286183-Non-verbal-feedback-and-reactions-), which are in the Meeting Controls panel at the bottom of the Zoom window. Have them select the thumbs up emoji if they successfully created and configured the robo advisor bot.

Use the feedback from this check to either recommend office hours for reviewing things in more depth or adjust your pace throughout the rest of the class.

Focus this review activity on the Python code. (We expect that all the students were able to create a Lambda function.) To do so, share your screen, and then review the solution code, highlighting the following points:

* After setting up the Lambda function in the AWS Management console, we just need to paste the provided code into the Lambda code editor.

* Note that as we did before, the first step is to import the required libraries. The biggest difference is that we need to import the Requests library from the `botocore.vendored` module, as the following code shows:

  ```python
  ### Required Libraries ###
  from datetime import datetime
  from dateutil.relativedelta import relativedelta
  from botocore.vendored import requests
  ```

* Now, let's review the helper functions, starting with `parse_float`. With this function, we can explicitly parse a number as a `float`. We pass the number that we want to parse as the `n` parameter. Note that the code is pure Python&mdash;the same type of Python code that we used before, as the following code shows:

  ```python
  def parse_float(n):
      """
      Securely converts a non-numeric value to float.
      """
      try:
          return float(n)
      except ValueError:
          return float("nan")
  ```

* Next, let's review the `get_btcprice` function. To do so, let's open the endpoint that the code provides to gain a better understanding of the response.

  * For this point, you (the instructor) should open your browser and then go to [this web link to demonstrate the API endpoint.](https://api.alternative.me/v2/ticker/bitcoin/?convert=USD).

  * The following image shows the JSON response that displays:

    ![A screenshot depicts the JSON response, including the bitcoin price in US dollars.](Images/15-2-btc-json.png)

  * Explain to the students that as they can note, we need to retrieve the bitcoin price from an inner list in the JSON response. So in the Python code of the Lambda function, we need to represent the location of the `price` key in the JSON response.

Move back to the Python code of the Lambda function:

```python
def get_btcprice():
    """
    Retrieves the current price of bitcoin in dollars from the alternative.me Crypto API.
    """
    bitcoin_api_url = "https://api.alternative.me/v2/ticker/bitcoin/?convert=USD"
    response = requests.get(bitcoin_api_url)
    response_json = response.json()
    price_dollars = parse_float(response_json["data"]["1"]["quotes"]["USD"]["price"])
    return price_dollars
```

To review the preceding code, highlight the following points:

* The `get_btcprice` function uses the Requests library to get the current price of a bitcoin, in US dollars, from the alternative.me Crypto API.

* Next, it uses the `reponse.json` function to access the data from the API response by using the keys. So, it gets the bitcoin price, in dollars, from the `["data"]["1"]["quotes"]["USD"]["price"]` path.

* Finally, it returns the price as a `float`.

* Using this Lambda function, we’ll make a bitcoin buying recommendation that’s based on the current Bitcoin Fear & Greed Index. So, we’ll use the `get_fg_index` function to get that index from a different endpoint of the alternative.me API, as the following code shows:

  ```python
  def get_fg_index():
      """
      Retrieves the current Bitcoin Fear & Greed Index from the alternative.me Crypto API.
      """
      fgi_url = "https://api.alternative.me/fng/"
      response = requests.get(fgi_url)
      response_json = response.json()
      fg_index = parse_float(response_json["data"][0]["value"])
      return fg_index
  ```

* With both the current bitcoin price and the Bitcoin Fear & Greed Index, we can make a buying recommendation. To do so, we have another function, named `get_recommendation`, that implements the decision-making process based on the range values of the index, as the following code shows:

  ```python
  def get_recommendation():
      """
      Returns a buying recommendation based on the current value of the Bitcoin Fear & Greed Index.
      """
      fg_index = get_fg_index()
      recommendation = ""
      if fg_index >= 0 and fg_index <=25:
          recommendation = "Be cautious about buying bitcoin today since the market feels 'Extreme Fear'."
      elif fg_index > 25 and fg_index < 50:
          recommendation = "Be cautious about buying bitcoin today since the market feels 'Fear'."
      elif fg_index == 50:
          recommendation = "You may buy bitcoin today since the market feels 'Neutral'."
      elif fg_index > 50 and fg_index <= 75:
          recommendation = "You may buy bitcoin today, the market feels 'Greed'"
      else:
          recommendation = "You may buy bitcoin today, the market feels 'Extreme Greed'"
      return recommendation
  ```

* Finally, the `convert_dollars` function implements the core functionality of this robo advisor in the "Intents Handlers" section. This function uses the helper functions and returns a recommendation in the following code block:

  ```python
  # Get the current price of bitcoin in dollars and make the conversion from dollars to bitcoin.
  btc_value = parse_float(dollars) / get_btcprice()
  btc_value = round(btc_value, 4)

  # Return a message with conversion's result.
  return close(
      intent_request["sessionAttributes"],
      "Fulfilled",
      {
          "contentType": "PlainText",
          "content": """Thank you for your information;
          you can get {} Bitcoins for your ${} dollars.
          {}
          """.format(
              btc_value, dollars, get_recommendation()
          ),
      },
  )
  ```

* The preceding code block gets the current price of a bitcoin&mdash;and uses it to compute the number of bitcoins that the user can buy with the number of dollars that they specified. Then, it rounds the conversion to four decimal places.

* This intent handler closes by sending a message from the Lambda function back to Amazon Lex. There, we’ll use the bitcoin conversion, the number of dollars that the user specified, and the recommendation from the `get_recommendation` function.

Explain to the students that in the forthcoming activities, they’ll learn how to connect the Lambda function to the AWS bot. They’ll also learn how to test and debug Lambda functions by using the Lambda code editor.

Before moving on, answer any questions that the students might have.

---

### 5. Instructor Do: Connecting AWS Lambda and Amazon Lex (15 min)

In this activity, the students will learn how to connect a Lambda function to Amazon Lex. You'll continue using the crypto converter bot for this demonstration.

Explain to the students that you’ll now demonstrate how to power up the Amazon Lex bot with the Lambda function.

#### Connect Amazon Lex with AWS Lambda

To connect Amazon Lex with Lambda, demonstrate the following steps:

1. In the Lambda console, with the `convertDollars` function open, click on the Services button in the top left of the screen. The Services drop-down list appears.

2. In the list, right-click Amazon Lex, and then click “Open Link in New Tab.” A new tab named Amazon Lex opens and contains the Amazon Lex console.

3. Click the Amazon Lex tab, and then in the Bots section, click CryptoConverter to open it.

The following animation shows the preceding steps:

![An animation depicts the steps.](Images/15-2-open-lex-in-new-tab.gif)

#### Enable AWS Lambda Initialization and Validation in Amazon Lex

Now that you’ve opened the Amazon Lex bot, you’ll allow the Lambda function to take control of the conversation flow. To do so, demonstrate the following steps:

1. Scroll down to the "Lambda initialization and validation" section. In this section, select the “Initialization and validation code hook” checkbox, and then in the “Lambda function” drop-down list that appears, click convertDollars. Then in the “Version or alias” drop-down list that appears, click Latest.

    **Note:** Explain to the students that in programming, the term **hook** describes a piece of code that allows the inclusion of a custom function. In this case, we’ll use the Lambda function code as a hook. Slack out the following link to [Hooking - Wikipedia article](https://en.wikipedia.org/wiki/Hooking) to the class, and encourage them to read the article to learn more about hooking.

2. If an “Add permission to Lambda Function” dialog box appears, click the OK button.

    **Note:** This permission allows communication between the bot and Lambda.

The following animation shows the preceding steps:

![An animation depicts the steps.](Images/15-2-linking-lambda-to-lex.gif)

#### Allow the AWS Lambda Function to Manage the Confirmation Prompts

Explain to the students that you’ll now allow the Lambda function to manage the confirmation prompts that display after filling the slots. To do so, demonstrate the following steps:

1. Scroll down to the "Confirmation prompt" section, and then clear the “Confirmation prompt” checkbox.

    ![“”](Images/15-2-disable-confirmation-prompt.png)

2. In the Fulfillment section, select “AWS Lambda function.” In the “Lambda function” drop-down list that appears, click convertDollars, and then in the “Version or alias” drop-down list, click Latest.

    ![A screenshot depicts the Fulfillment section.](Images/15-2-enable-lambda-fulfillment.png)

3. Let the magic begin! Click the Build button (in the upper-right corner of the page).

    ![“”](Images/15-2-building-the-bot.png)

4. Mention that the build process takes a few minutes. When the build process completes, explain to the class that the bot is connected to Lambda to control the user’s intent!

#### Test the AWS Lambda&ndash;Powered Bot

To test the Lambda-powered bot with sample utterances, demonstrate the following steps (recall that sample utterances are the starter conversation phrases that we define for an intent):

1. Have a dialogue with the bot that uses valid data for both slots.

    **Note:** Recall that the Lambda function has a `validate_data` function, which confirms that the `birthday` and `dollars` slots comply with the following rules:

    * The user is over 21 years old.

    * The dollar amount is greater than zero.

2. Note that after you supplied a birthday and a number of dollars to convert, everything processed without warning messages. That is, the bot didn’t ask you to reenter data, because the values that you supplied for both slots were valid.

3. Have a dialogue with the bot that uses invalid data for both slots.

4. Note that a different conversation occurs, because you entered invalid data for the `birthday` and `dollars` slots. Specifically, you receive warning messages that explain the errors and that ask for valid data.

Explain to the students that in this demo, the communication between Amazon Lex and Lambda flowed smoothly. But just as they might have bugs when coding Python in a Jupyter notebook, they might have bugs when they code in the Lambda console. That’s why later in this lesson, they’ll learn how to fix a buggy Lambda function.

Before moving on, answer any questions that the students might have.

---

### 6. Break (15 min)

---

### 7. Student Do: Adding Business Logic to the Robo Advisor with AWS Lambda (25 min)

**Corresponding activity:** [04-Stu_Adding_Lambda_Robo_Advisor](Activities/04-Stu_Adding_Lambda_Robo_Advisor)

**Files:**

* [Instructions](Activities/04-Stu_Adding_Lambda_Robo_Advisor/README.md)

* [lambda_function.py](Activities/04-Stu_Adding_Lambda_Robo_Advisor/Unsolved/lambda_function.py)

In this activity, the students will connect the Lambda function that they created before to the robo advisor to add business logic to it.

---

### 8. Instructor Do: Review Adding Business Logic to the Robo Advisor with AWS Lambda (15 min)

**Files:**

* [Instructions](Activities/04-Stu_Adding_Lambda_Robo_Advisor/README.md)

* [lambda_function.py (required activity solution)](Activities/04-Stu_Adding_Lambda_Robo_Advisor/Solved/lambda_function.py)

* [lambda_function_challenge.py (optional challenge solution)](Activities/04-Stu_Adding_Lambda_Robo_Advisor/Solved/lambda_function_challenge.py)

Start this review activity by conducting a pulse check to find out how many students were able to finish the activity.

Ask the class if they were able to finish this activity. If you’re teaching an online class by using Zoom, remain in the [Gallery View](https://support.zoom.us/hc/en-us/articles/201362323-Changing-the-video-layout-Speaker-view-and-Gallery-view-) for this activity so that you can observe your class on one screen. (If your teaching in person, you can skip the Zoom instructions below).

Ask the students to find the [Zoom Meeting Reactions](https://support.zoom.us/hc/en-us/articles/115001286183-Non-verbal-feedback-and-reactions-), which are in the Meeting Controls panel at the bottom of the Zoom window. Have them select the thumbs up or smile emoji if they successfully created and configured the robo advisor bot.

Use the feedback from this classroom check to either recommend office hours for reviewing things in more depth or adjust your pace throughout the rest of the class.

Focus this review on the code for the challenge activity. To do so, share your screen, and then review the solution code. Start with the `get_fg_index` function:

```python
def get_fg_index():
    """
    Retrieves the average Bitcoin Fear & Greed Index from the last ten days
    """

    # Fetch the Bitcoin Fear & Greed Index from the last ten days
    fgi_url = "https://api.alternative.me/fng/?limit=10"
    response = requests.get(fgi_url)
    response_json = response.json()

    # Create a list with the data of the index from the last ten days
    fg_index_list = response_json["data"]

    # Compute the sum of the index values over the last ten days
    index_sum = 0
    for index in fg_index_list:
        index_sum = index_sum + parse_float(index["value"])

    # Compute the average value of the index over the last ten days
    avg_index = index_sum / len(fg_index_list)

    return avg_index
```

Explain to the students that after the preceding function fetches the index from the last ten days, it creates a list in the `fg_index_list` variable to store all the index values. Then, it uses a `for` loop to compute the sum of the index values. Finally, it computes and returns the average index value.

Next, review the `get_recommendation` function:

```python
def get_recommendation():
    """
    Returns a buying recommendation based on the average value of the Bitcoin Fear & Greed Index from the last ten days.
    """
    fg_index = get_fg_index()
    recommendation = ""
    if fg_index >= 0 and fg_index <=25:
        recommendation = "Be cautious about buying bitcoin today since the market felt 'Extreme Fear' the last ten days."
    elif fg_index > 25 and fg_index < 50:
        recommendation = "Be cautious about buying bitcoin today since the market felt 'Fear' the last ten days."
    elif fg_index == 50:
        recommendation = "You may buy bitcoin today since the market felt 'Neutral' the last ten days."
    elif fg_index > 50 and fg_index <= 75:
        recommendation = "You may buy bitcoin today, the market felt 'Greed' the last ten days."
    else:
        recommendation = "You may buy bitcoin today, the market felt 'Extreme Greed' the last ten days."
    return recommendation
```

Explain to the students that the preceding function only updates the text messages of the rules. It does so to reflect the fact that the recommendation is based on the average value of the index over the last ten days.

Before moving on, answer any questions that the students might have.

---

### 9. Instructor Do: Dealing with Buggy Lambda Functions (20 min)

**Corresponding activity:** [05-Ins_Dealing_with_Buggy_Lambda](Activities/05-Ins_Dealing_with_Buggy_Lambda)

**Files:**

* [convertBirthdayError.json](Activities/05-Ins_Dealing_with_Buggy_Lambda/Solved/convertBirthdayError.json)

* [convertNoErrors.json](Activities/05-Ins_Dealing_with_Buggy_Lambda/Solved/convertNoErrors.json)

* [convertZeroAmount.json](Activities/05-Ins_Dealing_with_Buggy_Lambda/Solved/convertZeroAmount.json)

In this activity, the students will learn how to test and debug Lambda functions in the [AWS Management Console](https://aws.amazon.com/console/).

Explain to the students that Lambda interacts with other AWS services by processing event messages in the JSON format. Recall that the JSON format is one of the industry standards for sharing data on the internet. The comma-separated values (CSV) and XML formats are the other standards.

Mention that each AWS service uses a specific JSON format. In this activity, you’ll explain the one that Amazon Lex uses to communicate with Lambda and how we can use it to test and debug Lambda functions.

Open the AWS Management Console. Then launch the Lambda console, and open the `convertDollars` function.

![“”](Images/15-2-deploy-lambda-function.png)

Explain that one of the challenges with Lambda is dealing with errors. So, it’s important to know how to test a Lambda function in the Lambda console. To test a Lambda function, we use test events.

#### Define a Test Event

Explain to the class that a **test event** is a mechanism that the Lambda console provides for testing how a Lambda function responds. Explain that in this demo, you’ll cover how to test only Amazon Lex intents, and highlight the following points:

* We create a test event by placing its definitions and configurations in a JSON file.

* Lambda uses this file to send the test event to the Lambda function.

* The event structure depends on the service that we connect to Lambda. In this demo, we’ll learn how to define a test event that fulfils the intent of an Amazon Lex bot.

Remind the students that they learned about JSON files and their structure in the earlier module about APIs. And, remind them that the format of these files resembles that of Python dictionaries.

Using a text editor, like Sublime Text or Visual Studio Code, open the provided `convertNoErrors.json` file. Then use that file to explain how a test event for the `convertDollars` function might appear, as the following JSON data shows:

```json
{
  "messageVersion": "1.0",
  "invocationSource": "DialogCodeHook",
  "userId": "John",
  "sessionAttributes": {},
  "bot": {
    "name": "CryptoConverter",
    "alias": "$LATEST",
    "version": "$LATEST"
  },
  "outputDialogMode": "Text",
  "currentIntent": {
    "name": "convertUSD",
    "slots": {
      "birthday": "1978-12-16",
      "dollars": "10"
    },
    "confirmationStatus": "None"
  }
}
```

Point out that the preceding JSON data is human readable. Mention that they can use this structure as the boilerplate for creating test events for various testing scenarios.

Continue the demonstration by highlighting the most relevant keys in the JSON data, as follows:

* The `bot` key defines the name of the Amazon Lex bot. So, we should make sure that this name matches that of our bot&mdash;especially because it’s case sensitive.

* The `$LATEST` value is the default for the `alias` and `version` keys.

* Because this test event gets passed as text, the value of the `outputDialogMode` key is `Text`.

* The `currentIntent` key includes the name of the intent. It also includes names and values for both slots. All these names are case sensitive, too.

* For this test event, the `birthday` and `dollars` slots have valid data.

#### Create a Test Event

Explain that you’ll now demonstrate how to create a test event to test a Lambda function. To do so, demonstrate the following steps:

1. Open the Lambda console, and then complete the following steps:

    * In the left navigation pane, click Functions.

    * In the functions display, click convertDollars.

    * On the page that appears, scroll down to find the code editor.

    * Click the Test tab.

      ![“”](Images/15-2-open-lambda-test-tab.png)

2. In the “Test event” section, select the “New event” option.

    ![“”](Images/15-2-new-test-event.png)

3. In the box for the code, delete the template code that’s already there, and then paste the code of your test event. To name the test event, in the Name box, type convertNoErrors. Then click the “Save changes” button.

    ![“”](Images/15-2-create-new-test-event.png)

4. Note that the “Saved event” option is now selected. Additionally, a “Saved event” drop-down list appears that displays the name of the new test event.

    ![“”](Images/15-2-test-events-list.png)

5. In the “Saved event” drop-down list, click convertNoErrors. Then click the Invoke button to run the test. The test runs, and then a message displays with the test results. In this case, the message is “Execution result: succeeded.”

    ![“”](Images/15-2-test-event-results.png)

Now that you’ve demonstrated how to test valid values for the slots of the Amazon Lex bot, take a break to ask the following question to the class:

**Question:** Can you figure out how to create a test event to check an invalid value for the `dollars` slot?

**Answer:** To test an invalid value for the `dollars` slot, we can use the JSON test event structure that was presented earlier, and fill the slot with a negative amount&mdash;for example, &minus;10.

The following JSON data shows how to do this:

```json
{
  "messageVersion": "1.0",
  "invocationSource": "DialogCodeHook",
  "userId": "John",
  "sessionAttributes": {},
  "bot": {
    "name": "CryptoConverter",
    "alias": "$LATEST",
    "version": "$LATEST"
  },
  "outputDialogMode": "Text",
  "currentIntent": {
    "name": "convertUSD",
    "slots": {
      "birthday": "1978-12-16",
      "dollars": "-10"
    },
    "confirmationStatus": "None"
  }
}
```

Explain to the students that they can create as many test events as they want. They should create enough to test all the possible scenarios that a Lambda function might encounter during its execution. Next, you’ll demonstrate how to do that.

#### Add a Test Event

To add a test event, demonstrate the following steps:

1. Click the Test tab, and then select the “New event” option as you did before. Note that in the Template drop-down list, convertNoErrors is already selected. Additionally, the convertNoErrors code already appears in the box for the code. That’s because by default, the last-used test event is selected as a template so that you can use it as a baseline.

    ![“”](Images/15-2-configuring-new-test-event.png)

2. Using the previous test event as guidance, change the value of the `dollars` slot to 0 to test the amount validation code in the Lambda function. Name this new event convertZeroAmount, and then click the “Save changes” button.

    ![“”](Images/15-2-creating-new-test-event.png)

3. In the “Saved event” drop-down list, select convertZeroAmount, and then click the Invoke button. The test event successfully runs. But, clicking Details in the success message shows that Lambda will respond with an `ElicitSlot` type of dialogue. In such a dialogue, the message that’s defined in the Lambda function displays. An `ElicitSlot` slot is one that’s triggered when the bot requires new data from the user.

    The `convertZeroAmount` test event validates that the Lambda function catches the incorrect `dollars` value. It also validates that the Lambda function sends the appropriate elicitation of new data to the user via Amazon Lex. You can verify this, because the JSON data shows the result of your function execution, including the following line:

    ```json
    "type": "ElicitSlot",
    ```

    ![“An image shows the results of the invalid data test.”](Images/15-2-invalid-data-test-event-results.png)

If you have time, create a new test event to validate what happens when a user provides an invalid birthday—for example, 2015-12-16. You can find the code for this test event in the provided `convertBirthdayError.json` file.

Explain that now that the students have learned how to test the data validation code of a Lambda function, they’ll put into practice all the new skills that they’ve learned.

Before moving on, answer any questions that the students might have.

---

### 10. Student Do: Debugging Lambda Functions (15 min)

**Corresponding activity:** [06-Stu_Debuggin_Lambda_Functions](Activities/06-Stu_Debuggin_Lambda_Functions)

**Files:**

* [Instructions](Activities/06-Stu_Debuggin_Lambda_Functions/README.md)

* [correctAmount.json](Activities/06-Stu_Debuggin_Lambda_Functions/Unsolved/correctAmount.json)

In this activity, the students will test and debug the `getFGIndex` Lambda function that they created before.

---

### 11. Instructor Do: Review Debugging Lambda Functions (10 min)

**Files:**

* [Instructions](Activities/06-Stu_Debuggin_Lambda_Functions/README.md)

* [correctAmount.json](Activities/06-Stu_Debuggin_Lambda_Functions/Solved/correctAmount.json)

* [zeroAmount.json](Activities/06-Stu_Debuggin_Lambda_Functions/Solved/zeroAmount.json)

Start this review activity by conducting a pulse check to find out how many students were able to both add the provided test event and create a new one.

Ask the class to raise their hands if they were able to finish this activity. If you’re teaching an online class by using Zoom, remain in the [Gallery View](https://support.zoom.us/hc/en-us/articles/201362323-Changing-the-video-layout-Speaker-view-and-Gallery-view-) for this activity so that you can observe your class on one screen.

Ask the students to find the [Zoom Meeting Reactions](https://support.zoom.us/hc/en-us/articles/115001286183-Non-verbal-feedback-and-reactions-), which are in the Meeting Controls panel at the bottom of the Zoom window. Have them select the thumbs up emoji if they successfully created and configured the robo advisor bot.

Use the feedback from this check to recommend office hours for reviewing things in more depth.

Start this review by loading the provided test event. Mention to the students that as expected, this test event was successful. That’s because it provides a valid value for the `amount` slot according to the business rules that the Python code of the Lambda function defines.

Next, add a new test event that sets the `amount` slot to zero, as the following JSON data shows:

```JSON
{
  "messageVersion": "1.0",
  "invocationSource": "DialogCodeHook",
  "userId": "John",
  "sessionAttributes": {},
  "bot": {
    "name": "BitcoinAdvisor",
    "alias": "$LATEST",
    "version": "$LATEST"
  },
  "outputDialogMode": "Text",
  "currentIntent": {
    "name": "getFGIndex",
    "slots": {
      "amount": "0"
    },
    "confirmationStatus": "None"
  }
}
```

Explain that after you run this test event, the students can observe the expected response in the Lambda console, which states "The amount should be greater than zero, please provide a correct amount in dollars." Remind the class that the `validate_data` function of our Lambda architecture defined this message.

Before moving on, answer any questions that the students might have.

---

### 12. Instructor Do: Recap (5 min)

In this activity, you’ll do a final recap with the class. Use the lesson slides to summarise what the students learned in today's class:

* As we learned today, we can build complex and automatic dialogues with just a few clicks by using Lambda functions.

* We can use Lambda functions to improve the NLP experience for users by both debugging and adding customised business logic.

Congratulate the students on gaining a new valuable skill! Now, they can create and deploy a serverless application by using Lambda. They can also add customised business logic and data validation by making a connection to Amazon Lex.

Mention that CUIs offer several opportunities to engage with customers in a new way. And, a chatbot offers a virtual agent that can support customers of financial organisations 24-7. By adding rules with Lambda, the students can now create a bot that will help customers by answering questions in the form of natural language.

Highlight the fact that the next step toward becoming proficient with the machine learning services of the AWS cloud is to deploy machine learning models that they can connect with other AWS services to create more robust applications. And, that's what they’ll learn in the next class.

Before ending the class, answer any remaining questions that the students might have.

### End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
