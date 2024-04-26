## 10.1: Introduction to Machine Learning

### Overview

Today’s lesson will begin with an introduction to machine learning (ML). For many students, this will be their first exposure to the topic. Regarding code, one difference between what the students have written up to this point and what they'll write going forward is that machine learning code tends to be more "flexible." Rather than directly coding decision logic, machine learning models are designed to learn logic from the data, and then make decisions and predictions whenever new data is encountered.

In the field of machine learning, one type of "learned logic" is called unsupervised learning. In unsupervised learning the goal is often to let the ML help us figure out what the groups, patterns, and structures are for our data. It is able to accomplish this without us having to tell it what those patterns are—it learns from the data we provide, essentially figuring it out by itself. In this lesson, the students will learn how to use an unsupervised learning algorithm called k-means to help us cluster our data into groups.

### Class Objectives

By the end of this lesson, the students will be able to:

* Recognize the differences between supervised and unsupervised machine learning.

* Define clustering and how it is used in finance.

* Apply the k-means algorithm to identify clusters in a given dataset.

* Determine the optimal number of clusters for a dataset using the elbow method.

---

### Instructor Notes

* Send the students the [Installation Guide](../Supplemental/sklearn-hvplot-install-guide.md) to ensure they have set up the tools they’ll need for this unit.

* Welcome to the first day of machine learning! You will guide the students through a series of increasingly complex activities, which will serve as the foundation for the next class, as well as the homework. The class should feel like an evenly paced introduction to machine learning that provides a challenge and engages the students with relatable use cases.

* Today's class will introduce the students to fundamental unsupervised learning concepts, including the definitions of machine learning, supervised learning, and unsupervised learning; the technical and financial problems machine learning solves; and how to build unsupervised learning models in Python. The students' familiarity with unsupervised learning will likely vary, so be prepared to answer a variety of questions ranging from basic to complex.

