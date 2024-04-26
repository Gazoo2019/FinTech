## 10.2: Machine Learning in Practice

### Overview

In this class, the students will explore machine learning more deeply. The lesson begins with a recap from the last lesson, and then focuses on normalising, preprocessing, and segmentation. The goal is to enable students to refine their unsupervised learning algorithms and to flexibly apply them to a variety of financial applications.

### Class Objectives

By the end of this lesson, the students will be able to:

* Preprocess data by normalising it.

* Segment financial data.

* Prepare data for complex algorithms.

* Explain the importance of preprocessing and normalising data for unsupervised learning.

* Transform categorical variables into a numerical representation by using Pandas.

* Normalize data by using the `StandardScaler` module from Scikit-learn.

### Instructor Notes

* Welcome to the second day of machine learning! You will guide the students through a series of activities to build on what they know and can accomplish with K-nearest neighbours, their first unsupervised learning algorithm.

* Today's class will stretch the students’ ability to cluster algorithms by teaching them about necessary and commonly used practices in unsupervised learning, like standardising variables or dealing with categorical (non-numerical) data. They'll also be exposed to clustering methods outside of K-means.

* To some extent, this first part of the class should feel like a review that reinforces the techniques the students just learned. The latter half of the class should provide opportunities for the students to advance their skills by learning a new clustering technique and acquiring strategies to deal with more complex types of data.

* Help build the students’ confidence and engagement by being encouraging and by reminding them that anyone who uses machine learning has started where the students are right now. You can also promote effective problem-solving skills by letting the students explain concepts if they feel comfortable.

* As you review the activities, find ways to connect the concepts to fintech. Include brief discussions about emerging or disruptive/innovative technologies and how they have changed the fintech landscape.

* Activities that involve programming solutions will have an associated coding file linked at the beginning of the activity section. Click the link to go to the coding file required for the activity.

