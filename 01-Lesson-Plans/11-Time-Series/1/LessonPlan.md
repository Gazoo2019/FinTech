## 11.1: Introduction to Time Series

### Overview

This class introduces the students to the basics of time series analytics. A time series comprises a sequence of data points that occur over a defined time period. Almost all financial data is measured at discrete time points or intervals, so time series is an inherent component of fintech. Programmers incorporate time series data in creating machine learning models to make future predictions.

Most of these models are **supervised learning** models, and this week represents the students' first practical introduction to supervised learning methods. To develop proficiency in using time series data, the students will complete exploratory data analysis and build machine learning models to predict time series events.

### Class Objectives

By the end of this class, the students will be able to:

* Recognize the importance of time data in the financial industry.

* Manipulate time series data by using Pandas.

* Use exploratory data analysis techniques on time series data.

* Identify time series patterns in stock market data by using advanced slicing techniques and time pattern identification methods.

* Use heatmaps to identify relationships within time series data.

---

### Instructor Notes

* This class eases the students into the subject matter by providing them with the skills to work with time series data in Pandas and introducing fundamental concepts for Days 2 and 3.

* Be sure to emphasise the role of machine learning in time series analysis and **advanced analytics** (the application of advanced statistical models and intelligent algorithms).

* This class focuses on the mechanics and code of time series data, including `datetime` data and time series slicing. Be sure that the students have a solid understanding of the content before moving to the next activity or demonstration. This will build their confidence and prepare them for the rest of the module, where they will gain more practice with applying machine learning models to time series data.

