## 10.3: Principal Component Analysis (PCA)

### Overview

In this lesson, the students will learn how to use principal component analysis (PCA) to reduce the number of features in their machine learning models and improve model performance.

Clustering algorithms like K-means often suffer from the “curse of dimensionality,” which means there are far too many features that can be made sense of in a single model. We can often fix this and improve the efficiency of our clustering by applying PCA to identify the most important features for prediction.

### Class Objectives

By the end of this lesson, the students will be able to:

* Explain PCA and how it can be used to reduce dimensionality in data.

* Conceptualize how PCA relates to K-means and other applications in machine learning.

* Use PCA to reduce the number of features in an unsupervised learning setting.

---

### Instructor Notes

* Whenever possible, include real-world examples in your lectures to make concepts more concrete and relatable for students. Feel free to draw upon your own experience optimising machine learning models in the professional world.

* Help build the students’ confidence and engagement by being encouraging and by reminding them that anyone who uses machine learning has started where the students are right now. You can also promote effective problem-solving skills by letting the students explain concepts if they feel comfortable.

* As you review the activities, find ways to connect the concepts to fintech. Include brief discussions about emerging or disruptive/innovative technologies, and how they have changed the fintech landscape.

* Have your TAs keep track of the time with the [Time Tracker](TimeTracker.xlsx).

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 10.3 Slides](https://docs.google.com/presentation/d/1b33UPWAzscHhuUPZOnc44mAq7evwRHjmaoD7Fx_oIdI/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome the Class (5 minutes)

Welcome the students, and explain that today’s lesson will explore principal component analysis, or PCA, which will advance their skills in unsupervised learning. PCA was briefly mentioned in the previous lesson in the context of normalisation and scaling. In this lesson, the students will learn how to apply PCA.

Explain that as they learn PCA, they will also get more practice in deploying clustering algorithms for the purpose of unsupervised learning.

Answer any questions before introducing the warm-up activity, which is a refresher on the topics covered so far in this module.

---

### 2. Student Do: Warm-Up (20 minutes)

**Corresponding Activity:** [01-Warm_Up](Activities/01-Warm_Up/)

In this activity, the students will use the K-means algorithm to segment global currency and interest rate data. The students will evaluate the data by standardising and then segmenting the data into three clusters.

**Files:**

* [global_carry_trades.ipynb (Unsolved)](Activities/01-Warm_Up/Unsolved/global_carry_trades.ipynb)

* [global_carry_trades.csv](Activities/01-Warm_Up/Resources/global_carry_trades.csv)

---

### 3. Instructor Do: Review Warm-Up (15 minutes)

**Corresponding Activity:** [01-Warm_Up](Activities/01-Warm_Up/)

Review the solution to the activity, either by live coding or by presenting the solution file that is linked below. This activity was a refresher on concepts the students already learned, so use your judgment when it comes to pacing. Be sure to address any questions that arise, as many of the activities in this lesson build on the code from this warm-up.

**Files:**

* [global_carry_trades.ipynb (Solved)](Activities/01-Warm_Up/Solved/global_carry_trades.ipynb)

* [global_carry_trades.csv](Activities/01-Warm_Up/Resources/global_carry_trades.csv)

Go through each step of the solution.

#### Step 1

Read in the `global_carry_trades.csv` file from the `Resources` folder and create and review the DataFrame. Note that this step was done for the students in the starter code.

```python
# Read the CSV file into a Pandas DataFrame
# Set the index using the Ticker column
rate_df = pd.read_csv(
    Path("../Resources/global_carry_trades.csv"))

# Review the DataFrame
rate_df.head()
```

#### Step 2

To prepare the data, we use the `StandardScaler` module and the `fit_transform` function to scale all the columns containing numerical values. We then review a five-row sample of the scaled data using bracket notation ([0:5]).

```python
# Use the StandardScaler module and fit_transform function to
# scale all columns with numerical values
rate_df_scaled = StandardScaler().fit_transform(rate_df[["interest_differential" , "next_month_currency_return"]])

# Display the first three rows of the scaled data
rate_df_scaled[0:3]
```

#### Step 3

Step 3 consists of a few sub-steps.

* First, we create a new DataFrame called `rate_df_scaled` that contains the scaled data, using the same labels that were referenced in the `StandardScaler` for the column names.

```python
# Create a DataFrame called with the scaled data
# The column names should match those referenced in the StandardScaler step
rate_df_scaled = pd.DataFrame(
    rate_df_scaled,
    columns=["interest_differential" , "next_month_currency_return"])
rate_df_scaled
```

* Then, we use `pd.get_dummies` on the "IMF Country Code" column on the original `rate_df` DataFrame. These binary variables get saved as a DataFrame called `country_dummies`.

>**Note:** "IMF" stands for International Monetary Fund. This organisation does many things (like lending money to developing countries), but they also were the first to create a standardised three- digit classification code for each country.

```python
# Encode (convert to dummy variables) the "IMF Country Code" column
country_dummies = pd.get_dummies(rate_df['IMF Country Code'])

# Review the DataFrame
country_dummies.head()
```

* We then combine the two, using `pd.concat` to add the `country_dummies` DataFrame to the `rate_df_scaled` DataFrame.

Show the students the combined DataFrame so that they can observe the scaled data and encoded categorical variables (i.e., the country `str` codes).

```python
# Concatenate the `EnergyType` encoded dummies with the scaled data DataFrame
rate_df_scaled = pd.concat([rate_df_scaled, country_dummies], axis=1)

# Display the combined DataFrame.
rate_df_scaled.head()
```

Show the following image of the combined DataFrame:

![A screenshot shows the combined DataFrame containing columns for each country code.](Images/rate_df_preview.png)

#### Step 4

Now, we fit the model and cluster the data by using K-means.

* Using the concatenated DataFrame, we cluster the country-level data by using the K-means algorithm and a `k` value of 3.

* We then save the predicted model clusters to a new DataFrame.

```python
# Initialize the K-Means model with n_clusters=3
model = KMeans(n_clusters=3)

# Fit the model for the rate_df_scaled DataFrame
model.fit(rate_df_scaled)

# Save the predicted model clusters to a new DataFrame.
country_clusters = model.predict(rate_df_scaled)

# View the country clusters
print(country_clusters)
```

* Then, we create a copy of the `rate_df_scaled` DataFrame, saving it to a new DataFrame called `rate_scaled_predictions`.

* We then add the predicted `country_clusters` to this new DataFrame, then preview its content.

```python
# Create a copy of the concatenated DataFrame
rate_scaled_predictions = rate_df_scaled.copy()

# Create a new column in the copy of the concatenated DataFrame with the predicted clusters
rate_scaled_predictions["CountryCluster"] = country_clusters

# Review the DataFrame
rate_scaled_predictions.head()
```

The following image shows the combined DataFrame:

![scaled-predictions.png](Images/scaled-predictions.png)

#### Step 5

Now we plot and analyse the results.

* Group the saved DataFrame by cluster, using `groupby` to calculate the average `next_month_currency_return` by cluster.

* This tells us which group had the highest monthly currency returns.

```python
# Group the saved DataFrame by cluster using `groupby` to calculate average currency returns
rate_scaled_predictions.groupby(by=['CountryCluster'])['next_month_currency_return'].mean()
```

```text
CountryCluster
0    0.628660
1   -1.134452
2   -0.242211
Name: next_month_currency_return, dtype: float64
```

* The output indicates that cluster `0` has the highest average currency return, which is 0.62% per month.

* Another way to visualise this output is to use `hvplot` to create a scatter plot of `interest_differential` versus `next_month_currency_return`, and make the plot vary by `CountryCluster`. This is shown in the following code:

```python
rate_scaled_predictions.hvplot.scatter(
    x="interest_differential",
    y="next_month_currency_return",
    by="CountryCluster"
)
```

The following image shows the scatter plot:

![A scatterplot that shows the three clusters of the countries, labelled by colour.](images/country-clusters.png)

* Based on this plot, the `0` cluster of countries appears to provide not only the highest currency return, but also the highest interest spread.

#### Optional Challenge

Briefly go through the optional challenge solutions, highlighting the differences and similarities among them. (Note that depending on the algorithm and cluster count selected, the students' results may differ from what is shown in the solution file).

* The code in the solution file uses BIRCH with `k=5`:

```python
# Initialize a Birch model with n_clusters=5
birch_model = Birch(n_clusters=5)

# Fit the model for the df_bitcoin_scaled DataFrame
birch_model.fit(rate_df_scaled)

# Predict the model segments (clusters)
country_clusters = birch_model.predict(rate_df_scaled)

# View the stock segments
print(country_clusters)

# Create a copy of the concatenated DataFrame
rate_scaled_predictions = rate_df_scaled.copy()

# Create a new column in the copy of the concatenated DataFrame with the predicted clusters
rate_scaled_predictions["CountryCluster"] = country_clusters

# Review the DataFrame
rate_scaled_predictions.head()
```

* Finally, we plot these new predicted clusters, based on this alternative algorithm.

```python
rate_scaled_predictions.hvplot.scatter(
    x="interest_differential",
    y="next_month_currency_return",
    by="CountryCluster"
)
```

* Here, the `2` cluster displays the highest interest spread and next month's currency return.

Ask if there are any questions before moving on.

### 4. Instructor Do: Introduction to PCA (30 min)

**Files:**

* [pca.ipynb (Solved)](Activities/02-Ins_PCA/Solved/pca.ipynb)

* [pca.ipynb (Unsolved)](Activities/02-Ins_PCA/Unsolved/pca.ipynb)

In this activity, the students will review how to use PCA to reduce the number of features of a dataset, while still retaining most of the useful information in those features.

Play this [video](https://experiments.withgoogle.com/visualizing-high-dimensional-space
) for the students and slack out the link. This video shows a visualisation of high-dimensional data from researchers at Google and Illustrates some of the complexity inherent in machine learning datasets.

After playing the video, highlight the following points to the students:

* Some of these datasets displayed are very large, with thousands (or more!) columns.

* For some machine learning algorithms, this high dimensionality can become a problem.

* What if we could reduce the size of the dataset, while preserving as much useful information as possible?

* There’s an algorithm for this that is used often in machine learning: principal component analysis, or PCA.

* PCA works because all data has variability; variation contains useful information.

* By keeping only the most common variation across the dataset, we can reduce the size of our dataset, but still maintain a variety of useful features.

Slack out the [scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html) documentation on PCA, as you open the provided unsolved Jupyter notebook.

First, refer to the plot for the K-means segmentation of the credit card information.

```python
# Plot the clusters using the "limit_bal" and "age" columns
ccinfo_default_df.hvplot.scatter(
    x="limit_bal",
    y="age",
    by="customer_segments"
)
```

Show the following plot of the segmented data:

![A scatter plot depicts the relationship between age vs. limit_bal, divided into three clusters.](Images/ccinfo-segmented.png)

Point out how clearly segmented these groups are, at least when we look at age.

* Although the segments plot well for the "age," we can observe a different result if we choose different features.

Plot the clusters by using the "bill_amt" and "pay_amt" columns, and highlight the following:

```python
# Plot the clusters using the "bill_amt" and "pay_amt" columns
ccinfo_default_df.hvplot.scatter(
    x="bill_amt",
    y="pay_amt",
    by="customer_segments"
)
```

Show the following plot of pay_amt vs. bill_amt, which depicts the segmented data.

![A screenshot shows a plot of clusters.](Images/custumers_ugly_segments.png)

* But using a different combination of columns, the segments are not nearly as clear.

* That does not necessarily indicate a problem with the K-means algorithm, but rather that there were too many factors that influenced the outcome to plot only two dimensions and get an accurate representation. If we were able to plot in five dimensions, we might have a chance.

* As fintech professionals, you will most likely deal with datasets that have multiple columns, or factors, of data that influence the outcome of your analysis. Too many of these features could slow down the analysis or skew the results.

* PCA is a statistical technique that is used to streamline the machine learning process when too many factors exist in the data. "Too many" could be 5, like we just experienced, or 10, 100, or even 1000, depending on the dataset.

* PCA reduces the number of factors by transforming a large set of features into a smaller one that contains MOST of the information of the original, larger dataset.

* PCA is a dimensional-reduction method that looks at all of the dimensions (or data columns) in a dataset, which:

  * Analyzes the weight of their contribution to the variance in the dataset.

  * Reduces variables to a smaller set of dimensions that still contains as much of the information, or the maximum variance, of the original dataset as possible.

* Reducing the number of factors (dimensional reduction) comes at the expense of some accuracy, but the goal is to trade a little accuracy for simplicity.

* A reduced number of variables is easier to visualise in a plot, which is a primary goal of unsupervised machine learning, K-means, and segmentation.

Reiterate to the students that the goal of PCA is simple: reduce the number of factors in a dataset while preserving as much of the information from the original dataset as possible.

Next, go through the process of applying the PCA technique to the credit card information dataset.

Start by highlighting that the data must be transformed before we can apply the PCA technique to a dataset. For this demonstration, we will use the transformed version of the credit card info dataset.

Highlight the following:

* Once the PCA module has been imported from scikit-learn, the next step is to instantiate the PCA module and declare the number of principal components that will be used.

* Principal components are like new columns of data: each principal component will be a single column.

* Think of this like zipping or compressing a bunch of files into one file or folder. We still have essentially the same data, but compressed into a single file, instead of many.

  ```python
  # Import the PCA module
  from sklearn.decomposition import PCA

  # Instantiate the PCA instance and declare the number of PCA variables
  pca = PCA(n_components=2)
  ```

* Two components are often used because this works well with a 2D visualisation, such as plots with x- and y-axes.

* The next step is to fit the PCA model on the transformed credit card info DataFrame by using the `fit_transform` function. This is when all the factors from the original dataset are reduced to the number of factors set in the model. This process is called **dimensional reduction**.

```python
# Fit the PCA model on the transformed credit card DataFrame
ccinfo_pca = pca.fit_transform(ccinfo_default_df)
```

Review the result of the PCA technique with the students as you explain the following:

* The output is an array of a list of lists. Each nested list consists of two values.

* As the PCA output is a `list` of lists, you must use the index notation to view it.

* The combination of all these values is the distillation of all the factors from the model reduced to two principal components.

```python
# Review the first 5 rows of list data
ccinfo_pca[:5]
```

```text
array([[-11.4106317 ,  -1.19426208],
      [ -9.424725  ,  -0.75732157],
      [ -1.33620686,  -0.69534399],
      [  1.67884463,  -0.76676318],
      [ 21.58943237,  -0.9373152 ]])
```

Explain to the students that by using the information from the array and a function from the PCA module called `explained_variance_ratio_`, it is possible to determine exactly how much of the total variance from the original factors is captured by the two PCA components.

```python
# Calculate the PCA explained variance ratio
pca.explained_variance_ratio_
```

Show the variance ratio for our credit card data and highlight the following:

```text
array([0.95017303, 0.01898131])
```

* The total explained variance, or the amount of variance that the PCA technique captured, is the sum of these two numbers: 0.96915 or 96.9%.

* Nearly all of the total variance from the original dataset is captured by just these two PCA variables. In this case, the accuracy seems to be decent, with only 3.1% of the total variance in the original dataset given up for the sake of simplicity.

* The next step in the process involves converting the PCA data, which is an array, into a DataFrame so that it can be analysed by using the elbow method and K-means.

  ```python
  # Create the PCA DataFrame
  ccinfo_pca_df = pd.DataFrame(
      ccinfo_pca,
      columns=["PCA1", "PCA2"]
  )

  # Review the PCA DataFrame
  ccinfo_pca_df.head()
  ```

* The resulting DataFrame contains two columns, with each row being one of the nested lists from the array.

Here is an image of the resulting DataFrame:

  ![A screenshot shows the updated DataFrame.](Images/pca-dataframe.png)

Ask the students the following question:

* **Question:** Now that we have a Pandas DataFrame, if the goal is customer segmentation using K-means, what is the next step in the process?

  **Sample answer:** Because we are not entirely sure of k, the next step in the process is using the elbow method to determine the value for k.

The next steps should be familiar to the students.

* Use the elbow method and the `ccinfo_pca_df` DataFrame to determine the optimal value for k. Ask a student to volunteer the code for each of the steps in the elbow method.

```python
# Create a list to store inertia values and the values of k
inertia = []
k = list(range(1, 11))

# Append the value of the computed inertia from the `inertia_` attribute of the KMeans model instance
for i in k:
    k_model = KMeans(n_clusters=i, random_state=1)
    k_model.fit(ccinfo_pca_df)
    inertia.append(k_model.inertia_)

# Define a DataFrame to hold the values for k and the corresponding inertia
elbow_data = {"k": k, "inertia": inertia}
df_elbow = pd.DataFrame(elbow_data)

# Review the DataFrame
df_elbow.head()

# Plot the elbow curve
df_elbow.hvplot.line(
    x="k",
    y="inertia",
    title="Elbow Curve",
    xticks=k
)
```

Show the resulting plot, which once again identifies 3 as the optimal value for k:

![A line plot of the elbow curve, which changes slope at 3 clusters.](Images/pca-elbow-curve.png)

Explain that, with the optimal value for k as 3, the next step is coding the K-means.

```python
# Define the model with 3 clusters
model = KMeans(n_clusters=3, random_state=0)

# Fit the model
model.fit(ccinfo_pca_df)

# Make predictions
k_3 = model.predict(ccinfo_pca_df)

# Create a copy of the PCA DataFrame
ccinfo_pca_predictions_df = ccinfo_pca_df.copy()

# Add a class column with the labels
ccinfo_pca_predictions_df["customer_segments"] = k_3

# Plot the clusters
ccinfo_pca_predictions_df.hvplot.scatter(
    x="PCA1",
    y="PCA2",
    by="customer_segments"
)
```

Point out that the results of the data segmentation for the credit card information is much cleaner with only two dimensions, PCA1 and PCA, as the following image illustrates:

![A scatterplot of PCA2 vs. PCA1, with the points divided into three clusters.](Images/pca-segmentation-plot.png)

Explain that reducing the original dataset into only two factors was more easily visualised on a two-dimensional plot. As a result, the three customer segments were more easily visualized.

Before moving forward, ask the students if they have any questions about PCA or how it helps to simplify customer segmentation, and the resulting visualisations.

---

### 5. Student Do: Segmenting with PCA (25 min)

In this activity, the students will use their knowledge of PCA to reduce the dimensionality of the customers DataFrame they used before, and then compare that result to the segmentation of the data by using all of the factors.

**Files:**

* [segmenting_with_pca.ipynb](Activities/03-Stu_Segmenting_with_PCA/Unsolved/segmenting_with_pca.ipynb)

* [customers.csv](Activities/03-Stu_Segmenting_with_PCA/Resources/customers.csv)

**Instructions:**

* [README.md](Activities/03-Stu_Segmenting_with_PCA/README.md)

The PCA technique for dimensional reduction has just come to your attention. At this point, you have already segmented the data based on all of the factors, but are wondering if PCA would alter the segmentation results.

Using the [starter code](Activities/03-Stu_Segmenting_with_PCA/Unsolved/segmenting_with_pca.ipynb) and the customer data provided, do the following:

* Reduce the factors to only two dimensions by using PCA.

* Determine the optimal value for k by using the PCA DataFrame.

* Segment the data by using the K-means algorithm and the optimal value for k.

* Segment the preprocessed customer DataFrame by using the K-means algorithm and that same value for k.

* Compare the segmentation results.

---

### 6. Instructor Do: Review Segmenting with PCA (20 minutes)

**File:** [segmenting_with_pca.ipynb](Activities/03-Stu_Segmenting_with_PCA/Solved/segmenting_with_pca.ipynb)

The focus of this review should be on the steps required for the creation of the PCA DataFrame, as well as the advantages and disadvantages of using PCA. For this dataset, it turns out that the PCA segmentation is as good as the segmentation from the full-factored DataFrame.

First, briefly review the DataFrame that was imported for the activity. Confirm that this is the DataFrame that the students used before, and highlight the following:

![A screenshot shows the first five rows of a DataFrame with values for each of 10 features.](Images/customer-data-sample.png)

* After the PCA module is imported, the first step (as always in the model-fit-predict workflow) is to instantiate the model.

* Note that this is the stage where the number of PCA variables is declared.

  ```python
  # Import the PCA module
  from sklearn.decomposition import PCA

  # # Instantiate the PCA instance and declare the number of PCA variables
  pca = PCA(n_components=2)
  ```

* The next step is to fit the model by using the `fit_transform` function.

* Note that reviewing the data requires the use of index syntax. Here we are looking to see the first five rows of data—index positions 0–4.

  ```python
  # Fit the PCA model on the transformed credit card DataFrame
  customers_pca = pca.fit_transform(customers_transformed_df)

  # Review the first 5 rows of the array of list data
  customers_pca[:5]
  ```

* With our PCA variables created, we want to review the percentage of the total variance that is captured by the two PCA variables.

  ```python
  # Calculate the PCA explained variance ratio
  pca.explained_variance_ratio_
  ```

  ```text
  array([0.55083554, 0.30256389])
  ```

* In this case, the first PCA variable accounts for 0.55%, and the second 0.30%, for a total explained variance of 85%.

* The final step in the first part of this activity involves creating the PCA DataFrame, which is needed to be able to continue our segmentation analysis using the elbow method and K-means.

  ```python
  # Create the PCA DataFrame
  customers_pca_df = pd.DataFrame(
      customers_pca,
      columns=["PCA1", "PCA2"]
  )

  # Review the PCA DataFrame
  customers_pca_df.head()
  ```

* The following image shows the PCA DataFrame:

  ![A screenshot shows the first 5 rows of a DataFrame that includes a column for PCA1 and a column for PCA2.](Images/customers-pca-dataframe.png)

The following steps can be covered in as much detail as you feel the students require.

* As before, the elbow method is used to determine the optimal value for k given the PCA DataFrame.

  ```python
  # Create a list to store inertia values and the values of k
  inertia = []
  k = list(range(1, 11))

  # Create a for loop where each value of k is evaluated using the K-means algorithm
  # Fit the model using the service_ratings DataFrame
  # Append the value of the computed inertia from the `inertia_` attribute of the KMeans model instance
  for i in k:
      k_model = KMeans(n_clusters=i, random_state=1)
      k_model.fit(customers_pca_df)
      inertia.append(k_model.inertia_)

  # Define a DataFrame to hold the values for k and the corresponding inertia
  elbow_data = {"k": k, "inertia": inertia}

  # Create the DataFrame from the elbow data
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

* Once again, the optimal value for k is 3, as indicated by the following image, which shows the plotted elbow curve.

  ![A line plot of the elbow curve, which changes slope at 3 clusters.](Images/customers-pca-elbow-curve.png)

* With this information, the data can be segmented using the K-means algorithm.

  ```python
  # Define the model Kmeans model using the optimal value of k for the number of clusters.
  model = KMeans(n_clusters=3, random_state=0)

  # Fit the model
  model.fit(customers_pca_df)

  # Make predictions
  k_3 = model.predict(customers_pca_df)

  # Create a copy of the customers_pca_df DataFrame
  customer_pca_predictions_df = customers_pca_df.copy()

  # Add a class column with the labels
  customer_pca_predictions_df["customer_segments"] = k_3

  # Plot the clusters
  customer_pca_predictions_df.hvplot.scatter(
      x="PCA1",
      y="PCA2",
      by="customer_segments"
  )
  ```

* The result of segmenting the data with K-means shows three clear customer segments, as shown in the following image.

  ![A scatterplot of PCA2 vs. PCA1 with three clusters of points labelled by colour.](Images/customers-pca-segmentation.png)

* Finally, we compare the segmentation results between the PCA DataFrame and the full-factored DataFrame.

  ```python
  # Define the model Kmeans model using k=3 clusters
  model = KMeans(n_clusters=3, random_state=0)

  # Fit the model
  model.fit(customers_transformed_df)

  # Make predictions
  k_3 = model.predict(customers_transformed_df)

  # Create a copy of the customers_transformed_df DataFrame
  customers_transformed_predictions_df = customers_transformed_df.copy()

  # Add a class column with the labels
  customers_transformed_predictions_df["customer_segments"] = k_3

  # Plot the clusters using the age and spending columns
  customers_transformed_predictions_df.hvplot.scatter(
      x="feature_1",
      y="feature_2",
      by="customer_segments"
  )
  ```

Show the following plot of the three customer segments:

  ![A plot shows the three customer segments.](Images/customers-full-factored-segmentation.png)

* After comparing the results between the PCA DataFrame and the DataFrame with the original data, we can see that we get similar results in terms of clearly identifying three customer clusters.

* That means that by using two features, we can reach a decent segmentation that becomes cheaper in terms of computational resources, and it's faster to predict the outcome because we only require two features instead of one.

Ask if there are any questions before moving on.

---

### 7. Break (40 minutes)

---

### 8. Student Do: Energize Your Stock Clustering (30 minutes)

In this activity, the students will solidify their ability to reduce the number of features in your model by using PCA. They will cluster both standardised and principal components into various clustering algorithms and compare the results. By the end of this activity, the students should have a solid understanding of PCA and how to conduct PCA for the purpose of machine learning.

**Files:**

* [energize_your_stock_clustering.ipynb (Unsolved)](Activities/04-Stu-Energize_Your_Stock_Clustering/Unsolved/energize_your_stock_clustering.ipynb)

* [tsx-energy-2018.csv](Activities/04-Stu-Energize_Your_Stock_Clustering/Resources/tsx-energy-2018.csv)

**Instructions:**

* [README.md](Activities/04-Stu-Energize_Your_Stock_Clustering/README.md)

---

### 9. Instructor Do: Review Energize Your Stock Clustering (20 minutes)

In this section, review the previous activity with the class.

**Files:**

* [energize_your_stock_clustering.ipynb (Solved)](Activities/04-Stu-Energize_Your_Stock_Clustering/Solved/)

* [tsx-energy-2018.csv](Activities/04-Stu-Energize_Your_Stock_Clustering/Resources/tsx-energy-2018.csv)

Steps 1 and 2 will have already been completed for the students in the starter code. Feel free to review these first two steps briefly with the students.

```python
# Import the required libraries and dependencies
import pandas as pd
import hvplot.pandas
from path import Path
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
```

Go through each step of the activity and the solution.

#### Step 1

Read in the `tsx-energy-2018.csv` file from the `Resources` folder and create the DataFrame. Make sure to set the Ticker column as the DataFrame’s index. Then review the DataFrame.

  ```python
  # Read the CSV file into a Pandas DataFrame
  # Set the index using the Ticker column
  df_stocks = pd.read_csv(
      Path("../Resources/tsx-energy-2018.csv"),
      index_col="Ticker"
  )

  # Review the DataFrame
  df_stocks.head()
  ```

#### Step 2

Review the four code cells that are included in this step in the notebook. These cells contain the code that scales the `df_stocks` DataFrame and creates a new DataFrame that contains the scaled data.

```python
  # Scale price data, return, and variance values
stock_data_scaled = StandardScaler().fit_transform(
    df_stocks[["MeanOpen", "MeanHigh", "MeanLow", "MeanClose", "MeanVolume", "AnnualReturn", "AnnualVariance"]]
)

# Create a DataFrame with the scaled data
df_stocks_scaled = pd.DataFrame(
    stock_data_scaled,
    columns=["MeanOpen", "MeanHigh", "MeanLow", "MeanClose", "MeanVolume", "AnnualReturn", "AnnualVariance"]
)

# Copy the tickers names from the original data
df_stocks_scaled["Ticker"] = df_stocks.index

# Set the Ticker column as index
df_stocks_scaled = df_stocks_scaled.set_index("Ticker")

# Display sample data
df_stocks_scaled.head()

# Encode (convert to dummy variables) the `EnergyType` column, which categorizes oil versus non-oil firms
oil_dummies = pd.get_dummies(df_stocks["EnergyType"])
oil_dummies.head()

# Concatenate the `EnergyType` encoded dummies with the scaled data DataFrame
df_stocks_scaled = pd.concat([df_stocks_scaled, oil_dummies], axis=1)

# Display the sample data
df_stocks_scaled.head()
```

#### Step 3

Using the `df_stocks_scaled` DataFrame, cluster the data by using the K-means algorithm and a lowercase-k value of 3. Add the resulting list of company segment values as a new column in the `df_stocks_scaled` DataFrame.

```python
# Initialize the K-Means model with n_clusters=3
model = KMeans(n_clusters=3)

# Fit the model for the df_stocks_scaled DataFrame
model.fit(df_stocks_scaled)

# Predict the model segments (clusters)
stock_clusters = model.predict(df_stocks_scaled)

# View the stock segments
print(stock_clusters)

# Create a new column in the DataFrame with the predicted clusters
df_stocks_scaled["StockCluster"] = stock_clusters

# Review the DataFrame
df_stocks_scaled.head()
```

#### Step 4

Using hvPlot, create a scatter plot to visualize the clusters, setting `x="AnnualVariance"`,  `y="Annual Return"`, and `by="StockCluster"`. Be sure to style and format your plot.

```python
# Create a scatter plot with x="AnnualVariance:,  y="AnnualReturn"
df_stocks_scaled.hvplot.scatter(
  x="AnnualVariance",
  y="AnnualReturn",
  by="StockCluster",
  hover_cols = ["Ticker"],
  title = "Scatter Plot by Stock Segment - k=3"
```

#### Step 5

To get another perspective on the clusters, reduce the number of features to two principal components by using PCA. Make sure to do the following:

* Use the `df_stocks_scaled` DataFrame to complete this analysis.

* Review the PCA data.

* Calculate the explained variance ratio that results from the PCA data.

Here’s the code:

```python
# Create the PCA model instance where n_components=2
pca = PCA(n_components=2)
# Fit the df_stocks_scaled data to the PCA
stocks_pca_data = pca.fit_transform(df_stocks_scaled)

# Review the first five rows of the PCA data
# using bracket notation ([0:5])
stocks_pca_data[:5]

# Calculate the explained variance
pca.explained_variance_ratio_
```

```text
array([0.64310452, 0.1572319 ])
```

* Based on the results, the first principal component explains 64% of the features data. The second component explains a further 15.7% of the data.

#### Step 6

Using the PCA data calculated in the previous step, create a new DataFrame called `df_stocks_pca`. Make sure to do the following:

* Add an additional column to the DataFrame that contains the tickers from the original `df_stocks` DataFrame.

* Set the new Tickers column as the index.

* Review the DataFrame.

Here’s the code:

  ```python
  # Creating a DataFrame with the PCA data
  df_stocks_pca = pd.DataFrame(stocks_pca_data, columns=["PC1", "PC2"])

  # Copy the tickers names from the original data
  df_stocks_pca["Ticker"] = df_stocks.index

  # Set the Ticker column as index
  df_stocks_pca = df_stocks_pca.set_index("Ticker")

  # Review the DataFrame
  df_stocks_pca.head()
  ```

#### Step 7

Rerun the K-means algorithm with the new principal-components data, and then create a scatter plot by using the two principal components for the x and y axes, and by using `StockCluster`. Be sure to style and format your plot.

```python
# Initialize the K-Means model with n_clusters=3
model = KMeans(n_clusters=3)

# Fit the model for the df_stocks_pca DataFrame
model.fit(df_stocks_pca)

# Predict the model segments (clusters)
stock_clusters = model.predict(df_stocks_pca)

# View the stock segments
print(stock_clusters)

# Create a copy of the df_stocks_pca DataFrame and name it as df_stocks_pca_predictions
df_stocks_pca_predictions = df_stocks_pca.copy()

# Create a new column in the DataFrame with the predicted clusters
df_stocks_pca_predictions["StockCluster"] = stock_clusters

# Review the DataFrame
df_stocks_pca_predictions.head()

# Create the scatter plot with x="PC1" and y="PC2"
df_stocks_pca_predictions.hvplot.scatter(
    x="PC1",
    y="PC2",
    by="StockCluster",
    title = "Scatter Plot by Stock Segment - PCA=2"
)
```

#### Optional Challenge

> **Note:** Only review this portion of the activity if you have enough time.

Go through each step:

* First, we create a list to hold the possible values of `k`.

```python
# Create a list with the number of k-values to try
# Use a range from 1 to 11
k = list(range(1, 11))
```

* We save a list to hold these inertia values which we'll calculate.

```python
# Create an empty list to store the inertia values
inertia = []
```

* Then, for each possible `k`, we fit clusters on the `PCA` data, saving the inertia values to the `inertia` list.

```python
# Create a for loop to compute the inertia with each possible value of k
# Inside the loop:
# 1. Create a KMeans model using the loop counter for the n_clusters
# 2. Fit the model to the data using `df_stocks_pca`
# 3. Append the model.inertia_ to the inertia list
for i in k:
    model = KMeans(n_clusters=i, random_state=0)
    model.fit(df_stocks_pca)
    inertia.append(model.inertia_)
```

* We then save the `k` number and its corresponding inertia to a newly assembled DataFrame:

```python
# Create a dictionary with the data to plot the Elbow curve
elbow_data_pca = {
    "k": k,
    "inertia": inertia
}

# Create a DataFrame with the data to plot the Elbow curve
df_elbow_pca = pd.DataFrame(elbow_data_pca)
```

* Plotting `k` against the inertia values, we construct the elbow plot:

```python
# Plot a line chart with all the inertia values computed with
# the different values of k to visually identify the optimal value for k.
elbow_plot_pca = df_elbow_pca.hvplot.line(x="k", y="inertia", title="Elbow Curve Using PCA Data", xticks=k)
elbow_plot_pca
```

* The following image shows the elbow plot:

![A line plot of the elbow curve, with a slope change between 2 and 3.](Images/elbow-curve-pca.png)

Ask the students the following questions. If no one responds, provide them with the answer.

* **Question:**What is the best value for k when using the PCA data? Does it differ from the best k value found using the original data?

  * **Answer:** Based on this elbow curve, it looks like `k=3` is still the correct one.

Answer any questions before moving on.

---

### 10. Instructor Do: Structured Review (35 minutes)

> **Note:** If you are teaching this lesson on a weeknight, please save this 35-minute review for the next Saturday class.

Please use the entire time to review questions with the students before officially ending class.

Here’s the suggested format:

* Ask the students if there are any specific activities they would like to revisit.

* Revisit key activities for the Challenge.

* Allow the students to start the Challenge assignment with extra TA support.

Take your time in this section! This is a great time to reinforce concepts and clear up misunderstanding.

---

## End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
