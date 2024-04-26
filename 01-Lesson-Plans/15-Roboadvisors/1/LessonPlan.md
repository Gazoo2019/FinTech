## 15.1: Introduction to AWS Machine Learning and Robo Advisors

### Overview

This is the final module of the machine learning section of this boot camp. Over the last few weeks, the students learned about supervised and unsupervised learning, neural networks, and how to build an algorithmic trading strategy. In this module, the students will combine all their machine learning skills with conversational user interfaces (CUIs) and cloud services.

For a fintech professional, creating CUIs and managing cloud services are two valuable skills. That’s because financial services providers use these technologies to offer chatbots and robotic advisors (robo advisors) as additional communication channels for customers.

In today's class, the students will start learning about **natural language processing (NLP)**. With NLP, computers and people can interact via human language. The students will then learn a practical application of NLP: using CUIs to build a robo advisor in AWS.

### Class Objectives

By the end of this class, the students will be able to:

* Describe the applications of CUIs in finance and banking.

* Identify the scope and the limits of the AWS free tier offers.

* Explain Amazon Lex and its main features.

* Build and test a robo advisor by using Amazon Lex.

---

### Instructor Notes

* Although the cloud is a core concept for fintech professionals, some students might find it unclear and complex. So, it's important to highlight how companies like AWS have reduced the technological complexity behind the cloud. Specifically, they offer user-friendly interfaces that require only a few lines of code and some clicks to deploy a machine learning model.

* Be sure to set the pace for the class. Encourage the students to attend office hours if they feel lost or stuck. Also, encourage them to work with partners.

* **Important:** Amazon Lex supports two versions. In this module, you’ll work with **Version 1**. Bots created in Version 1 aren’t compatible with Version 2. Make sure that you don't switch to the Amazon Lex V2 console.

* Prior to class, make sure that all the students have followed the [AWS Account Setup Guide](../Supplemental/AWS-Account-Setup.md) and created their AWS accounts. Ask the TAs to help troubleshoot any issues. If any students can’t access a free tier account, ask them to pair up with a peer for this week.

  * **Important:** At the beginning of today's class, slack out the [Amazon Web Services Free Tier](../Supplemental/AWS-Free-Tier.md) disclaimer. Explain that although they’ll use only free tier services in class, they should review this disclaimer to avoid accidentally incurring charges.

### Class Slides and Time Tracker