* In this module, the students will learn how to both analyse time series data and automate time series forecasting by using [Prophet](https://facebook.github.io/prophet/), a tool created by Facebook. Prophet's machine learning algorithms can quickly automate and complete an analysis that previously took financial professionals hours to work through.

* Slack out the following links, and encourage the students to review them as well as search for additional resources outside of class:

  * [What Is Time Series Forecasting?](https://machinelearningmastery.com/time-series-forecasting)

  * [7 Exciting Uses of Machine Learning in FinTech](https://rubygarage.org/blog/machine-learning-in-fintech)

  * [Predictive Analytics for FinTech](https://www.prnewswire.com/news-releases/predictive-analytics-for-fintech-an-increasingly-necessary-tool-to-stay-competitive-says-frere-enterprises-300757420.html)

  * [How Machines Learn](https://www.youtube.com/watch?v=R9OHn5ZF4Uo&start=0&end=72)

  * [A.I. Experiments: Visualizing High-Dimensional Space](https://www.youtube.com/watch?v=wvsE8jm1GzE)

Encourage the students to review the [Student Guide](../Supplemental/StudentGuide.md), which contains helpful information and frequently asked questions about this unit.

### Class Slides and Time Tracker

You can review the slides for this lesson on Google Drive at [11.1 Slides](https://docs.google.com/presentation/d/132QsQ4KuVzIBucvcSo0R0kHtvSSlzxOFpFw636c05eo/edit?usp=sharing).

To add the slides to the student-facing repository, download the slides as a PDF by selecting "Download" on the File menu, and then clicking "PDF document (.pdf)." Then add the PDF file to your class repository along with the other necessary files. You can review the instructions for this in the [Sharing Slides with Students](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing) document.

**Note:** Editing access is not available for this slide deck. If you want to modify the slides, create a copy by clicking "Make a copy" on the File menu.

You can review the time tracker for this lesson at [Time Tracker.xlsx](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome, Machine Learning Recap, and Time Series Introduction (10 minutes)

Welcome the students to Module 11, and congratulate them on reaching this week of the boot camp! Explain that in this module, they’ll learn how they can use a new type of machine learning tool, supervised learning on time series data, to boost their financial analysis skills.

Begin with a recap of machine learning.

#### Machine Learning Recap

Open the lesson slides, and ask the students to recall what they know about machine learning. Their responses should cover the following points:

* **Machine learning** is a programming approach for designing applications that learn from their inputs and make adjustments based on their outputs.

* A machine learning algorithm automatically adapts (automatic configuration) to improve the accuracy and precision of outcomes and predictions, so we don't need to configure inputs and manually make changes to the algorithm.

* Because machine learning algorithms can learn on their own, developers don’t need to worry about coding for every scenario.

* To summarise, we use machine learning when we develop a statistical or algorithmic model of existing data that can automatically make predictions or decisions about new data.

Explain to the students that all machine learning pipelines follow a **Model-Fit-Predict** paradigm, where we use a dataset or data model to fit, or train, the algorithm. Once the algorithm has been trained, we can use the model and the algorithm to make actual predictions.

Point out that machine learning has two main approaches: supervised learning and unsupervised learning.

* We have already covered **unsupervised learning**, which is when an intelligent algorithm learns as it goes, without having observed any type of data before. The algorithm will identify all the data points, cluster them, make predictions, and then improve its predictions over time.

  * Unsupervised learning includes dimensionality reduction and **clustering** (finding groups within a population).

* The approach we will encounter this week is **supervised learning**, where we feed data to the algorithm so it can learn and make predictions based on the data.

  * Categories of supervised learning include **classification** (classifying outcomes as classes, or groups) and **regression** (fitting data to predict where a new data point lies), both of which are used for making predictions. With **supervised learning**, we need to know the potential outcomes from the beginning.

To create some excitement about machine learning, play the following video clip on algorithms for business decision making:

* [How Machines Learn](https://www.youtube.com/watch?v=R9OHn5ZF4Uo)

  **Note:** Play only until the 1:11 mark.

Point out to the students the following machine learning examples that were mentioned in the video.

* An algorithm decides what price you are willing to pay at a particular moment.

* An algorithm predicts which financial transactions are fraudulent.

* Algorithms continuously trade against other algorithms in the stock market.

All these examples involve two things:

* The concept of time is an important element to decision making.

  * Your willingness to pay for something might depend on the time of day (late-night shopping) or year (holiday season).

  * Specific financial transactions that happen very late at night or very early in the morning have a greater chance of being fraudulent.

  * Profitable strategies might appear and disappear depending on market conditions that change constantly.

* For a machine learning model to make predictions about all these outcomes, such as when a particular stock trade would be profitable, it requires plenty of historical data on both good and bad outcomes. To make good decisions, a model has to have many examples to learn from.

* Many practical applications for machine learning models in finance involve **supervised learning** of **time series data**. Assure the students that each of these concepts will be explored in more detail over the next several weeks.

#### Introduction to Time Series Data

Start this section by discussing the relevance of time in our lives. Reinforce how our lives are based on the results of decisions that we make at specific times.

Illustrate how time is relevant by discussing the following example.

* Time might lead us to buy warm clothes in the winter or search for the perfect vacation spot in the summer. Have you ever noticed these kinds of patterns in your life?

* Time impacts not only our behaviour but also how the financial world works. For example, when you make an investment or deposit money in your savings account, the value of the money can increase over time.

* Time is so important in finance that we need to learn how to manipulate, analyse, and understand data that’s measured over time. This type of data is called **time series data**.

Explain that, in this class, the students will learn the details of manipulating time series data with Python and Pandas. They will learn to use these tools' advanced capabilities for analysing and working with data in multiple formats from different sources. With these skills, students can build more sophisticated time series models, including ones that can make predictions across different time scales, such as days, weeks, and years, or time zones.

---

### 2. Instructor Do: Challenge Demo (10 minutes)

In this activity, you’ll review the Challenge assignment instructions. Provide time for the students to ask questions about the assignment.

**Files:**

* [Challenge instructions](../../../02-Homework/11-Time-Series/Instructions/README.md)

Open the Challenge instructions, then go through the steps while emphasising the following points:

* Advanced analytics is becoming very popular in the fintech industry. It offers developers and companies a way to analyse thousands of large datasets and to use computer predictions that drive investments and decision making.

* These large datasets typically contain data that involves a time series. A **time series** consists of a specific set of discrete and consecutive time values over a defined time span.

* In this module’s Challenge assignment, you will assume the role of a growth analyst for [Mercado Libre](https://investor.mercadolibre.com/), the most popular e-commerce site in Latin America. They will create a model for a time series analysis of the site's user traffic, and analyse financial and user data to help grow the company.

* The assignment requires the students to:

  * Identify unusual patterns in time series data by using Pandas and other tools.

  * Mine the data for patterns in seasonality by using the hvPlot visualisation tool.

  * Build sales-forecast and user-interest predictive models for the firm by using Facebook Prophet. The students will learn about Prophet in the second day of Module 11.

Answer any questions before moving on.

---

### 3. Instructor Do: The Importance of Time in Finance (15 minutes)

**Corresponding Activity:** [01-Ins_Time_in_Finance](Activities/01-Ins_Time_in_Finance)

**Files:**

* [importing-sp500-data.ipynb (solved)](Activities/01-Ins_Time_in_Finance/Solved/importing-sp500-data.ipynb)

* [importing-sp500-data.ipynb (unsolved)](Activities/01-Ins_Time_in_Finance/Unsolved/importing-sp500-data.ipynb)

* [sp500.csv](Activities/01-Ins_Time_in_Finance/Resources/sp500.csv)

In this section, you’ll explain the importance of time and time data in the financial industry. You'll also demonstrate how to use Pandas to work with `datetime` objects.

#### Aspects of Time Data

Highlight the following details about time data.

* Time plays a role in almost every financial analysis task. Some examples include:

  * Discovering the closing prices on various stock exchanges around the globe.

  * Aggregating the daily revenue for a firm that has sales in different countries or regions.

  * Forecasting cryptocurrency prices.

* To model and predict future events in time, we need proficiency in handling everything that relates to time data. Because financial markets stay active all around the world and at all hours of the day, we need the ability to convert time zones.

* To recognise patterns in time data, we need the ability to resample our data, converting hourly data to daily data or daily data to weekly data.

* In this lesson, we will learn how to complete these tasks.

#### Using Pandas to Work with Time Data

Explain to the students that you’ll demonstrate how they can use Pandas to manipulate time data. Open the unsolved version of the provided Jupyter notebook, and highlight the following information.

* The concept of dates and times in a programming language can be complicated. This is especially true when we consider the globe with its various time zones and levels of granularity.

* These levels range from daily data to data measured at the microsecond. Also, many ways exist to format and store dates and times on computers.

* As you learned in earlier units, Python and Pandas supply functions that help us work with dates and times in a DataFrame. These functions use `datetime` objects, which will also make it easier to work with time series models.

* In today's lesson, you’ll process and analyse time series data by using Python and Pandas.

A common example of time series data in the fintech space involves the stock market. We can measure the price of each stock at specific intervals throughout the trading day, such as every minute, hourly, or daily (which gives us the closing price).

In this demo, we'll analyse the [S&P 500](https://en.wikipedia.org/wiki/S%26P_500), which is the index of the top 500 public stocks in the United States.

Start live-coding the demo, and highlight the following points.

* First, we read the time series data from a CSV file into a DataFrame by using Pandas, as the following code shows:

  ```python
  # Read the S&P 500 CSV data into a DataFrame
  df_sp500 = pd.read_csv(
      Path("../Resources/sp500.csv")
  )

  # Display the DataFrame
  df_sp500.head()
  ```

  The following image shows the head of the DataFrame:

  ![A screenshot depicts the head of the S&P 500 DataFrame, which has “time” and “close” columns.](Images/11-1-load-sp500-data.png)

* We can examine the data types of the data that we just read by using `dtypes`, as the following code shows:

  ```python
  # Verify the data types using dtypes
  df_sp500.dtypes
  ```

  The following image shows the data types:

  ![A screenshot depicts that the “time” column is of type object and that the “close” column is of type float64.](Images/11-1-data-types-checking.png)

* You might have noticed that the “time” column is of type `object`. But why is that? When we read data from a CSV file that contains time data, the `pd.read_csv` function will read the date and time values contained in the “time” column as generic strings.

* Because we want to do complex calculations with our date and time information, we need to convert it.

Explain to the students that fintech professionals often encounter business scenarios that have a global impact. Data can come from different countries or regions and have different formats, so we need the ability to work with the different formats of dates and times.

Python has many types of data structures for storing time data. Highlight the following points.

* Python considers dates and times to have the following elements:

  * The date, which includes the year, month, and day

  * The time, which includes the hour, minute, and second

  * The time zone

* A `date` object stores the year, month, and day. A `time` object stores the hour, minute, second and, sometimes, the time zone.

* A `datetime` object stores both a `date` object and a `time` object. The `datetime` format is the most common one students will work with. The following code block shows one of these objects in our data:

  ```python
  # Review the time value from index position 0
  df_sp500["time"][0]
  ```

  ```text
  '2019-01-02 12:45:00+00:00'
  ```

Ask the students the following question.

* **Question:** Based on the "time" value of the first entry in the DataFrame, is the value formatted as a `date`, a `time`, or a `datetime`?

  * **Possible Answer:** The value has a `datetime` format. The reason is that the value has the year, month, day, and time. And, the time includes the hour, minute, second, and time zone.

* We can observe that our `datetime` value above contains all the date and time information. The year, month, and day are clear. Then, we have the hour, minute, and second. Finally, the value has a plus sign (`+`) followed by `00:00`. This final part refers to the time zone.

#### What Is Coordinated Universal Time?

* Coordinated Universal Time (UTC—the acronym switches the T and the C) is a time standard that anyone in the world can use to specify an exact moment in time, regardless of the location.

* UTC doesn’t adjust for daylight savings time, which is what [differentiates it from Greenwich Mean Time (GMT)](https://www.timeanddate.com/time/gmt-utc-time.html).

* Whenever a timestamp includes a plus sign (+) or a minus sign (-), the number after the sign indicates the number of hours that we need to add or subtract from UTC to get the correct time zone.

  * Common time zones for stock data include `-05:00` for New York in standard time and `-04:00` for New York in daylight savings time. Note that the UTC time standard also matches London's time zone at `+00:00`.

* The Time Zone Database contains the time zone codes that Python and other programming languages use. This database is an international collaboration project that the Internet Assigned Numbers Authority (IANA) supports. The database is updated to reflect changes that governments make to time zone boundaries, UTC offsets, and daylight savings rules.

Encourage the students to learn more about the Time Zone Database and how it’s managed. Slack out the links to the IANA [Time Zone Database](https://www.iana.org/time-zones) page and the [list of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) from Wikipedia.

#### Using Pandas for datetime Objects

* With Pandas, we can use `datetime` objects to perform mathematical and other programming operations on dates and times. For example, we can get today's date (and the current time) by running the following code:

```python
# Get the current date and time
pd.to_datetime("today")
```

```text
Timestamp('2021-11-04 19:08:45.534840')
```

Explain that calling the Pandas `to_datetime` function and passing it a parameter of “today” returns an object called `Timestamp`, which contains the following parts.

* The `date` and `time` information of the user’s current date in the form of year-month-day

* The time in the format of hours-minutes-seconds-milliseconds

Highlight the fact that `Timestamp` is the Pandas equivalent of the Python `datetime` object. It’s used for entries that make up the Pandas `DatetimeIndex` and other time-oriented data structures. Slack out the link to the [Timestamp documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Timestamp.html) for further reference.

* This Pandas function is convenient when we want to use an API to pull financial market data that ranges from a particular time in the past to today.

#### Using the Time-Related Functions

Now that students understand the format of a time series, you can demonstrate using the `pd.to_datetime` function to convert the “time” column of our S&P 500 data to a `datetime` Series. Continue the demo, and highlight the following points:

* When we use the `pd.to_datetime` function to convert a data column into a `Timestamp` object, we can use various time-related functions, such as `pd.date_range`, which allows us to generate dates that span a specific period.

* The following code shows how to convert our “time” column into a `datetime` object:

  ```python
  # Transform the time column to a datetime data type
  df_sp500["time"] = pd.to_datetime(
      df_sp500["time"],
      infer_datetime_format =True,
      utc = True
  )

  # Verify the data type transformation using the info function
  df_sp500.info()
  ```

  ```text
  <class 'pandas.core.frame.DataFrame'>
  RangeIndex: 9328 entries, 0 to 9327
  Data columns (total 2 columns):
  #   Column  Non-Null Count  Dtype
  ---  ------  --------------  -----
  0   time    9328 non-null   datetime64[ns, UTC]
  1   close   9328 non-null   float64
  dtypes: datetime64[ns, UTC](1), float64(1)
  memory usage: 145.9 KB
  ```

* The preceding code calls the `pd.to_datetime` function, which accepts three parameters.

  * The DataFrame column that we want to convert.

  * The `infer_datetime_format` parameter.  Just like the `read_csv` function, this parameter tells Pandas whether to guess the format of the time data.

  * The `utc` parameter. Here, we set `utc = True`, because we know that the time zone in our data has the UTC format.

* After running this code, we can observe in the output that the time series has the `datetime64[ns, UTC]` data type! The `64` in the `datetime` name might seem mysterious, but it just relates to the way that the data is stored (that is, in a 64-bit format).

* By transforming the “time” column in our S&P 500 DataFrame, every value in this series now has the `datetime` data type, giving us access to all the native features of `datetime`. For example, we can perform arithmetic operations on dates. We can also use the convenient Pandas time series functions, such as querying data by using date ranges.

Explain to the students that they will gain practical experience with these Python tools throughout the module. Encourage the class to read the [datetime module documentation](https://docs.python.org/3/library/datetime.html#datetime.datetime) and the [Time series / date functionality](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html) article in the Pandas User Guide. Slack out these links for future reference.

#### Converting UTC Data to a Specific Time Zone

Continue the demo and explain that one of the largest stock markets is based in New York’s Eastern Time zone. So, we'll need to convert our time series to that time zone. Highlight the following points as you go through the code.

* Because the “time” column in our DataFrame already has a `datetime` format, we can use the Pandas `dt.tz_convert` function to convert the series to the `US/Eastern` time zone, as the following code shows:

  ```python
  # Convert the time column to the US/Eastern timezone
  df_sp500["time"] = df_sp500["time"].dt.tz_convert("US/Eastern")

  # Verify the data type transformation using the info function
  df_sp500.info()
  ```

  ```text
  <class 'pandas.core.frame.DataFrame'>
  RangeIndex: 9328 entries, 0 to 9327
  Data columns (total 2 columns):
  #   Column  Non-Null Count  Dtype
  ---  ------  --------------  -----
  0   time    9328 non-null   datetime64[ns, US/Eastern]
  1   close   9328 non-null   float64
  dtypes: datetime64[ns, US/Eastern](1), float64(1)
  memory usage: 145.9 KB
  ```

* In the preceding output, notice that the format of the “time” column in our `datetime` data now uses the `US/Eastern` time zone.

* For example, when we display sample data by using the Pandas `head` function, the time portion in each of the first five entries of this column has changed from `12:45:00+00:00` to `07:45:00-05:00`, as the following code shows:

  ```python
  # Review the DataFrame with the new timezone information
  df_sp500.head()
  ```

  The following image shows the head of the DataFrame:

  ![A screenshot depicts the head of the DataFrame.](Images/11-1-verifying-new-timezone.png)

Explain to the students that financial markets commonly trade in different time zones. To compare assets across these markets, we need to convert from one time zone to another. We also need to ensure that users see the correct time zone for their location.

* In general, we need to convert time zones whenever we aggregate data from multiple geographical locations.

Transition to the student activity by explaining that now it's time to put this new knowledge into action! In the next activity, the students will practice reading some data, reviewing its time zone, and converting it to another time zone.

Answer any questions before moving on.

---

### 4. Student Do: Inspecting Time Zones in Stock Data (20 minutes)

**Corresponding Activity:** [02-Stu_Inspecting_Time_Zones](Activities/02-Stu_Inspecting_Time_Zones)

**Files:**

* [Instructions](Activities/02-Stu_Inspecting_Time_Zones/README.md)

* [inspecting_time_zones_in_stock_data.ipynb](Activities/02-Stu_Inspecting_Time_Zones/Unsolved/inspecting_time_zones_in_stock_data.ipynb)

* [tsla_historical.csv](Activities/02-Stu_Inspecting_Time_Zones/Resources/tsla_historical.csv)

In this activity, the students will load historical stock data about Tesla Motors (TSLA) to practice their `datetime` data transformation skills.

---

### 5. Instructor Do: Review Inspecting Time Zones in Stock Data (10 minutes)

**Files:**

* [Instructions](Activities/02-Stu_Inspecting_Time_Zones/README.md)

* [inspecting_time_zones_in_stock_data.ipynb (unsolved)](Activities/02-Stu_Inspecting_Time_Zones/Unsolved/inspecting_time_zones_in_stock_data.ipynb)

* [inspecting_time_zones_in_stock_data.ipynb (solved)](Activities/02-Stu_Inspecting_Time_Zones/Solved/inspecting_time_zones_in_stock_data.ipynb)

* [tsla_historical.csv](Activities/02-Stu_Inspecting_Time_Zones/Resources/tsla_historical.csv)

Open the unsolved version of the Jupyter notebook, and then live-code the solution while covering the following points.

* We start by importing the required libraries, Pandas and Path, as the following code shows:

  ```python
  # Import the required libraries and dependencies.
  import pandas as pd
  from path import Path
  ```

* Next, we use the `read_csv` function from Pandas to read the provided data:

  ```python
  # Read the data from the tsla_historical.csv file into a Pandas DataFrame
  df_tsla = pd.read_csv(
      Path("../Resources/tsla_historical.csv")
  )
  ```

* We use the `head` function to inspect a sample of the data, and then use the Pandas `info` function to check the data types of each column, as the following code shows:

  ```python
  # Display the first five rows of the DataFrame
  df_tsla.head()

  # Inspect the DataFrame's data types using the info function
  df_tsla.info()
  ```

  The following image shows both a sample of the data and the data types in the DataFrame:

  ![A screenshot depicts the TSLA data.](Images/11-1-tsla-data-sample.png)

* Notice that the data type of the “time” column is `object` because this column has been imported as plain text and not as a `datetime` object. So, we can use the Pandas `to_datetime` function to convert this column to the `datetime` data type, as the following code shows:

  ```python
  # Transform the time column to a datetime data type
  df_tsla["time"] = pd.to_datetime(
      df_tsla["time"],
      infer_datetime_format = True,
      utc = True
  )
  ```

* We set the `infer_datetime_format` to `True`, which allows Pandas to manage this column as a `datetime` object. Because the “time” column contains UTC timestamp data, we also set `utc = True`.

* Now, we'll use the Pandas `head` and `info` functions to verify the data type transformation and the time zone, as the following code shows:

  ```python
  # Display the first five rows of the DataFrame to confirm
  # changes to the time column
  df_tsla.head()

  # Use the info function to confirm the change in data type
  # for the time column
  df_tsla.info()
  ```

  The following image shows a sample of the “time” column transformed into a `datetime` object:

  ![A screenshot depicts both a sample of the “time” column and the data types of the columns.](Images/11-1-tsla-data-sample-trasformed.png)

* The data in the “time” column now has changed to have a data type of `datetime`. We can start using this column to perform data operations, like changing the time zone.

* Next, we can use the Pandas `dt.tz_convert` function to convert the time zone to that of Berlin, as the following code shows:

  ```python
  # Convert the time column to the Europe/Berlin timezone
  df_tsla["time"] = df_tsla["time"].dt.tz_convert("Europe/Berlin")
  ```

* Pandas `head` and `info` functions let us verify the time zone transformation:

  ```python
  # View the first five rows of the DataFrame to confirm the
  # conversion of the time column
  df_tsla.head()

  # Use the info function to confirm the change in the time zone
  # associated with the time column
  df_tsla.info()
  ```

  The following image shows a sample of the “time” column transformed into `datetime` objects:

  ![A screenshot depicts both a sample of the “time” column and the data types of the columns.](Images/11-1-tsla-berlin-tz.png)

Now that the students can convert time series to the `datetime` format, they are ready to learn how to take data conversion a step further.

Point out that the next part of the lesson contains more strategies for dealing with `datetime` data. These include **index slicing**, which means getting a subset of elements at a higher frequency (for example, at minutes instead of days), and declaring different `DatetimeIndex` types. Both strategies will allow students to perform more-complex analyses.

Answer any questions before moving on.

---

### 6. Instructor Do: Analyzing Market Data Across Time (15 min)

**Corresponding Activity:** [03-Ins_Analyzing_Market_Data](Activities/03-Ins_Analyzing_Market_Data)

**Files:**

* [analyzing-market-data-across-time.ipynb (solved)](Activities/03-Ins_Analyzing_Market_Data/Solved/analyzing-market-data-across-time.ipynb)

* [analyzing-market-data-across-time.ipynb (unsolved)](Activities/03-Ins_Analyzing_Market_Data/Unsolved/analyzing-market-data-across-time.ipynb)

* [sp500.csv](Activities/03-Ins_Analyzing_Market_Data/Resources/sp500.csv)

In this activity, the students will learn how to analyse data across time by using advanced slicing techniques and time pattern identification.

Explain to the students that you’ll demonstrate Pandas slicing functionality to analyse date data and search for specific days, months, minutes, or hours within a DataFrame.

Note that this demo also uses the S&P 500. Open the unsolved version of the provided Jupyter notebook, and then live-code the demo while highlighting the following information.

* First, review how to set a `DatetimeIndex`. Once we load the data, setting a `DatetimeIndex` resembles setting a regular index. We use the Pandas `set_index` function and pass it the column name as a parameter, as the following code shows.

  ```python
  # Set the time column as DataFrame index
  df_sp500 = df_sp500.set_index("time")

  # Display the DataFrame
  df_sp500.head()
  ```

  The following image shows the DataFrame with the “time” column as the `DatetimeIndex`:

  ![A screenshot points out the “time” column as the DatetimeIndex.](Images/11-1-create-datetimeindex.png)

* Now, we can start using our new `DatetimeIndex` to analyse the data across time with Pandas slicing features.

Remind the students that they've learned how to create subsets, or selections, of data in a DataFrame by referencing the index together with the Pandas `loc` or `iloc` function. Slack out the [Indexing and selecting data](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html) article in the Pandas documentation so the students can review creating subsets of data by using Pandas.

#### Stock Market Patterns

Now, the students will learn how to select data by using the `DatetimeIndex` for different hours of the day. This will let us identify patterns in the stock market. Highlight the following points:

* We'll slice data by the hour to visualise trends that occur over different hourly periods. Visualising time series data can be a powerful first step toward identifying patterns.

* In addition to using the querying feature of the `loc` function for`DatetimeIndex`, we can also query the individual date and time components. Examples include the `year`, `month`, `day`, and `quarter`. The following code shows how we access these properties:

  ```python
  # Query individual date and time components
  print(df_sp500.index.year)
  print(df_sp500.index.month)
  print(df_sp500.index.quarter)
  ```

  ```text
  Int64Index([2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019,
              ...
              2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019],
            dtype='int64', name='time', length=9328)
  Int64Index([ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1,
              ...
              12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
            dtype='int64', name='time', length=9328)
  Int64Index([1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              ...
              4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            dtype='int64', name='time', length=9328)
  ```

Slack out the [pandas.DatetimeIndex](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DatetimeIndex.html) documentation for future reference about these individual components.

* By querying a `DateTimeIndex`, we can identify the patterns in price movements that are associated with the different time periods of the stock market. We can then teach our time series models to incorporate them into their predictions.

* The more we understand the patterns in our data, the better we become at training and building models that involve this data.

* In the stock market, patterns of behaviour often result from everyday human activities and behaviours. Examples include going to lunch or feeling excited about the market opening or closing.

* These identifiable patterns in our data are known as **common intraday stock market patterns** and **time-of-day stock market patterns**.

* Some of the more common patterns include:

  * A surge in trading volume at the opening of the market at 9:30 a.m. Eastern Time

  * A spike in trading volume when the market closes its positions at lunchtime

  * A daily high or low price that’s tested around lunchtime

  * Increases in trading volume and the potential for price movement between 2:00–3:00 p.m. Eastern Time

  * A final push before the market closes, just before 4:00 p.m. Eastern Time

* Keeping these patterns in mind, let's try to find some of them in our S&P 500 data by visualising them with some plots!

##### Checking the Closing Prices

* We start by checking the closing prices across all our data, as the following code shows:

  ```python
  # Plot the close column to examine the trend for closing prices
  df_sp500['close'].plot(
      title="Historical S&P 500 Closing Prices",
      figsize=[20, 10]
  )
  ```

  The following image shows a plot of the S&P 500 closing prices:

  ![A screenshot depicts the plot.](Images/11-1-sp500-price-plot.png)

* Now, we can choose a date to analyse in more detail. Let’s choose `2019-06-06` because, as we’ll find out, this date demonstrates some of the common trading patterns that we mentioned earlier.

* Slicing times is just as easy as slicing dates. Pandas is flexible about how you reference this time data. So, we can use various levels of granularity—from years to specific seconds.

* Because we have already set the `DatetimeIndex`, we can use the `loc` function to choose the day that we want to analyse. We simply pass it a date or a `datetime`.

* In this case, we want to find out what happened on June 6, 2019. Let’s start by examining the first 20 rows of data from that day. The following code displays the first 20 rows:

  ```python
  # Pick a single date from the DataFrame
  # Display the first 20 rows
  df_sp500.loc["2019-06-06"].head(20)
  ```

  The following image shows the first 20 rows of data for June 6, 2019:

  ![A screenshot depicts the rows.](Images/11-1-single-day-slice.png)

* Notice that the code selected everything that happened from 7:00 a.m. to 11:45 a.m. Eastern Time. To find out what happened during the premarket trading from 7:00 a.m. to the market opening time of 9:30 a.m., we give Pandas a `datetime` range, as the following code shows:

  ```python
  # Picking specific times from a datetime range
  df_sp500.loc["2019-06-06 07:00:00":"2019-06-06 9:30:00"]
  ```

  The following image shows the data for 7:00 a.m. to 9:30 a.m. on June 6, 2019:

  ![A screenshot depicts the data.](Images/11-1-datetime-range-slice.png)

  **Note:** In U.S. stock exchanges, premarket hours allow for trading in most stocks before the official trading hours begin. Most premarket trading occurs between 7:00 a.m. and 9:30 a.m., but some trading can occur even earlier in the morning. After-hours trading, which occurs in the hours after the markets officially close, is also a possibility.

* Now that we have a `datetime` range of 7:00 a.m. to 9:30 a.m., we can use the same format to plot the closing prices at those times, as the following code shows:

  ```python
  # Plot pre-market hours trading (7:00 am - 9:30 am)
  df_sp500.loc["2019-06-06 07:00:00":"2019-06-06 9:30:00"]["close"].plot(figsize=[15,10])
  ```

  The following image shows a plot of the closing prices from 7:00 a.m. to 9:30 a.m. on June 6, 2019:

  ![A screenshot depicts the plot.](Images/11-1-datetime-range-plot.png)

* As you can observe, the S&P 500 traded down in the early hours. The price began to recover as the market formally opened at 9:30 a.m.

* Now, we'll examine the price action during the first 15 minutes after the market opened to find out if the upward trend continued. The code is as follows:

  ```python
  # Check prices during the first 15 minutes of trading
  df_sp500.loc["2019-06-06 09:30":"2019-06-06 09:45"]["close"].plot(figsize=[15,10])
  ```

  The following image shows a plot of the closing prices from 9:30 a.m. to 9:45 a.m. on June 6, 2019:

  ![A screenshot depicts the plot.](Images/11-1-fifteen-minutes-plot.png)

* With this small change in price, from just under 283.3 to just under 282.9, it appears that the price didn’t move dramatically, although it did trend downward.

* Next, let's check the closing prices during lunchtime:

  ```python
  # Check closing prices during lunch time
  df_sp500.loc["2019-06-06 11:00":"2019-06-06 12:00"]["close"].plot(figsize=[15,10])
  ```

  The following image shows a plot of the closing prices from 11:00 a.m. to 12:00 noon on June 6, 2019:

  ![A screenshot depicts the plot.](Images/11-1-sp500-price-lunch-time.png)

* Wow, it seems that everyone closed their positions and left!

* Between 11:15 a.m. and 11:30 a.m. in the Eastern Time zone, where the New York Stock Exchange is based, the U.S. market leaves for lunch, and London is closing its positions for the day. This can lead to changes in the trend for the price of the markets.

Explain to the students that slicing time data illustrates the advantage of occasionally zooming in on our data to identify trends.

* If we examined the entire dataset, we would have difficulty observing a lunchtime trend. But by zooming in to a specific time, smaller trends like this become more apparent.

* When we identify trends, we can incorporate them—big or small—into our time series models for better accuracy.

Point out that the daily market high or low is usually tested around lunchtime. In this case, the plot indicates that the market tested toward the high end.

#### Further Time Slicing with Pandas

Continue the demo, and explain to the students that you'll now check what happened with the prices a little more than an hour before the market closed, as the following code shows:

```python
# Check closing prices just a little over an hour before market close
df_sp500.loc['2019-06-06 14:00':'2019-06-06 14:45']["close"].plot(figsize=[15,10])
```

The following image depicts the plot of the closing prices from 2:00 p.m. to 2:45 p.m.:

![A screenshot depicts the plot.](Images/11-1-price-before-market-closes.png)

Highlight the following details:

* As the market close approached, things started to get exciting! Let's find out what happened in the last but seemingly longest 30 minutes of the market, as the following code shows:

  ```python
  # Check closing prices thirty minutes before market closes
  df_sp500.loc['2019-06-06 15:30':'2019-06-06 16:00']["close"].plot(figsize=[15,10])
  ```

  The following image depicts the plot of the closing prices from 3:30 p.m. to 4:00 p.m.:

  ![A screenshot depicts the plot.](Images/11-1-price-30min-before-market-closes.png)

* We notice that the S&P 500 had a good day overall, with a 4:00 p.m. close of 284.78 versus a 9:30 a.m. open of 283.29. But, the last 30 minutes of trading had a slight decrease.

* This provides yet another example of why Pandas can give us superpowers for data analysis. And, it now has a place in the students' tool kit.

* We can take any data that has time-related elements, tell Pandas its time data, start slicing, and then start analysing.

* As you practice applying real-world knowledge to their data, you will recognise how to use these techniques in different contexts.

* In this module’s Challenge, you will use time zone manipulation and slicing methods to perform a time series analysis on the data and to ultimately model and predict time series data.

Answer any questions before moving on.

---

### 7. Break (15 minutes)

---

### 8. Student Do: Visualizing Stock Data (20 minutes)

**Corresponding Activity:** [04-Stu_Visualizing_Stock_Data](Activities/04-Stu_Visualizing_Stock_Data)

**Files:**

* [Instructions](Activities/04-Stu_Visualizing_Stock_Data/README.md)

* [visualizing-stock-data.ipynb](Activities/04-Stu_Visualizing_Stock_Data/Unsolved/visualizing-stock-data.ipynb)

* [tsla_historical.csv](Activities/04-Stu_Visualizing_Stock_Data/Resources/tsla_historical.csv)

In this activity, the students will convert a date column to `datetime` and perform slicing functions on various dates.

---

### 9. Instructor Do: Review Visualizing Stock Data (10 minutes)

**Files:**

* [Instructions](Activities/04-Stu_Visualizing_Stock_Data/README.md)

* [visualizing-stock-data.ipynb (unsolved)](Activities/04-Stu_Visualizing_Stock_Data/Unsolved/visualizing-stock-data.ipynb)

* [visualizing-stock-data.ipynb (solved)](Activities/04-Stu_Visualizing_Stock_Data/Solved/visualizing-stock-data.ipynb)

* [tsla_historical.csv](Activities/04-Stu_Visualizing_Stock_Data/Resources/tsla_historical.csv)

Open the unsolved version of the provided Jupyter notebook. Live-code the solution while highlighting the following details:

* You were asked to use the same Tesla (TSLA) stock data from an earlier activity. So, the first section of this activity is a review.

* After the data preparation, we set the “time” column of the DataFrame as the index, as the following code shows:

  ```python
  # Set the time column as DataFrame index
  df_tsla = df_tsla.set_index("time")

  # Display the first five rows of the DataFrame
  df_tsla.head()
  ```

  The following image shows the first five rows of the DataFrame:

  ![A screenshot depicts the DataFrame.](Images/11-1-tsla-set-index.png)

* Next, we use the Pandas `plot` function to visualise the closing price of the TSLA stock:

  ```python
  # Plot the closing price of TSLA
  df_tsla["close"].plot(
      title="Historial TSLA Closing Prices",
      figsize=[20, 10]
  )
  ```

  The following image shows a line plot of the closing prices of the TSLA stock:

  ![A screenshot depicts the line plot.](Images/11-1-tsla-closing-price.png)

* You might notice that the stock price increased in 2020. We can examine 2020 more closely by using our slicing capabilities on the Pandas DataFrame.

* We can use either the Pandas `loc` function or the `index.year` attribute. Let's start creating the plot by using the `loc` function, as the following code shows:

  ```python
  # Select and plot the TSLA closing prices from 2020
  df_tsla.loc["2020"].plot()
  ```

  The following image shows a line plot of the closing prices of TSLA stock in 2020:

  ![A screenshot depicts the line plot.](Images/11-1-2020-tsla-price.png)

  * We can also use the `index.year` attribute. Notice that we create the same type of plot but use a different slicing approach, as the following code shows:

  ```python
  # Select and plot the TSLA closing prices from 2020 using DatetimeIndex attributes
  df_tsla.loc[df_tsla.index.year == 2020].plot()
  ```

  The following image shows a line plot of the closing prices of TSLA stock in 2020:

  ![A screenshot depicts the line plot.](Images/11-1-2020-tsla-price-bis.png)

* After more closely examining the TSLA stock price in 2020, we can observe that the price dropped between August and September. The following code shows how we can dig into that period by using the Pandas `loc` function:

  ```python
  # Select and plot the TSLA closing prices from August and September 2020
  df_tsla.loc["2020-08" : "2020-09"].plot()
  ```

  The following image shows a line plot of the closing prices of TSLA stock in August and September 2020:

  ![A screenshot depicts the line plot.](Images/11-1-tsla-price-aug-sep-2020.png)

* Finally, we can zoom in even further to analyze the TSLA closing prices from August 22 to September 5, when the price had its largest decrease (which is due to a stock split, 5:1 on August 31st 2020- see comment below). We'll use the `loc` function to plot a time slice at a daily level of detail, as the following code shows:

  ```python
  # Select and plot the TSLA closing prices from August 22 to September 5, 2020
  df_tsla.loc["2020-08-22" : "2020-09-05"].plot()
  ```

  The following image shows a line plot of the closing prices of TSLA stock from August 22 to September 5:

  ![A screenshot depicts the line plot.](Images/11-1-tsla-price-day-level.png)

Before pointing out to students that this large price decrease is related to a 5:1 Stock split, ask the group whether they can guess what might have caused this large price decline. Use this as an opportunity to remind them to be mindful of any data they are using and whether any outliers or unusual data points might be present. Finally, explain to them that we can avoid this issue by using adjusted close prices or conducting the stock split adjustemnts ourselves. 

Congratulate the students on sharpening their time series slicing skills by using Pandas. So far, today's class has refreshed and enhanced students' ability to work with `datetime` data. This is an essential skill because most financial data involves time series data.

Answer any questions before moving on.

---

### 10. Instructor Do: Exploring Time Series Data (20 minutes)

**Corresponding Activity:** [05-Ins_Exploring_Time_Series_Data](Activities/05-Ins_Exploring_Time_Series_Data)

**Files:**

* [exploring-time-series-data.ipynb (solved)](Activities/05-Ins_Exploring_Time_Series_Data/Solved/exploring-time-series-data.ipynb)

* [exploring-time-series-data.ipynb (unsolved)](Activities/05-Ins_Exploring_Time_Series_Data/Unsolved/exploring-time-series-data.ipynb)

* [national-home-sales.csv](Activities/05-Ins_Exploring_Time_Series_Data/Resources/national-home-sales.csv)

In this section, the students will learn how they can use Pandas to explore time series data for identifying seasonal patterns.

Explain to the students that one of the goals of time series analysis is to support better decision making by understanding the behaviour of time series events. Give the following example:

* For example, by using home sales data, we can identify the best time to sell a property based on increasing demand or higher sale prices. To make such decisions, we need to identify any pattern that exists in a visualisation that depicts financial data over time.

Explain that, in this section, we’ll create and interpret visualisations, such as line plots, to analyse time series data for decision making. We’ll also analyse time series data by using heatmaps to recognise relationships.

Open the unsolved version of the provided Jupyter notebook. Live-code the demo, and highlight the following information:

* First, we need the number of homes that are listed for sale each month (that is, the inventory) along with the number of homes that actually sold during the same period.

* We’ll use a dataset of national home sales in the US that comes from [Redfin](https://www.redfin.com/), a national real estate brokerage.

* Let's start by loading the data into a Pandas DataFrame. We’ll set the “period_end_date” column as the index, and we’ll set `parse_dates=True`, as the following code shows:

  ```python
  # Set the file path
  file_path = Path("../Resources/national-home-sales.csv")

  # Load time series data into Pandas
  df_home_sales = pd.read_csv(file_path, index_col="period_end_date", parse_dates=True)

  # Display sample data
  df_home_sales.head(10)
  ```

  The following image shows the DataFrame:

  ![A screenshot depicts the DataFrame.](Images/11-1-load-home-sales-data.png)

* To analyse the time series data in chronological order, we next use the Pandas `sort_index` function to order the data in ascending order by the `DateTime` index, as the following code shows:

  ```python
  # Sort the DataFrame index in ascending order
  df_home_sales = df_home_sales.sort_index()

  # Display sample data
  df_home_sales.head(10)
  ```

  The following image shows the sorted DataFrame:

  ![A screenshot depicts the DataFrame.](Images/11-1-load-home-sales-data-ordered.png)

* We can make some initial observations by plotting the number of homes for sale and the number of homes sold in the DataFrame:

  ```python
  # Plot the inventory and homes_sold series
  df_home_sales[["inventory", "homes_sold"]].plot()
  ```

  The following image shows the plot:

  ![A screenshot depicts the plot.](Images/11-1-inventory-homes-sold-chart.png)

* In the preceding image, notice that the inventory starts high, and the number of homes sold starts low. Both trend toward each other over time.

* We can also observe that both have seasonal patterns. First, they appear to typically peak at a certain time every year. Second, we can possibly detect a long-term trend: fewer homes seem to be available for sale each year.

* Let’s take note of the interesting patterns that are emerging.

  * Every year, home sales show a recurring pattern. They’re low at the start and at the end of the year, with an obvious sales peak in the middle.

  * The inventory has a similar pattern. Fewer homes are available at the start and the end of the year, and more homes are available in the middle of the year.

* Both time series clearly show **periodicity**, where a pattern repeats at regular time intervals. We refer to this as **seasonality** in time series analysis.

* We can observe seasonality in different time scales. The preceding plot suggests that US home sales might exhibit yearly seasonality. We'll plot the time series of a single year to further investigate, as the following code shows:

  ```python
  # Select homes sold in 2014 using the year
  sales_2014 = df_home_sales["homes_sold"].loc["2014"]

  # Plot 2014 home sales data
  sales_2014.plot(title="Homes Sold in 2014")
  ```

  The following image shows the plot of homes sold from January 2014 to December 2014:

  ![A screenshot depicts the plot.](Images/11-1-sales-2014-chart.png)

* This type of plot proves useful for visually inspecting how the data behaves over a period of time.

* First, we can observe that the 2014 sales had an ascending trend starting in January and reached the highest number of sales in June. We can also observe a drastic sales drop from October to November with a slight increase in December. This is the kind of exploratory analysis and observation that you make as a fintech professional by using time series data. A further step involves discovering what produces these ups and downs in the time series.

#### Analyzing Time Data from a Quarterly Perspective

Continue the demo, and explain to the students that you’ll now analyse the homes sold series from a quarterly perspective. You’ll use the `DatetimeIndex` attributes and the `groupby` function to compute the total home sales per quarter, as the following code shows:

```python
# Compute the total home sales per quarter
quarterly_sales = df_home_sales["homes_sold"].groupby(by=[df_home_sales.index.quarter]).sum()

# Display total home sales per quarter
quarterly_sales
```

This is the result:

```text
period_end_date
1    10081561
2    14788243
3    14518462
4    11126303
Name: homes_sold, dtype: int64
```

Highlight the following details:

* We used the `quarter` attribute of `DatetimeIndex` to group the data by quarter. With this attribute, we can drill up and down among the dates to get different granularity levels in the time series analysis.

* For example, we can drill down from analysing yearly home sales to analysing quarterly home sales per year, as the following code shows:

```python
# Compute total quarterly home sales per year
quarterly_sales_per_year = df_home_sales["homes_sold"].groupby(by=[df_home_sales.index.year, df_home_sales.index.quarter]).sum()

# Display total quarterly home sales per year
quarterly_sales_per_year
```

The following data is the result:

```text
period_end_date  period_end_date
2012             1                   698771
                 2                  1357167
                 3                  1329120
                 4                  1212750
2013             1                  1053470
                 2                  1521401
                 3                  1533894
                 4                  1240531
2014             1                  1006881
                 2                  1494496
                 3                  1519277
                 4                  1304816
2015             1                  1105378
                 2                  1676173
                 3                  1714455
                 4                  1379792
2016             1                  1194478
                 2                  1779674
                 3                  1750930
                 4                  1476636
2017             1                  1264554
                 2                  1841266
                 3                  1756771
                 4                  1521970
2018             1                  1264974
                 2                  1849516
                 3                  1763335
                 4                  1453438
2019             1                  1201775
                 2                  1822709
                 3                  1797069
                 4                  1536370
2020             1                  1291280
                 2                  1445841
                 3                  1353611
Name: homes_sold, dtype: int64
```

Highlight the following details:

* If we plot the quarterly sales per year, we can still observe a seasonal pattern, as the following code shows:

  ```python
  # Plot total quarterly home sales per year
  quarterly_sales_per_year.plot()
  ```

  The following image shows the plot:

  ![A screenshot depicts the plot.](Images/11-1-quarter-sales-per-year.png)

* In the preceding plot, we might notice the first few labels associated with the x-axis, as follows:

  ```text
  (2012, 1) (2013, 2) (2014, 3)
  ```

* These labels show the year and the quarter associated with that point on the line plot. The plot starts with the value associated with the first quarter of 2012. The labels on the x-axis are then spaced out every five quarters, with the second label detailing the second quarter of 2013, and so on for the duration of the dataset.

* Reviewing the plot, we can observe that the line representing the number of home sales moves in an up-and-down pattern over the course of each year.

#### Visualizing Time Data by Using hvPlot

Explain that grouping time series data and creating line plots offers a visual method for analysing time series and identifying trends. But, depending on the patterns that we want to explore, we might want to use other types of visualisations, such as scatter plots, heatmaps, or histograms.

Tell the students that you’ll now demonstrate how to use the hvPlot library to provide more information about the time series in the plot. Highlight the following information:

* The hvPlot library offers an interesting alternative for visualising seasonal patterns: heatmaps. Let’s explore the quarterly sales per year from this new perspective.

* The following code plots the quarterly home sales per year on a heatmap:

  ```python
  # Plot quarterly home sales per year using a heatmap
  df_home_sales.hvplot.heatmap(
      x="index.year",
      y="index.quarter",
      C="homes_sold",
      cmap="blues"
  ).aggregate(function=np.mean)

  ```

  The following image shows the resulting heatmap”

  ![A screenshot depicts the heatmap.](Images/11-1-heatmap.png)

* In this heatmap, the x-axis represents the year, and the y-axis represents the quarter.

* The number of homes sold during the year and in each quarter are represented by the colours associated with each of the boxes at the intersection of the axes. The index for the colours associated with the heatmap is located on the right side of the visualisation. The lighter the colour, the fewer homes that were sold. The darker the colour, the more homes that were sold.

* Reviewing this heatmap, we can observe that the fewest homes were sold in the first quarter of 2012, and the most homes were sold around the third quarter of 2020.

* The line plot of quarterly home sales and the heatmap tell us about people’s interest in buying homes. Specifically, people are less willing to buy a home during the first quarter of the year. People are more interested in buying during the second and third quarters (which are both generally periods of good weather). Using different types of plots gives us additional perspectives on the time series and the behaviours over time that are represented.

Ask the students to examine the preceding heatmap again, and then ask the following question.

* **Question:** We can observe that the third quarter has the highest sales activity. But, has this seasonal effect grown stronger or weaker over recent years?

  * **Possible Answer:** The seasonal effect on home sales grew progressively stronger over each third quarter. We can observe this in the colour of the blocks associated with the third quarter of each year. The blocks get progressively darker (from left to right) along the x-axis.

Elaborate on the answer:

* Our answer to this question illustrates why visualising seasonal effects can be useful. By examining the heatmap, we can observe that the third quarter always had lots of real estate activity relative to the rest of the year.

* But in recent years, this quarterly effect is more pronounced. The third quarter of 2020, for example, shows an unprecedented amount of seasonal sales activity. (We can observe this in the heatmap by the dark blue colouring for this period). If we notice an increasing trend in this third-quarter effect, that insight will prove useful for making future predictions.

Answer any questions before moving on.

---

### 11. Student Do: Analysing Time Series Patterns in the S&P 500 Index (20 minutes)

**Corresponding Activity:** [06-Stu_Visualizing_Time_Patterns](Activities/06-Stu_Visualizing_Time_Patterns)

**Files:**

* [Instructions](Activities/06-Stu_Visualizing_Time_Patterns/README.md)

* [visualizing_time_patterns.ipynb](Activities/06-Stu_Visualizing_Time_Patterns/Unsolved/visualizing_time_patterns.ipynb)

* [sp500_stock_volume.csv](Activities/06-Stu_Visualizing_Time_Patterns/Resources/sp500_stock_volume.csv)

In this activity, the students will use their newly developed skills to visualise and analyse time-series patterns in the S&P 500 volume data.

---

### 12. Instructor Do: Review Analyzing Time Series Patterns in the S&P 500 Index (10 minutes)

**Files:**

* [Instructions](Activities/06-Stu_Visualizing_Time_Patterns/README.md)

* [visualizing_time_patterns.ipynb (unsolved)](Activities/06-Stu_Visualizing_Time_Patterns/Unsolved/visualizing_time_patterns.ipynb)

* [visualizing_time_patterns.ipynb (solved)](Activities/06-Stu_Visualizing_Time_Patterns/Solved/visualizing_time_patterns.ipynb)

* [sp500_stock_volume.csv](Activities/06-Stu_Visualizing_Time_Patterns/Resources/sp500_stock_volume.csv)

Remind the students that the S&P 500 dataset is an exchange-traded fund (ETF) of the largest 500 public firms in the US. It acts as an indicator of the condition and activity for the broader economy.

Open the unsolved version of the provided Jupyter notebook. Live-code the solution while highlighting the following points.

* We start by importing the required libraries and dependencies, as the following code shows:

  ```python
  import pandas as pd
  from pathlib import Path
  import hvplot.pandas
  ```

* Next, we import the data and read the CSV file into a Dataframe, accounting for date and time considerations, as the following code shows:

  ```python
  # Import data
  sp500_path = Path('../Resources/sp500_stock_volume.csv')

  # Read the S&P 500 volume into a DataFrame. (Make sure to declare the datetime index).
  sp500_data = pd.read_csv(
      sp500_path,
      index_col='Date',
      parse_dates=True,
      infer_datetime_format=True
  )
  ```

* Next, we slice the DataFrame to include only the volume data, as the following code shows:

  ```python
  # Slice the dataframe so that it just includes the volume data.
  sp500_volume = sp500_data['volume']
  ```

* To create a plot of the volume data according to the day of the week, we first declare the group level to be the day of the week (Mon, Tues, and so on). We then use hvPlot to create a plot that shows the average daily volume according to the day of the week:

  ```python
  # Declare the group level to be the day of the week (e.g., Mon, Tues,...)
  group_level = sp500_volume.index.dayofweek

  # Plot average daily volume according to day of the week
  sp500_volume.groupby(group_level).mean().hvplot()
  ```

  The following image shows the resulting line plot of the S&P 500 volume data at the day level:

  ![A screenshot depicts the line plot.](Images/11-1-sp500-volume-plot.png)

* Based on the preceding image, we can observe that share trading activity reaches its highest levels later in the week (Wednesday through Friday).

* Next, we use hvPlot to visualise the hourly trends across the days of week in a heatmap, as the following code shows:

  ```python
  sp500_volume.hvplot.heatmap(
      x='index.hour',
      y='index.dayofweek',
      C='volume',
      cmap='reds'
  ).aggregate(function=np.mean)
  ```

  The following image shows the resulting heatmap:

  ![A screenshot depicts the heatmap.](Images/11-1-sp500-heatmap.png)

* By finding the placement of the darker region on the heatmap, we can determine that most of the share trading for the S&P 500 is concentrated in the last hour or two of the day. Except for Mondays (the "hottest" point on the heatmap), this effect doesn't seem to depend much on the day of the week.

* Finally, we group the data by the calendar week in the year (week of year), as the following code shows:

  ```python
  # Group the data by the calendar week in the year (week of year).
  sp500_volume.groupby(by=[sp500_volume.index.year, sp500_volume.index.weekofyear]).mean().plot(
      title="SP500 Mean Volume per Week",
      figsize=[10, 5]
  )
  ```

  The following image shows the resulting line plot:

  ![A screenshot depicts the line plot.](Images/11-1-sp500-weekofyear-plot.png)

* Based on this plot, it seems that the share activity generally stays constant throughout the year, except for somewhere around the 11th to the 14th week (approximately March to April). Many company annual reports come out during these weeks, so that might be one reason why we get a consistent volume pattern around that time. (An **annual report** is a presentation and discussion of the annual financial results of the company.)

Before moving on, ask the students if they have any questions about hvPlot or the process of analysing the visual output of time series data.

---

### 13. Recap (5 minutes)

Before ending the class, point out that this lesson introduced the importance of time in finance. The students also learned a visual technique for exploring time series data to identify seasonal patterns.

In the next class, the students will learn how to use correlations to identify whether two time series with seasonal patterns have a relationship—and whether that relationship is predictable. Also, they’ll learn how to forecast time series and interpret the forecasting results.

Answer any questions before ending the class.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