* Have your TAs keep track of the time with the [Time Tracker](TimeTracker.xlsx).

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 10.2 Slides](https://docs.google.com/presentation/d/1AP_kW-uu-mW1pm7J_T70-ENOxPDTvHyEgQ3hQ3mNzXk/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The Time Tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome the Class (10 minutes)

Remind the students that in the previous lesson they learned the following:

* How to recognise the differences between supervised and unsupervised machine learning.

* What clustering is and how it is used in finance.

* How to apply the K-means algorithm to identify clusters to several datasets.

* How to determine the optimal number of clusters for a dataset by using the elbow method.

To reinforce their learning and check their understanding, ask the following questions:

* **Question:** How is machine learning used in finance? Give examples.

  * **Sample answer:** Examples of machine learning in finance include: finding outliers, classifying fraudulent credit card charges, predicting customer preferences, and algorithmic trading.

* **Question:** What is the difference between unsupervised and supervised learning?

  * **Sample answer:** The main distinction between the two approaches is the use of labelled datasets.

  * **Sample answer:** Supervised learning uses labelled input and output data, while an unsupervised learning algorithm only has labelled input data.

As another refresher, copy and paste the following Python code sample into a Jupyter notebook and then explain what the code is doing:

  ```python
  # Create a for loop where each value of k is evaluated using the K-means algorithm
  # Fit the model using the home_sales_df DataFrame
  # Append the value of the computed inertia from the `inertia_` attribute of the K-means model instance
  for i in k:
      k_model = KMeans(n_clusters=i, random_state=1)
      k_model.fit(spread_scaled_df)
      inertia.append(k_model.inertia_)

  # Create a dictionary that holds the list values for k and inertia
  elbow_data = {"k": k, "inertia": inertia}

  # Create a DataFrame using the elbow_data dictionary
  df_elbow = pd.DataFrame(elbow_data)

  # Review the DataFrame
  df_elbow.head()
  ```

* Here we are fitting a `KMeans` model to unlabeled data multiple times, each selecting a different number of clusters by which to segment this data.

* We can use the elbow method to select the number of clusters which best describe this data.

Answer any questions before moving on
---

### 2. Student Do: Warm Up (15 minutes)

In this activity, the students will revisit some concepts and code related to K-means from the previous class. This will help refresh the students on these concepts and build their confidence in preparation for the more advanced topics they will learn later in the lesson.

**Corresponding Activity:** [01-Warm_Up](Activities/01-Warm_Up/)

**Files:**

* Solved: [01-Warm_Up](Activities/01-Warm_Up/Solved/homebuying_eras.ipynb)

* Unsolved: [01-Warm_Up](Activities/01-Warm_Up/Unsolved/homebuying_eras.ipynb)

* [national-home-sales.csv](Activities/01-Warm_Up/Resources/national-home-sales.csv)

**Instructions:**

* [README.md](Activities/01-Warm_Up/README.md)

---

### 3. Instructor Do: Review Warm Up (10 minutes)

**File:**

* Solved: [01-Warm_Up](Activities/01-Warm_Up/Solved/homebuying_eras.ipynb)

Review the following solution with students:

  ```python
  # Import the modules
  import pandas as pd
  import hvplot.pandas
  from pathlib import Path
  from sklearn.cluster import KMeans
  # Read in the CSV file as a Pandas DataFrame
  home_sales_df = pd.read_csv(
      Path("../Resources/national-home-sales.csv"),
      index_col="date",
      parse_dates=True,
      infer_datetime_format=True
  )

  # Review the DataFrame
  home_sales_df.head()
  ```

As you work through the solution to the previous activity, be sure to emphasise the following points:

* The lists for inertia and the values of k are used in the `for`loop and then used to construct the DataFrame that defines the plot of the elbow curve. These two variables are the two central components of what the elbow method works to create.

  ```python
  inertia = []
  k = list(range(1, 11))
  ```

* The `for` loop is where the K-means algorithm comes into play. The `inertia` attribute that is vital to the elbow is calculated as part of the K-means algorithm.

  ```python
  for i in k:
      k_model = KMeans(n_clusters=i, random_state=2)
      k_model.fit(home_sales_df)
      inertia.append(k_model.inertia_)
  ```

* The elbow DataFrame could be created in one step instead of two, as demonstrated in the following code:

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

* For this activity, the values of 3 and 4 are most likely the optimal values of k. The following code produces the visualisations for each value:

  ```python
  # For k = 3
  model = KMeans(n_clusters=3, random_state=1)

  # Fit the model
  model.fit(home_sales_df)

  # Make predictions
  k_lower = model.predict(home_sales_df)

  # Create a copy of the DataFrame and name it home_sales_predictions_df
  home_sales_predictions_df = home_sales_df.copy()

  # Add a class column with the labels to the home_sales_predictions_df DataFrame
  home_sales_predictions_df['clusters_lower'] = k_lower

  # Plot the clusters
  home_sales_predictions_df.hvplot.scatter(
      x="inventory",
      y="homes_sold",
      by="clusters_lower"
  ).opts(yformatter="%.0f")
  ```

The following code produces the visualisations for 4 clusters:

  ```python
  # For k = 4
  model = KMeans(n_clusters=4, random_state=1)

  # Fit the model
  model.fit(home_sales_df)

  # Make predictions
  k_higher = model.predict(home_sales_df)

  # Add a class column with the labels to the home_sales_predictions_df DataFrame
  home_sales_predictions_df['clusters_higher'] = k_higher

  # Plot the clusters
  home_sales_predictions_df.hvplot.scatter(
      x="inventory",
      y="homes_sold",
      by="clusters_higher"
  ).opts(yformatter="%.0f")
  ```

Ask the students what the optimal value of k is.

* From the scatter plots, it appears that the optimal number of clusters, or value of k, is probably 3. It appears to better group the monthly housing trends among different levels of inventory.

* However, 4 clusters are probably not wrong either. This is because for a certain range of inventory, it appears to identify two unique clusters according to the number of homes sold. Overall, the best differentiation across multiple variables would likely be 3 clusters.

Ask the students if they have any additional questions about the elbow method and how it relates to the K-means algorithm.

Answer any questions before moving on.

---

### 4. Instructor Do: Preparing Data by Normalising It (20 minutes)

In this section, you’ll introduce the students to normalising data and then do a brief coding demo.

**Corresponding Activity:** [02-Preparing_Data_by_Normalizing](Activities/02-Preparing_Data_by_Normalizing/)

**Files:**

* [segmenting_customer_data.ipynb (Unsolved)](Activities/02-Preparing_Data_by_Normalizing/Unsolved/Preparing_Data_by_Normalizing.ipynb)

* [segmenting_customer_data.ipynb (Solved)](Activities/02-Preparing_Data_by_Normalizing/Solved/Preparing_Data_by_Normalizing.ipynb)

First, give the students some context about what they are doing and why, with the next few talking points. Begin with an introduction to standard scaling and principal component analysis (PCA).

* Data clustering can be optimised by selecting the best value for k. Using the K-means algorithm is useful for grouping and understanding financial data.

* Machine learning algorithms can often be enhanced and optimised by applying principal component analysis, or PCA. PCA is an important optimisation technique widely used in the world of quantitative finance, particularly for portfolio construction.

* Before learning PCA, which is the focus of the next lesson, we first need to learn how to transform the features of data. We'll do this by applying **standard scaling**.

* After scaling, we’ll combine PCA with the K-means algorithm. This will give us a strategy to better handle extremely large financial datasets.

Connect this topic to this week's Challenge assignment:

* In the Challenge, you’ll manage data and optimise the clusters with PCA, and then analyse the results. Then, you’ll propose the best number of cryptocurrency clusters for the portfolio.

Slack out this [link to Portfolio Construction Using Principal Component Analysis](https://web.wpi.edu/Pubs/ETD/Available/etd-080614-144242/unrestricted/Chen,_Huanting_PCA_2014-07-31_FINAL_VERSION.pdf) by Huanting Chen and tell students that this is a good point of reference.

In the next few talking points, refer to the “Normalizing Data” slides as you introduce the class to the process of preparing data by normalising it.

* Preparing data can be time consuming if we do it manually. This is especially true if we have several columns in a DataFrame to normalise, or transform.

* Remember, the K-means algorithm requires all the columns in a DataFrame to have numeric values. With K-means, it's also best that the numeric values all have the same scale. This prevents K-means from putting too much weight on any one single variable.

* When we **normalise** data, we eliminate the measurement units and scale the numeric values to a similar scale. We can then compare data of differing natures.

* Instead of manually normalising, or transforming our data, we can use functions from Pandas and the scikit-learn library to simplify our data preparation.

Now, do a brief coding demo while discussing the following talking points about applying standard scaling:

* The most common way to normalise data is to apply **standard scaling**, which is a method of centring values around the mean. Let's review one of our credit card spending datasets to illustrate how standard scaling works.

![A screenshot depicts the original shopping data. The columns are Card Type, Age, Annual Income, and Spending Score.](Images/10-4-original-shopping-data.png)

* Instead of manually scaling the Annual Income column, this module from scikit-learn can be used. The `StandardScaler` will transform our data by calculating the mean value of the column and scaling the data in the column to a standard deviation of 1.

* It does this by first subtracting the mean value of the column, and then dividing by the standard deviation of the column for each value in the column: (value - mean)/standard deviation.

* Scaling the data so that it has a mean of 0 and a standard deviation of 1 is useful, because it puts all variable ranges on the same footing. Otherwise, our results in machine learning models might become distorted: if some columns of data with larger values or values that range more widely than others, some ML algorithms (such as K-means) could ascribe disproportionate importance to those wider ranging columns.

* **Data standardisation**, or **data normalisation**, is a common practice in the data preprocessing that occurs before training a machine learning model.

Slack out the [scikit-learn documentation on preprocessing and Standardization](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing-scaler) so the students can learn more about data standardisation. Encourage them to refer to the [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html).

Next, start the coding demo. Follow these steps:

* Import the `StandardScaler` module.

  ```python
  from sklearn.preprocessing import StandardScaler
  ```

* Transform the data by using the `fit_transform` function. It's usually a good idea to scale all the numeric columns. So, we’ll transform the Age, Annual Income, and Spending Score columns, as the following code shows:

```python
# Scaling the numeric columns
shopping_data_scaled = StandardScaler().fit_transform(df_shopping[["Age", "Annual Income", "Spending Score"]])

# Creating a DataFrame with the scaled data
df_shopping_transformed = pd.DataFrame(shopping_data_scaled, columns=["Age", "Annual Income", "Spending Score"])

# Display sample data
df_shopping_transformed.head()
```

* The following image shows the head of the transformed DataFrame:

  ![A screenshot depicts the resulting DataFrame with the three transformed columns.](Images/10-4-using-standard-scaler.png)

* The `StandardScaler().fit_transform` function does not return a Pandas DataFrame. Instead, it returns an array of data that must be converted to a Pandas DataFrame.

* The columns in the new DataFrame will be returned in the same order that they were provided to the `StandardScaler().fit_transform` function; therefore, the list provided to that function can be used to assign the column names in the new DataFrame.

* The `StandardScaler` gives us the ability to scale several columns in a single function call. The `StandardScaler` is useful for columns with data that ranges continuously, like Age and Annual Income.

* The columns with data in string or category-type format will need to be handled differently. These `object` types of variables aren't easily standardised. The variable "Card Type", for example, consists of data in a **binary** (that is, "yes" or "no") type of categorical variable.

* In order to transform this "Card Type" categorical column, we can use the `get_dummies` function from the Pandas library.

Slack out [this link on Pandas' `get_dummies` function](https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html) as you elaborate on its usage with the following talking points.

* The `get_dummies` function converts categorical data into a numerical format that machine learning models recognise. To do that, the Pandas `get_dummies` function transforms a categorical column of data into multiple columns of separate data, where each entry is a `1` or `0` representation.

* It's easier to explain what's happening with `get_dummies` with an example. Here, with the "Card Type" variable, we call `pd.get_dummies` to transform this single "Credit" or "Debit" `str` type variable into two numerical columns, depending on whether that "Card Type" value for each row was a "Credit" or "Debit" transaction.

```python
# Transform the Card Type column using get_dummies()
card_dummies = pd.get_dummies(df_shopping["Card Type"])

# Display sample data
card_dummies.head()
```

* The following image shows the head of the resulting DataFrame:

  ![A screenshot depicts the transformed DataFrame.](Images/10-4-get-dummies.png)

* Point out that `get_dummies` converted the Card Type column into two separate columns named "Credit" and "Debit". Each value in each new column is `1` or `0`, with `1` representing that a credit or debit value, respectively, was present in that row in the original Card Type column.

* Note that `get_dummies` produces a new, separate DataFrame, but one in which the index is still the same as the original DataFrame that we called `get_dummies` on.

* Because `card_dummies` and `df_shopping_transformed` are two DataFrames with the same index, we can concatenate (or combine) them by using the Pandas `concat` function to have all the transformed data in a single DataFrame, as the following code shows:

```python
# Concatenate the df_shopping_transformed and the card_dummies DataFrames
df_shopping_transformed = pd.concat([df_shopping_transformed, card_dummies], axis=1)

# Display sample data
df_shopping_transformed.head()
```

* The following image shows the resulting DataFrame:

  ![A screenshot depicts the concatenated DataFrame with Age, Annual Income, Spending Score, Credit, and Debit columns.](Images/10-4-concatenating-transformed-data.png)

Slack out the [Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html) so that the students can learn more about the `concat` function.

Explain that scaling numeric data and encoding categorical data are common practices in the data preparation phase. The students should get used to performing these operations every time they want to cluster data by using the K-means algorithm.

Recap what we just did:

* In the preceding example, we went through how to transform a DataFrame so that all the columns have the same scale. This is an important step if we want to cluster data by using the K-means algorithm&mdash;because it ensures that all the data is comparable.

* Without that scaling, the K-means algorithm might give too much weight to one variable over another when clustering&mdash;just because that variable has been measured differently. In addition, we learned a convenient way to encode `str` type variables&mdash;specifically, by using the Pandas `get_dummies` function.

Ask if there are any questions before moving on.

### 5. Everyone Do: Preprocessing Data (20 minutes)

**Corresponding Activity:** [03-Evr_Preprocessing](Activities/03-Evr_Preprocessing/)

**Files:**

* [cc_preprocessing.ipynb (Unsolved)](Activities/03-Evr_Preprocessing/Unsolved/cc_preprocessing.ipynb)

* [cc_preprocessing.ipynb (Solved)](Activities/03-Evr_Preprocessing/Solved/cc_preprocessing.ipynb)

Reiterate to the students that an important aspect of machine learning is data preparation, or data preprocessing.

Explain that, after importing a dataset into a Pandas DataFrames, not all the data is ready for immediate analysis by a machine learning model. The following considerations are recommended for using data to feed a machine learning model:

* First, most machine learning models cannot directly work with data that is in the form of strings or text. These elements will need to be encoded, or converted, into numeric categories.

* Second, machine learning algorithms have a hard time adjusting for data with wildly different scales.

* Third, missing values are difficult for machine learning models to navigate.

* There is a saying, "Garbage in, garbage out." The data going into a machine learning model must be clean in order for the predictions coming out to be accurate.

Open the unsolved version of the provided Jupyter notebook. Tell the students that you will demonstrate how data can be prepared to feed into an unsupervised machine learning model, this time using a different credit dataset. You will use a dataset that contains information from nearly 5,000 credit card holders.

Live code the demonstration, and suggest that the students follow along, asking any questions as they occur. Follow these steps:

* Import the raw data into a Pandas DataFrame and share a sample of the data with the students as the following image shows:

![A screenshot shows the DataFrame containing credit card information.](Images/ccinfo-DataFrame.png)

* Ask the students if they can identify any preprocessing that needs to be done on the `ccinfo_df` DataFrame before a machine learning algorithm can be applied. Potential answers include the following:

  * The four categories associated with the "education" column need to be encoded so that each category is represented by a number.

  * Based on the last five rows of the DataFrame, the "marriage" column seems likely to include only  “yes” or “no” values. This needs to be converted to a binary data category.

  * "limit_bal", "bill_amt", and "pay_amt" should all be normalised so that they are on the same scale.

Work through the code needed to address each of these issues, as follows:

* The first issue is to address the "education" column. Confirm that there are four categories associated with this column: `primary`, `secondary`, `post-grad`, and `other`. Each of these categories needs to be converted into a corresponding numerical value.

![A screenshot shows a table that includes the value counts for each of the categories in the education column.](Images/ccinfo-education-value-counts.png)

* As introduced previously, one way to address transforming categorical variables into numeric ones is with the Pandas `get_dummies` function. This function converts categorical data into a numerical format.

* The `get_dummies` function also separates the single column of data into a number of columns that is equal to the number of different categories found in the column. In this case, four categories equals four new columns of data.

  ```python
  # Transform the education column using get_dummies
  education_dummies = pd.get_dummies(ccinfo_df["education"])

  # Display the transformed data
  education_dummies.tail()
  ```

* The result of the transformation is an `education_dummies` DataFrame:

  ![A screenshot shows the last five rows of the DataFrame.](Images/education-dummies.png)

* The next step is to incorporate the `education_dummies` DataFrame into the `ccinfo_df` DataFrame so that it can be used as part of the segmentation analysis. The original "education" column will also need to be dropped.

  ```python
  # Concatenate the df_shopping_transformed and the card_dummies DataFrames
  ccinfo_df = pd.concat([ccinfo_df, education_dummies], axis=1)

  # Drop the original education column
  ccinfo_df = ccinfo_df.drop(columns=["education"])

  # Display the DataFrame
  ccinfo_df.head()
  ```

* The resulting DataFrame is shown in the following image:

  ![A screenshot shows the first five rows of the revised DataFrame.](Images/ccinfo-with-edu-dummies.png)

Reiterate to the students that the `get_dummies` function is a quick and efficient way to convert categorical data into corresponding numerical categories. But there is also another way to accomplish this process. The process is called encoding.

* **Encoding** is a preprocessing technique for creating a sequential representation of a categorical variable.

* Encoding can be handled in a function that uses `if-else` statements to process the data transformation.

Demonstrate encoding by transforming the "marriage" column with the following code:

  ```python
  # Encode the marriage column using a custom function
  def encode_marriage(marriage):
      """
      This function encodes marital status by setting yes as 1 and no as 0.
      """
      if marriage == "yes":
          return 1
      else:
          return 0

  # Call the encode_marriage function on the marriage column
  ccinfo_df["marriage"] = ccinfo_df["marriage"].apply(encode_marriage)

  # Review the DataFrame
  ccinfo_df.head()
  ```

Explain to the students that the "marriage" data was not split into multiple categories like the "education" categories were when `get_dummies` was applied. Rather, the data in the "marriage" column was adjusted—it now has binary values. Here’s the resulting DataFrame:

![A screenshot shows the first five rows of the revised DataFrame.](Images/ccinfo-marriage-encoded.png)

Explain that the final step of data preprocessing is to **normalise**, **scale**, or **standardise** (which in this case all mean the same thing) the data contained in the "limit_bal", "bill_amt", and "pay_amt" columns.

Remind the students that data columns in a DataFrame need to be normalised when they're in different scales.

* Data is normalised when the values in the column have a **mean of 0** and a **standard deviation of 1**. This same scale is applied to all of the columns that need to be normalised.

* This is important because it provides all of the columns that contain numeric data (not to be confused with those columns that had their categorical data transformed) with the same foundation. That is, they are considered to have similar importance, or weight, to the machine learning model.

* It is possible to normalise, or scale, each of these columns manually, but it is much easier to apply the `StandardScaler` module from the scikit-learn library.

Start by importing the module from the scikit-learn library with the following code.

  ```python
  # Import the module
  from sklearn.preprocessing import StandardScaler
  ```

Then, explain that the next step is to call the `StandardScaler` and the `fit_transform` function on the columns from the DataFrame that need to be normalised.

  ```python
  # Scaling the numeric columns
  ccinfo_data_scaled = StandardScaler().fit_transform(ccinfo_df[["limit_bal", "bill_amt", "pay_amt"]])

  # Review the scaled data
  ccinfo_data_scaled
  ```

* The result of the scaling is an array that contains a list of lists. Each nested list is a row of scaled values with one entry for each column.

![A screenshot shows an array that contains nested lists.](Images/ccinfo-scaled-data.png)

* Now, all we need to do is replace the original numeric data from the "limit_bal", "bill_amt", and "pay_amt" columns with its scaled counterparts. This is done with the following code:

  ```python
  # Create a DataFrame of the scaled data
  ccinfo_data_scaled = pd.DataFrame(ccinfo_data_scaled, columns=["limit_bal", "bill_amt", "pay_amt"])

  # Replace the original data with the columns of information from the scaled Data
  ccinfo_df["limit_bal"] = ccinfo_data_scaled["limit_bal"]
  ccinfo_df["bill_amt"] = ccinfo_data_scaled["bill_amt"]
  ccinfo_df["pay_amt"] = ccinfo_data_scaled["pay_amt"]

  # Review the DataFrame
  ccinfo_df.head()
  ```

* And now we have a DataFrame that can be segmented by using K-means.

![A screenshot shows the first five rows of the revised DataFrame.](Images/ccinfo-transformed.png)

Briefly review the elbow method and K-means module.

* The following code applies the elbow method, or determining the optimal value for `k`.

  ```python
  # Import the K-means module from SKLearn
  from sklearn.cluster import KMeans

  # Create a list to store inertia values and the values of k
  inertia = []
  k = list(range(1, 11))

  # Create a for loop where each value of k is evaluated by using the K-means algorithm
  # Fit the model by using the service_ratings DataFrame
  # Append the value of the computed inertia from the `inertia_` attribute of the K-means model instance
  for i in k:
      k_model = KMeans(n_clusters=i, random_state=0)
      k_model.fit(ccinfo_df)
      inertia.append(k_model.inertia_)

  # Define a DataFrame to hold the values for k and the corresponding inertia
  elbow_data = {"k": k, "inertia": inertia}
  df_elbow = pd.DataFrame(elbow_data)

  # Review the DataFrame
  df_elbow.head()

  # Plot the DataFrame
  df_elbow.hvplot.line(
      x="k",
      y="inertia",
      title="Elbow Curve",
      xticks=k
  )
  ```

* The following plot results from the elbow method:

  ![A plot shows the elbow curve, with the number of clusters on the x-axis and inertia on the y-axis.](Images/ccinfo-elbow-method-plot.png)

Explain that the optimal number for `k` appears to be 3 because it's the section of the plot where an elbow is formed. With this information, the K-means algorithm can be applied to segment the data. The following code applies the K-means algorithm:

  ```python
  # Define the model with 3 clusters
  model = KMeans(n_clusters=3, random_state=3)

  # Fit the model
  model.fit(ccinfo_df)

  # Make predictions
  k_3 = model.predict(ccinfo_df)

  # Create a copy of the preprocessed data
  ccinfo_predictions_df = ccinfo_df.copy()

  # Add a class column with the labels
  ccinfo_predictions_df['customer_segments'] = k_3

  # Plot the clusters
  ccinfo_predictions_df.hvplot.scatter(
      x="limit_bal",
      y="age",
      by="customer_segments"
  )
  ```

* The following image shows the resulting plot:

  ![A scatter plot shows age versus limit_bal and includes three clusters.](Images/ccinfo-segmented.png)

Let the students know that, as shown by the plot, we can identify the three customer segments by using the "limit_bal" and the "age" columns. The plot also shows that the limit balance increases as age increases.

Explain that in the next activity, the students will apply data preprocessing on their own.

Answer any questions before moving on.

---

### 6. Break (15 minutes)

---

### 7. Student Do: Standardizing Stock Data (25 minutes)

**Corresponding Activity:** [04-Stu-Standardizing_Stock_Data](Activities/04-Stu-Standardizing_Stock_Data/)

In this activity, the students will use the K-means algorithm to segment customer data for mobile versus in-person banking service ratings. Before doing so, the students will have to preprocess the data by using the techniques that they've learned in this lesson.

**Files:**

* [standardizing_stock_data.ipynb](Activities/04-Stu-Standardizing_Stock_Data/Unsolved/standardizing_stock_data.ipynb)

* [tsx-energy-2018.csv](Activities/04-Stu-Standardizing_Stock_Data/Resources/tsx-energy-2018.csv)

---

### 8. Instructor Do: Review Standardizing Stock Data (15 minutes)

**Corresponding Activity:** [04-Stu-Standardizing_Stock_Data](Activities/04-Stu-Standardizing_Stock_Data/)

**Files:**

* [standardizing_stock_data.ipynb (Solved)](Activities/04-Stu-Standardizing_Stock_Data/Solved/standardizing_stock_data.ipynb)

* [tsx-energy-2018.csv](Activities/04-Stu-Standardizing_Stock_Data/Resources/tsx-energy-2018.csv)

Review the solution to the activity, going through each step.

* Step 1: Read in the `tsx-energy-2018.csv` file from the `Resources` folder and create the DataFrame. Make sure to set the `Ticker` column as the DataFrame’s index. Then review the DataFrame.

  ```python
  # Import the required libraries and dependencies
  import pandas as pd
  from path import Path
  from sklearn.cluster import KMeans
  from sklearn.preprocessing import StandardScaler
  # Read the CSV file into a Pandas DataFrame
  # Set the index using the Ticker column
  df_stocks = pd.read_csv(
      Path("../Resources/tsx-energy-2018.csv"),
      index_col="Ticker"
  )

  # Review the DataFrame
  df_stocks.head()
  ```

* Step 2: To prepare the data, use the `StandardScaler` module and the `fit_transform` function to scale all the columns containing numerical values. Review a five-row sample of the scaled data using bracket notation ([0:5]).

  ```python
  # Use the StandardScaler module and fit_transform function to
  # Scale all columns with numerical values
  stock_data_scaled = StandardScaler().fit_transform(df_stocks[["MeanOpen", "MeanHigh", "MeanLow", "MeanClose", "MeanVolume", "AnnualReturn", "AnnualVariance"]])

  # Display the first five rows of the scaled data
  stock_data_scaled[0:5]
  ```

* Step 3: Create a new DataFrame called `df_stocks_scaled` that contains the scaled data. Make sure to do the following:

  * Use the same labels that were referenced in the `StandardScaler` for the column names.

  * Add a column to the DataFrame that consists of the tickers from the original DataFrame. (Hint: This column was the index).

  * Set the new column of tickers as the index for the new DataFrame.

  * Review the resulting DataFrame.

  ```python
  # Create a DataFrame called with the scaled data
  # The column names should match those referenced in the StandardScaler step
  df_stocks_scaled = pd.DataFrame(
      stock_data_scaled,
      columns=["MeanOpen", "MeanHigh", "MeanLow", "MeanClose", "MeanVolume", "AnnualReturn", "AnnualVariance"]
  )

  # Create a Ticker column in the df_stocks_scaled DataFrame
  # using the index of the original df_stocks DataFrame
  df_stocks_scaled["Ticker"] = df_stocks.index

  # Set the newly created Ticker column as index of the df_stocks_scaled DataFrame
  df_stocks_scaled = df_stocks_scaled.set_index("Ticker")

  # Review the DataFrame
  df_stocks_scaled.head()
  ```

* Step 4: Encode the “EnergyType” column by using `pd.get_dummies`, and save the result in a separate DataFrame called `df_oil_dummies`. Note that because the company name isn’t relevant for clustering, you don’t need to encode the “CompanyName” column.

  ```python
  # Encode (convert to dummy variables) the EnergyType column
  df_oil_dummies = pd.get_dummies(df_stocks["EnergyType"])

  # Review the DataFrame
  df_oil_dummies.head()
  ```

* Step 5: Using the `pd.concat` function, concatenate the `df_stocks_scaled` DataFrame with the `df_oil_dummies` DataFrame, along an axis value of 1 (`axis=1` tells Pandas to join the data horizontally by columns). Review the concatenated DataFrame.

  ```python
  # Concatenate the `EnergyType` encoded dummies with the scaled data DataFrame
  df_stocks_scaled = pd.concat([df_stocks_scaled, df_oil_dummies], axis=1)

  # Display the sample data
  df_stocks_scaled.head()
  ```

* Step 6: Using the concatenated DataFrame, cluster the data by using the K-means algorithm and a k value of 3. Create a copy of the concatenated DataFrame, and add the resulting list of company segment values as a new column.

  ```python
  # Initialize the K-Means model with n_clusters=3
  model = KMeans(n_clusters=3)

  # Fit the model for the df_stocks_scaled DataFrame
  model.fit(df_stocks_scaled)

  # Predict the model segments (clusters)
  stock_clusters = model.predict(df_stocks_scaled)

  # View the stock segments
  print(stock_clusters)

  # Create a copy of the concatenated DataFrame
  df_stocks_scaled_predictions = df_stocks_scaled.copy()

  # Create a new column in the copy of the concatenated DataFrame with the predicted clusters
  df_stocks_scaled_predictions["StockCluster"] = stock_clusters

  # Review the DataFrame
  df_stocks_scaled_predictions.head()
  ```

Ask if there are any questions before moving on.

---

### 9. Instructor Do: Clustering Complex Data (20 minutes)

**Corresponding Activity:** [05-Ins-Complex-Data](Activities/05-Ins-Complex-Data/)

**Files:**

* [ins-complex-data.ipynb (Solved)](Activities/05-Ins-Complex-Data/Solved/ins-complex-data.ipynb)

* [ins-complex-data.ipynb (Unsolved)](Activities/05-Ins-Complex-Data/Unsolved/ins-complex-data.ipynb)

Explain to the students that sometimes, complex or unusual datasets might require alternative algorithms for clustering. In this demonstration, we'll introduce two: **BIRCH** and **agglomerative clustering**.

#### BIRCH

* **BIRCH** stands for **balanced iterative reducing and clustering using hierarchies**.

* It is an unsupervised data mining algorithm that is similar to but different from K-means.

* In particular, BIRCH uses **hierarchical clustering**. This approach may start out with many clusters, but then over the process of learning, combine these clusters until there is only the specified number left.

* BIRCH was originally created for extremely large datasets, and is still often used for this purpose. One of the reasons for this is that it tends to be relatively memory efficient.

* Just like K-means, scikit-learn makes it relatively straightforward to cluster data by using BIRCH.

Slack out the [documentation for BIRCH](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html) from scikit-learn for the students to refer to later.

#### Agglomerative Clustering

* Scikit-learn makes it possible to use other clustering routines too, such as another hierarchical clustering routine called **agglomerative clustering**.

Slack out the [scikit-learn documentation on agglomerative clustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering) as you explain the following.

* Agglomerative clustering is like BIRCH. Neither requires you to specify the appropriate cluster count `k`, unlike K-means. While you can specify a specific cluster count with these two approaches, they are flexible enough to divide the data into categories without much input from you.

* Sometimes there isn't a single, catch-all answer when deciding to use one clustering routine over another. Instead, data scientists often have to try multiple algorithms to find out which one appears to work best on their specific data.

Use this piece of advice to segue into the code demonstration, where we’ll try out all three clustering methods on a single dataset and preview the resulting labels.

#### Compare and Contrast Alternative Clustering Algorithms

First, create a new notebook and copy-paste the required imports:

```python
import numpy as np
np.random.seed(0)
import pandas as pd
import hvplot.pandas
from sklearn import datasets
```

Explain that we’ll now create a dataset to visualise clustering and classification algorithms. Specifically, `make_moons` will create a complex, crescent-shaped dataset with two columns and 500 data points.

```python
# Create a simulated dataset for illustration
X, y = datasets.make_moons(n_samples=(500), noise=0.05, random_state=1)
# Preview the numpy array
X[0:10]
```

Import the three algorithms and then cluster the data by using `KMeans`.

```python
from sklearn.cluster import KMeans, AgglomerativeClustering, Birch
k_model = KMeans(n_clusters=3, random_state=0)
k_model.fit(X)
predictions = k_model.predict(X)
```

Explain that the next lines of code are new: these are the lines necessary to cluster using `Birch` and `AgglomerativeClustering`. This code should appear similar to the previous code for `KMeans`; the main difference is that here we specify `Birch`.

```python
birch_model = Birch(n_clusters=2)
birch_model.fit(X)
birch_predictions = birch_model.predict(X)
```

* `AgglomerativeClustering` is only slightly different: rather than using `fit` and then `predict`, we combine both into one line:

```python
agglo_model = AgglomerativeClustering(n_clusters=3)
agglo_predictions = agglo_model.fit_predict(X)
```

* It helps to plot labels against various columns which we used to cluster. It assists in telling us which variables tend to influence whether an observation belongs in one cluster versus another.

* For example, we can plot the model predictions for `Birch`.

  * To do so, we create a `DataFrame` out of our underlying data (which is currently a `numpy` array).

  * Then, we add the `birch_predictions` as a column to this DataFrame.

```python
predictions_df = pd.DataFrame(X)
predictions_df['birch-labels'] = birch_predictions
predictions_df
```

Use `hv.plot` to create a scatter plot:

  ```python
  predictions_df.hvplot.scatter(x="0", y="1", by="birch-labels")
  ```

* The following image shows the scatter plot:

![A scatter plot shows two clusters of data points.](Images/birch-predictions.png)

* The plot shows that the algorithm is separating the two clusters of data on the basis of the values in the two feature columns. For example, red labels tend to have negative levels of the `0` column, but positive levels of the `1` column.

* Plotting cluster labels in this way can be helpful as it removes some of the mystery regarding  how clustering decides on labelling choice. It can help us quickly determine which features of the data tend to be concentrated in which clusters.

Point out to the students that so far, we specified `2` clusters for BIRCH, but this was just a default value, not based on any reason.

* Unlike K-means, BIRCHBirch doesn't have an `inertia` score we can save and keep track of to use the elbow method to determine the optimal number of clusters.

* Instead, we can use a different metric, or score, to keep track of how well a particular cluster count is describing our data. As it turns out, this metric can be used for all three of our algorithms for this purpose.

Slack out the scikit-learn documentation on [clustering performance evaluation](https://scikit-learn.org/stable/modules/clustering.html#clustering-performance-evaluation) as you explain the following.

* If we had actual labels of what we were trying to categorise, our job would be a little easier. If we were trying to cluster customers into customer groups beforehand—like "in-store shopper" versus "online-shopper", and had some historical data on customers and whether they shopped online or in-store, then we could use that data as a sort of "answer key" for our clustering algorithm. We could compare whether our clustering algorithm actually labeled these customers correctly as "in-store" or "online" customers.

* Here, and commonly in unsupervised learning, we don't have the "answer key" to which clustering algorithm is most accurate. Instead, we have various metrics to capture how similar observations are within each cluster, and how distinct each cluster is.

* There are many such metrics, sometimes called "scores," that we can use.

Introduce the students to one such score, the **Calinski-Harabasz Index**, also known as the [variance ratio criterion](https://scikit-learn.org/stable/modules/clustering.html#calinski-harabasz-index).

* This score will produce one number which tells us, for any given clustering model, how well our clusters are defined.

* Once this score is developed for a model, we can save it and use it to compare one version of the model versus another.

To demonstrate this idea, live code the following:

* First two `Birch` models are built and fit—one with 2 clusters, and another with 3:

```python
birch_model_two_clusters = Birch(n_clusters=2)
birch_model_two_clusters.fit(X)
birch_predictions_2 = birch_model_two_clusters.predict(X)

birch_model_three_clusters = Birch(n_clusters=3)
birch_model_three_clusters.fit(X)
birch_predictions_3 = birch_model_three_clusters.predict(X)
```

* Then the new code is introduced, which is the variance ratio criterion. This is called on each model.

  * Note that we are using the `labels_` attribute here, which gives us our predicted labels for the saved model. This gives the same result as the `predict` function we previously ran on each model (i.e., labels).

  * With the labels saved, we feed them and the underlying data into the `metrics.calinski_harabasz_score` function.

  * We then save and output the result:

```python
from sklearn import metrics
labels = birch_model_two_clusters.labels_
score = metrics.calinski_harabasz_score(X, labels)
score
```

```text
588.1123857523019
```

* In a new Jupyter cell, we do the same thing, this time for the model with 3 clusters:

```python
from sklearn import metrics
labels = birch_model_three_clusters.labels_
score = metrics.calinski_harabasz_score(X, labels)
score
```

```text
654.2904571777167
```

Reiterate to the students that for this particular metric, higher scores are better; they are indicative of better clustering of the data, or better distinction between the various cluster groups. As a result, it looks like 3 clusters are better than 2 when it comes to this data and classification with the BIRCH algorithm.

Answer any questions before moving on.

---

### 10. Student Do: Segmenting Customer Data (25 minutes)

In this activity, the students will use BIRCH, agglomerative clustering, and the K-Means model to segment a dataset on thousands of consumer credit card holders, courtesy of a [Kaggle](https://www.kaggle.com/) competition. They'll use the issuing bank's customer information to group these customers into the optimal number of clusters. In doing so, they'll also gain their first attempt in comparing one machine learning algorithm over another.

**Files:**

* [segmenting_customer_data.ipynb (Unsolved)](Activities/06-Stu_Segmenting_Customers/Unsolved/segmenting_customer_data.ipynb)

* [customers.csv](Activities/06-Stu_Segmenting_Customers/Resources/customers.csv)

**Instructions:**

* [README.md](Activities/06-Stu_Segmenting_Customers/README.md)

---

### 11. Instructor Do: Review Segmenting Customer Data (15 minutes)

**Files:**

* [segmenting_customer_data.ipynb (Unsolved)](Activities/06-Stu_Segmenting_Customers/Unsolved/segmenting_customer_data.ipynb)

* [segmenting_customer_data - Solved.ipynb](Activities/06-Stu_Segmenting_Customers/Solved/segmenting_customer_data.ipynb)

* [customers.csv](Activities/06-Stu_Segmenting_Customers/Resources/customers.csv)

Open the unsolved version of the provided Jupyter notebooks, live code the solution, and highlight the following:

* Companies worldwide are using the potential of communities like Kaggle to solve critical problems thanks to the collaboration of multidisciplinary and global teams like the ones that participate in Kaggle.

* Regardless of whether you are participating in a Kaggle contest or working as a consultant in the fintech industry, providing preprocessed and anonymised data is a common practice to share real-world data while protecting  privacy. This is the type of scenario that we want to provide you with for this activity.

* In Part 1, we load the data into a Pandas DataFrame.

  ```python
  # Set the file path
  file_path = Path("../Resources/customers.csv")

  # Read the CSV file into a Pandas DataFrame
  customers_df = pd.read_csv(file_path)

  # Review the DataFrame
  customers_df.head()
  ```

The following screenshot shows the DataFrame:

  ![A screenshot shows the first five rows of the customer DataFrame.](Images/customer-data-sample.png)

* Note that the data contains 10 features labelled as `feature_1` to `feature_10`. For companies that share data in this way, there is a feature mapping each anonymous column. As a fintech professional, you will add a meaningful value to the data by applying machine learning and results from interpretation.

* After loading the data, it's always helpful to check for null values and corroborate the data type of each column. To do so, we use the Pandas `info` function.

  ```python
  customers_df.info()
  ```

  ```text
  <class 'pandas.core.frame.DataFrame'>
  RangeIndex: 1000 entries, 0 to 999
  Data columns (total 10 columns):
  #   Column      Non-Null Count  Dtype
  ---  ------      --------------  -----
  0   feature_1   1000 non-null   float64
  1   feature_2   1000 non-null   float64
  2   feature_3   1000 non-null   float64
  3   feature_4   1000 non-null   float64
  4   feature_5   1000 non-null   float64
  5   feature_6   1000 non-null   float64
  6   feature_7   1000 non-null   float64
  7   feature_8   1000 non-null   float64
  8   feature_9   1000 non-null   float64
  9   feature_10  1000 non-null   float64
  dtypes: float64(10)
  memory usage: 78.2 KB
  ```

* Thanks to the `info` Pandas function, we can see that there are no null values, and all columns were correctly loaded as numerical values.

* Next, we compute the summary statistics by using the Pandas `describe` function.

  ```python
  customers_df.describe()
  ```

The following screenshot shows the updated DataFrame:

  ![A screenshot shows the DataFrame that now includes statistics for each of the 10 features.](Images/customers_summary_stats.png)

* In Part 2, we find the optimal number of clusters for this dataset by using the elbow method.

* We start by importing the `KMeans` module from the scikit-learn library and setting the initial configurations for the `for` loop that we will use to compute the data to plot the elbow curve.

  ```python
  # Import the KMeans module from SKLearn
  from sklearn.cluster import KMeans

  # Create a list to store inertia values and the values of k
  inertia = []

  # Create a list to set the range of k values to test
  k = list(range(1, 11))
  ```

* Next, we define a `for` loop to iterate from 1 to 11 and compute the data to plot the elbow curve.

  ```python
  for i in k:
      k_model = KMeans(n_clusters=i, random_state=0)
      k_model.fit(customers_df)
      inertia.append(k_model.inertia_)
  ```

* After finishing the loop, we create a Pandas DataFrame, and we plot the elbow curve by using hvPlot.

  ```python
  # Define a DataFrame to hold the values for k and the corresponding inertia
  elbow_data = {"k": k, "inertia": inertia}
  df_elbow = pd.DataFrame(elbow_data)

  # Plot the DataFrame to identify the optimal value for k
  df_elbow.hvplot.line(
      x="k",
      y="inertia",
      title="Elbow Curve",
      xticks=k
  )
  ```

The following image shows the elbow curve:

  ![A line plot shows the relationship between inertia and number of clusters.](Images/customers_elbow_curve.png)

* After inspecting the elbow curve, we can observe that the optimal number of clusters for this dataset seems to be 3.

* This means that we can infer that the bank which shares this data can split their clients into three customer segments for marketing purposes.

* In Part 3, we use `k=3` to fit a K-Means model and assign a cluster to each data point in the dataset.

  ```python
  # Define the model with optimal number of clusters
  model = KMeans(n_clusters=3, random_state=0)

  # Fit the model
  model.fit(customers_df)

  # Make predictions
  kmeans_predictions = model.predict(customers_df)
  ```

* In Part 4, we can do clustering again, this time using the `Birch` and `AgglomerativeClustering` algorithms.

* First, we fit `AgglomerativeClustering`, and save its predictions. Note that predicting and fitting with `AgglomerativeClustering` is slightly different, as it combines both steps into one line of code:

```python
agglo_model = AgglomerativeClustering(n_clusters=3)
agglo_predictions = agglo_model.fit_predict(customers_df)
```

* After that, we fit a `Birch` clustering routine, and predict clusters with that. Again, we'll use three clusters.

```python
# Fit a Birch Model
birch_model = Birch(n_clusters=3)
birch_model.fit(customers_df)
# Make predictions with the Birch model
birch_predictions = birch_model.predict(customers_df)
# Previewing the predicted customer classifications for BIRCH
birch_predictions[-10:]
```

Finally, in Part 5, we graphically compare the results from each of these clustering algorithms.

* First, we create a DataFrame which is a copy of the original `customers_df` data.

* Then, we add the `kmeans_predictions`, `agglo_predictions`, and `birch_predictions` as columns to the DataFrame.

```python
# Create a copy of the customers_df DataFrame
customers_predictions_df = customers_df.copy()
# Add class columns with the labels to the new DataFrame
customers_predictions_df["kmeans-segments"] = kmeans_predictions
customers_predictions_df["agglomerative-segments"] = agglo_predictions
customers_predictions_df["birch-segments"] = birch_predictions
customers_predictions_df[['kmeans-segments','agglomerative-segments', 'birch-segments']].head(3)
```

* Next, we can use hvPlot to visualise these clusters by creating a scatter plot, using the `feature_1` and `feature_2` columns and colouring the data points by setting `by="customer_segments"`. To facilitate comparison, we'll do this for each of the three algorithms, as shown in the following code:

```python
customers_predictions_df.hvplot.scatter(
    x="feature_1",
    y="feature_2",
    by="kmeans-segments"
)

customers_predictions_df.hvplot.scatter(
    x="feature_1",
    y="feature_2",
    by="agglomerative-segments"
)

customers_predictions_df.hvplot.scatter(
    x="feature_1",
    y="feature_2",
    by="birch-segments"
)
  ```

Here’s the scatter plot:

  ![A scatterplot shows the relationship between feature_2 vs. feature_1 and three clusters.](Images/customer_segments_plot.png)

* The result for one of the plots (K-means) is shown above. Although we don't know the meaning of each feature, we can observe that the data is fairly accurately split into three clusters.

* For the most part, each of the three algorithms appear to be dividing clusters similarly on the basis of these two features we're plotting.

Explain to students that while it's often difficult to articulate why a particular observation fits in one cluster or another. Plotting cluster labels against various features in this way helps us to identify more qualitatively the way groups are forming.

* For instance, a distinct cluster (labelled as `2`) is found for all three algorithms, in which observations in this cluster tend to have high values of `feature_2` and simultaneously low values of `feature_1`.

* This data on customers has been anonymised and standardised, but if we had the original variable names, we might be able to communicate with non-technical members of the bank about why, intuitively, our algorithm is categorising a customer with a particular label.

Answer any questions before moving on.

> **Note:** If you are pressed for time, you can skip the optional challenge.

Remind the students that the optional challenge was to loop through each clustering algorithm, using an alternative metric to determine the optimal number of clusters.

* This `for` loop is similar to the one we created by using the elbow method to select the optimal number of clusters for the K-means approach. This time, however, we'll use a metric that can be applied to the other algorithms as well. Specifically, we’ll use the Calinski-Harabasz index (variance ratio criterion).

Go through the steps:

* First, we preview the `labels_` from one of the algorithms, just to see what we're working with.

  * Note that the predictions and the `labels_` have the same values here. `labels_` gives us the same data that we have in our predictions DataFrames. (There is a distinction that has to do with in-sample and out-of-sample usage, which isa topic we'll cover in the upcoming unit on supervised learning.)

```python
# Preview the predictions for one of the algorithms
birch_predictions[0:10]

# Equivalently, preview the labels_ attribute for one of the algorithms
birch_model.labels_[0:10]
```

* Because we're estimating scores for each of the algorithms, we'll create three lists.

  * Note: Some students may have used a dictionary or a DataFrame to hold this information, which is an equally valid approach.

* As with the elbow method, we also need a list, `k`, which contains the cluster counts that we'll loop through.

```python
# Create a list to store values and the values of k
score_kmeans = []
score_agglomerative = []
score_birch = []

# Create a list to set the range of k values to test
k = list(range(2, 11))
```

* Finally, we have the content in the loop itself. The code for each algorithm, separated by paragraph spacing here, is mostly similar. The difference is mainly which list we save to.

  * Specifically, for each model, we fit it, each iteration selecting a different cluster count (`i`). We then calculate the variance ratio for each algorithm, given that specified cluster count.

```python
from sklearn import metrics

for i in k:
    k_model = KMeans(n_clusters=i, random_state=0)
    k_model.fit(customers_df)
    labels = k_model.labels_
    score = metrics.calinski_harabasz_score(customers_df, labels)
    score_kmeans.append(score)

    agglo_model = AgglomerativeClustering(n_clusters=i)
    agglo_predictions = agglo_model.fit_predict(customers_df)
    labels = agglo_model.labels_
    score = metrics.calinski_harabasz_score(customers_df, labels)
    score_agglomerative.append(score)

    birch_model = Birch(n_clusters=i)
    birch_model.fit(customers_df)
    labels = birch_model.labels_
    score = metrics.calinski_harabasz_score(customers_df, labels)
    score_birch.append(score)

```

* Finally, we make the comparison. There are fancier ways of doing this, but outputting the content of these lists is probably the quickest approach:

```python
display(score_kmeans)
display(score_agglomerative)
display(score_birch)
```

* Based on each of the three lists, the highest value for each of the three algorithms appears to be at the two-cluster count. Based on this metric, two clusters would actually be sufficient to classify these customers, regardless of which of these three algorithms were used.

  * Note that this is different from the `3` clusters we obtained by the elbow method. This is a common feature of machine learning—there is rarely any clear-cut answer, as different models or approaches will often give slightly different results.

  * For that reason, it often pays to try many different approaches, and triangulate on the best combination of parameters and models.

Explain to the students that we'll learn some special tools to combine predictions from different machine learning models soon, when we start our unit on supervised learning.

Answer any questions before ending class.

—

## End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