* For one of the activities, you’ll be using a demo made by using the [Teachable Machine project from Google](https://teachablemachine.withgoogle.com/v1/) to show the students how machine learning works and to build excitement about the machine learning curriculum. Be sure to practice the demo before class. If you are not familiar with this project, we encourage you to [watch this video](https://youtu.be/3BhkeY974Rg).

* Whenever possible, include real-world examples in your lectures to make concepts more concrete and relatable for students. Feel free to draw upon your own experience using unsupervised learning in the professional world.

* As you review the activities, find ways to connect the ML concepts to fintech. Include brief discussions about emerging or disruptive/innovative technologies, and how they have changed the fintech landscape.

* Activities that involve programming solutions will have an associated coding file linked at the beginning of the activity section. Click the link to go to the coding file required for the activity.

* Have your TAs keep track of the time with the [Time Tracker](TimeTracker.xlsx).

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 10.1 Slides](https://docs.google.com/presentation/d/1Esbmon0G-stHCE1VgA6MUTORqs-cS0YOeXSpxCGD03M/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The Time Tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Introduction to Machine Learning in Finance (15 minutes)

In this section, you’ll discuss the benefits of knowing how to apply machine learning when working in the field of financial technology. Cover the following talking points:

* Machine learning is a type of artificial intelligence that uses algorithms and statistical models to make decisions or predictions about data.

* Today, machine learning is changing the financial world faster than ever before. These changes are being driven by automation power which enables decisions to be made more quickly and efficiently than ever.

* Explain to the students that in this week’s Challenge assignment, they will create a machine learning model that groups cryptocurrencies to assemble investment portfolios that are based on the profitability of those cryptocurrencies.

#### The Mysticism of Machine Learning

Slack out the link (Source: [Twilio blog](https://www.twilio.com/blog/ultimate-guide-openai-gpt-3-language-model)) while explaining the following:

* Despite the mainstream use of the term “machine learning,” most people still don't know what machine learning really is. **Machine learning** is the practice of applying computer algorithms and statistics to create models that can learn from data and then make decisions or predictions about future data.

* Machine learning algorithms learn how to make decisions without needing anyone to program all that logic. They learn the patterns, behaviour, and logic on their own directly from the data and then use that knowledge to make decisions and predictions.

* Here’s an example of how machine learning can be useful:

  * Imagine that you work as a fraud analyst in a bank and want to identify fraudulent transactions. One option is to create a 5,000-line if-else decision structure that evaluates every price range and product category to determine if a transaction counts as fraudulent. Or, you can use machine learning algorithms to review all the transactions that an account owner has ever made. Then, you can group the transactions and predict whether the most recent transaction counts as fraudulent.

  * This is the kind of machine learning solution that you’ll learn to build!

#### Machine Learning in Fintech

For the following talking points, refer to the “Why Is Machine Learning Essential for Fintech?” slides.

* Applications for machine learning range widely. They run the gamut from the textual analysis of fraudulent contracts to determining interest rates.

* Machine learning applications have streamlined many operational processes that are associated with finance.

* For example, machine learning models can detect instances of credit card fraud more quickly and with greater accuracy than previously experienced. Besides increasing operational efficiencies, incorporating machine learning into the finance industry has helped increase its responsiveness to customer demands. This plays a key role in attracting and retaining business.

* As AI gets smarter and machine learning models become more entrenched in the finance industry, understanding how they work will become a necessary skill for all employees in fintech. And you'll have a head start!

#### ML Application: Financial Advising

While covering the next few talking points, refer to the slides for “Machine Learning in Financial Advising.”

* One intriguing use of machine learning is replacing the traditional financial advisor with artificial intelligence (AI). For example, fintech companies that automate saving for retirement include Wealthfront, Betterment, and SoFi.

Slack out the following links. Explain to the students that they can explore these company websites to learn more about fintech companies in the financial advising sector:

* [Wealthfront](https://www.wealthfront.com/methodology)

* [Betterment](https://www.betterment.com/category/engineering/)

* [SoFi](https://www.sofi.com/learn/content/what-is-an-automated-advisor/)

Explain that using machine learning to recommend tailored portfolios and manage the whole process of financial advising means that customers no longer have to pay high annual fees to traditional advisors.

* The automation to reduce costs isn’t isolated to fintech products oriented toward end users, like individuals saving for retirement.

* J.P. Morgan, for example, has developed a program named COIN. It uses natural language processing (NLP) to automatically run due diligence on its commercial-credit contract agreements. These lines of code compress the 360,000 hours of work that humans previously did into seconds. (Source: [Harvard Business School Digital Initiative](https://digital.hbs.edu/platform-rctom/submission/jp-morgan-coin-a-banks-side-project-spells-disruption-for-the-legal-industry/))

#### ML Application: Forecasting Market Results

While covering the next few talking points, refer to the slides for “Machine Learning in Forecasting Market Results”:

* Machine learning models are used to forecast financial-market results. These forecasts range from loan evaluation (for example, predicting the default rates on bonds or consumer loans) to high-frequency algorithmic trading in the stock market.

* Algorithmic trading driven by statistical models has been around since the late 1990s.

* An example is the quant hedge fund Two Sigma Securities which automatically trades more than 300 million shares a day. (This equals about one share per day for every person in the United States.)

* The fund has been in business since the early 2000s. Within the last five years, however, algorithmic trading has come to account for 75% to 80% of all equity trades in the United States.

Slack out the source article containing this data: [Seeking Alpha](https://seekingalpha.com/article/4230982-algo-trading-dominates-80-of-stock-market)).

* Algorithmic trading requires many kinds of decisions, all of which are made by using machine learning models. More cryptocurrency exchanges and trading firms are seeking individuals who can write machine learning code that trades profitably.

#### Additional ML Applications in Fintech

Refer to the slides as you discuss the next few talking points describing machine learning uses for other applications.

* The use of machine learning in fintech is vast. These include identifying money laundering and legal violations; recognising satellites for the real-time awareness of trading opportunities in commodities; and predicting customer churn in financial products.

* Even the venture capital and private equity industries have begun to experiment with machine learning models to predict the likelihood of start-up success.

  * An aspect of machine learning called natural language processing (NLP) is helping to redefine the investment process. NLP models are used to pore over social media, news feeds, and annual report documents in search of specific words or phrases that tip off investors to the potential future direction of a company's stock price, allowing them to establish a trading position ahead of the market move.

Slack out the following links and provide a summary of each:

* This [article from McKinsey Quarterly](https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/a-machine-learning-approach-to-venture-capital) shows how the venture capital industry is using machine learning.

* This [article from the Wharton School](https://knowledge.wharton.upenn.edu/article/data-analytics-slowly-transforming-private-equity/) provides some insight on how machine learning is disrupting the private equity industry.

#### Types of ML

Ask the students for some examples of machine learning models that they have heard of before.  If no one volunteers, provide some examples of your own, such as regression, clustering, neural networks, and deep learning. Explain that we can group all of these models into two main buckets:

* **Supervised learning**: The algorithm learns on a labelled dataset, where each example in the dataset is tagged with the answer. This provides an answer key that can be used to evaluate accuracy of the training data.

* **Unsupervised learning**: The algorithm tries to make sense of an unlabeled dataset by extracting features and patterns on its own.

* In addition to supervised and unsupervised learning, there is a third category of machine learning algorithm that is used less frequently, but still has important applications in finance. This is called reinforcement learning. In this type of machine learning, the algorithm attempts to find the optimal way to accomplish a goal or complete a task. As the algorithm improves in achieving that goal, it receives a reward.

Explain that the lessons in this unit will explore each of these three categories. The following image shows how the different models typically apply to different financial applications:

![A diagram depicts the three main models, with each having further classifications of financial applications.](Images/10-1-ml-overview-diagram.png)

As the image shows, the three main models of machine learning and how they generally apply to financial application are as follows:

* **Supervised learning**—This model has the following categories:

  * **Classification**: This category generally applies to the following financial applications:

    * Fraud detection

    * Image classification

    * Customer retention

    * Credit approval

  * **Regression**: This category generally applies to the following financial applications:

    * Fraud detection

    * Trend identification

    * Time series forecasting

* **Unsupervised learning**: This model has the following categories:

  * **Dimensionality reduction**: This category generally applies to the following financial applications:

    * Feature discernment

    * Structure discovery

    * Big data visualisation

  * **Clustering**: This category generally applies to the following financial applications:

    * Recommended systems

    * Targeted marketing

    * Customer segmentation

* **Reinforcement learning**: This category generally applies to the following financial applications:

  * Real-time decisions

  * Venture funding

  * Learning tasks

  * Skill acquisition

  * Algorithmic trading

* The majority of Python libraries for machine learning use a common interface to build and use machine learning models.

* In later lessons, the students will discover how to create and use machine learning models in different applications. In fact, over the next several lessons and units, they will learn how to apply machine learning to all the applications that we just listed.

Answer any questions before moving on.

---

### 2. Instructor Do: Machine Learning Is Awesome (10 minutes)

This section uses a demo made by the [Teachable Machine project from Google](https://teachablemachine.withgoogle.com/v1/) to show the students how machine learning works and to build excitement about the machine learning curriculum.

Highlight an up-and-coming area of machine learning called **neural networks** in the following demonstration:

* Open your web browser and navigate to [the Teachable Machine website](https://teachablemachine.withgoogle.com/v1/). This web application shows the fundamental mechanism of a neural network by training a model that recognises gestures from your webcam to predict one of three classes.

Once you open the Teachable Machine website, follow the next steps to conduct the demo.

* Click the “skip the tutorial” option to start the demo.

![A screenshot shows the website and the option to start the demo.](Images/intro_nns_1.png)

* Allow the web application to use your webcam and microphone.

![A screenshot shows the website and the option to allow webcam and microphone access.](Images/intro_nns_2.png)

Explain to the students that now you are going to train the neural network model by doing the following:

* Raise your left hand and press the TRAIN GREEN button for a few seconds. Your current image is the input data for the neural network. It's learning that these visual patterns correspond to a cute kitten.

![An animation of the “train green” button being clicked, resulting in a video of a kitten in the output box.](Images/intro_nns_3.gif)

* Continue to train the purple class by posing seriously for the camera. Press the TRAIN PURPLE button for a few seconds. Now the neural network is learning that your poker face corresponds to a furry dog.

![An animation of the “train purple” button being clicked, resulting in an image of a dog in the output box.](Images/intro_nns_4.gif)

* Finally, train the orange class by making a funny face and pressing the TRAIN ORANGE button for a few seconds. You are telling the neural network that this funny pose corresponds to a little bunny.

![An animation of the “train orange” button being clicked, resulting in an image of a bunny in the output box.](Images/intro_nns_5.gif)

Now that you have trained the model, play around by making several poses and faces for the camera:

* Raise your right hand. Although the neural network was trained to recognise your left hand raised, these kinds of models are continuously learning and capable of recognising and learning new patterns.

* Make a tricky test by partially raising your left hand. The neural network gets confused but is still learning, as can be seen on the confidence bars; finally, the model can decide on your partially raised hand.

![A video of a person raising their hand.](Images/intro_nns_6.gif)

Explain to the students that this funny experiment is just an example of the power of machine learning. But instead of matching gestures with silly pets, you can use this kind of technology for fintech applications.

With their excitement about machine learning at a peak, let the students know that their exploration of the world of machine learning will begin with the area of unsupervised machine learning.

---

### 3. Instructor Do: Introduction to Unsupervised Learning (15 minutes)

This section introduces the students to the concepts of unsupervised machine learning.

Explain that unsupervised learning is a method of machine learning that is popular in the fintech industry. Cover the following talking points:

* With **unsupervised learning** algorithms use test data to construct models that categorise relationships among data points. For example, when you’re reviewing a particular item for purchase on a website, unsupervised learning algorithms might be used to identify related items that are frequently bought together.

* This recognition power for data patterns has broad applications in finance. For example, unsupervised learning can be used to identify **clusters**, or related groups, of clients to target with product offerings or marketing campaigns. The **K-means algorithm** is used for marketing use cases because of its ability to segment customers for financial benefits.

* In this lesson, you’ll apply unsupervised learning by using the K-means algorithm to define customer segments, or clusters.

* In this week’s homework, you’ll apply the K-means algorithm to cluster data and prepare a cryptocurrency portfolio proposal to the company’s board of directors.

Remind the students that the two most frequently used methods of machine learning are **supervised learning** and **unsupervised learning**.

* Explain the following characteristics of unsupervised learning:

  * Deals with unlabeled input data—the category that the data belongs to is not identified.

  * Only uses input data.

  * Has the goal of determining patterns or groups of data, called data **clusters**.

* Compare unsupervised learning to supervised learning by explaining that:

  * Supervised learning uses labelled input data, and unsupervised learning takes unlabeled data.

  * Supervised learning uses training datasets, whereas unsupervised takes only input data.

  * The goal of supervised learning is to predict a class or value, while unsupervised determines patterns or groups of data.

Explain that unsupervised learning comes with some challenges:

* Because the data isn't labelled, we don't know if the output is correct.

* The algorithm is creating its own categories for the data, so an expert is needed to determine if these categories are meaningful.

* Even with its challenges, unsupervised learning can be very useful in a variety of fintech applications. Examples include customer segmentation tasks like grouping customers by spending habits, finding fraudulent credit card charges, or even identifying unusual data points (outliers) within the dataset.

Ask the students the following questions. If no one responds, call on a volunteer to share their answer:

* **Question:** How might clustering be used by fintech businesses?

  * **Answer:** One possible answer is that it can be used to group customers by spending habits and create customised offers via email or mobile apps.

* **Question:** How might anomaly detection be used by credit card companies?

  * **Answer:** One possible answer is that it can be used to detect anomalous and potentially fraudulent credit card transactions (by grouping transactions into normal and abnormal).

Now that the students are familiar with the concept that unsupervised learning is often used to identify groups, or clusters of data, let's find out how to do this by using Python and machine learning algorithms.

---

### 4. Instructor Do: Clustering Explained (15 minutes)

**Corresponding Activity:** [Clusters Demo](Activities/01-Ins_Clusters/Solved/clusters.ipynb)

Explain that unsupervised learning models are often created by using a clustering algorithm. **Clustering** is grouping data together so that every member of that group is similar in some way.

To demonstrate the concept of clusters, you will generate two fake clusters of data by using the `make_blobs` function from scikit-learn.

Demonstrate the following code to the students

  ```python
  # Import the modules
  from sklearn.datasets import make_blobs
  import matplotlib.pyplot as plt

  # Generate synthetic clusters
  X, y = make_blobs(
      centers=3,
      random_state=1
  )

  # Visualizing both classes
  plt.scatter(X[:, 0], X[:, 1], c=y)
  ```

* For this demonstration, highlight that the scikit-learn `make_blobs` function is part of a `samples_generator` that helps to generate sample datasets.

  * These sample datasets are used to help evaluate the performance of machine learning models.

  * The `make_blobs` function actually makes blobs, or clusters.

  * The number of clusters is determined by the `centers` parameter.

  * The  `random_state` variable helps to determine the pattern of the clusters.

Highlight the parameter `random_state=1`, which ensures that code will return the same randomised data set each time it is run; this ensures the same output every time.

* The `X` and `y` values will be the same as long as `random_state=1` is provided. The values will change as the number assigned to `random_state` changes.

* The students will encounter this `random_state` parameter quite often in the code associated with the machine learning lessons.

Show the students the clusters that result from running the code, and then explain them by using the following talking points:

  ![A scatterplot shows three clusters.](Images/cluster_example.png)

* The data points fall into distinct groups or clusters. We can assume that points in each cluster are similar.

* There are three distinct groups of data points on the chart, or clusters.

* Each cluster contains data points that are more similar to their respective clusters and different to points on other clusters.

Explain that the process of clustering data points into groups is called centring.

* **Centering** is a part of the pre-process step of advanced analytics that helps dictate the number of classes/groups to create.

* Centering improves the performance of logistic regression models by ensuring that all data points share the same starting mean value. Data points with the same starting mean value are clustered together.

Have a TA slack out the following code to the students. Ask them to open a Jupyter notebook and generate various clusters by changing the values associated with the parameters `centers` and `random_state`.

  ```python
  # Import the modules
  from sklearn.datasets import make_blobs
  import matplotlib.pyplot as plt

  # Generate synthetic clusters
  X, y = make_blobs(
      centers=3,
      random_state=1
  )

  # Visualize both classes
  plt.scatter(X[:, 0], X[:, 1], c=y)
  ```

* The students should apply a different number of `center` points to the same `random_state` variable, and the same number of centre points to different `random_state` variables in order to compare and contrast the results. The following are examples of different permutations and combinations:

  ```python
  # Generate synthetic clusters
  X, y = make_blobs(
      centers=5,
      random_state=1
  )

  # Visualize both classes
  plt.scatter(X[:, 0], X[:, 1], c=y)

  # Generate synthetic clusters
  X, y = make_blobs(
      centers=5,
      random_state=1
  )

  # Visualize both classes
  plt.scatter(X[:, 0], X[:, 1], c=y)

  # Generate synthetic clusters
  X, y = make_blobs(
      centers=3,
      random_state=1
  )

  # Visualize both classes
  plt.scatter(X[:, 0], X[:, 1], c=y)
  ```

* Although they are not exact, the distribution of clusters across the plot is essentially the same for the same `random_state` values.

Explain that the examples used thus far have assigned the number of clusters by setting the parameter `clusters`. Unfortunately, not all datasets start out with a defined set of clusters like this. Rather, the role of the unsupervised learning algorithm is to identify the number of distinct sets of clusters in the dataset. This is accomplished by way of the **K-means algorithm**.

---

### 5. Everyone Do: The K-means Algorithm (15 minutes)

**Corresponding Activity:** [02-Ins_Kmeans](Activities/02-Ins_Kmeans)

**Files:**

* [services_clustering.ipynb (Unsolved)](Activities/02-Ins_Kmeans/Unsolved/services_clustering.ipynb)

Explain that in real life, it's not always easy to identify the correct number of clusters in the data. Often, the distinguishing features between different groups are not so clear cut. However, an unsupervised learning algorithm called **K-means** can help us to objectively and automatically group our data.

* The K-means algorithm is the simplest and most common algorithm used to group data points into clusters. K-means takes a predetermined amount of clusters to make, and then assigns each data point to one of those clusters.

* The K-means algorithm works by performing two steps:

  1. Assigns points to the closest cluster centre.

  2. Re-adjusts the cluster's centre by setting each centre as the mean of all the data points contained within that cluster.

* The K-means algorithm then repeats this process, again and again, each time getting a little bit better at separating the data points into distinct groups.

* Let's review an example where the clusters aren't so obvious, by using a dataset of the average ratings for types of customer service at a financial services company.

* These ratings are from customers that have rated both the mobile application and a personal banker for customer service. Let's say you are trying to group people together based on how they viewed their experiences with each type of service.

  * Start by loading in your dependencies, and then reading in the `service_ratings.csv` dataset by using the following code.

    ```python
    # Import dependencies
    import pandas as pd
    from pathlib import Path
    import hvplot.pandas

    # Read in the CSV file as a Pandas DataFrame
    service_ratings_df = pd.read_csv(
        Path("../Resources/service_ratings.csv")
    )

    # Review the DataFrame
    service_ratings_df.head()
    ```

  * Next, plot the data on a scatter plot to observe what the spread of data looks like.

    ```python
    # Visualize a scatter plot of the data
    service_ratings_df.hvplot.scatter(
      x="mobile_app_rating",
      y="personal_banker_rating"
    )
    ```

The following image shows the scatter plot:

  ![An image depicts a scatter plot of service ratings.](Images/scatter_services.png)

* The clusters aren't so obvious. The K-means algorithm will be used to break the data into clusters.

  The first step is to import the K-means module from scikit-learn:

  ```python
  from sklearn.cluster import KMeans
  ```

* Following a "model-fit-predict" pattern—which you will use over and over with machine learning—we will create a model that starts by identifying just two clusters (parameter `n_clusters=2`) within the dataset. Here’s the code:

    ```python
    # Create and initialize the K-means model instance for 2 clusters
    model = KMeans(n_clusters=2, random_state=1)

    # Print the model
    model
    ```

Point out that we are again using the `random_state` parameter to ensure that our outcome is consistent every time we rerun this for the same dataset.

* Once the instance of our model has been created, the next step is to fit, or train, the model by using the DataFrame, in this case, `service_ratings_df`. The code is as follows:

    ```python
    # Fit the data to the instance of the model
    model.fit(service_ratings_df)
    ```

* Then we'll have the model create the predictions for which cluster each data point will belong to. This is done with the following code:

    ```python
    # Make predictions about the data clusters using the trained model
    customer_ratings = model.predict(service_ratings_df)

    # Print the predictions
    print(customer_ratings)
    ```

* Now, we will create a copy of the `service_rating_df` DataFrame and name it `service_rating_predictions_df`. Then we’ll add a column to the `service_rating_predictions_df` DataFrame that will contain the customer rating information. These steps are shown in the following code:

    ```python
    # Create a copy of the DataFrame
    service_rating_predictions_df = service_ratings_df.copy()

    # Add a column to the DataFrame that contains the customer_ratings information
    service_rating_predictions_df['customer rating'] = customer_ratings

    # Review the DataFrame
    service_rating_predictions_df.head()
    ```

* Now, we'll plot the results, but this time we will factor in the `customer_ratings` that the K-means algorithm assigned the data points to.

    ```python
    # Plot the data points based on the customer rating
    service_rating_predictions_df.hvplot.scatter(
        x="mobile_app_rating",
        y="personal_banker_rating",
        by="customer rating"
    )
    ```

The following image shows the scatter plot:

  ![An image shows the scatter plot of service ratings with two clusters.](Images/scatter_services_2.png)

Explain the scatter plot:

* With two groups, it looks like there is a group that favours using the mobile application and a group that prefers to use an in-person banker to help with their financial transactions.

* Does this breakdown really provide enough information on customer service preferences for this institution?

* Would breaking the information down into three or four clusters provide additional detail?

Let the students know that identifying the optimal number of clusters will be their task in the following activity.

---

### 6. Student Do: Segmenting Customers (20 minutes)

**Corresponding Activity:** [03-Stu_Segmenting_Customers](Activities/03-Stu_Segmenting_Customers)

In this activity, the students will use the K-means algorithm to segment customer data for mobile versus in-person banking service ratings. The students will evaluate the data by segmenting the data into three and four clusters.

**Files:**

* [segmenting_customers.ipynb (Unsolved)](Activities/03-Stu_Segmenting_Customers/Unsolved/segmenting_customers.ipynb)

* [service_ratings.csv](Activities/03-Stu_Segmenting_Customers/Resources/service_ratings.csv)

**Instructions:**

* [README.md](Activities/03-Stu_Segmenting_Customers/README.md)

---

### 7. Instructor Do: Review Segmenting Customers (10 minutes)

**Files:**

* [segmenting_customers.ipynb (Solved)](Activities/03-Stu_Segmenting_Customers/Solved/segmenting_customers.ipynb)

Review the process of clustering the `service_ratings_df` DataFrame into four segments.

Highlight the steps associated with the process of model-fit-predict as you go.

Explain that the process that the students should have followed in the activity:

* Create the K-means model for four clusters. Emphasise the role that the `random_state` parameter plays in ensuring that all of the groups get the same result.

  ```python
  # Create and initialize the K-means model instance for 4 clusters
  model = KMeans(n_clusters=4, random_state=1)

  # Print the model
  model
  ```

* Fit or train the model based on the `service_ratings_df` DataFrame. Stress that the "model-fit-predict" pattern will be one that they use repeatedly during this section of the course.

  ```python
  # Fit the data to the instance of the model
  model.fit(service_ratings_df)
  ```

* Make predictions for the four customer segments. Highlight that the customer segments print out as a Python list, which corresponds with the first segment being assigned the value of 0.

  ```python
  # Make predictions about the data clusters using the trained model
  customer_segment_4 = model.predict(service_ratings_df)

  # Print the predictions
  print(customer_segment_4)
  ```

* Add the customer segmentation information to the `service_ratings_predictions_df` DataFrame. This allows us to visualise the customer segmentation data in relation to the two columns of rating information.

  ```python
  # Add a column to the DataFrame that contains the customer_segment information
  service_ratings_predictions_df['customer_segment_4'] = customer_segment_4

  # Review the DataFrame
  service_ratings_predictions_df.head()
  ```

* Finally, plot the data with four customer segments.

  ```python
  # Plot the data points based on the customer rating
  service_ratings_predictions_df.hvplot.scatter(
      x="mobile_app_rating",
      y="personal_banker_rating",
      by="customer_segment_4"
  )
  ```

* The following image shows the data clustered into four segments:

![services 4 segments](Images/scatter_services_4.png)

Ask the students if they gleaned any potential insights from the four-cluster grouping of data, and how that could potentially affect the firm's revenue.

* Here’s one possible interpretation: Segmenting the data into four clusters was quite insightful. In what is designated as cluster 3, customers with the highest personal banker service ratings rated the service that received through the mobile application quite poorly. Those users will either continue to consume in-person banking services, or they should be contacted for additional assistance on using the mobile application.

Ask the students if they have any additional questions about K-means clustering or the value of including `random_state` as a model parameter.

Transition to the next topic, the elbow method, by proposing the following questions:

* How can we be sure that the number of clusters that we chose, four, is the optimal number of clusters to segment this dataset?

* Do we explore the data using different values for the `n_clusters` parameter, or do you think there would be a more programmatic way to go about the process of discovering the optimal number for lowercase-k?

---

### 8. Break (15 minutes)

---

### 9. Instructor Do: Introduction to Clustering Optimisation (5 minutes)

Refer to the “Introduction to Clustering Optimisation” slides as you discuss the following points about clustering optimisation:

* Begin by explaining that the appropriate clustering algorithm and parameter settings (for example, the parameters such as the distance function to use, a density threshold, or the number of expected clusters) depends on the individual dataset and intended use of the results.

* Cluster analysis is not an automatic task. As a fintech professional, you will need to do some trial and error to find the optimal clusters.

* This process includes modifying the data preprocessing and model parameters until the result achieves the desired properties.

* So far, you’ve used the K-means algorithm to define customer segments. Do you know the optimal number of clusters, or value of k, and how to find it?

Explain that one of the challenges of working with unlabeled data is the unknown number of existing segments, or clusters. Give the following example:

* Suppose that you’re working with credit-card transaction data, and you want to create a cluster of cardholders to whom you’ll offer other financial products, such as loans, health insurance, retirement investment options, or mortgages. Finding the best number of clusters seems like a tough problem to solve. Fortunately, a simple solution exists called the elbow method.

* Next, you’ll learn how to apply the elbow method to find the ideal number of clusters. You will also use the elbow method to estimate the best cluster design for several equity option contracts.

* In the Challenge assignment, you will use the elbow method to find the best number of clusters for grouping cryptocurrencies by their price actions.

Answer any questions before moving on.

---

### 10. Everyone Do: The Elbow Method (20 minutes)

**Corresponding Activity:** [Elbow Method Demo](Activities/04-Evr_Elbow_Method)

Introduce the elbow method by asking the students the following:

* **Question:** Since the K-means algorithm needs to have the amount of clusters given ahead of time, how can you be sure the amount of clusters you chose is correct?

* One method for determining the optimal value of k, or the number of clusters in a dataset, is the elbow method.

  * The elbow method runs the K-means algorithm for a range of possibilities for `k` (the number of clusters).

  * The resulting elbow curve plots the amount of clusters, x, vs. an objective function called inertia.

  ![A line chart shows the elbow curve.](Images/elbow_chart.png)

  * Inertia involves some complicated math, but is basically a measure of how concentrated the elements are in a dataset.

    * Datasets with a high concentration of elements (where elements are tightly grouped together) have a low value of inertia. This means that there is a small standard deviation for the elements in the cluster relative to the cluster mean value.

    * Datasets with a low concentration of elements (where elements are spread out) have a high value of inertia. This means that there is a high standard deviation for the elements in the cluster relative to the cluster mean value.

    ![A plot shows the low-inertia clusters versus high-inertia clusters.](Images/clusters-inertia.png)

  * The goal is to find a value for k that corresponds to a measure of inertia that shows minimal change for each additional cluster (or value of k) that is added to the dataset. The spot is indicated by the bend in the elbow.

* Let's return to the fintech firm's customer ratings example, and see what this would look like in code.

  * Start by importing dependencies and reading in the dataset.

  ```python
    # Import the modules
  import pandas as pd
  from pathlib import Path
  import hvplot.pandas
  from sklearn.cluster import KMeans
  # Read in the CSV file as a Pandas DataFrame
  service_ratings_df = pd.read_csv(
      Path("../Resources/service_ratings.csv")
  )
  # Review the DataFrame
  service_ratings_df.head()
  ```

  * Next, we create an empty list to store inertia values and a list of k values to test.

    ```python
    # Create lists to store inertia values and the values of k
    inertia = []
    k = list(range(1, 11))
    ```

  * Explain that, in general, the elbow method evaluates the data for 1 to 10 clusters, or values of `k`. The `range` function is not inclusive of the last number, so the values 1 to 11 are used.

  * Next, loop through the values running the K-means algorithm on each value for k and append the inertia to our lists.

    ```python
    # Create a for loop where each value of k is evaluated using the K-means algorithm
    # Fit the model using the service_ratings DataFrame
    # Append the value of the computed inertia from the `inertia_` attribute of the KMeans model instance
    for i in k:
        k_model = KMeans(n_clusters=i, random_state=1)
        k_model.fit(service_ratings_df)
        inertia.append(k_model.inertia_)
    ```

  * The next step is to create a DataFrame to hold the list of values for `k` and `inertia`.

    ```python
      # Create a Dictionary that holds the list values for k and inertia
    elbow_data = {"k": k, "inertia": inertia}

    # Create a DataFrame using the elbow_data Dictionary
    df_elbow = pd.DataFrame(elbow_data)

    # Review the DataFrame
    df_elbow.head()
    ```

* Explain that the following image shows the updated DataFrame with an index, a column labelled “k” that shows the number of clusters, and a column labelled “inertia” that shows the inertia values for each number of clusters.

  ![A screenshot shows the DataFrame with the inertia values.](Images/dataframe-k-inertia.png)

* Finally, plot the DataFrame.

  ```python
  # Plot the DataFrame
  df_elbow.hvplot.line(
      x="k",
      y="inertia",
      title="Elbow Curve",
      xticks=k
  )
  ```

* Now revisit the elbow curve to observe the relationship between the number of clusters and the inertia value.

  ![A line chart shows the number of clusters on the x axis and the inertia on the y axis.](Images/elbow_chart.png)

* On the chart, you can observe a change in steepness between two x values, more so than other two points. This is considered the **elbow** of the chart. Here, that point is at 4.

  ![A plot shows the elbow curve, with a circle around the point where the number of clusters equals 4.](Images/highlighted_elbow.png)

* The value for x where we find this elbow gives us a good indication for how many clusters should be used.

* Ultimately, it looks like our original insight about 4 being an ideal number of clusters for the dataset has proven true. You can rerun the K-means algorithm and the resulting plot with four clusters by using the following code:

  ```python
  # Define the model with 4 clusters
  model = KMeans(n_clusters=4, random_state=1)

  # Fit the model
  model.fit(service_ratings_df)

  # Make predictions
  k_4 = model.predict(service_ratings_df)

  # Create a copy of the DataFrame
  service_ratings_predictions_df = service_ratings_df.copy()

  # Add a class column with the labels
  service_ratings_predictions_df['customer_segment'] = k_4
  ```

Before moving on to the student activity, convey that an elbow curve is not a definite answer for how many clusters there should be; rather, it works as a guide. Ultimately, it's up to the data professional to determine the right amount.

Answer any questions before moving on.

---

### 11. Student Do: Finding k (20 minutes)

**Corresponding Activity:** [05-Finding_the_Best_k](Activities/05-Stu_Finding_k)

**Files:**

* Solved: [finding_k.ipynb (Solved)](Activities/05-Stu_Finding_k/Solved/finding_k.ipynb)

* [stock_data.csv](Activities/05-Stu_Finding_k/Resources/stock_data.csv)

**Instructions:**

* [README.md](Activities/05-Stu_Finding_k/README.md)

---

### 12. Instructor Do: Review Finding k (10 minutes)

**Corresponding Activity:** [05-Stu_Finding_k](Activities/05-Stu_Finding_k/Solved/finding_k.ipynb)

**Files:**

* [finding_k.ipynb (Solved)](Activities/05-Stu_Finding_k)

As you work through the solution to the previous activity, be sure to emphasise the following points:

* The lists for inertia and the values of k are being used in the `for` loop and then to eventually construct the DataFrame that defines the plot of the elbow curve. These two variables are the two central components of what the elbow method works to create.

  ```python
  inertia = []
  k = list(range(1, 11))
  ```

* The `for` loop is where the K-means algorithm comes into play. The `inertia` attribute, which is vital to the defining the "elbow" shape, is calculated as part of the K-means algorithm:

  ```python
  for i in k:
      k_model = KMeans(n_clusters=i, random_state=0)
      k_model.fit(spread_df)
      inertia.append(k_model.inertia_)
  ```

* The elbow DataFrame could be created all in one step rather than two, as demonstrated in the following code:

  ```python
  elbow_data = {"k": k, "inertia": inertia}
  df_elbow = pd.DataFrame(elbow_data)
  df_elbow.head()
  ```

  OR

  ```python
  df_elbow = pd.DataFrame({"k": k, "inertia": inertia})
  df_elbow.head()
  ```

* The elbow curve is a plot of the inertia value that is associated with each value of k. The curve of the elbow is the point where the values for the inertia, or spread between the cluster elements, nears its smallest point. For any value of k beyond the optimal, the change in the value of inertia is minimal. Adding additional clusters does not add much information.

  ```python
  # Plot the DataFrame
  df_elbow.hvplot.line(
      x="k",
      y="inertia",
      title="Elbow Curve",
      xticks=k
  )
  ```

  ![A line chart that shows the number of clusters on the x axis and the inertia on the y axis.](Images/elbow-curve.png)

* For this activity, the values of 3 and 4 are most likely the optimal values of k. Here is the code and visualisations for each value.

  ```python
  # For k = 3
  model = KMeans(n_clusters=3, random_state=1)

  # Fit the model
  model.fit(spread_df)

  # Make predictions
  k_lower = model.predict(spread_df)

  # Create a copy of the DataFrame and name it spread_df_predictions
  spread_df_predictions = spread_df.copy()

  # Add a class column with the labels to the spread_df_predictions DataFrame
  spread_df_predictions['clusters_lower'] = k_lower

  # Plot the clusters
  spread_df_predictions.hvplot.scatter(
      x="hi_low_spread",
      y="close",
      by="clusters_lower"
  ).opts(yformatter="%.0f")
  ```

Here is the plot of the day’s trading volume as a function of the spread between the high and low trading price when the number of clusters is set to 3:

  ![A scatter plot of the relationship between daily trading volume and trading price shows three clusters.](Images/spread-volume-k-3.png)

Here is the code to plot four clusters:

  ```python
  # For k = 4
  model = KMeans(n_clusters=4, random_state=1)

  # Fit the model
  model.fit(spread_df)

  # Make predictions
  k_higher = model.predict(spread_df)

  # Add a class column with the labels to the spread_df_predictions DataFrame
  spread_df_predictions['clusters_higher'] = k_higher

  # Plot the clusters
  spread_df_predictions.hvplot.scatter(
      x="hi_low_spread",
      y="close",
      by="clusters_higher"
  ).opts(yformatter="%.0f")
  ```

Notice how the plot changes when the number of clusters is set to 4 instead of 3:

  ![A scatter plot that represents the relationship between daily trading volume and trading price shows four clusters.](Images/spread-volume-k-4.png)

Ask the students what they think the optimal value for k is. From the plots, it appears that the optimal value for k is 3.

Ask the students if they have any additional questions about the elbow method and how it relates to the K-means algorithm.

Answer any questions before moving on.

### 13. Instructor Do: Lesson Recap (10 minutes)

Congratulate the students on learning their first machine learning skills!

Recap what they learned today:

* You can explain the differences between supervised and unsupervised machine learning.

* You can describe the purpose of clustering and how it’s used in finance.

* You can use the K-means algorithm to identify clusters in a given dataset, and how to optimise this algorithm by using the elbow method.

Explain to the students that they’re ready to take the next step: preprocessing the data which goes into these types of models, and creating models which can adapt and perform better on more complex types of data. This is what they will learn in the next class.

Answer any questions before moving on.

## End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