* You can review the slides for this lesson on Google Drive at [Lesson 15.1 Slides](https://docs.google.com/presentation/d/17Ei8kJIFkGITd1Th8izGrkXbAXv8RjnkPbGpsp7D6CY/edit?usp=sharing).

  * **Note:** If you want to modify the slides, create a copy as follows: on the File menu, select "Make a copy," and then select “Entire presentation.”

* To add the slides to the student-facing repository, first download the slides as a PDF. To do so, open the slide deck for this lesson. On the File menu, select Download, and then select "PDF Document (.pdf)." Then add the PDF file and other necessary files to your class repository. This way, if the curriculum changes in the future, your students will always have the slides that align with the lesson you taught.

* You can review the Time Tracker for this lesson at [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome and Challenge Review (10 min)

In this activity, you’ll welcome the students to the last module of the machine learning section of the boot camp.

Welcome the class to Module 15! Explain to the students that in this module, they’ll use their current Python and machine learning skills to build a robo advisor. This robo advisor will use a **conversational user interface**, or **CUI**, which is a special type of user interface that allows people to interact with computers via human language. They’ll also gain practical experience with AWS, which Gartner features as the leading company for cloud infrastructure and platform services ([Gartner Names AWS a 2021 Magic Quadrant Leader](https://pages.awscloud.com/GLOBAL-multi-DL-gartner-mq-cips-2020-learn.html)). Point out that they’ll specifically learn how to both enhance their machine learning applications and deliver CUI applications by using the power of the cloud.

Explain that CUIs are an evolution in the way that we communicate with computers. With CUIs, we can speak with computers or mobile devices by using human language via either voice or text. Furthermore, CUIs are transforming machine learning applications by understanding human language. When computers and people can interact via human language, that’s called **NLP**.

Highlight the following:

* Apple Siri, Amazon Alexa, and Google Assistant are common examples of CUIs. When robo advisors use CUIs to provide financial advice or other information to customers, they’re disrupting the field of finance. And thanks to the power of cloud services, millions of people can reach these CUIs.

* Robo advisors and cloud services are not only essential in finance, but they’re driving innovation in enterprises that were previously traditional and skeptical of adopting information technologies. By the end of this module, the students will gain two valuable skills for financial services. The first is creating CUIs to build robo advisors. The second is managing cloud services to both deploy a robo advisor and enhance machine learning models.

* Although we’re still in the early days of CUIs, financial institutions are seeking innovative ways to engage with customers and offer 24-7 communication channels. So, understanding how to use this technology to create a robo advisor is becoming an increasingly in-demand skill for fintech professionals.

* In the early stages of cloud computing, financial firms and governments perceived it as a nonsecure technology. But, cloud security has matured enough in recent years that it has earned the trust of financial institutions and government agencies.

* Furthermore, according to [a study that Accenture and WSP conducted in collaboration with Microsoft](https://www.microsoft.com/en-us/download/details.aspx?id=56950), organisations that use cloud services gain the greatest cost savings. This happens especially because of reduced energy use and a more efficient allocation of technology resources and personnel. Practical experience with cloud computing will certainly boost the fintech professional path of the students!

Slack out [the link to the page where they can download the study](https://www.microsoft.com/en-us/download/details.aspx?id=56950), and encourage them to read it outside of class.

Next, demonstrate the construction of the NLP chatbot. If you already built the chatbot for the Challenge solution in your AWS account, you can log in to the AWS Management Console for this demo. Alternatively, you can show the chatbot execution in the lesson slides, as the following animation shows:

![An animation depicts using the Amazon Lex bot from the Challenge assignment.](Images/15-1-robo-advisor-test-without-lambda.gif)

Explain that by using Amazon Lex, the students will create a robo advisor in the Challenge assignment for this module. Further explain that by using the NLP capabilities of Amazon Lex, a person and a chatbot can have a dialogue by using human language, as the following example shows:

```text
User: I want to invest for my retirement

Robo advisor: Thank you for trusting me to help, could you please give me your name?

User: Arturo

Robo advisor: How old are you?

User: 42

Robo advisor: How much do you want to invest?

User: 4000

Robo advisor: What level of investment risk would you like to take? (None, Low, Medium, High)

User: Low

Robo advisor: Thanks, now I will look for the best investment portfolio for you.
```

Before moving on, answer any questions that the students might have.

---

### 2. Instructor Do: AWS Account Checkup (20 min)

In this activity, you’ll make sure that all the students have created the following required resources (as the [AWS Account Setup Guide](../Supplemental/AWS-Account-Setup.md) specifies):

* An AWS account

* An administrator user

* AWS usage alerts

* An Amazon Simple Storage Service (Amazon S3)

It's crucial to ensure that all the students have these resources up and running to succeed in this module's activities. For each of the AWS resources in the preceding list, conduct a pulse check activity as follows:

1. If you’re teaching an online class by using Zoom, remain in the [Gallery View](https://support.zoom.us/hc/en-us/articles/201362323-Changing-the-video-layout-Speaker-view-and-Gallery-view-) for this activity so that you can observe your class on one screen.

2. Ask the students to find the [Zoom Meeting Reactions](https://support.zoom.us/hc/en-us/articles/115001286183-Non-verbal-feedback-and-reactions-), which are in the Meeting Controls panel at the bottom of the Zoom window. Have them select the thumbs up emoji if they successfully created and configured the AWS resource that you’re checking.

3. Use the feedback from this check to either recommend office hours for reviewing things in more depth or adjust your pace throughout the rest of the class.

Before moving on, answer any questions that the students might have.

---

### 3. Instructor Do: Applications of NLP in Finance (10 min)

In this activity, you’ll highlight some of the most prominent applications of NLP in finance to the students.

Start with an explanation of how NLP works by posing the following day-to-day example to the class:

* Many of us have played movies and television shows in which computers and robots have conversations with people, making life more comfortable.

* Today, this scenario is no longer fictional. Thanks to NLP, we can create software applications that interact with people via spoken or written dialogues.

Explain to the students that NLP is an exciting area of machine learning and that it widely intersects the fields of research in computer science, statistics, linguistics, and other disciplines. The fintech industry uses NLP in various contexts, such as sentiment analysis, quantitative trading, fraud detection, and chatbots for client interaction. In today's class, we’ll review some of the most relevant examples.

Mention that in today's class, they’ll first learn the fundamental concepts of NLP and CUIs. They’ll then use Amazon Lex, a cloud service that AWS provides, to create a chatbot, which is often shortened to just **bot**. Explain that in the fintech industry, chatbots make up one of the most common applications of CUIs.

#### Sentiment Analysis

Explain to the students that **sentiment analysis** is the computational study of the opinions, sentiments, emotions, and attitudes of people. It’s one of the most popular applications of NLP. Highlight the following:

* Although sentiment analysis is normally tied to marketing, the fintech world has given it significant attention because of its wide range of applications.

* These range from customer service, competition benchmarking, and investment assistance to news and social media analysis.

* With sentiment analysis, we can answer questions like the following: will a stock that’s unpopular on social media open with a loss today? Besides analysing social media, we can use sentiment analysis to understand what news headlines express about a stock&mdash;for the purpose of supporting investment decisions.

* For example, on September 8, 2020, Tesla (TSLA) shares lost 21% of their value after Standard & Poor’s declined to add Tesla to the S&P 500. The news about this decision influenced the sentiments of traders about TSLA shares&mdash;and the TSLA stock price slumped!

You’re encouraged to illustrate this example with the following image, which shows a line plot of the TSLA price over time:

![A screenshot depicts the line plot.](Images/15-1-tsla-price-slump.png)

Explain to the students that as the image shows, sentiments can impact how the stock market behaves. Point out that thanks to NLP, we can assess the impact and gain additional insights for making better financial decisions.

Explain that by using NLP, we can introduce sentiment analysis as part of a trading strategy&mdash;specifically, to predict the effects of breaking news or social media on the stock market. Although traders don’t formally use sentiment analysis, several researchers are working toward integrating it into trading strategies.

Slack out the following research papers to the students, and encourage them to read these papers to learn more about how sentiment analysis is being used in the financial industry:

* [Predicting the Effects of News Sentiments on the Stock Market](https://www.researchgate.net/publication/329588387_Predicting_the_Effects_of_News_Sentiments_on_the_Stock_Market)

* [Stock Prediction Using Twitter Sentiment Analysis](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.375.4517)

#### Conversational User Interfaces

Explain to the students that CUIs and robo advisors make up another disruptive application of NLP in the fintech realm. Highlight the following:

* In the early years of computing history, people communicated with computers by using text interfaces, such as the Windows command line. These required entering instructions that were not human friendly. But thanks to advances in NLP, we can now communicate with computer systems by using human language via voice or text that goes through CUIs.

* The chatbot is the most common application of the CUI. Amazon Alexa, Apple Siri, and Google Assistant are the most popular examples of this type of interface.

* In this module’s Challenge assignment, you’ll use Amazon Lex to create a robo advisor for an investment portfolio. Amazon Lex is the NLP technology that uses Alexa, which is the virtual assistant that Amazon developed.

* CUIs, and chatbots in particular, have been disrupting finance as an additional communication channel for customers.

* The most relevant benefits of this technology include the following:

  * **Support and advice:** Because of chatbots, financial institutions can offer 24-7 support and advice to customers. They can also reduce operational costs through this enhancement of the customer experience, especially by offering fast-paced communication.

  * **A customised experience:** By using NLP and sentiment analysis, chatbots understand how people communicate. Financial institutions can thus respond more appropriately to customer needs. This is because the machine learning algorithms behind chatbots can learn how a customer behaves&mdash;and then offer a customised experience.

  * **Efficiency:** CUIs boost employee satisfaction. This is particularly true in call centres, where operators will respond to fewer calls about common questions that a chatbot can answer. The operators can then focus their efforts on responding to complex financial issues that keep customers awake at night.

Continue the explanation of CUIs by highlighting the following aspects of their application to banking:

* According to Juniper Research, [banks will annually save $7.3 billion by 2023](https://www.juniperresearch.com/press/press-releases/bank-cost-savings-via-chatbots-reach-7-3bn-2023), thanks to chatbot use.

* Customers don't need to wait for people to perform common tasks or reply to common inquiries. Instead, [chatbots can improve the customer experience](https://www.processmaker.com/blog/how-chatbots-improve-customer-experience/) by performing tasks 24-7.

* Around the world, some institutions and emerging startups already use chatbots. In Canada, for example, Bank of Montreal uses a chatbot [BMO Bolt](https://www.bmo.com/main/personal/chatbot/) so that  customers can contact the bank 24-7 via Facebook or Twitter for questions about products, foreign exchange rates, branch locations, and ATM locations.

* Bank of America launched [Erica](https://promotions.bankofamerica.com/digitalbanking/mobilebanking/erica) to customers. Erica provides a digital banking experience that includes voice communication, in-app messaging, and predictive analytics. By December 2021, Erica had reached more than 17 million users.

Explain to the students that thanks to modern cloud computing services, like the ones that AWS offers, we can start creating a chatbot by making a few selections.

Before moving on, answer any questions that the students might have.

---

### 4. Instructor Do: Introduction to Amazon Lex (15 min)

In this activity, you’ll introduce the students to Amazon Lex. You’ll need to log in to the AWS Management Console, so be sure not to expose your credentials or any other confidential information while presenting your screen to the class.

Open the lesson slides, and then introduce Amazon Lex by highlighting the following:

* Amazon Lex is an AWS service that developers can use to create CUIs. This service uses the same machine learning technology that powers Amazon Alexa.

* As a fintech professional using Amazon Lex, you’ll be able to build chatbots that enhance the customer care services in financial institutions. You’ll also be able to develop robo advisor applications that can help people make financial decisions.

* The advantage of using CUIs is that we can use human language, as voice or text, to enable a 24-7 communication channel. Amazon Lex and the other AWS cloud services that we’ll learn in this module will support the channel that we enable.

Tell the students that Amazon Lex supports two versions. Tell them that In this module, they’ll work with Version 1. That’s because Version 2 launched on January 22, 2021, and bots created in Version 1 aren’t compatible with Version 2.

* **Important:** Emphasize that the students should not switch to the Amazon Lex V2 console.

Continue introducing Amazon Lex by highlighting the following features that it includes:

* **Automatic speech recognition:** Amazon Lex uses automatic speech recognition to convert speech to text. It then uses NLP to recognise the intent of the text.

* **Deep learning algorithms:** Amazon Lex captures all the complexity of deep learning algorithms. So, using Amazon Lex requires no coding, and neither does creating a CUI.

* **Third-party application integration:** With Amazon Lex, you can integrate third-party applications (like Slack or Facebook Messenger) and other AWS services (like Amazon S3 or Amazon SageMaker). With AWS Lambda, you can also use your own Python code to create custom functionality that extends Amazon Lex.

* **A two-step process:** Getting started with Amazon Lex is straightforward:

  1. Create a bot, and configure it to understand the user’s goals, or intent.

  2. Test the bot on the Amazon Lex console.

Explain to the students that Amazon Lex is available in only some AWS regions. For Lex V1, these are US East (N. Virginia), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Europe (Frankfurt), Europe (Ireland), Europe (London), and AWS GovCloud (US-West). Furthermore, the pricing varies among the regions. Before starting to use Amazon Lex, they should make sure that it’s available in the AWS region where they want to deploy their Amazon Lex bot.

For the latest list of the supported AWS regions, slack out the link to the [Amazon Lex endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/lex.html) page. Mention that in this module, we’ll use the US West (Oregon) region.

Before using Amazon Lex to create the first chatbot, use the lesson slides to introduce the following Amazon Lex terminology:

* **Bot:** The core component of Amazon Lex. A bot performs automated tasks, such as booking a hotel, making a wire transfer, or suggesting an investment portfolio.

* **Intent:** An action that the user wants to perform, such as `BookHotel`, `TransferMoney`, or `SuggestPortfolio`. A bot can have more than one intent.

* **Utterance:** A speech or text phrase that triggers the intent. This refers to the dialogue between the user and the bot. An example is: I want to send 100 dollars to Laila.

* **Slot:** An allotted place for a piece of data that the chatbot needs to fulfil the user’s intent. Think of it as a required user-input item.

* **Prompt:** A question that asks the user to input data.

* **Fulfillment:** The business logic that the chatbot needs to fulfil the user’s intent. When the chatbot has collected all the slot values, it proceeds with the logic in the fulfilment section. This is where you can use an AWS Lambda function if you need business logic.

The following image illustrates these terms in a sample conversation between a user and a bot:

![An illustration of the conversation.](Images/15-1-amazon-lex-concepts.png)

The preceding image includes the following conversation for the `convertDollars` intent:

1. Person: I want to convert dollars to crypto (this is the intent)

2. Bot: Sure, which cryptocurrency would you like? (this is an utterance)

3. Person: Bitcoin (this fills a slot)

4. Bot: How many dollars do you want to convert? (this is a prompt)

5. Person: 150 (this is the fulfilment)

6. Bot: You can get 0.0030 bitcoins for your 150 dollars

#### Setting Up a Bot with Amazon Lex

* **Important:** Amazon Lex supports two versions. In this module, you’ll work with **Version 1**. Bots created in Version 1 aren’t compatible with Version 2. Make sure that you don't switch to the Amazon Lex V2 console.

Explain to the students that you'll follow the two-step process to build a chatbot by using Amazon Lex. Mention that you’ll start by demonstrating how to set up an Amazon Lex bot that will establish a dialogue for converting dollars to bitcoins.

**Important:** In this module, the screenshots and descriptions of the AWS user interface appear as they exist at the time of this writing. But, you might find slight differences because of updates.

Open your browser, and then log in into the [AWS Management Console](https://aws.amazon.com/console/). Explain to the students that using the administrator IAM user is recommended, which they learned when following the AWS Account Setup Guide for this module.

Demonstrate starting to create the bot by completing the following steps:

1. In the AWS Management Console, in the AWS Region drop-down list, click “US West (Oregon) us-west-2”.

    ![“”](Images/15-1-selecting-aws-oregon-region.png)

2. In the Find Services search box, type Lex, and then in the Services list that displays, click Amazon Lex.

    ![“”](Images/15-1-choosing-amazon-lex-from-aws-services-list.png)

3. If you’ve created a bot before, skip to Step 4. Otherwise, on the Amazon Lex page that displays, click the Get Started button.

    ![“”](Images/15-1-amazon-lex-starting-page.png)

4. If this is the first time that you’re creating a bot, skip this step. Otherwise, if you’ve created a bot before, note that an Amazon Lex page displays with a list of your current bots. On this page, click the Create button.

    ![“”](Images/15-1-alternate-amazon-lex-start-page.png)

Explain to the students that you’re now ready to start creating the bot. Explain that when you create a bot with Amazon Lex, you can either create a bot from scratch or try one of the sample bots that AWS offers to test the service. Mention that you’ll create a custom bot.

Demonstrate continuing to create the bot by completing the following steps:

1. On the “Create your bot” page, click the "Custom bot" button.

    ![“”](Images/15-1-lex-bot-initial-configuration.png)

2. Still on the “Create your bot” page, configure the bot as follows:

    * In the “Bot name” box, type CryptoConverter.

    * In the Language drop-down list, click “English (US).”

      * Mention that Amazon Lex is available only in German, English (Australian, UK, India, and US), Spanish (Latin American, Spain, and US), French (Canada and France), Italian, Japanese, and Korean. For the latest list of the available languages, slack out the link to [Languages Supported in Amazon Lex](https://docs.aws.amazon.com/lex/latest/dg/how-it-works-language.html) in the Amazon Lex Developer Guide.

    * In the “Output voice” drop-down list, click Joanna.

    * In the “Session timeout” box, type 5, and then in the associated drop-down list, click “min.”

    * For the “Sentiment analysis” option, select No.

      * Explain that late in 2019, AWS added the sentiment analysis feature to Amazon Lex. With this feature, we can score the sentiment of each user utterance by using another service named [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html)&mdash;which incurs an additional cost. We won’t use this feature in this lesson, but slack out the link to the [sentiment analysis documentation](https://docs.aws.amazon.com/lex/latest/dg/sentiment-analysis.html), which the students can review for further research.

    * For “IAM role,” leave the default value.

    * For the COPPA option, select No.

    * For the “Advanced options” option, select No.

      **Important:** Explain to the students that the reason for selecting No concerns information privacy. Selecting Yes causes the dialogues to be sent as training data to improve AWS algorithms. If the students ever create an Amazon Lex bot for any company, we recommend reviewing the company's information privacy policies before selecting Yes.

    * In the “Confidence score threshold” box, leave the default value.

3. Click the Create button.

The following image shows the final configuration:

![A screenshot depicts the selections on the “Create your bot” page.](Images/15-1-creating-amazon-lex-bot.png)

Mention that you’ve now shown the students how to set up an Amazon Lex bot. Explain that they’ll follow the same steps to start creating a robo advisor in the next activity.

Before moving on, answer any questions that the students might have.

---

### 5. Student Do: Setting Up a Bitcoin Fear & Greed Robo Advisor (15 min)

**Corresponding activity:**

* [01-Stu_Setting_Up_Robo_Advisor](Activities/01-Stu_Setting_Up_Robo_Advisor)

**File:**

* [Instructions](Activities/01-Stu_Setting_Up_Robo_Advisor/README.md)

In this activity, the students will set up an Amazon Lex bot that will implement a robo advisor.

Some students might need extra time for this activity. If any students get stuck, move forward with the class, and help those students during the break.

---

### 6. Instructor Do: Review Setting Up a Bitcoin Fear & Greed Robo Advisor (10 min)

Start this review activity by conducting a pulse check to find out how many students were able to set up an Amazon Lex bot.

Ask the class if they were able to finish this activity. If you’re teaching an online class by using Zoom, remain in the [Gallery View](https://support.zoom.us/hc/en-us/articles/201362323-Changing-the-video-layout-Speaker-view-and-Gallery-view-) for this activity so that you can observe your class on one screen.

Ask the students to find the [Zoom Meeting Reactions](https://support.zoom.us/hc/en-us/articles/115001286183-Non-verbal-feedback-and-reactions-), which are in the Meeting Controls panel at the bottom of the Zoom window. Have them select the thumbs up emoji if they successfully created and configured the robo advisor bot.

Use the feedback from this check to either recommend office hours for reviewing things in more depth or adjust your pace throughout the rest of the class.

Before moving on, answer any questions that the students might have.

---

### 7. Break (15 min)

---

### 8. Instructor Do: Bringing an Amazon Lex Bot to Life (15 min)

In this activity, the students will learn how to add intents and utterances to an Amazon Lex bot for interacting with a user by using human language. You’ll continue building the bot that converts dollars to bitcoins.

Open the [AWS Management Console](https://aws.amazon.com/console/). Then go to the Amazon Lex console, and open the CryptoConverter bot. Explain to the students that you’ll now demonstrate how to add user interaction to the bot by creating an intent.

#### Create an Intent to Respond

To create an intent to respond to the user, demonstrate the following steps:

1. Click the Create Intent button, and then in the "Add intent" dialog box that appears, click “Create intent,” as the following animation shows:

    ![An animation depicts this step.](Images/15-1-creating-intent.gif)

2. Note that in the “Create intent” dialog box that appears, you need to name the intent. Usually, you name an intent to describe the action that the bot will perform. So in the “Give a unique name for the new intent” box, type convertUSD, and then click the Add button.

    ![“”](Images/15-1-create-intent.png)

#### Configure the Intent to Interact with Natural Language

Explain to the students that you’ll now configure the intent so that the bot can interact with the user by using natural language. To do so, you’ll supply some starting context about the conversation that the bot will conduct. You’ll supply this context by adding sample utterances. **Sample utterances** are phrases that a user might use to start a conversation with the bot.

Explain that the deep learning algorithm of Amazon Lex will use the sample utterances to understand the context of the conversation. The more sample utterances that you add, the better the conversation will flow between the bot and the user. You’ll start by adding three sample utterances.

To add the sample utterances, demonstrate the following steps:

1. On the CryptoConverter page, in the “Sample utterances” box, type the following utterance, and then click the Add button, which has a plus sign (+) icon:

    * I want to convert USD to BTC

2. Note that the utterance displays under the “Sample utterances” box. Repeat Step 1 for the following two utterances, and note that they also appear:

    * I want to convert dollars to BTC

    * I want to convert dollars to bitcoin

The following image shows the result:

![A screenshot depicts the three utterances displayed on the page.](Images/15-1-adding-sample-utterances.png)

Explain to the students that you just configured the sample utterances, which are examples of what a user might enter to start the expected dialogue. Next, you’ll define how the bot should answer the user &mdash;for the purpose of requesting the data that it needs to make a decision or perform a task.

#### Define Slots to Capture User Input

Remind the students that this bot will convert dollars to bitcoins. So, we need a way for the bot to ask how many dollars the user wants to convert. To do that, we allow the bot to ask questions by using slots.

Explain to the students that **slots** are like variables in a Python program. For each slot, we define a name, a data type (known as the **slot type** in Amazon Lex), and a prompt. The **prompt** is the question that the bot will ask the user to get the data to fill the slot.

Explain that for this bot, you’ll add two slots. You'll define the first slot as follows:

* **Name:** `birthday`

* **Slot type:** `AMAZON.DATE`

  * Mention that Amazon Lex supplies several built-in slot types for the most common types of data that a bot might need to get during a conversation.

* **Prompt:** This service can only be used by people over 21 years old, could you please give me your date of birth?

Next, you’ll define the second slot as follows:

* **Name:** `dollars`

* **Slot type:** `AMAZON.NUMBER`

* **Prompt:** How many dollars do you want to convert?

To add the two slots, scroll down to the Slots section, and then demonstrate the following steps:

1. In the Name box, type birthday,

    ![“”](Images/15-1-adding-slot-name.png)

2. Click the “Slot type” drop-down list box, and then in the “Search by slot type name” box that appears, type DATE. In the drop-down list that appears, click AMAZON.DATE. The following animation shows this step:

    ![An animation depicts this step.](Images/15-1-adding-slot-type.gif)

3. In the Prompt box, type the following text, and then click the Add button, which has a plus sign (+) icon:

    * This service can only be used by people over 21 years old, could you please give me your date of birth?

    ![“”](Images/15-1-adding-slot-prompt.png)

4. Repeat Steps 1&ndash;3 with the info for the second slot:

    * **Name:** `dollars`

    * **Slot type:** `AMAZON.NUMBER`

    * **Prompt:** How many dollars do you want to convert?

5. Notice that both slot definitions now appear in the Slots section. For each one, select the Required checkbox.

    ![“”](Images/15-1-checking-slots-as-required.png)

Explain to the students that once a bot gets all the data that it needs to help the user, it needs to respond to find out if the user wants to continue or cancel the conversation. So, we need to configure how the bot will respond.

#### Create the Bot Response

Explain to the students that the final part of building a bot is defining how it will respond when it successfully fills all the slots. This includes how it will respond if the user wants to cancel the conversation. Point out that we do this in the “Confirmation prompt” section of the CryptoConverter page.

To create the bot response, demonstrate the following steps:

1. Scroll down to the “Confirmation prompt” section, and then select the “Confirmation prompt” checkbox.

2. In the Confirm box, type the following text:

    * Are you sure you want to convert ${dollars} to Bitcoin?

      **Note:** Explain to the students that in this text, `{dollars}` is like a variable. It will get replaced with the value that the user supplies in the conversation.

3. In the Cancel box, type the following text:

    * Okay, let’s start again.

The following image shows Steps 1&ndash;3 completed in the “Confirmation prompt” section:

![A screenshot points out the “Confirmation prompt” section.](Images/15-1-setting-confirmation-prompts.png)

Explain to the students that you’ve now set all the necessary configurations for the bot. And after the break, they’ll have a chance to create their own intent for their robo advisor bot!

Before moving on, answer any questions that the students might have.

---

### 9. Student Do: Adding User Interaction to the Robo Advisor (20 min)

**Corresponding activity:**
[02-Stu_Adding_Interaction_Robo_Advisor](Activities/02-Stu_Adding_Interaction_Robo_Advisor)

**File:**

* [Instructions](Activities/02-Stu_Adding_Interaction_Robo_Advisor/README.md)

In this activity, the students will add an intent to provide user interaction to the robo advisor that they created earlier.

---

### 10. Instructor Do: Review Adding User Interaction to the Robo Advisor (10 min)

Start this review activity by conducting a pulse check to find out how many students were able to both add the intent and create the slots for the Amazon Lex bot.

Ask the class if they were able to finish this activity. If you’re teaching an online class by using Zoom, remain in the [Gallery View](https://support.zoom.us/hc/en-us/articles/201362323-Changing-the-video-layout-Speaker-view-and-Gallery-view-) for this activity so that you can observe your class on one screen.

Ask the students to find the [Zoom Meeting Reactions](https://support.zoom.us/hc/en-us/articles/115001286183-Non-verbal-feedback-and-reactions-), which are in the Meeting Controls panel at the bottom of the Zoom window. Have them select the thumbs up or smile emoji if they successfully created and configured both the intents and the slots.

Use the feedback from this check to either recommend office hours for reviewing things in more depth or adjust your pace throughout the rest of the class.

Explain to the students that the names of intents and slots are case sensitive. So, they should remain aware of how they name their intent and their slots. Later, when they learn how to connect an Amazon Lex bot with Python code by using a service named AWS Lambda, they’ll use these case-sensitive names.

Before moving on, answer any questions that the students might have.

---

### 11. Instructor Do: Building and Testing an Amazon Lex Bot (10 min)

In this activity, the students will learn how to build and test an Amazon Lex bot. You’ll build and test the bot that converts dollars to bitcoins.

Open the AWS Management Console. Then go to the Amazon Lex console, and open the CryptoConverter bot. Explain to the students that now that you’ve added user interaction to the bot, you can interact with it by testing it in the Amazon Lex console.

It’s time to observe the bot in action! To do so, demonstrate the following steps:

1. Click the Build button (in the upper-right corner of the page), and then in the “Build your bot” dialog box that appears, click the Build button, as the following animation shows:

    ![An animation depicts this step.](Images/15-1-building-bot-for-testing.gif)

2. Note that the build process takes a couple of minutes. When it finishes, a confirmation message displays that states “CryptoConverter build was successful,” and the “Test bot” pane appears.

    ![“”](Images/15-1-bot-successfully-built.png)

3. Close the confirmation message. Then in the “Test bot” pane, test the bot by completing the following steps:

    * In the “Chat with your bot” box, type the following sample utterance:

      I want to convert dollars to bitcoin

    * Note that the bot asks for your date of birth. Type your date of birth.

      **Important:** Explain that the `AMAZON.DATE` slot type automatically converts dates to the yyyy-mm-dd format. You can type your date of birth in any format. Examples are 12/16/1978 and Dec 16, 1978.

    * When the bot asks how many dollars you want to convert, type 100.

    * When the bot asks if you’re sure that you want to convert $100 to Bitcoin, type yes.

    * Note that the bot displays a final confirmation message.

      The following animation shows these steps:

      ![An animation depicts these steps.](Images/15-1-testing-bot.gif)

4. Note that at this time, the bot has no business logic attached. The bot can have a dialogue with the user and get the data that it needs, but it won’t yet fulfil the user’s intent to convert dollars to bitcoins. That’s why the final confirmation message is somewhat impersonal, stating “Intent convertUSD is ReadyForFulfillment.”

    ![“Message from the bot displaying fulfilment.”](Images/15-1-fulfillment-message.png)

Explain to the students that you’ll add more functionality to the bot by using an Amazon Lambda function later in this module. But now, it’s their turn to test their own Amazon Lex bots.

Before moving on, answer any questions that the students might have.

---

### 12. Student Do: Building and Testing the Robo Advisor (15 min)

**Corresponding activity:** [03-Stu_Testing_Robo_Advisor](Activities/03-Stu_Testing_Robo_Advisor)

**File:**

* [Instructions](Activities/03-Stu_Testing_Robo_Advisor/README.md)

In this activity, the students will build and test their Bitcoin Fear & Greed robo advisors.

---

### 13. Instructor Do: Review Building and Testing the Robo Advisor (10 min)

Start this review activity by conducting a pulse check to find out how many students were able to build and test the Amazon Lex bot.

Ask the class if they were able to finish this activity. If you’re teaching an online class by using Zoom, remain in the [Gallery View](https://support.zoom.us/hc/en-us/articles/201362323-Changing-the-video-layout-Speaker-view-and-Gallery-view-) for this activity so that you can observe your class on one screen.

Ask the students to find the [Zoom Meeting Reactions](https://support.zoom.us/hc/en-us/articles/115001286183-Non-verbal-feedback-and-reactions-), which are in the Meeting Controls panel at the bottom of the Zoom window. Have them select the thumbs up emoji if they’ve successfully built and tested the robo advisor bot.

Use the feedback from this check to recommend office hours for reviewing things in more depth.

Explain to the students that currently, the bot has no business rules logic attached. That’s why the final message that the bot sends after fulfilling all the slots is an unfriendly confirmation message. Later in this module, we’ll improve this by adding an Amazon Lambda function to the bot.

![“Example message from the bot”](Images/15-1-fulfillment-message-stu.png)

Before moving on, answer any questions that the students might have.

---

### 14. Instructor Do: Recap (5 min)

In this activity, you’ll do a final recap with the class. Use the lesson slides to summarise what the students learned in today's class:

* As you learned today, NLP is disrupting the finance industry with multiple applications, where chatbots enable better customer communications.

* AWS is a leading cloud platform that you can use to build chatbots&mdash;for implementing automated communication channels with customers by using human language.

* As you experienced in today's class, you can create and test a chatbot with just a few clicks and without code.

Mention that in the next class, the students will learn how to enhance the interaction between a bot and a person by adding business logic rules. To do so, they’ll use Python and another AWS service, named AWS Lambda.

Before ending the class, answer any remaining questions that the students might have.

### End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
