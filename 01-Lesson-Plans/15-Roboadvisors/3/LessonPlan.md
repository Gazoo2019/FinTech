## 15.3: Running Machine Learning Models in the Cloud

### Overview

In today's class, the students will learn how to use Amazon SageMaker Studio. Specifically, they’ll use it with their Python and machine learning skills to deploy and run machine learning models in the cloud.

### Class Objectives

By the end of this class, the students will be able to:

* Explain how SageMaker Studio works and use it to deploy machine learning models.

* Identify fintech business cases for which they can use Amazon SageMaker to enhance decision making.

* Orchestrate a machine learning cloud solution by combining AWS services.

---

### Instructor Notes

* This lesson rapidly introduces new content. And, the students might express frustration about learning new cloud technologies. Remind them that although the learning curve might seem steep at first, AWS and cloud experience are highly sought after and well worth the effort that’s required to become comfortable with them.

* In the past, the AWS content has appeared differently for some instructional teams. It seems that AWS does A/B testing on their UI. If your AWS views don't match those in this lesson plan, check that you've pulled the latest updates from GitHub. Or, check the instructional team Slack channel for announcements about this.

* Today's class should be fun! The students will combine many of the technologies that have been covered so far and learn how they can interact with cloud services.

* A few activities require setup. In these cases, have the class follow along and ask questions as you go.

