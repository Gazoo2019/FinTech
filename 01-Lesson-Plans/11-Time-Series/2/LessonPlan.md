## 11.2: Introduction to Time Series Forecasting

### Overview

In this class, the students will build their time series analysis skills by identifying patterned relationships and analysing data correlations. The students will also get an introduction to Prophet, a library developed by Facebook that helps to automate time series analysis and forecasting.

### Class Objectives

By the end of this class, the students will be able to:

* Identify relationships among time series patterns.

* Use data correlation to evaluate the predictive relationship among time series patterns.

* Compute data correlation of time series data by using the Pandas `corr` function.

* Describe the business value of time series forecasting.

* Recognise the value of automating time series forecasting.

---

### Instructor Notes

* This class will introduce the students to time series forecasting but does not cover its mathematical complexity. Instead, the lesson focuses on the business value of time series forecasting. The students will learn how to automate and speed up time series analysis and forecasting by using Prophet.

* We have identified some issues with Prophet when it runs over certain configurations on both macOS and Windows systems. To avoid these issues, the students will use Google Colab to work with Prophet.

* You're encouraged to read the [Overview of Colaboratory Features](https://colab.research.google.com/notebooks/basic_features_overview.ipynb) quick start guide if you have not used Google Colab before.

* Explain to the students that the Jupyter notebooks that they will execute in Google Colab will be saved in their personal Google Drive.

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [11.2 lesson slides](https://docs.google.com/presentation/d/1YuKV54FYotWzWrIdjiEOISKs0u5t1kMu-WO5d_n5LuU/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. [View instructions with images.](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome (5 minutes)

Welcome the students to the second class of Module11.

Explain that today’s class is an introduction to time series forecasting. The students will learn how to use Prophet, a library that automates the process of time series forecasting. By using automation tools, they can focus on analysing the forecast results and assessing their business value.

Answer any questions before moving on.

---

### 2. Students Do: Time Series Warm-Up (20 minutes)

**Corresponding Activity:** [01-Stu_Warm_Up](Activities/01-Stu_Warm_Up)

**Files:**

* [Instructions](Activities/01-Stu_Warm_Up/README.md)

* [time_series_warm_up.ipynb](Activities/01-Stu_Warm_Up/Unsolved/time_series_warm_up.ipynb)

* [bitcoin_hourly.csv](Activities/01-Stu_Warm_Up/Resources/bitcoin_hourly.csv)

Engage the students in a conversation about how their week has progressed and their comfort level with analysing financial time series data.

Next, introduce the first activity, which is a warm-up to strengthen the students' time series analysis skills and to review the Pandas functions that they learned in the previous class.

---

### 3. Instructor Do: Review Time Series Warm-Up (10 minutes)

**Files:**

* [Instructions](Activities/01-Stu_Warm_Up/README.md)

* [time_series_warm_up.ipynb (Unsolved)](Activities/01-Stu_Warm_Up/Unsolved/time_series_warm_up.ipynb)

* [time_series_warm_up.ipynb (Solved)](Activities/01-Stu_Warm_Up/Solved/time_series_warm_up.ipynb)

* [bitcoin_hourly.csv](Activities/01-Stu_Warm_Up/Resources/bitcoin_hourly.csv)

Open the unsolved version of the provided Jupyter notebook, and then live-code the solution while highlighting the following steps:

* We start by importing the libraries and dependencies. Then, we read in the `bitcoin_hourly` CSV file and prepare the data. These steps have been completed for you in the starter code. Note that we automatically read and declare a `datetime` index, which generates `hvplot` graphs with x-axes that show dates instead of integers.

* Next, we plot volume in a line plot by using `hvplot`. This provides a sense of the typical volume for the cryptocurrency, as the following code and image show:

  ```python
  # Plot volume by using hvplot to get a sense of what's typical volume for the cryptocurrency
  df['volume'].hvplot()
  ```

  ![A line plot shows the bitcoin market volume.](Images/11-2-btc-volume.png)

* We use Pandas `groupby` and the `weekofyear` function on the `datetime` index to create a `hvplot` bar plot of the data. Note that we use `kind='bar'` as a parameter in the hvPlot function:

  ```python
  # Use groupby and the weekofyear function on the datetime index to create a hvplot bar plot of the data
  df.groupby(df.index.weekofyear).mean().hvplot(kind='bar')
  ```

  ![A bar chart shows the bitcoin market volume.](Images/11-2-btc-volume-bars.png)

* Note how prices tend to be highest around the beginning of the year (mostly in January).

* Similarly, we can use the `datetime` index to group our dataframe by the hour. This allows us to plot average prices and volume, for each of the 24 hours in a day. This is illustrated by the following code and image:

  ```python
  # Plot hourly trends in prices and volume for the cryptocurrency
  df.groupby(df.index.hour).mean().hvplot(kind='bar')
  ```

  ![A bar chart shows the hourly bitcoin market volume.](Images/11-2-btc-volume-bars-hourly.png)

* Here, the patterns in price aren't very clear. But there seems to be an increase in volume in the middle of the business day (between the hours of 12:00 p.m. and 4:00 p.m.).

* Now, let’s take a look at some thoughts expressed about Bitcoin. Specifically, we want to determine whether a couple of tweets about Bitcoin by Elon Musk have moved the market.

* Using datetime indexing, we slice the volume and price DataFrame to one day before and after Jan 29, 2021, when Elon Musk added the hashtag #bitcoin to his Twitter bio:

```python
# Slice to one day before and after Jan 29, 2021
df.loc['2021-01-27':'2021-01-31'].hvplot()
```

![A line plot that shows the BTC close price and volume from January, 27th to 31nd 2021](Images/11-2-btc-sentiment.png)

* After analysing this data, we can conclude that Musk's tweet caused both volume and price for Bitcoin to increase.

Answer any questions before moving on.

---

### 4. Instructor Do: Identifying Patterned Relationships and Correlation (15 minutes)

**Corresponding Activity:** [02-Ins_Relationships_and_Correlation](Activities/02-Ins_Relationships_and_Correlation)

**Files:**

* [relationships_and_correlation.ipynb](Activities/02-Ins_Relationships_and_Correlation/Unsolved/relationships_and_correlation.ipynb)

* [national-home-sales.csv](Activities/02-Ins_Relationships_and_Correlation/Resources/national-home-sales.csv)

In this section, the students will learn how to use Pandas to identify patterned relationships among time series. They will also learn to use correlation as a measure to assess the predictive power of time series.

Explain that when analysing time series, finding seasonal patterns is just one part of the job. Another important task is identifying any relationships among time series patterns and determining if these relationships are predictable.

Open the unsolved version of the Jupyter notebook provided and highlight the following:

* We’ll examine the time series of home inventory and homes sold from a different perspective.

* To start, recall our first plot of this dataset.

  ```python
  # Plot the inventory and homes_sold series
  df_home_sales[["inventory", "homes_sold"]].plot()
  ```

  ![A screenshot depicts the plot. The inventory starts high. The homes sold start low. Both trend toward each other over time.](Images/11-2-inventory-homes-sold-chart-2.png)

* After examining both series on the plot, we can infer a relationship between them. While the number of homes sold increases, the inventory decreases. We can verify this relationship quantitatively by using a correlation.

* In statistics, a **correlation** defines the relationship between two or more variables. We can use Pandas to compute a correlation by using the [`corr` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html), as follows:

  ```python
  # Compute the correlation between "inventory" and "homes_sold"
  df_home_sales[["inventory", "homes_sold"]].corr()
  ```

  ![A screenshot depicts the DataFrame.](Images/11-2-time-series-correlation.png)

* Notice that the DataFrame has two columns, one for the inventory and one for the homes sold. And, it has two rows, one each for the inventory and the homes sold. Each numerical value indicates the correlation between these variables.

* The value of a correlation ranges from -1 to +1. A positive value implies that both variables have an increasing (or direct) relationship because both variables increase over time. In contrast, a negative value implies a decreasing (or inverse) relationship—as one variable increases, the other decreases.

* The correlation between the two variables gets stronger as the correlation approaches either -1 or +1.

* A correlation is a useful statistical tool because it can indicate a predictive relationship that we can take advantage of in practice.

* For example, a natural gas supplier might deliver more gas on cold days based on the correlation between gas consumption and weather. Extreme weather might cause people to consume more gas for heating.

* From our correlation, we can observe that the inventory and the homes sold seem to have a decreasing relationship: the more homes that are for sale at any time, the fewer homes that actually seem to sell. However, the correlation at -0.006937 isn’t strong, which indicates that no predictable relationship exists between these two factors.

* In this week’s Challenge, you’ll use a correlation to check whether any predictable relationship exists between internet search traffic and the stock volatility of Mercado Libre.

Explain to the students that while correlations can be very helpful, they don’t provide enough information to infer the relationship between two variables. Highlight the following points:

* Statisticians state that a correlation does not imply causation. In other words, you can’t assume causation from only a correlation value.

* We will need a lot of information to determine causation between factors, including expertise in the field and extensive testing, which will likely include the ability to control for other related factors.

Point out that a correlation evaluates how much two variables move in a similar pattern at the same time, so we can apply correlations to the analysis of stocks, too.

Use the slides to pose the following question to the students.

* **Question:** Consider the following correlation table in the form of a heatmap that contains the correlations of various intraday stock returns (the returns are measured by using minute-level price data). Can you identify which stocks tend to move together the most strongly?

  ![A screenshot depicts a heatmap that has the same stocks on the y-axis and on the x-axis.](Images/11-2-correlation-heatmap.png)

  * **Answer:** It seems that CRS and AMRC and CRS and BBJP both have the highest correlation. (All three stocks pertain to the heavy manufacturing industry, so it makes sense that their returns closely move together).

In the next activity, the students will use the code for computing correlations in the same way, but the interpretation will differ somewhat.

* Going forward, they’ll use correlations to identify the relationships between current observations and **future** values.

* This differs from identifying the relationships for variables that are measured at the same time.

Answer any questions before moving on.

---

### 5. Students Do: Stock Volatility and Google Trends (20 minutes)

**Corresponding Activity:** [03-Stu_Stock_Volatility_and_Google_Trends](Activities/03-Stu_Stock_Volatility_and_Google_Trends)

**Files:**

* [Instructions](Activities/03-Stu_Stock_Volatility_and_Google_Trends/README.md)

* [stock_volatility_and_google_trends.ipynb](Activities/03-Stu_Stock_Volatility_and_Google_Trends/Unsolved/stock_volatility_and_google_trends.ipynb)

* [aapl-price.csv](Activities/03-Stu_Stock_Volatility_and_Google_Trends/Resources/aapl-price.csv)

* [apple-trends.csv](Activities/03-Stu_Stock_Volatility_and_Google_Trends/Resources/apple-trends.csv)

In this activity, the students will analyse time series data about Apple to identify any correlations among Google Trends, the stock price returns, and the stock volatility.

---

### 6. Instructor Do: Review Stock Volatility and Google Trends (10 minutes)

**Files:**

* [Instructions](Activities/03-Stu_Stock_Volatility_and_Google_Trends/README.md)

* [stock_volatility_and_google_trends.ipynb (Unsolved)](Activities/03-Stu_Stock_Volatility_and_Google_Trends/Unsolved/stock_volatility_and_google_trends.ipynb)

* [stock_volatility_and_google_trends.ipynb (Solved)](Activities/03-Stu_Stock_Volatility_and_Google_Trends/Solved/stock_volatility_and_google_trends.ipynb)

* [aapl-price.csv](Activities/03-Stu_Stock_Volatility_and_Google_Trends/Resources/aapl-price.csv)

* [apple-trends.csv](Activities/03-Stu_Stock_Volatility_and_Google_Trends/Resources/apple-trends.csv)

Open the unsolved version of the Jupyter notebook provided. Live-code the solution and highlight the following information.

* The first section of the activity may seem simple, but there are a couple of important aspects to remember when we load time data into Pandas.

* It's a good idea to open the data file into a spreadsheet program or a text editor to inspect the data and identify the column containing the dates. We can use that column as the DataFrame index.

* Both of the provided CSV files have a column called “date.” So, we can set that column as the index when we load the data into the DataFrame. Remember to set `parse_dates=True` and `infer_datetime_format=True`:

  ```python
  # Read the data from the apple-price.csv file into a Pandas DataFrame
  df_stock = pd.read_csv(
      Path("../Resources/aapl-price.csv"),
      index_col="date",
      parse_dates=True,
      infer_datetime_format=True
  )

  # Review the DataFrame
  df_stock.head()

  # Read the data from the apple-trends.csv file into a Pandas DataFrame
  df_trends = pd.read_csv(
      Path("../Resources/apple-trends.csv"),
      index_col="date",
      parse_dates=True,
      infer_datetime_format=True
  )

  # Review the DataFrame
  df_trends.head()
  ```

  ![A screen capture shows the Apple stock price and Google trends data loaded into two different DataFrames.](Images/11-2-aapl-stock-data.png)

* Next, we use the `concat` Pandas function to combine the stock price and the trends data into a single DataFrame:

  ```python
  # Concatenate Apple's stock price and Google trends data
  df_apple = pd.concat([df_stock, df_trends], axis=1).dropna()

  # Review the df_apple DataFrame
  df_apple.head()
  ```

  ![A screen capture shows the Apple stock price and Google trends data concatenated into a single DataFrame.](Images/11-2-aapl-price-trends-concat.png)

* As an initial analysis, we use hvPlot to visualise and identify any trends or correlations:

  ```python
  # Use hvplot to visualize the time series data in the df_apple DataFrame
  df_apple.hvplot()
  ```

  ![A line plot shows the Apple stock price and Google trends.](Images/11-2-aapl-price-trends-plot.png)

* On September 10, 2019, Apple organised an event where it presented the new iPhone 11 family, the Apple Watch Series 5, and a new iPad. This event gained worldwide attention.

* To more closely observe the data from March 1, 2019 to January 31, 2020, we create a new DataFrame and plot the data by using hvPlot to verify whether both time series indicate a common trend that might correspond to this narrative, as the following code shows:

  ```python
  # Using the df_apple DataFrame, use the loc function to select a
  # range of data from March 1st, 2019 to January 31st, 2020
  df_spotlight = df_apple.loc["2019-03-01":"2020-01-31"]

  # Review the df_spotlight DataFrame
  df_spotlight

  # Use hvPlot to visualize the df_spotlight DataFrame
  df_spotlight.hvplot()
  ```

  ![A screen capture shows Apple data from March 1, 2019 to January 31, 2020.](Images/11-2-aapl-spotlight.png)

* Before finding correlations between these time series, we add columns to the `df_apple` DataFrame. This allows us to analyse the impact of the Google Trends data on the weekly returns and stock volatility:

  ```python
  # Create a column which lags Google trends by one week
  # Use the shift function, and move the data down by one row
  df_apple["lagged_trends"] = df_apple["trend-worldwide"].shift(1)

  # Create a column that contains the Apple weekly return data
  # Use the pct_change function to calculate the weekly return values
  df_apple["weekly_returns"] = df_apple["close"].pct_change()

  # Create a column of Apple weekly rolling stock volatility
  # Chain the pct_function, the rolling function and a 4 period window, and the std function
  df_apple["weekly_volatility"] = df_apple["close"].pct_change().rolling(window=4).std()
  ```

* Finally, we use the Pandas `corr` function to compute the correlations among the lagged Google Trends data, the price returns, and the stock volatility, as the following code shows:

  ```python
  # Use the corr function to compute the correlation between the lagged Google Trends data, price returns, and stock volatility
  df_apple[["lagged_trends", "weekly_returns", "weekly_volatility"]].corr()
  ```

  ![A screen capture shows the correlation between the lagged Google Trends data, price returns, and stock volatility.](Images/11-2-aapl-corr.png)

* After examining the correlation results, we can conclude that there is a positive correlation. However, because the values are far from the absolute value of 1, the correlation is not strong.

Answer any questions before moving on.

---

### 7. Break (15 minutes)

---

### 8. Instructor Do: Introduction to Time Series Forecasting (15 minutes)

**Corresponding Activity:** [4-Ins_Intro_Time_Series_Forecasting](Activities/04-Ins_Intro_Time_Series_Forecasting)

In this activity, the students will be introduced to the concept of time series forecasting. You can use the slides to help with the theoretical explanation of the concept. In the last part of the activity, you will explain how to configure Google Colab for the rest of today's activities.

Open the lesson slides and highlight the following points.

* The financial world makes great use of time series forecasting because of its origins in the mathematics and statistics space.

* People sometimes refer to time series forecasting as a statistical tool, but there’s a lot of overlap between statistical tools and machine learning models. Both can solve similar problems.

* As you learned previously, time series analysis involves analysing time series data to identify meaningful patterns in the data.

* Time series forecasting involves using a model that’s based on historical data to predict future values in the time series.

* In this lesson, you’ll perform time series forecasting by creating models to predict the future.

#### Automating Time Series Forecasting

Continue the explanation by using the lesson slides while highlighting the following details.

* Time series forecasting can be challenging. External factors, such as holidays, breaking news, and special events, can impact the usual behaviour of the patterns. Additionally, it can be challenging to select the best statistical technique for analysis.

* Let's look at a scenario where we are collaborating with the [International Co-operative Alliance](https://www.ica.coop/) on a project. The project will help alpaca farms in Bolivia owned by the Aymara indigenous people to export alpaca wool scarves to Japan.

* We've been asked to find the best season to sell scarves in Japan and to forecast the demand for scarves for one year.

* We don’t know anything about the scarf market in Japan, so we've obtained some data from Google Trends to figure out the optimal selling season, as the following image shows:

  ![A screenshot depicts the graph of scarf purchases from January 2017 to October 2019. The graph peaks around December 3, 2017.](Images/11-2-scarf-google-trends-japan.png)

* Using our time analysis skills, we've identified that people in Japan have more interest in scarves in the winter months because of the weather. So, it might be optimal to start marketing campaigns in August and start selling scarves by October.

Explain to the students that external factors, like weather or holidays, impact a time series and sometimes introduce noise.

* **Noise** is information in the data that is essentially meaningless and distracts from the overall trend, or signal, of the data.

* Noise acts as another independent variable in our models, but we can use some statistical techniques to manually reduce it. However, dealing with noise reduction adds more complexity to a time series analysis, and adjusting our models for it can be time-consuming.

#### Focusing on Results Analysis and Decision Making with Prophet

Introduce Prophet to the students. Slack out the [Prophet website](https://facebook.github.io/prophet/) for further reference. You can also open this site on your computer as you highlight the following information.

* Prophet is an open-source library for time series forecasting that Facebook developed to analyse their data. They use Prophet to forecast Facebook's growth, technological infrastructure demand, services revenue, and fraudulent activity.

* Prophet automates the process of time series forecasting, allowing you as a fintech professional to focus on a business problem. It also tests and forecasts as many scenarios as you identify.

* Prophet's forecasting automation can help to simplify your time series analysis. It deals with noise, holidays or special events, and **time series decomposition**, which is the process of analysing trends and seasonal patterns within time series data.

#### Configuring Google Colab

Explain to the class that installing Prophet can be tricky on some machines. To simplify things, we'll be using Google Colab—an IDE that allows us to run Jupyter notebooks in the cloud, which allows everyone to have the same computational environment.

Slack out the [Google Colab URL](https://colab.research.google.com/) to students. Open Google Colab on your computer and create a new notebook, as in the following image:

![A screenshot depicts how to create a new notebook in Google Colab.](Images/11-2-new-notebook-colab.png)

After creating the new notebook, highlight the following points.

* Running Jupyter Notebook with Google Colab is simple. Notebooks that run in the cloud use a base configuration of Python 3 components, which includes many popular libraries like Pandas and Matplotlib.

* Other libraries, such as hvPlot and Prophet, require installation.

* Google Colab notebooks are compatible with Jupyter notebooks. However, because they reside in the cloud, these notebooks will be saved in your Google Drive in a folder called "Colab Notebooks" in the root folder of your drive.

* Now, we’ll install the necessary libraries for Google Colab and Prophet. To use Prophet, we'll just need to install `prophet`.

* We'll be plotting with hvPlot in this lesson. To use hvPlot in Google Colab, we'll need to install both `hvplot` and its dependency `holoviews`. The following code accomplishes these tasks:

  ```python
  # Install the required libraries
  !pip install prophet
  !pip install hvplot
  !pip install holoviews
  ```

  ![A screen capture of Google Colab shows the execution of the code needed to install the required libraries for time series forecasting.](Images/11-2-installing-libraries-colab.png)

* Once the installations are complete, we'll import the needed libraries in the Google Colab notebook:

  ```python
  # Import the required libraries and dependencies
  import pandas as pd
  import holoviews as hv
  from prophet import Prophet
  import hvplot.pandas
  import datetime as dt
  %matplotlib inline
  ```

* Next, we need to upload our CSV files to Google Colab. We can then store the files in a DataFrame by calling `pd.read_csv` and supplying the CSV filename.

* The following code selects a file from your local machine and uploads the file into your Google Colab notebook instance:

  ```python
  # Import the `files` library to allow files upload
  from google.colab import files
  ```

* hvPlot renders differently in Google Colab than in a local Jupyter instance, so we might see a blank plot. To avoid this, we can use the Bokeh data visualisation library.

* We'll use the following line of code to set the Bokeh library to render hvPlot charts in the notebook before every chart is displayed:

  ```python
  # Setting bokeh to render hvPlot charts
  hv.extension("bokeh")
  ```

Explain that once the students have completed the Google Colab configuration, they should have a notebook like the one shown in the following image:

![A screen capture shows the code needed to configure Google Colab.](Images/11-2-final-conf-colab.png)

Slack out to the students the [Overview of Colaboratory Features](https://colab.research.google.com/notebooks/basic_features_overview.ipynb). Google created this notebook for use as a quick start guide to Google Colab.

Answer any questions before moving on.

---

### 9. Students Do: Setting Up Google Colab (10 minutes)

**Corresponding Activity:** [05-Stu_Setting_Up_Google_Colab](Activities/05-Stu_Setting_Up_Google_Colab)

**Files:**

* [Instructions](Activities/05-Stu_Setting_Up_Google_Colab/README.md)

* [setting-up-google-colab.ipynb](Activities/05-Stu_Setting_Up_Google_Colab/Solved/setting-up-google-colab.ipynb)

In this activity, the students will get additional practice with opening and configuring Google Colab.

---

### 10. Instructor Do: Review Setting Up Google Colab (10 minutes)

**Files:**

* [Instructions](Activities/05-Stu_Setting_Up_Google_Colab/README.md)

* [setting-up-google-colab.ipynb](Activities/05-Stu_Setting_Up_Google_Colab/Solved/setting-up-google-colab.ipynb)

Review the previous activity to ensure that all students were able to open Google Colab, create a new notebook, and follow the activity instructions to set up their notebook.

Answer any questions before moving on.

---

### 11. Instructor Do: Data Preparation for Time Series Forecasting with Prophet (15 minutes)

**Corresponding Activity:** [06-Ins_Data_Prep_Time_Series](Activities/06-Ins_Data_Prep_Time_Series)

**Files:**

* [data-prep-time-series.ipynb](Activities/06-Ins_Data_Prep_Time_Series/Solved/data-prep-time-series.ipynb)

* [hourly_grid_prices.csv](Activities/06-Ins_Data_Prep_Time_Series/Resources/hourly_grid_prices.csv)

In this activity, the students will learn how to prepare a time series dataset for time series forecasting with Prophet.

Open Google Colab and import the unsolved version of the provided Jupyter notebook. Live-code the demo and highlight the following details:

* The world of fintech isn’t limited to peer-to-peer lending and mobile banking. Fintech use cases can include anything that involves saving, borrowing, or paying.

* Consider green energy, for example. In this case, the need to borrow money can be large because solar panels are expensive.

* In this part of the lesson, you’ll learn how to use Prophet to automate time series forecasting in a business scenario. In the scenario, you’ll contribute to reducing the impact of climate change by demonstrating how people can earn money over time through the use of solar panels.

* Let's say that we’re building a solar financing company. We lend money to borrowers who want to convert their energy consumption source to one that’s environmentally conscious. These borrowers don’t have the money to cover the upfront costs for a big solar-panel installation.

* We want to show them how much money they can earn if they take a loan and install the panels themselves. By using a time series model, we can forecast the price for which they’ll be able to sell their generated electricity.

* To start, we will read-in some hourly data for the price of electricity just outside Chicago, Illinois.

Run the cells under the "Notebook Set Up" section to get started. Before jumping into model building, explain to students that first we'll plot the data to get a better sense of what’s happening, using the following code:

```python
# Upload "hourly_grid_prices.csv" into Colab, then store in a DataFrame
uploaded = files.upload()

hourly_prices = pd.read_csv(
    "hourly_grid_prices.csv",
    index_col='day-hour',
    parse_dates=True,
    infer_datetime_format=True
).dropna()

# Display the first and last five rows of the DataFrame
display(hourly_prices.head())
display(hourly_prices.tail())

# Holoviews extension to render hvPlots in Colab
hv.extension('bokeh')

# Plot the DataFrame
hourly_prices.hvplot()
```

![A screenshot depicts the DataFrame of data and then a plot of the data.](Images/11-2-chicago-electricity-data.png)

Highlight that the DataFrame has the day and hour in one column and the price in the second column. Point out the following details:

* The plot shows the price over time from 2016 to 2021.

* Plotting the data reveals that electricity prices are pretty spiky. The average hourly price is less than $100 but occasionally spikes to more than $500.

* The prices even go negative on occasion, meaning that the sellers of electricity had to pay others to take their energy during that time.

The next step is to prepare the data to be read into a Prophet model. Explain that Prophet requires specific column names and a specific column structure for the model to work correctly. Continue the demo and highlight the following steps.

* First, we'll create a standard numerical index by moving our “day_hour” column back into the DataFrame with the other columns. We'll do this by resetting our `DatetimeIndex`, as the following code shows:

  ```python
  # Reset the index of the DataFrame
  prophet_df = hourly_prices.reset_index()

  # Review the first and last five rows of the DataFrame
  display(prophet_df.head())
  display(prophet_df.tail())
  ```

  ![A screenshot depicts the DataFrame with a numeric index starting with 0 and two columns, the “day-hour” column and the “Price” column.](Images/11-2-reset-index-to-fit-prophet.png)

* The data contained in the “day_hour” column is no longer the index of the DataFrame. It is now a column in the DataFrame.

Explain to the students that Prophet is designed to accept a DataFrame that has two specific columns: “ds” and “y”.

* The “ds” column refers to the date stamp. Data in this column should be formatted as `YYYY-MM-DD` for a date or `YYYY-MM-DD HH:MM:SS` for a time stamp.

* The “y” column needs to be a numeric value and refers to the measurement that we want to forecast.

Slack out to the students the [Prophet Quick Start guide](https://facebook.github.io/prophet/docs/quick_start.html), which provides more information about these columns.

Continue the demo and highlight the following information.

* We need to rename the columns so that Prophet will recognise them. "ds" is the date, and “y” refers to the hourly prices that we can get for our electricity generation:

  ```python
  # Prepare the training data to be read into a Prophet model
  # Rename the columns to names that Prophet recognizes
  prophet_df.columns = ['ds', 'y']
  prophet_df.head()
  ```

  ![A screenshot depicts the DataFrame with the columns now named ds and y.](Images/11-2-renaming-columns-for-prophet.png)

* We need to be aware that Prophet doesn’t work well with missing data, so let’s drop any `NaN` values that may exist in the DataFrame, as in the following code:

  ```python
  # Confirm that there are no NaN values
  prophet_df = prophet_df.dropna()
  prophet_df.tail()
  ```

  ![A screenshot depicts the tail of the DataFrame.](Images/11-2-removing-nans.png)

* With the DataFrame prepared, we’re ready to use a Prophet time series model to estimate electricity prices and encourage the generation and use of green energy. But we need to practice the data cleaning process first, and we'll do that in the next activity.

Answer any questions before moving on.

---

### 12. Students Do: Data Preparation to Forecast Market Opportunities (20 minutes)

**Corresponding Activity:** [07-Stu_Data_Prep](Activities/07-Stu_Data_Prep)

**Files:**

* [Instructions](Activities/07-Stu_Data_Prep/README.md)

* [data-prep.ipynb](Activities/07-Stu_Data_Prep/Unsolved/data-prep.ipynb)

* [scarf-google-trends-data.csv](Activities/07-Stu_Data_Prep/Resources/scarf-google-trends-data.csv)

In this activity, the students will use Google Colab to prepare a dataset and then use that dataset and Prophet to forecast market opportunities. Explain to the students that they will use the prepared data from this activity in the next class.

---

### 13. Instructor Do: Review Data Preparation to Forecast Market Opportunities (10 minutes)

**Files:**

* [Instructions](Activities/07-Stu_Data_Prep/README.md)

* [data-prep.ipynb (Unsolved)](Activities/07-Stu_Data_Prep/Unsolved/data-prep.ipynb)

* [data-prep.ipynb (Solved)](Activities/07-Stu_Data_Prep/Solved/data-prep.ipynb)

* [scarf-google-trends-data.csv](Activities/07-Stu_Data_Prep/Resources/scarf-google-trends-data.csv)

Open Google Colab and import the unsolved version of the provided Jupyter notebook. Live-code the solution and highlight the following information.

* As we did before, the first task is to configure the Colab notebook with the required libraries for this activity. This code is provided in the starter notebook.

* Next, we upload the provided CSV file and read it into a Pandas DataFrame:

  ```python
  # Upload the scarf-google-trends-data.csv file
  from google.colab import files
  uploaded = files.upload()

  # Read the data from the scarf-google-trends-data.csv file into a Pandas DataFrame
  df_alpaca = pd.read_csv("scarf-google-trends-data.csv")

  # Review the DataFrame
  df_alpaca.head()
  ```

  ![A screen capture shows the results after uploading the CSV file and loading it into a DataFrame.](Images/11-2-stu-data-load.png)

* Once we have loaded the data, we can plot the time series to visualise the general trends, as the following code shows:

```python
# Set `bokeh` to render hvPlot charts
hv.extension("bokeh")

# Plot the general trends by using hvPlot
df_alpaca.hvplot()
```

![A screen capture shows a line plot with Google trends data.](Images/11-2-stu-trends.png)

* Finally, we prepare the data so it will fit the Prophet model. We create two new DataFrames: one for Canada and another for Uruguay:

```python
# Create a DataFrame for Canada to include the week and Canada columns
df_canada = df_alpaca[["week", "canada"]]

# Rename the columns to the Prophet model syntax
df_canada = df_canada.rename(columns={"week":"ds", "canada":"y"})

# Review the Canada DataFrame
df_canada.head()

# Create a DataFrame for Uruguay to include the week and Uruguay columns
df_uruguay = df_alpaca[["week", "uruguay"]]

# Rename the columns to the Prophet model syntax
df_uruguay = df_uruguay.rename(columns={"week":"ds", "uruguay":"y"})

# Review the Uruguay DataFrame
df_uruguay.head()
```

![A screen capture shows two DataFrames.](Images/11-2-stu-data-prepared.png)

Answer any questions before moving on.

---

### 14. Instructor Do: Recap (5 minutes)

Congratulate the students on sharpening their time series analysis skills, and recap what they learned today:

* You used Pandas to analyse time series data. This is one of Pandas’ most important capabilities.

* Time series analysis is a crucial skill for fintech professionals, so students learned how to create and analyse visualisations for time series data.

* You also learned about the benefits of automating time series forecasting.

Explain to the students that they’re ready to take the next step, which will happen in the next class: managing time series data and creating models to predict the future by using Prophet.

Answer any questions before ending class.

---

### End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