* You’ll guide the students on the process of launching SageMaker Studio for the first time. To follow the steps in this lesson plan, you might need to delete your current SageMaker Studio domain. To do so, follow the steps in [Delete a Amazon SageMaker Domain (Console)](https://docs.aws.amazon.com/sagemaker/latest/dg/gs-studio-delete-domain.html#gs-studio-delete-domain-studio) in the Amazon SageMaker Developer Guide.

### Class Slides and Time Tracker

* You can review the slides for this lesson on Google Drive at [Lesson 15.3 Slides](https://docs.google.com/presentation/d/1C7lpPSPcQMr_9eW1ye-V0p2NLBW1z6Oc5sWgvi4Wi9s/edit?usp=sharing).

  * **Note:** If you want to modify the slides, create a copy as follows: on the File menu, select "Make a copy," and then select “Entire presentation.”

* To add the slides to the student-facing repository, first download the slides as a PDF. To do so, open the slide deck for this lesson. On the File menu, select Download, and then select "PDF Document (.pdf)." Then, add the PDF file and other necessary files to your class repository. This way, if the curriculum changes in the future, your students will always have the slides that align with the lesson you taught.

* You can review the Time Tracker for this lesson at [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome and Introduction to Machine Learning Models in the Cloud (10 min)

In this activity, you'll welcome the students to the last class of Module 15. Then, the students will learn how they can use cloud services in the fintech industry and some pros and cons of this technology.

Start the class by welcoming the students to the last day of this module. Explain that today, they’ll work with SageMaker Studio&mdash;a service that AWS provides for running machine learning models in the cloud. Mention that although using this service is not required for this module’s Challenge assignment, SageMaker is a powerful tool that will act as an ally in their careers as fintech professionals. This will happen every time that they need to deploy a machine learning model in the cloud. Also, remind the students that they can use SageMaker Studio as part of their second project.

Open the lesson slides, and highlight the following:

* Thanks to the current prices of computers, we can have powerful equipment at home on which to run machine learning models at different levels of complexity. For models that vary from a simple linear regression model to a complex deep learning model, we can mostly use our personal computers.

* Using our personal computers to create prototypes of machine learning models is terrific. But for placing a model in a production environment, we can’t use our own computers.

* Cloud services, like those that AWS offers, ease the creation, testing, and deployment of machine learning models in the cloud. Hundreds or even thousands of people will be able to reach and use those models. And, we have more computing power to process large datasets than we do when using our personal computers.

* In today's class, you’ll learn how to create, fit, and deploy a machine learning model in the cloud by using Amazon SageMaker. This AWS service offers an extensive library of machine learning models that are optimised for the cloud and that we can use with Python.

* For a fintech professional, being able to orchestrate a cloud-based machine learning solution that combines various AWS services is a valuable skill. After completing this class, you’ll be able to benefit from your current machine learning skills by using the power of the cloud to run machine learning models.

#### Fintech and the Computing Power of Cloud Services

Now, you’ll engage the students with the benefits of using the cloud by presenting facts about this technology and some real-world applications in the fintech industry. Highlight the following:

* As you’ve experienced by now, cloud services are magnificent! They offer lots of computing power that’s readily available.

* In fact, the **cloud** refers to the on-demand availability of computer resources, such as computer processing power; data storage; and other resources, like chatbots and serverless applications.

* One of the greatest advantages of cloud computing is that we don’t need physical access to the hardware. Instead, we access the hardware through the internet (via public or private networks).

* Normally, you pay as you go for what you use&mdash;sometimes down to the second or the byte&mdash;with little or no up-front costs.

* Cloud services usually charge like utility services do (think of an electricity bill). So, cloud computing usually costs less than having your own hardware. That’s because of the economics of scale (and no up-front costs for the physical hardware, setup, or provisioning).

* Cloud computing is also considered secure enough for many banks and government offices to use it. And, several well-known cloud service providers exist, including Amazon, Microsoft, Google, Oracle, and IBM.

Explain that multiple service models exist with trade-offs in the areas of responsibility and control. The most common are the following:

* **Infrastructure as a service (IaaS)**: Supplies APIs for accessing various infrastructure elements, such as servers, virtual machines, storage solutions, load balancers, and network interfaces. An example is [Azure Virtual Machines](https://azure.microsoft.com/en-us/services/virtual-machines/).

* **Platform as a service (PaaS)**: Supplies a platform on which customers can develop, run, and manage applications&mdash;without the complexity of building and maintaining their own physical infrastructure. An example is [AWS](https://aws.amazon.com/).

* **Software as a service (SaaS)**: Refers to a software licensing and delivery model, which licenses software that’s centrally hosted on a subscription basis. An example is [Microsoft Office 365](https://www.office.com).

* **Function as a service (FaaS)**: Offers the ability to deploy individual functions in the cloud that run in response to events. FaaS is also known as **serverless computing**. An example is [AWS Lambda](https://aws.amazon.com/lambda/).

Explain to the students that cloud computing is becoming a game changer in financial services. That’s because it reduces operational costs, improves productivity, and allows for advanced data analytics that can lead to a competitive advantage over the long term. Nowadays, instead of having large IT departments, financial institutions are partnering with technology companies to deliver joint solutions in the cloud.

Engage the students with the benefits of cloud services in the fintech industry by presenting the following examples about financial institutions partnering with technology companies to deliver cloud-powered services. Feel free to enrich this section with examples from your professional experience:

* In 2020, [AWS and HSBC made a strategic deal](https://fintechranking.com/2020/07/15/aws-and-hsbc-strike-global-cloud-banking-deal/) to support the digital transformation efforts of HSBC.

* Google partnered with [Deutsche Bank](https://www.fnlondon.com/articles/deutsche-bank-google-to-enter-strategic-partnership-20200707) to deliver cloud services.

* Google also partnered with [Goldman Sachs](https://youtu.be/LsZq6_wZAHM), one of the world’s leading investment management firms, to drive innovation to solve problems for its clients as quickly as possible.

Explain to the students that despite the benefits of cloud computing, they should be aware of some drawbacks:

* Trusting a third-party provider with your data. (But, encryption can address this.)

* Compromising privacy and confidentiality.

* Depending on the provider’s service level agreements for addressing issues.

* Failing hardware incidents, with less oversight of their resolution.

* Sharing hardware with other tenants. The bad behaviour of other tenants can affect your resources.

* Having downtime, including periods of planned maintenance that are out of your control.

* Lacking a universal compliance program for adopting cloud services in the fintech industry. You must deal with the particular laws and regulations in every country or region in which you want to use this technology.

Explain that for many years in the financial industry, the chief information officer (CIO) had the responsibility of making most of the decisions about technology. But today technology impacts all the functional areas of a financial organisation. That’s why it’s crucial to involve all the C-level executives in the adoption of new technologies&mdash;like machine learning applications and cloud services. In this way, a better consensus will be reached regarding technology adoption decisions.

Point out that as fintech professionals, they might become C-level executives or offer expert advice as consultants. So, it’s important to break the paradigm that technology is only for techies and recognise that technology is for everyone. Slack out the following links, and encourage the students to read the reports If they want to learn more about the importance of the cloud to all C-level executives:

* [Public Cloud Adoption in Financial Services: 7 Key Considerations for CIOs and Other Key Stakeholders](https://www.ibm.com/downloads/cas/A2YBMXWZ) from Celent.

* [Cloud banking: More than just a CIO conversation](https://www2.deloitte.com/us/en/pages/financial-services/articles/bank-2030-financial-services-cloud.html) from Deloitte.

Finally, explain that financial services demand accurate and secure computing power&mdash;especially when deploying machine learning solutions as part of their services. AWS provides a platform, named Amazon SageMaker, that provides such capability. Specifically, SageMaker offers the ability to build, train, and deploy machine learning models in the cloud. In the next activity, the students will learn more about this platform and how to use it.

Before moving on, answer any questions that the students might have.

---

### 2. Everyone Do: Getting Started with Amazon SageMaker Studio (30 min)

In this activity, the students will learn how SageMaker works. And, they’ll start to learn the process of launching a Jupyter notebook in the cloud by using SageMaker Studio.

Explain to the students that this activity is intended to be done collaboratively. So, they should follow along with you as you demonstrate the process of configuring and launching SageMaker Studio.

Before you do so, open the lesson slides, move to the "Getting Started with Amazon SageMaker Studio" section, and highlight the following points:

* We’ve learned a lot about machine learning in the past few weeks. But, deploying a machine learning model in a production environment can become complex and expensive. This might happen because of the necessary configuration of several computer servers, the implementation of security policies, and the need for gigabytes of disk space and memory.

* Fortunately, we have cloud services that can handle the complexity behind deploying such a model. So, we can focus on finding the best model for a financial business scenario, such as detecting fraud, predicting stock prices, or clustering customer information for new services discovery.

* Part of the AWS family, the [SageMaker](https://aws.amazon.com/sagemaker/) PaaS (Platform as a Service) consists of four main components: Prepare, Build, Train & Tune, and Deploy & Manage. We can use these components either together or independently for the four stages of the machine learning development workflow.

  ![“”](Images/15-3-sagemaker-components.png)

* SageMaker implements the machine learning development workflow as follows:

  * Prepare: This component offers tools for automating the data preparation tasks that are required to train and validate a machine learning model.

  * Build: With this component, machine learning developers can create notebooks to build models and explore data. The component also provides access to several prebuilt algorithms and models through a marketplace.

  * Train & Tune: This component offers tools for model training, debugging, and tuning. A remarkable feature of this component is automatic model tuning, which offers one-click hyperparameter optimisation.

  * Deploy & Manage: This component allows for publishing and hosting a model as an API and offers model monitoring tools.

* Covering all the tools that the preceding components contain is beyond the scope of this lesson. Instead, we’ll focus on learning about SageMaker Studio, which is an integrated development environment (IDE) that’s based on Jupyter notebooks. It offers the capability to build, train, tune, and deploy machine learning applications in the cloud.

* With SageMaker Studio, we can work with machine learning models in the same way that we worked with Jupyter notebooks locally on our computers. The main difference is that Studio runs in the cloud and provides access to all the AWS machine learning libraries in a convenient way&mdash;specifically, through Python and notebooks.

#### Launch the Amazon SageMaker Console

You'll lead the class on launching the SageMaker console. Log in to the AWS Management Console with the administrator user, and ask the students to do the same. Confirm that everyone in the class is logged in to AWS, and then demonstrate the following steps:

1. In the AWS Management Console, click the Find Services search box, and then type sagemaker. In the resulting Services list, click Amazon SageMaker.

    ![“”](Images/15-3-launching-sagemaker.png)

2. Note that the SageMaker console is launched.

3. In the navigation pane on the left side, click Studio:

    ![“”](Images/15-3-launching-sagemaker-studio.png)

    **Note:** Not all AWS regions make Studio available. The demos and activities in this lesson use the “US West (Oregon)” AWS region. For the latest list of the AWS regions where you can use this service, refer to [Service Endpoints](https://docs.aws.amazon.com/general/latest/gr/sagemaker.html) in the AWS Reference guide.

Now that you’ve launched the Sagemaker console, you’ll next demonstrate how to set up Studio.

#### Set Up Amazon SageMaker Studio

Explain to the students that before we can start using Studio, we need to create a SageMaker domain. Explain that a **SageMaker domain** is a group of elements in the cloud (such as virtual machines, cloud storage, IAM users, and security policies) that we need to host a running Studio environment.

To create this domain, demonstrate the following steps, and ask the class to follow along with you as you do so:

1. Note that the first step is creating a user profile. But, we can let SageMaker handle the configuration. To do so, in the AWS Zone drop-down list (in the upper-right part of the screen), select Oregon as the AWS zone. Then in the Setup SageMaker Domain pane on the right side, leave “Quick setup” selected. In the same pane, in the “User profile” section, in the “Name” and "Default execution role" boxes, leave the defaults selected. Then click the Submit" button.

    ![“”](Images/15-3-setting-studio-user.png)

2. Note that next, we need to select a **virtual private cloud** (VPC). With a VPC, we can launch AWS resources into a virtual network. So in the “Choose a VPC” dialog box that appears, select the "Default vpc" option.

    ![“”](Images/15-3-select-default-vpc.png)

    **Note:** The exact name of the "Default vpc" option will differ for every user. It will be “Default vpc” followed by a hyphen (-) followed by a string of hex numbers followed by an IP address in parentheses.

3. In the Subnet box, select the first available option, and then click the "Save and continue" button.

    ![“”](Images/15-3-vpc-subnet.png)

4. Note that a “Preparing SageMaker Domain” message appears.

    ![“”](Images/15-3-sagemaker-domain-creation.png)

5. Note that after a few minutes, the Studio Domain is ready, and the “SageMaker Domain is ready” message appears.

    ![“”](Images/15-3-studio-instance-created.png)

Now that you’ve set up Studio, you’ll next demonstrate how to launch Studio.

#### Launch Amazon SageMaker Studio for the First Time

To launch Studio, demonstrate the following steps, and ask the class to follow along with you as you do so:

1. In the SageMaker Domain Control Panel, which the SageMaker Domain pane on the right side already displays, click the "Launch app" list, and then select Studio.

    ![“”](Images/15-3-open-sagemaker-studio.png)

2. Note that the Studio loading page appears, stating “Amazon SageMaker Studio: Loading the JupyterServer application default.” This page remains for up to five minutes the first time that you launch Studio. While you’re waiting, you and your TAs should check that everyone in the class has reached this point.

3. When the SageMaker Studio instance gets created, the Amazon SageMaker Studio user interface appears. Point out that the interface is based on JupyterLab but slightly differs from it. The following image shows the Studio interface with the Launcher tab selected:

    ![A screenshot depicts the Studio interface.](Images/15-3-sagemaker-studio-ui.png)

Explain to the students that we’re now ready to start building and deploying machine learning models in the cloud! Tell them that next, you'll demonstrate how to create a Jupyter notebook by using Studio.

#### Create a Jupyter Notebook by Using Amazon SageMaker Studio

Explain to the students that once Studio opens, we can start using it in a similar way as JupyterLab. Point out that the initial window displays the Launcher tab. That’s where we’ll need to choose a SageMaker image for creating the notebook.

Explain that a SageMaker image is a preconfigured running environment that resembles a Python virtual environment and that contains a set of Python libraries. Highlight the following:

* The SageMaker images are prebuilt Python environments that each contain the latest version of the [SageMaker Python SDK](https://sagemaker.readthedocs.io/).

* Each image also contains libraries that are specific to that image. Besides the Data Science image that we’ll use in this lesson, other images are available. We can choose an image depending on the project that we want to work on. And, we can create a custom image.

Slack out the link to [Available Amazon SageMaker Images](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-available-images.html), which provides a complete list of all the SageMaker images. Also, slack out the link to [Bring your own SageMaker image](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi.html), which explains how to use a custom image. Mention that both articles are in the Amazon SageMaker Developer Guide.

Explain to the students that we'll use the Data Science image, because it includes all the basic packages of Anaconda. To choose this image, demonstrate the following step, and ask the class to follow along with you as you do so:

* On the Launcher tab, in the “Select a SageMaker image” drop-down list, click Data Science.

  ![“”](Images/15-3-selecting-sagemaker-studio-image.png)

Next, explain that we need to create a Python 3 notebook to begin creating our machine learning model. To create this notebook, demonstrate the following steps, and ask the class to follow along with you as you do so:

1. In the “Notebooks and compute resources” section, click the “Notebook Python 3” button.

    ![“”](Images/15-3-creating-new-notebook.png)

2. Note that a new Jupyter notebook opens in the Untitled.ipynb pane.

    ![“”](Images/15-3-notebook-ui.png)

    Point out that the notebook is running in Studio and resembles a regular Jupyter notebook. The key difference is that all the AWS computer power is available. Explain that it’s remarkable that with just a few selections, we can deploy a notebook in the cloud with several server and network configurations behind it! This is part of the magic and benefits of using cloud services, like those that AWS offers. They automate the technical work so that we can focus on our projects. In minutes, we did what manually deploying a notebook in the cloud would take hours or even days!

3. Try the new notebook in the cloud by printing a “Hello World!” message, as the following animation shows:

    ![An animation depicts printing the message.](Images/15-3-simple-hello-world-in-cloud-notebook.gif)

    In the preceding animation, we type the following code in the first cell:

    ```python
    print("Hello World!")
    ```

    Then, the “Hello World!” message displays.

Point out to the class that we just ran a “Hello World” program in the cloud! Explain that in the next activity, you'll demonstrate how to start creating a machine learning model by loading and preprocessing data. Be sure that all the students have followed you up to this point.

Before moving on, answer any questions that the students might have.

---

### 3. Instructor Do: Load and Preprocess the Data in Amazon SageMaker Studio (15 min)

**Corresponding activity:** [01-Ins_Load_and_Preprocessing_Data](Activities/01-Ins_Load_and_Preprocessing_Data)

**Files:**

* [loading_and_preprocessing_data.ipynb](Activities/01-Ins_Load_and_Preprocessing_Data/Unsolved/loading_and_preprocessing_data.ipynb)

* [german_credit_data.csv](Activities/01-Ins_Load_and_Preprocessing_Data/Resources/german_credit_data.csv)

In this activity, the students will learn how to load and preprocess data by using SageMaker Studio. Specifically, you'll take the students through a refresher on the data loading and preprocessing procedure while highlighting some particulars of using Studio.

Explain to the students that as we did before, we need to load and prepare the data that we want to fit into a machine learning model. So, you’ll demonstrate how to do so.

Mention that for this demo, you’ll use the popular German credit risk dataset and a built-in SageMaker algorithm to deploy a machine learning model in the cloud that predicts credit risk.

Explain that the German credit risk dataset classifies people who are described by a set of attributes as good or bad credit risks. Because of the complex encoding of the original dataset, we’ll use an adapted version of a curated dataset. Slack out the link to [Statlog (German Credit Data) Data Set](https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data)) from the UCI Machine Learning Repository. At that link, the students can learn more about the original dataset.

Explain that before using Studio to run a machine learning model in the cloud, we need to get our data and perform the necessary transformations for fitting the model.

Note that for this demo, you’ll continue using the notebook that you already created in an earlier activity.

#### Upload the CSV File to Amazon SageMaker Studio

Start this demo by uploading the CSV file to SageMaker Studio. To do so, complete the following steps:

1. Delete the “Hello World!” code cell, and then create a new folder named `Resources`. To create a new folder, click the New Folder button, like we do in JupyterLab and as the following image shows:

    ![A screenshot points out the New Folder button.](Images/15-3-new-folder.png)

2. Open the `Resources` folder, click the Upload Files button, and then upload the CSV file that contains the data from the German credit risk dataset, as the following image shows:

    ![A screenshot points out the Upload Files button.](Images/15-3-upload-csv-file.png)

Explain to the class that now that you’ve uploaded the CSV file, you’ll next demonstrate how to preprocess the data.

#### Preprocess the Data

Explain that you’ll continue the demo by following the procedure for creating a machine learning model&mdash;but it will now run in the cloud. To preprocess the data, navigate to the main folder, open the notebook, and then continue with the following subsections:

* Load the Data Into Pandas

* Encode the Categorical Data

* Create the Features and Target Sets

* Create the Training and Testing Sets

* Scale the Features Data

##### Load the Data into Pandas

To load the data into Pandas, demonstrate the following steps:

1. Import the required libraries and modules. To do so, import the standard libraries that we need to load a dataset into Pandas and the scikit-learn modules that we’ll use to preprocess the data, as the following code shows:

    ```python
    import pandas as pd
    from pathlib import Path
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import OneHotEncoder, StandardScaler
    ```

2. Load the data into a Pandas DataFrame, and then display some sample data to understand the information that we’ll use, as the following code shows:

    ```python
    # Load the CSV data into a DataFrame
    file_path = Path("Resources/german_credit_data.csv")
    df = pd.read_csv(file_path)

    # Display sample data
    df.head()
    ```

    The following image shows the sample data in the DataFrame:

    ![A screenshot depicts the DataFrame.](Images/15-3-loading-credit-risk-data-into-pandas.png)

    In the preceding image, notice that the data contains typical customer information along with the customer credit information that the financial institution provided. The columns are “Age”, “Job”, “Housing”, “Saving accounts”, “Checking account”, “Credit amount”, “Duration”, “Purpose”, and “Risk”.

##### Encode the Categorical Data

Remind the students that because some columns contain categorical (that is, non-numerical) data, you need to transform that data into numerical representations before fitting the machine learning model. You’ll transform the data by encoding it.

To encode the categorical data, demonstrate the following steps:

1. Encode the categorical variables by using one-hot encoding. Remember to create an instance of the encoder and then use the `fit_transform` function to encode the data, as the following code shows:

    ```python
    # Create a OneHotEncoder instance
    enc = OneHotEncoder(sparse=False)

    # Create a list of categorical variables
    categorical_variables = ["Housing", "Saving accounts", "Checking account", "Purpose", "Risk"]

    # Encode categorical variables using OneHotEncoder
    encoded_data = enc.fit_transform(df[categorical_variables])

    # Create a DataFrame with the encoded variables
    encoded_df = pd.DataFrame(
        encoded_data,
        columns = enc.get_feature_names(categorical_variables)
    )

    # Display sample data
    encoded_df.head()
    ```

    The following image shows the resulting DataFrame:

    ![A screenshot depicts the encoded DataFrame.](Images/15-3-encoding-categorical-variables.png)

2. Concatenate the numerical columns from the original DataFrame with the encoded DataFrame to have all the numerical columns together, as the following code shows:

    ```python
    # Add the numerical variables from the original DataFrame to the one-hot encoding DataFrame
    encoded_df = pd.concat(
        [
            df[["Age", "Job", "Credit amount", "Duration"]],
            encoded_df
        ],
        axis=1
    )

    # Display sample data
    encoded_df.head()
    ```

    The following image shows the resulting DataFrame:

    ![A screenshot depicts the DataFrame.](Images/15-3-concatenating-numerical-data.png)

##### Create the Features and Target Sets

To create the features (`X`) and target (`y`) sets, demonstrate the following steps:

1. Create the features set by taking all the columns except “Risk_bad” and “Risk_good”, as the following code shows:

    **Note:** Explain to the class that we drop the “Risk_bad” and “Risk_good” columns, because they represent the target variable&mdash;that is, whether to consider the loan candidate a bad or a good risk.

    ```python
    # Creating the features set X
    X = encoded_df.drop(columns=["Risk_bad", "Risk_good"])

    # Display sample data
    X.head()
    ```

    The following image shows the resulting DataFrame:

    ![A screenshot depicts the DataFrame of features data.](Images/15-3-create-features-set.png)

2. Create the target set by taking only the “Risk_bad” column (where a value of 1 means that the candidate is a bad risk for a loan, and a value of 0 means a good risk), as the following code shows:

    ```python
    # Creating the target set y
    y = encoded_df["Risk_bad"]

    # Display sample data
    y.head()
    ```

    The following image shows the resulting DataFrame:

    ![A screenshot depicts the DataFrame.](Images/15-3-create-target-set.png)

##### Create the Training and Testing Sets

Remind the students that to create the training and testing sets, we use the `train_test_split` function from scikit-learn to split the features and target sets into training and testing datasets, as the following code shows:

```python
# Split the preprocessed data into training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
```

##### Scale the Features Data

Explain to the students that for the final data preprocessing task, you need to scale the features data. To do so, you'll use the `StandardScaler` module from scikit-learn, as the following code shows:

**Note:** Remind the students that before fitting a machine learning model, we need to standardise the numerical features values so that they all have a similar scale. In earlier lessons, we used the `StandardScaler` module to accomplish this. Slack out the link to the [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html) page of the scikit-learn documentation, which the students can use for a refresher on how to use this module.

```python
# Create a StandardScaler instance
scaler = StandardScaler()

# Fit the StandardScaler
X_scaler = scaler.fit(X_train)

# Scale the data
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)
```

Explain that we can now fit a machine learning model with our data! All the data preprocessing tasks that you just demonstrated resemble the ones that we did in earlier lessons.

Explain to the students that they’ll next have the opportunity to practice the data preparation process before learning how to deploy a machine learning model in SageMaker Studio.

Before moving on, answer any questions that the students might have.

---

### 4. Student Do: Preventing Money Laundering with Amazon SageMaker - Data Preparation (15 min)

**Corresponding activity:** [02-Stu_Money_Laundering-Data-Prep](Activities/02-Stu_Money_Laundering-Data-Prep)

**Files:**

* [Instructions](Activities/02-Stu_Money_Laundering-Data-Prep/README.md)

* [predicting_money_laundering.ipynb](Activities/02-Stu_Money_Laundering-Data-Prep/Unsolved/predicting_money_laundering.ipynb)

* [money_laundering.csv](Activities/02-Stu_Money_Laundering-Data-Prep/Resources/money_laundering.csv)

In this activity, the students will gain practical experience with using SageMaker Studio to prepare the data for a machine learning application. This application will predict whether a cash or transfer bank transaction is potentially money laundering fraud.

For this activity, we encourage you to have the students work in groups of two or three.

---

### 5. Instructor Do: Review Preventing Money Laundering with Amazon SageMaker - Data Preparation (10 min)

**Files:**

* [Instructions](Activities/02-Stu_Money_Laundering-Data-Prep/README.md)

* [predicting_money_laundering.ipynb (unsolved)](Activities/02-Stu_Money_Laundering-Data-Prep/Unsolved/predicting_money_laundering.ipynb)

* [predicting_money_laundering.ipynb (solved)](Activities/02-Stu_Money_Laundering-Data-Prep/Unsolved/predicting_money_laundering.ipynb)

* [money_laundering.csv](Activities/02-Stu_Money_Laundering-Data-Prep/Resources/money_laundering.csv)

Start this review activity by checking in with the class to find out how comfortable they're feeling with using SageMaker Studio to preprocess data.

If you're teaching an online class by using Zoom, stop sharing your screen for a moment and switch to the [Gallery View](https://support.zoom.us/hc/en-us/articles/201362323-Changing-the-video-layout-Speaker-view-and-Gallery-view-). Check the students' level of understanding by soliciting thumbs up/smiley face Zoom emoji or thumbs down/sad face emoji. If you’re in person, ask the class directly.

Either way, use the feedback from this check to either recommend office hours for reviewing things in more depth or adjust your pace throughout the activity review.

Next, review the solved version of the notebook as follows:

1. Open SageMaker Studio, upload the provided dataset to a folder named `Resources`, and then upload the provided solved notebook to the root folder of SageMaker Studio.

2. Go through the solved notebook, cell by cell, highlighting the following points:

    * In this scenario, the output of the machine learning model prediction is a binary label&mdash;specifically, 0 for a nonfraudulent transaction or 1 for a fraudulent transaction.

    * Despite using a curated dataset, we still need to perform some data preparation tasks. Specifically, we need to hot encode, split, and scale the input features.

    * Because the “typeofaction” column contains categorical data, we use the `OneHotEncoder` module from scikit-learn to transform this column's categories into numerical representations.

    * We start by creating an instance of the `OneHotEncoder` module, as the following code shows:

      ```python
      # Create a OneHotEncoder instance
      enc = OneHotEncoder(sparse=False)
      ```

    * We continue by creating a list of the columns that contains categorical variables, as the following code shows:

      ```python
      # Create a list of the columns with categorical variables
      categorical_variables = ["typeofaction"]
      ```

    * The next step is to use the `fit_transform` function from `OneHotEncoder` to encode the data, as the following code shows:

      ```python
      # Use the fit_transform function from the OneHotEncoder to encode the data
      encoded_data = enc.fit_transform(df[categorical_variables])
      ```

    * Now, we create a DataFrame with the encoded variables, as the following code shows:

      ```python
      # Create a DataFrame with the encoded variables
      encoded_df = pd.DataFrame(
          encoded_data,
          columns = enc.get_feature_names(categorical_variables)
      )

      # Display sample data
      encoded_df.head()
      ```

    * After encoding the data, we create a DataFrame with the encoded variables and drop the “typeofaction” column from the original DataFrame, as the following code shows:

      ```python
      # Drop the 'typeofaction' column from the original DataFrame
      df = df.drop(columns=["typeofaction"])

      # Display sample data
      df.head()
      ```

    * Next, we add a new column, named `operationtype`, to the original DataFrame. In this column, 1 represents a cash operation, and 0 will represent a transfer, as the following code shows:

      ```python
      # Add the encoded 'typeofaction' data to the original DataFrame
      df["operationtype"] = encoded_df["typeofaction_cash-in"]

      # Display sample data
      df.head()
      ```

    * Now that we’ve encoded all the features as numerical values, we’ll create the features (`X`) and target (`y`) sets.

    * The features set will consist of all the columns from the original DataFrame except the `isfraud` column, because that one makes up the target set, as the following code shows:

      ```python
      # Create the features set X
      X = df.drop(columns=["isfraud"])

      # Display sample data
      X.head()

      # Create the target set y
      y = df["isfraud"]

      # Display sample data
      y.head()
      ```

    * Now, we can create the training and testing sets to fit and test the machine learning model. To do so, we use the `train_test_split` function from scikit-learn, as the following code shows:

      ```python
      # Split the preprocessed data into a training and testing dataset
      X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
      ```

    * You might have noticed that despite having only numerical features, the values are at different scales.

    * So as the final step of the data preparation, we use the scikit-learn `StandardScaler` module to scale the features data, as the following code shows:

      ```python
      # Create a StandardScaler instance
      scaler = StandardScaler()

      # Fit the StandardScaler
      X_scaler = scaler.fit(X_train)

      # Scale the data
      X_train_scaled = X_scaler.transform(X_train)
      X_test_scaled = X_scaler.transform(X_test)
      ```

Before moving on, answer any questions that the students might have.

---

### 6. Break (15 min)

---

### 7. Instructor Do: Deploy a Machine Learning Model in Amazon SageMaker Studio (25 min)

**Corresponding activity:** [03-Ins_Deploy_ML_Model_SageMaker](Activities/03-Ins_Deploy_ML_Model_SageMaker)

**Files:**

* [deploy_ml-model-sagemaker.ipynb](Activities/03-Ins_Deploy_ML_Model_SageMaker/Unsolved/deploy_ml-model-sagemaker.ipynb)

* [german_credit_data.csv](Activities/03-Ins_Deploy_ML_Model_SageMaker/Resources/german_credit_data.csv)

In this activity, the students will learn how to create, fit, train, and validate a machine learning model in SageMaker Studio. In this activity, you'll continue to use the German credit dataset.

Open SageMaker Studio, and then load the provided unsolved version of the Jupyter notebook. Note that the first code cells, from Cell 1 to Cell 11, contain the code that you demonstrated in an earlier activity. Specifically, you loaded and preprocessed the German credit dataset. Run those cells now, and then start this demo at Code Cell 12. Note that this starts at the “Importing the Required Libraries” subsection of the "Creating a Machine Learning Model in SageMaker Studio" section in the Jupyter notebook.

![“”](Images/15-3-create-ml-model-demo-start.png)

#### Import the Required Modules and Libraries

Explain to the students that in this demo, you’ll demonstrate how to train and deploy a binary classification model that uses the German credit risk dataset and that predicts whether a loan will default. Further explain that Amazon has created an extensive library of machine learning models that are optimized for the cloud. And to begin the demo, you’ll import the required modules and libraries.

Point out the code of each cell, and highlight the following:

* In earlier modules, we followed the model-fit-predict pattern when creating a machine learning model. With SageMaker, the pattern differs because of particular tasks that we need to perform. We’ll start by importing the required Python libraries.

* To use SageMaker to run a model in the cloud, we need to import some SageMaker modules, as the following code shows:

  ```python
  import sagemaker
  import sagemaker.amazon.common as smac
  from sagemaker import get_execution_role
  from sagemaker.predictor import csv_serializer, json_deserializer
  ```

  * We’ll go into more detail about the preceding modules as we use them.

* We also need to import the Boto3 library and several support libraries, as the following code shows:

  ```python
  # Import AWS Python SDK
  import boto3

  # Import support libraries
  import io
  import os
  import json
  import numpy as np
  ```

* The [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) library is the AWS software development kit (SDK) for Python.

  **Note:** Feel free to slack out the link to the [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) so that the students can have it for future reference.

* After importing all the required modules and libraries, we can get started with SageMaker. We’ll start with the initial configurations that creating a model requires.

#### Configure the General Settings for the Amazon SageMaker Model

To configure the general settings for the SageMaker model, point out the code of each cell, and highlight the following:

* Unlike the machine learning models that we created with scikit-learn, a SageMaker model requires that we store our preprocessed training and testing data in an Amazon S3 bucket. The SageMaker model can then use the data.

* We’ll use the S3 bucket that we created when using the [AWS Account Setup Guide](../Supplemental/AWS-Account-Setup.md) for this module. To store the name of the bucket, we create a variable named `bucket`, as the following code shows:

  ```python
  bucket = "fintech-bootcamp-activities-jams-2021-02-11"
  ```

* We can store several files in an S3 bucket. To identify the data files that we’ll store in the bucket for this model, we set a prefix for these files, which we store in the `prefix` variable, as the following code shows:

  ```python
  prefix = "credit-risk"
  ```

* To run our model in the cloud, we also need the name of the IAM execution role that we defined when we created the Studio instance. We create a variable named `role` to store this role, as the following code shows:

  ```python
  role = get_execution_role()
  ```

#### Upload the Training and Testing Data to Amazon S3

Explain to the students that before creating our model, we need to upload our training and testing data to Amazon S3. To train the machine learning model by using SageMaker, we first need to format our preprocessed training and testing data in the [protobuf recordIO format](https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-training.html#td-serialization) and then upload it into our Amazon S3 bucket.

Explain that overall, the data in the protobuf recordIO format is the result of transforming structured data (similar to JSON data) into a format that allows applications to communicate with each other or to store data.

Point out that with the protobuf recordIO format, we can use Pipe mode when training algorithms that support it. Slack out the link to [Accelerate model training using faster Pipe mode on Amazon SageMaker](https://aws.amazon.com/blogs/machine-learning/accelerate-model-training-using-faster-pipe-mode-on-amazon-sagemaker/) from the AWS Machine Learning Blog, which the students can read to learn more about Pipe mode in SageMaker.

Explain that for the purpose of training a machine learning model in SageMaker Studio, we’ll use the following code as boilerplate to first format our training and testing data into protobuf recordIO format and then upload it into the Amazon S3 bucket:

```python
# Encode the training data as Protocol Buffer
buf = io.BytesIO()
vectors = np.array(X_train_scaled).astype("float32")
labels = np.array(y_train).astype("float32")
smac.write_numpy_to_dense_tensor(buf, vectors, labels)
buf.seek(0)

# Upload encoded training data to Amazon S3
key = 'linear_train.data'
boto3.resource("s3").Bucket(bucket).Object(os.path.join(prefix, "train", key)).upload_fileobj(buf)
s3_train_data = "s3://{}/{}/train/{}".format(bucket, prefix, key)
print("Training data uploaded to: {}".format(s3_train_data))

# Encode the testing data as Protocol Buffer
buf = io.BytesIO()
vectors = np.array(X_test_scaled).astype("float32")
labels = np.array(y_test).astype("float32")
smac.write_numpy_to_dense_tensor(buf, vectors, labels)
buf.seek(0)

# Upload encoded testing data to Amazon S3
key = "linear_test.data"
boto3.resource("s3").Bucket(bucket).Object(os.path.join(prefix, "test", key)).upload_fileobj(buf)
s3_test_data = "s3://{}/{}/test/{}".format(bucket, prefix, key)
print("Testing data uploaded to: {}".format(s3_test_data))
```

#### Choose the Machine Learning Model

Explain that now, we’ll choose the machine learning model that we want to use. Point out that SageMaker offers various built-in algorithms for supervised, unsupervised, and reinforcement learning. Remind them that as they learned in earlier modules, we choose the algorithm based on the outcome that we want to predict.

Explain that in this demo, we want to predict a binary outcome: a value of 1 if the credit applicant is a bad risk, and a value of 0 if a good risk. To do so, we’ll use the SageMaker linear learner algorithm to run a binary classification model.

We encourage you to slack out the link to the [Linear Learner Algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/linear-learner.html) documentation, which the students can read for detailed information about this algorithm.

Remind the students that we use classification algorithms to predict discrete outcomes. For example, say that we want to use a person's traits, such as age, income, and geographic location, to predict whether that person will vote Yes or No on an issue. The outcome is finite, with two possibilities in this case. The classification model will try to learn patterns from the data and, if successful, gain the ability to make accurate predictions for new voters.

#### Specify the Amazon SageMaker Session to Use

Explain to the class that before creating our machine learning model, we need to tell SageMaker which session we want to use to create and run the model. A session is tied to the AWS user or IAM user that launched Studio. We used our administrator IAM user, and because we have administrative rights, we already have all the necessary permissions for creating and running a model by using Studio.

Mention that usually, we use the current session to proceed. And, the following code stores the current session in a variable named `sess`:

```python
sess = sagemaker.Session()
```

#### Create an Instance of the Machine Learning Model

Now, we’re ready to create our machine learning model! Explain to the class that as we did with scikit-learn, we first need to create an instance of the machine learning model. But in SageMaker, a model is more than a Python library.

Explain to the students that a machine learning model in SageMaker runs in the cloud in a container. A **container** is an [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/) instance&mdash;a virtual machine in the cloud&mdash;that stores and runs the model.

Explain that Amazon EC2 instances are virtual machines that we can configure and run in the cloud by using the AWS infrastructure. Each time that we create a machine learning model, SageMaker automatically provisions an EC2 instance to deploy and run that model. Several instance types are available. For detailed information about them, refer to [Available SageMaker Studio Instance Types](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-available-instance-types.html) in the Amazon SageMaker Developer Guide. Feel free to also slack out the link to this page.

Explain that the AWS infrastructure stores containers as reusable packages, called **container images**, that anyone can use to create their own containers. The first step toward creating a machine learning model is to import the container image. To do so, we import the `get_image_uri` module from the SageMaker library to create an instance of the linear learner container, as the following code shows:

```python
# Import the get_image_uri module from the sagemaker library
from sagemaker.amazon.amazon_estimator import get_image_uri

# Import the container image
container = get_image_uri(boto3.Session().region_name, "linear-learner")
```

We now have a new container image, stored in the `container` variable, for running our machine learning model.

**Note:** In August 2020, AWS released version 2 of the SageMaker Python SDK. Because version 2 was still under development at the time of this writing, the code in this lesson uses version 1.x. You might get warnings about version 2 renaming some functions, but don’t worry. The model will run and work perfectly.

Explain that we use the `sagemaker.estimator.Estimator` function to create an instance of the machine learning model, as the following code shows:

```python
linear_learner = sagemaker.estimator.Estimator(
  container,
  role,
  train_instance_count=1,
  train_instance_type="ml.m4.xlarge",
  output_path="s3://{}/{}/output".format(bucket, prefix),
  sagemaker_session=sess
  )
```

Explain that because the model will run on a virtual machine that Amazon EC2 supplies, the preceding code sets several parameters, such as the type of EC2 infrastructure that we want to use. In this demo, we’ll use an `ml.m4.xlarge` EC2 instance for training the model.

#### Define the Linear Learner Hyperparameters

Explain to the students that now that we’ve created an instance of our model, we need to define some parameters before fitting the model. Specifically, we’ll define the linear learner hyperparameters. Explain that **hyperparameters** are configurations that define how a machine learning model will work during the training process. For example, we can define how many features to use, the number of training examples to use in one iteration, and the type of prediction that we want to make.

Explain that in SageMaker Studio, it’s important to define the `features_dim` hyperparameter so that it matches the number of predictors in the features (`X`) set. To do so, we use the Pandas `shape` function to get the number of columns in the `X` set that corresponds to the number of predictors, as the following code shows:

```python
# Get the dimension of the feature-input set
feature_dim = X.shape[1]
```

Explain that after getting the number of predictors, we define the other linear learner hyperparameters. Note that in this case, we use `predictor_type="binary_classifier"` to allow the model to make binary classifications for credit risk (1 for bad or 0 for good), as the following code shows:

```python
# Define linear learner hyperparameters
linear_learner.set_hyperparameters(
    feature_dim=feature_dim,
    mini_batch_size=200,
    predictor_type="binary_classifier"
)
```

Have a short pause. Mention that we had a long journey to create a machine learning model by using SageMaker. But, it was worth it, because we now have access to a model that can run in the cloud with the ability to use the computing power of AWS!

#### Fit the Machine Learning Model in Amazon SageMaker Studio

Now, you’ll demonstrate how to fit the model by using SageMaker.

Explain to the students that as you demonstrated, creating a machine learning model in SageMaker differed quite a bit from the process that we followed when using scikit-learn or TensorFlow. But, fitting a model corresponds quite a bit, as they’ll learn in this section.

Explain that to fit our model, we use the `fit` function and pass the training and testing data as parameters. Recall that we uploaded the training and testing data to our Amazon S3 bucket. So, we pass the locations of these datasets in the bucket&mdash;and not the preprocessed training and testing data that we stored in Pandas, as parameters, as the following code shows:

```python
# Fitting the linear learner model
linear_learner.fit({"train": s3_train_data, "test": s3_test_data})
```

**Important:** The preceding code can take up to 15 minutes to run and uses resources from the AWS account. Typically, this time doesn’t get billed during the two-month trial period. But, the policies of the AWS free tier regularly change. So, explain to the students that they should always check the pricing pages for any service that they want to use.

The following animation shows what happens when we run this code in Studio:

![An animation depicts running the code in Studio.](Images/15-3-model-fitting.gif)

In the preceding animation, extensive output appears in blue text. It’s extensive because it includes all the operations that occur during the training process. Then, we scroll down to review the test results that the code returns after fitting the model.

#### Deploy the Model

Explain to the class that following the pattern we used with scikit-learn, after fitting the model, we can deploy it to make predictions. Again, this process differs, because we need to deploy the model to an Amazon EC2 instance to run it. Highlight the following points:

* To have the model make predictions, we need to deploy it in a different instance than the one that we used for training.

* In this demo, we’ll define `ml.t2.medium` as the instance type, because this instance type is part of the free tier. The following code shows how to deploy the model:

  ```python
  # Deploy an instance of the linear learner model to create a predictor
  linear_predictor = linear_learner.deploy(initial_instance_count=1, instance_type="ml.t2.medium")
  ```

  Notice that the preceding code consists of just one line. But, that line triggers several tasks, which include deploying a new Amazon EC2 instance. Be aware that deploying the model might take a few minutes because of all the tasks that need to run.

#### Configure the Predictor

Explain that before making predictions, we need to configure two items. Specifically, we need to indicate the type of the data files that we’ll use and define how the model will treat the data.

Explain that in this case, we’ll send the data as CSV files and retrieve JSON files in response. The following code shows these configurations:

```python
# Linear predictor configurations
linear_predictor.serializer = csv_serializer
linear_predictor.deserializer = json_deserializer
```

#### Make Predictions by Using the Testing Data

Finally, we can make predictions! Explain to the class that we do this in a way that resembles using scikit-learn. To make predictions, we use the `predict` function of the model.

Continue the demo, and highlight the following:

* We make predictions by using the preprocessed testing data that we stored in the `X_test_scaled` Python variable. We retrieve and store the prediction results in the `model_predictions` variable, as the following code shows:

  ```python
  # Making some predictions using the test data
  model_predictions = linear_predictor.predict(X_test_scaled)
  ```

* The predictions that the model makes are returned in a JSON file. This file is parsed into a Python dictionary, which is stored in the `model_predictions` variable. The `predictions` dictionary key contains all the predictions. The following code displays some of this prediction data:

  ```python
  # Display sample predictions
  model_predictions["predictions"][:3]
  ```

  Running the preceding code produces the following output:

  ```text
  [{'score': 0.3425270617008209, 'predicted_label': 0},
  {'score': 0.20269660651683807, 'predicted_label': 0”,
  {'score': 0.006089568138122559, 'predicted_label': 0”]
  ```

  ![“”](Images/15-3-model-predictions-sample.png)

* Note that we just got three sample predictions. They were returned as a Python list of dictionaries, where each dictionary entry has two keys. The `score` key contains the accuracy metric value for the prediction. The `predicted_label` key contains the value of the label that the model predicted.

* We now want to create an array of the predictions so that we can evaluate the model later. To do so, we extract each predicted value from the dictionary to create a Python list, which we then transform into an array. The following code shows this process, storing the prediction results in the `y_predictions` array:

  ```python
  # Creating a list with the predicted values
  y_predictions = [np.uint8(value["predicted_label"]) for value in model_predictions["predictions"]]

  # Transforming the list into an array
  y_predictions = np.array(y_predictions)

  # Display sample data
  y_predictions[:10]
  ```

  Running the preceding code produces the following output:

  ```text
  array([0, 0, 0, 0, 0, 1, 1, 0, 0, 0], dtype = uint8)
  ```

  ![“”](Images/15-3-making-credit-risk-predictions.png)

* Because we created a list of the predicted labels, we just got a Python list, named `y_predictions`, that contains only the predicted labels.

#### Evaluate the Machine Learning Model in Amazon SageMaker Studio

It’s now time to evaluate the model. Explain to the class that to do so, that we can use the scikit-learn metrics module, as we did before.

Continue the demo, and highlight the following:

* To evaluate the predictions by using the preprocessed testing data that we stored in `y_test`, we import the `classification_report` module and then display the classification report, as the following code shows:

  ```python
  # Import the classification report from scikit-learn
  from sklearn.metrics import classification_report

  # Display classification report
  print("Classification report")
  print(classification_report(y_test, y_predictions))
  ```

  Running the preceding code produces the following output:

  ![“”](Images/15-3-classification-report.png)

* Note that the accuracy of this model is about 50%. We can thus use this model as a prototype, but we might want to benchmark different models before putting one into production.

Explain to the students that up till now, they learned how to deploy a machine learning model in the cloud by using SageMaker. But in a typical business scenario, like predicting credit risk, they might want to create a prototype model locally on their computer before running the model in the cloud. Although they can use SageMaker Studio to create a prototype, using it to run early-stage prototypes can become costly.

Point out that in this demo, we used only one of the built-in SageMaker algorithms. The advantage of these algorithms is twofold: they’re optimised for working with high volumes of data, and they take advantage of the computing power of AWS.

Slack out the link to the [Use Amazon SageMaker Built-in Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html) page of the Amazon SageMaker Developer Guide. The students can read this page to learn more about these algorithms.

#### Delete the Amazon SageMaker Endpoint

Explain to the class that each time we use SageMaker to deploy a machine learning model, AWS creates an endpoint for communicating with other services. This endpoint gets billed to our AWS account if we exceed the quota of the free tier.

Further explain that when we finish with our model, we should avoid unnecessary charges by deleting the endpoint. To do so, we run the following code at the end of our notebook:

```python
# Delete Amazon SageMaker endpoint
sagemaker.Session().delete_endpoint(linear_predictor.endpoint)
```

Tell the students that next, they’ll have the opportunity to put these new skills into action.

Before moving on, answer any questions that the students might have.

---

### 8. Student Do: Preventing Money Laundering with Amazon SageMaker - Model Deployment (25 min)

**Corresponding activity:** [04-Stu_Money_Laundering-Model-Deploy](Activities/04-Stu_Money_Laundering-Model-Deploy)

**Files:**

* [Instructions](Activities/04-Stu_Money_Laundering-Model-Deploy/README.md)

* [predicting_money_laundering.ipynb](Activities/04-Stu_Money_Laundering-Model-Deploy/Unsolved/predicting_money_laundering.ipynb)

* [money_laundering.csv](Activities/04-Stu_Money_Laundering-Model-Deploy/Resources/money_laundering.csv)

In this activity, the students will use the data that they prepared in an earlier activity. Specifically, they’ll use it to train a machine learning model to predict whether a cash or transfer bank transaction is potentially money laundering fraud. The machine learning model will be in the cloud, and they'll use the SageMaker linear learner algorithm.

For this activity, we encourage you to have the students continue working in groups of two or three.

---

### 9. Instructor Do: Review Preventing Money Laundering with Amazon SageMaker - Model Deployment (10 min)

**Files:**

* [Instructions](Activities/04-Stu_Money_Laundering-Model-Deploy/README.md)

* [predicting_money_laundering.ipynb (unsolved)](Activities/04-Stu_Money_Laundering-Model-Deploy/Unsolved/predicting_money_laundering.ipynb)

* [predicting_money_laundering.ipynb (solved)](Activities/04-Stu_Money_Laundering-Model-Deploy/Solved/predicting_money_laundering.ipynb)

* [money_laundering.csv](Activities/04-Stu_Money_Laundering-Model-Deploy/Resources/money_laundering.csv)

Start this review activity by checking in with the class to find out how comfortable they're feeling with using SageMaker Studio to deploy a machine learning model.

If you're teaching an online class by using Zoom, stop sharing your screen for a moment and switch to the [Gallery View](https://support.zoom.us/hc/en-us/articles/201362323-Changing-the-video-layout-Speaker-view-and-Gallery-view-). Ask the students to rate their level of understanding by raising their hands for a "Fist-to-Five" check.

Use the feedback from this check to either recommend office hours for reviewing things in more depth or adjust your pace throughout the activity review.

Next, go through the solved version of the notebook, cell by cell, and highlight the following points:

* Recall that the output of the model prediction is a binary label&mdash;specifically, 0 for a nonfraudulent transaction or 1 for a fraudulent transaction.

* Despite using a curated dataset, we still need to perform some data preparation tasks. Specifically, we need to hot encode, split, and scale the input features.

* We use the linear learner algorithm that’s built in to SageMaker by setting the `predictor_type` hyperparameter to "binary_classifier".

* The predictions exist in the `predictions` list in the prediction result.

* For our model evaluation, we use the classification report to get an overall sense of the model's prediction combinations of true positives with negatives and false positives with negatives.

Before moving on, answer any questions that the students might have.

---

### 10. Everyone Do: Deleting AWS Resources (20 min)

**File:**

* [AWS Account Setup Guide](../Supplemental/AWS-Account-Setup.md)

In this activity, you’ll lead the students on deleting the AWS resources that they created to avoid additional costs.

Explain to the students that even if we set usage alerts, it’s possible to incur additional costs while using AWS. For example, we might accidentally incur a cost by leaving a SageMaker instance running for several days.

Mention that next, you’ll demonstrate how to avoid additional costs by stopping and deleting AWS resources.

#### Stop the Amazon SageMaker Studio Instances

First, you’ll stop the SageMaker Studio instances. Begin by highlighting the following points to the students:

* As we learned today, SageMaker Studio is a service that AWS provides and that allows us to run Jupyter notebooks in the cloud to build and run machine learning models.

* The user interface resembles that of JupyterLab. So, the process of stopping a running instance might seem familiar.

* When you finish working in SageMaker Studio, you must stop all the running instances. If you don’t, AWS will charge your credit card.

To stop an instance, demonstrate the following steps, and ask the class to follow along with you as you do so:

1. On the navigation bar on the left side, click the “Running Terminal and Kernels” button.

    ![“”](Images/15-3-open-running-instances.png)

2. Note that a list of all the running resources appears. To stop all the running resources, you only need to shut down the running instances. To do so, in the Running Instances section, click the “Shut down” button.

    ![](Images/15-3-shut-down-instance.png)

3. Note that a warning message displays, asking “Shut down all processes running on ml.t3.medium?” Click the “Shut down all” button.

    ![“”](Images/15-3-shut-down-warning.png)

4. Wait a few seconds for the system to shut down all the running resources. Check the display to ensure that all the resources have stopped running. When they have, the Running Instances, Running Apps, Kernel Sessions, and Terminal Sessions sections will all be empty.

    ![“”](Images/15-3-resources-stopped.png)

Explain to the class that if they haven’t exceeded the limits of the free tier, shutting down all the running instances will prevent them from being billed for additional SageMaker instance usage.

#### Manually Delete the Amazon SageMaker Endpoints

Now, you’ll manually delete the SageMaker endpoints. Begin by highlighting the following points to the students:

* Each time that you build a model in SageMaker, an endpoint gets created.

* We already learned how to delete endpoint instances by using Python code. But each time that you finish a working session in SageMaker, you’re encouraged to check that you’ve successfully deleted all the endpoints.

* If you leave any endpoints running beyond the minutes that the free tier offers, AWS will charge your credit card.

To ensure that you don’t leave any endpoints running, demonstrate the following steps, and ask the class to follow along with you as you do so:

1. In the SageMaker console, in the Amazon SageMaker Studio navigation pane on the left side, click Endpoints

    ![“”](Images/15-3-open-endpoints.png)

2. In the Endpoints pane that appears on the right side, if a message states, “There are currently no resources,” and no endpoints are listed, move on to the next section. No endpoints are running for you to delete.

    ![“”](Images/15-3-no-endpoints.png)

3. If running endpoints are listed, select an endpoint that you want to delete.

    ![“”](Images/15-3-active-endpoints.png)

4. On the Actions drop-down menu, click Delete.

    ![“”](Images/15-3-actions-delete.png)

5. Note that a warning message displays, which states, “This will permanently delete your endpoint and cannot be undone. This may affect other resources.” Click the Delete button.

    ![“”](Images/15-3-confirm-delete.png)

6. Note that in the Endpoints pane, the status of the endpoint changes to Deleting.

    ![“”](Images/15-3-deleting-endpoint.png)

7. Wait a few minutes for the endpoint to be deleted. When it is, it won’t appear in the list of endpoints anymore.

8. If you have more endpoints running, repeat Steps 3&ndash;7 for each one.

#### Delete the Amazon S3 Buckets

To avoid incurring additional costs for using cloud storage space in Amazon S3, demonstrate the following steps to delete any bucket that you’ve created, and ask the class to follow along with you as you do so:

1. Open the Amazon S3 console.

    **Note:** Before deleting a bucket, you must delete any file or resource that it stores.

2. In the Buckets pane on the right side, select the bucket that you want to delete, and then click the Delete button.

    ![“”](Images/15-3-choose-bucket.png)

3. Note that the “Delete bucket” page appears. In the “To confirm deletion, type the name of the bucket” box, type the name of the bucket, and then click the “Delete bucket” button.

    ![“”](Images/15-3-delete-bucket.png)

4. Note that back in the Buckets pane, the deleted bucket no longer appears in the list. Repeat Steps 2&ndash;3for each remaining bucket. When all the buckets are deleted, the list in the Buckets pane is empty and states, “No buckets” and “You don’t have any buckets.”

    ![“”](Images/15-3-empty-bucket-list.png)

Explain to the students that they can review all the preceding steps in the [AWS Account Setup Guide](../Supplemental/AWS-Account-Setup.md), which they can find in the `Supplemental` folder.

Before moving on, answer any questions that the students might have.

---

### 11. Instructor Do: Recap (5 min)

In this activity, you’ll do a final recap with the class. Use the lesson slides to summarise what the students learned in today's class:

* In today's class, you learned how to create, fit, and deploy a machine learning model in the cloud by using Amazon SageMaker. This AWS service offers an extensive library of machine learning models that are optimised for the cloud and that we can use with Python. Specifically, you can now do the following:

  * Set up Amazon SageMaker Studio on your own
  * Create and run a Jupyter notebook within Amazon SageMaker Studio
  * Load, preprocess, build, and then deploy a machine learning model within Sagemaker Studio

Before ending the class, congratulate the students on reaching the last class of the machine learning section! In today's class, they were able to combine their Python skills with the power of the cloud to deploy a machine learning model.

Explain to the students that although this week’s Challenge doesn’t require SageMaker, it remains a valuable skill in the fintech job market. This is especially true for companies seeking to automate their machine learning pipelines.

Explain that SageMaker is a service that they can connect to other AWS services to build end-to-end machine learning applications. Start sharing your screen, open your browser, and then navigate to the [Amazon SageMaker customers](https://aws.amazon.com/sagemaker/customers/) page. Then go through the various industrial applications that are using SageMaker.

Before ending the class, answer any questions that the students might have.

### End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
