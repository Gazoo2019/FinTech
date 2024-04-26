## 11.3: Time Series Forecasting with Prophet

### Overview

This class will complete the subject of time series forecasting by using Prophet. The students will follow up with activities that use the same data about alpaca wool scarves that they prepared in an earlier class.

### Class Objectives

By the end of this class, the students will be able to:

* Use Prophet for time series forecasting.

* Interpret the forecasting results for decision making.

* Apply advanced times-series forecasting models by using Prophet.

---

### Instructor Notes

* The students will solidify the skills gained during the previous two days by completing activities that use Prophet for time series forecasting. During the longer activities, you and your TAs should be ready to help students who are having difficulties. Help those students stay on track while ensuring that they have a good grasp of time series forecasting.

* The students will continue working with Google Colab. Remind them that they can download the notebooks.

### Class Slides and Time Tracker

You can review the slides for this lesson on Google Drive at [11.3 slides](https://docs.google.com/presentation/d/1a5lUtMqnUQSLuZywOdX_AwvWQdmtm7E0fJVXa8K8fpM/edit?usp=sharing).

To add the slides to the student-facing repository, download the slides as a PDF. Select "Download" on the File menu, and then click "PDF document (.pdf)." Then add the PDF file to your class repository along with the other necessary files. You can review the instructions for this in the [Sharing Slides with Students](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing) document.

**Note:** Editing access is not available for this slide deck. If you want to modify the slides, create a copy by clicking "Make a copy" on the File menu.

You can review the time tracker for this lesson at [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome the Class (5 minutes)

Welcome the students to the final class of the time series unit and provide an overview of today’s lesson:

* You will use Prophet for time series forecasting.

* You’ll also experience the benefits of automating time series forecasting, including having more time for interpreting the results for decision making.

* At the end of the class, you will have all the skills that they need to succeed on the Challenge assignment. In this assignment, you will create a model that predicts web traffic for a major e-commerce entity. You’ll then take the firm’s historical revenue and build a time-series model that forecasts the revenue going forward.

Ask the students to open Google Colab, and then move to the next activity.

---

### 2. Instructor Do: Time Series Forecasting with Prophet (20 minutes)

**Corresponding Activity:** [01-Ins_Time_Series_Forecasting_Prophet](Activities/01-Ins_Time_Series_Forecasting_Prophet)

**Files:**

* [time-series-forecasting-prophet.ipynb](Activities/01-Ins_Time_Series_Forecasting_Prophet/Solved/time-series-forecasting-prophet.ipynb)

* [hourly_grid_prices.csv](Activities/01-Ins_Time_Series_Forecasting_Prophet/Resources/hourly_grid_prices.csv)

In this section, you will demo how to create a Prophet model and use it for time series forecasting. We’ll use the hourly data (the price of electricity for the area just outside Chicago, Illinois) from an activity in the previous class.

Open Google Colab, import the unsolved version of the provided Jupyter notebook, and then live-code the demonstration. Explain to the students that you’ll show them how to use Prophet for time series forecasting. Cover the following points:

* This activity uses the hourly data of the price of electricity in the Chicago, Illinois area. We used this same data in the previous class.

* Run the cells of the "Notebook Set Up" section. We need to prepare our notebook with the required libraries before using Prophet in Google Colab.

* Next, run the cells for the "Plot the Data'' and "Prepare the Data" sections. Remember that to fit a Prophet model with data, we need to rename the DataFrame columns so that  Prophet will  recognize them. Specifically, we need “ds” to be the column name for the date column, and “y” to be the column name for the variable that we want to forecast. In our case, “y” refers to the hourly prices that we can get for our electricity generation.

Explain that now it's time to predict the future by using Prophet. Here are the basic steps:

1. Create a Prophet model.

2. Fit the Prophet model.

3. Create a DataFrame to hold predictions.

4. Build a table of predictions.

Note that the following subsections provide the details for each of these steps.

#### Create a Prophet Model

Go over the following steps:

* We first create a Prophet model and store that model as a variable. In this case, we refer to the model as `m`, as the following code shows:

```python
# Call the Prophet function and store as an object
m = Prophet()
m
```

Show the output from running the code:

```text
<prophet.forecaster.Prophet at 0x7fd9e3480450>
```

* By storing the model as a variable, we can now directly run all the functions that we need by using this variable. For example, let’s fit the model to the data that we just constructed.

#### Fit the Prophet Model

Transition to the next step by explaining that the mathematics behind fitting a model is complex, but Prophet handles this task quickly. Remind the students that fitting a model to the data means training the model to recognise patterns that exist specifically in that data. When we fit a model, it is learning the patterns in our training dataset.

Continue the demo while highlighting the following information.

* To fit a Prophet model, we call the `fit` function on it and make sure to specify the data that we want to learn about. The following code demonstrates this:

  ```python
  # Fit the time series Prophet model
  m.fit(prophet_df)
  ```

  ```text
  <prophet.forecaster.Prophet at 0x7fd9e3480450>
  ```

**Note:** The execution time for fitting the model is about 35 seconds.

* Wait for the fit to complete, and then move to the next section. Explain to the students that Prophet requires just one more step to visualise the output from this model training.

#### Create a DataFrame to Hold Predictions

Explain that we can discover how well the model learned our data and also start to forecast the future by using the `make_future_dataframe` function. Highlight the following details:

* To apply this function to the model, we must specify the number of predictions ahead (`periods`) we want to make and the frequency (`freq`) of those predictions.

* We will generate a 30-day forecast. Because our data is hourly, we need to predict 720 periods ahead and specify `freq='H'`. The math for this is 24 x 30 = 720.

* Note that the `freq` parameter can take different values depending on the frequency of the time series data. The frequency can be anything from the Pandas [Offset aliases
](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-offset-aliases) list, which is the list of frequency strings. This list includes options such as business day frequency, calendar day frequency, weekly frequency, and month end frequency.

Live-code the following:

```python
# Create a future DataFrame to hold predictions
# Make the prediction go out as far as 720 hours (30 days)
future = m.make_future_dataframe(periods=720, freq='H')

# Review the first and last 10 rows of the DataFrame
display(future.head(10))
display(future.tail(10))
```

Show the following image, which depicts the resulting head and tail of the DataFrame:

![Two screenshots depict the head and the tail of the DataFrame.](Images/11-3-making-future-dataframe-with-prophet.png)

When we preview the `future` DataFrame, we can verify what is created by the `make_future_dataframe` function.

* We can observe that it contains one column of dates and times.

* This column has the same beginning date as the original dataset on which we trained the model, but it ends an additional 30 days beyond that original dataset. Now, we can make predictions.

* We’ll use this `future` DataFrame to make predictions for both the data that we already have and the data that we haven’t gotten (that is, 30 days into the future). This is known as **in-sample vs. out-of-sample predictions**.

* Explain to the students that in the world of machine learning and other statistical models, **in-sample predictions** are those that we make for the data that the model was originally trained on. We can use in-sample predictions as a first step to check whether the model is performing well.

* Ultimately, we want the model to make predictions about data that we haven't received— predictions about the future. These are called **out-of-sample predictions**.

#### Build a Table of Predictions

Explain that now we've pre-populated the `future` DataFrame with dates, we can create in-sample and out-of-sample predictions. Cover the following points:

* Remember that the pre-populated dates begin when our sample data begins and end 30 days beyond our sample data.

* We call the `predict` function on the model that we just built, as the following code shows:

```python
# Make a forecast based on the future DataFrame
forecast = m.predict(future)

# Review the first five rows of the forecast DataFrame
display(forecast.head())
display(forecast.tail())
```

* The following image shows the head and the tail of the forecast DataFrame:

  ![A screenshot depicts the DataFrame.](Images/11-3-making-forecast-using-prophet.png)

* This result, which we saved to a variable named `forecast`, is a DataFrame with lots of forecast information. Columns contain dates and upper, lower, and average estimates for the forecasted time series data. The next section will explain this in more detail.

Point out that with one function call, we predicted the electricity prices by using Prophet. But, the resulting DataFrame might be challenging to understand. The next section will explain how to interpret these predictions and how to use them for decision making. But first, we'll practice making predictions by using Prophet.

Answer any questions before moving on.

---

### 3. Student Do: Forecasting Market Opportunities with Prophet (20 minutes)

**Corresponding Activity:** [02-Stu_Forecasting_Market_Opportunities](Activities/02-Stu_Forecasting_Market_Opportunities)

**Files:**

* [Instructions](Activities/02-Stu_Forecasting_Market_Opportunities/README.md)

* [forecasting-market-opportunities.ipynb](Activities/02-Stu_Forecasting_Market_Opportunities/Unsolved/forecasting-market-opportunities.ipynb)

* [scarf-google-trends-data.csv](Activities/02-Stu_Forecasting_Market_Opportunities/Resources/scarf-google-trends-data.csv)

In this activity, the students will use time series forecasting to analyse Google Trends data.

---

### 4. Instructor Do: Review Forecasting Market Opportunities with Prophet (10 minutes)

**Files:**

* [Instructions](Activities/02-Stu_Forecasting_Market_Opportunities/README.md)

* [forecasting-market-opportunities.ipynb (unsolved)](Activities/02-Stu_Forecasting_Market_Opportunities/Unsolved/forecasting-market-opportunities.ipynb)

* [forecasting-market-opportunities.ipynb (solved)](Activities/02-Stu_Forecasting_Market_Opportunities/Solved/forecasting-market-opportunities.ipynb)

* [scarf-google-trends-data.csv](Activities/02-Stu_Forecasting_Market_Opportunities/Resources/scarf-google-trends-data.csv)

Open Google Colab, import the unsolved version of the provided notebook, and then live-code the solution. Highlight the following points:

* In this activity, we will use the same dataset about alpaca wool scarves that we used in the previous class.

* Because this is a new notebook, we start by configuring it and preparing the data by running the code cells that follow the "Step 2" heading in the notebook.

* Once we have the data prepared with the format required by Prophet, we can create a model for each country, as the following code shows:

  ```python
  # Create a Prophet model for Canada
  model_canada = Prophet()

  # Create a Prophet model for Uruguay
  model_uruguay = Prophet()
  ```

* Next, we fit the Prophet model of each country, as the following code shows:

  ```python
  # Fit the Canada Prophet model
  model_canada.fit(df_canada)

  # Fit the Uruguay Prophet model
  model_uruguay.fit(df_uruguay)
  ```

* After fitting the models, we can use the `make_future_dataframe` function from Prophet to pre-populate one year of future dates (separately for Canada and Uruguay). These will be used to hold our forecasts:

  ```python
  # Prepopulate one year of weekly future data for Canada
  future_canada = model_canada.make_future_dataframe(periods=52, freq="W")

  # Display the last five rows of the future_canada DataFrame
  future_canada.tail()

  # Forecast one year of weekly future trends data for Uruguay
  future_uruguay = model_uruguay.make_future_dataframe(periods=52, freq="W")

  # Display the last five rows of the future_uruguay DataFrame
  future_uruguay.tail()
  ```

  The following image shows the tail of each DataFrame:

  ![A screenshot depicts the two DataFrames of forecasted dates.](Images/11-3-alpaca-forecast.png)

* Finally, we use the `predict` function on both models to predict future trends, as the following code shows:

  ```python
  # Make predictions for Canada using the future_canada DataFrame
  forecast_canada = model_canada.predict(future_canada)

  # Display the first five rows of the forecast_canada DataFrame
  forecast_canada.head()

  # Make predictions for Uruguay using the future_uruguay DataFrame
  forecast_uruguay = model_uruguay.predict(future_uruguay)

  # Display the first five rows of the forecast_uruguay DataFrame
  forecast_uruguay.head()
  ```

  The following image shows the head of each DataFrame:

  ![A screenshot depicts the two DataFrames of forecasted trends.](Images/11-3-alpaca-predictions.png)

Answer any questions before moving on.

---

### 5. Instructor Do: Interpreting Prophet Forecasts for Decision Making (20 minutes)

**Corresponding Activity:** [03-Ins_Interpreting_Prophet_Forecasts](Activities/03-Ins_Interpreting_Prophet_Forecasts)

**Files:**

* [interpreting-prophet-forecasting-prophet.ipynb](Activities/03-Ins_Interpreting_Prophet_Forecasts/Solved/interpreting-prophet-forecasting-prophet.ipynb)

* [hourly_grid_prices.csv](Activities/03-Ins_Interpreting_Prophet_Forecasts/Resources/hourly_grid_prices.csv)

In this activity, the students will learn how to both visualise Prophet forecasts and interpret the results. Here, you’ll continue using the hourly data for the price of electricity for the areas near Chicago, Illinois.

Open Google Colab, import the unsolved version of the provided notebook, and run all the code cells that precede the "Plot the Forecast" section.

Explain to the students that you’ll continue analysing the data for the hourly price of electricity in the Chicago, Illinois area. You'll demonstrate how to visualise the Prophet forecast results and interpret them.

Highlight the following details:

* We can start analysing the predictions by plotting the `forecast` data. Then, we’ll learn what’s happening in more detail.

* Prophet has a built-in `plot` function for plotting forecasts, as the following code shows:

  ```python
  # Plot the forecast using the model’s plot function
  m.plot(forecast)
  ```

  The following image shows the resulting scatter plot. The dates appear along the x-axis, and the price forecast info appears along the y-axis:

  ![A screenshot depicts the scatter plot.](Images/11-3-plotting-forecast.png)

* On the plot of our forecast, the data that’s associated with values from the “ds” column appear along the x-axis. The forecast values that are associated with prices from the “y” column appear along the y-axis.

* On the plot, each black dot represents the actual data at that time.

* Notice that at the far right of the plot, no black dots exist, but the thick blue line tracking the dots continues—this indicates the forecast for prices in the future, even though Prophet hasn’t received any data for that time period.

#### Read the Forecast Results

Explain to the students that any model’s prediction will contain errors. Cover the following points:

* The line on the plot represents Prophet’s **best estimate** of the prices. But, Prophet also quantifies the amount of uncertainty that’s inherent in this estimate.

* We can examine this uncertainty (and the estimate) in more detail through the underlying `forecast` DataFrame. The following code displays the “ds”, “yhat”, “yhat_lower”, and “yhat_upper” columns in the tail of this DataFrame:

```python
# Display the underlying forecast dataframe (tail)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
```

* The following image shows the four columns in the tail of the Dataframe:

  ![A screenshot depicts the four columns.](Images/11-3-analyzing-model-uncertainty.png)

Highlight the following details regarding this DataFrame:

* As we mentioned earlier, the `forecast` DataFrame holds lots of data. Let's focus on the most important columns—those that relate to the hourly predictions for prices and those that quantify the uncertainty in the predictions.

  * “ds”: The date (and maybe the time) for which the prediction is valid.

  * “yhat”: The most likely prediction for what “y” will be, as produced by the model.

  * “yhat_lower”: The lowest prediction for what “y” will be (which is less likely to occur than “yhat”).

  * “yhat_upper”: The highest prediction for “y” (which is also less likely to occur than “yhat”).

* You might be wondering about these column names. Why does Prophet call its forecast “yhat”, for example? The answer goes back to standard statistical notations in formulas. With time series and other statistical models, we’re usually trying to predict a single column, which we generically call “y”.

* We need a way to differentiate “y”, which contains the actual values, from the model’s predictions for it. To denote that difference in formulas, we add a caret (^) over “y” when we mean the predictions for “y”. The caret looks somewhat like a hat, which is the origin of this naming convention:  “yhat” for predictions, and “y” for actual values.

* Notice that a model produces more than just a prediction. It also produces upper and lower bounds for what it thinks the prediction could be.

* These bounds are useful, because they help us gauge the reliability of the main prediction, "yhat" (which people sometimes call the **point estimate**).

#### Plot the Upper and Lower Bounds of the Forecast

Explain to the students that to get a better understanding of these three predictions, we need to reset the index on this DataFrame to the date that each prediction is for. Then, we’ll slice to only “yhat”, “yhat_lower”, and “yhat_upper”. Then, we’ll plot the last 720 rows in this DataFrame, which encompasses the rows for the 30 days of Prophet's pricing forecasts. This out-of-sample forecast is the period that we want to review.

Live-code the following:

```python
# Reset the index to this datetime column so that our plot looks nice
forecast = forecast.set_index('ds')

# Display the DataFrame
forecast.head()

# Holoviews extension to render hvPlot plots in Colab
hv.extension('bokeh')

# Plot predictions for our forecast period
forecast[['yhat', 'yhat_lower', 'yhat_upper']].iloc[-720:,:].hvplot()
```

Show the following image, which depicts an overlay plot consisting of three line plots for the three predictions: “yhat”, “yhat_lower”, and “yhat_upper”:

![A screenshot depicts the overlay plot.](Images/11-3-plotting-y-hat-predictions.png)

Highlight the following information about this overlay plot (note that the colours of the lines may vary from computer to computer):

* The blue middle line for “yhat” represents the most likely price for that day and hour. The model clearly picks up some hourly variation in the prices each day, among other cyclical patterns.

* The green upper line and the orange lower line represent the upper and lower ranges, respectively, for the predictions.

* By these three lines, the model is saying that its best guess appears in blue. However, the range of prices between the green and orange lines for each hour are all possible (although they’re certainly less likely).

#### Break Down the Forecast

Explain that time series models are useful for making forecasts as well as for understanding general patterns in our data. Highlight the following:

* Using our DataFrame of predictions (both in-sample and out-of-sample), we can use Prophet to analyse the time series patterns by calling the `plot_components` function.

* First, we have to reset the index so that “ds” becomes a column again. (Recall that we set it as an index for the plot in the preceding image.) Otherwise, the code won’t work.

Live-code the following:

```python
# Reset "ds" from the datetime index back to a column
forecast = forecast.reset_index()
forecast.head()
```

Show the following image, which depicts the head of the resulting DataFrame:

![A screenshot depicts the DataFrame.](Images/11-3-reset-ds-back-to-column.png)

Explain that we can now call the `plot_components` function to plot some of the relevant forecast information, as the following code shows:

```python
# Plot the individual time series components of the model
fig2 = m.plot_components(forecast)
```

Show the following image, which depicts the resulting four plots:

![A screenshot depicts the plots.](Images/11-3-calling-plot-components-function.png)

Explain the following information about these plots:

* The resulting plots of individual time series components from the DataFrame will help us better understand the patterns in our time series data.

* Note that one line of code produced a series of plots for us to review. Each of these four plots displays a different range and period of time.

* Essentially, the code breaks down the time series data into several patterns. These include a long-term trend in the prices, daily factors that influence the prices, a calendar trend that accounts for changes in the prices throughout the year, and even a time-of-day pattern in the prices.

  * The first plot depicts the trend in the hourly price of solar electricity on the y-axis for the years 2016 to 2021, which appears on the x-axis.

  * The second plot depicts the weekly patterns on the y-axis and the specific day of the week on the x-axis. This plot illustrates how each day of the week incrementally affects the expected price of solar energy.

  * The third plot depicts yearly trends along the y-axis and the month along the x-axis. This plot illustrates how each month of the year incrementally affects the expected price of solar energy.

  * The fourth plot depicts daily patterns on the y-axis and the time of day on the x-axis. This plot illustrates how each hour of the day incrementally affects the expected price of solar energy.

* Let’s examine these plots in more detail and then think about how we could present our findings for our scenario.

  * The first plot indicates a long-term downward trend in the cost of electricity over the last five or six years (thanks, renewables!). But, there are short-term patterns for us to discover. For example, the second plot indicates that prices are highest in the middle of the working week (Tuesday to Thursday) and at their lowest on Sundays.

  * The third plot indicates that the prices are generally at their highest in July and August,  regardless of the day. This is likely due to increased demand as people and businesses use more air conditioning to cope with the summer heat.

  * Finally, the fourth plot indicates that electricity is the most expensive from noon to 5:00 p.m. and the least expensive at around 4:00 a.m. This plot provides good news for our potential borrowers. It tells them that they can earn the highest prices for their solar electricity during the times when they’re the most likely to generate it (that is, during the sunniest times of the day).

Recap what we just did in this activity:

* Our goal was to help our potential borrowers make better investment decisions regarding loans for purchasing solar panels.

* We used Prophet to analyse electricity prices and break down price data as an hourly time series.

* We separated the data into identifiable patterns that occur across days of the week, hours of the day, and months of the year.

* By breaking down a complicated series into these types of patterns, we can better predict the future data.

Now, pose the following question to the class and show the overlay plot:

* **Question:** Recall the plot of “yhat”, “yhat_lower”, and “yhat_upper” from earlier in this lesson. How could you explain the meaning of this plot to a potential client so that they can understand how much they might be able to sell their power for?

  The following image shows the overlay plot of the three line plots for the three predictions: “yhat”, “yhat_lower”, and “yhat_upper”:

  ![A screenshot depicts the overlay plot.](Images/11-3-y-hat-predictions-callout.png)

  * **Answer:** One answer is to note that the orange line (for “yhat_lower” at the bottom of the plot) represents the worst-case scenario for the price that they’ll be able to sell their electricity for. The green line (for “yhat_upper” at the top) represents the highest price that they’re likely to receive. The most likely outcome is that they’ll be able to sell their electricity on most days for the prices that the middle blue line (for “yhat”) indicates.

Summarise and contextualise this activity for the students:

* Prophet helped us analyse our time series data by breaking down its many patterns and by producing forecasts for patterns in the future.

* We applied these patterns to the problem of predicting electricity prices, but we can use the same code to solve other problems. Examples include predicting a stock or commodity price over time, predicting sales trends in a local real-estate market, and forecasting and understanding the patterns in a company’s revenue.

Answer any questions before moving on.

---

### 6. Student Do: Interpreting Forecasting Results (20 minutes)

**Corresponding Activity:** [04-Stu_Interpreting_Forecasting_Results](Activities/04-Stu_Interpreting_Forecasting_Results)

**Files:**

* [Instruction](Activities/04-Stu_Interpreting_Forecasting_Results/README.md)

* [interpreting_forecasting_results.ipynb](Activities/04-Stu_Interpreting_Forecasting_Results/Unsolved/interpreting_forecasting_results.ipynb)

* [scarf-google-trends-data.csv](Activities/04-Stu_Interpreting_Forecasting_Results/Resources/scarf-google-trends-data.csv)

In this activity, the students will interpret the time-series forecasting results of the Google Trends data.

---

### 7. Instructor Do: Review Interpreting Forecasting Results (10 minutes)

**Files:**

* [Instruction](Activities/04-Stu_Interpreting_Forecasting_Results/README.md)

* [interpreting_forecasting_results.ipynb (unsolved)](Activities/04-Stu_Interpreting_Forecasting_Results/Unsolved/interpreting_forecasting_results.ipynb)

* [interpreting_forecasting_results.ipynb (solved)](Activities/04-Stu_Interpreting_Forecasting_Results/Solved/interpreting_forecasting_results.ipynb)

* [scarf-google-trends-data.csv](Activities/04-Stu_Interpreting_Forecasting_Results/Resources/scarf-google-trends-data.csv)

Open Google Colab, import the unsolved version of the provided notebook, and then live-code the solution. This activity complements the workflow of time-series forecasting with Prophet by allowing us to visualise and then interpret the forecast results.

Run the code cells under the "Step 2" heading in the notebook, and continue live coding the solution as you highlight the following:

* We start by using the `plot` function of the model to plot the Prophet prediction, as the following code shows:

  ```python
  # Plot the Prophet predictions for Canada
  model_canada.plot(forecast_canada)

  # Plot the Prophet predictions for Uruguay
  model_uruguay.plot(forecast_uruguay)
  ```

  The following image shows the resulting forecast plot for Canada and one for Uruguay:

  ![A screenshot depicts the plots.](Images/11-3-alpaca-forecast-plot.png)

* Next, we analyse the forecast results by using the Pandas `plot` function to plot the “yhat”, “yhat_lower”, and “yhat_upper” columns of the forecast DataFrame for both the Canada and the Uruguay models:

  ```python
  # Set the index in the forecast_canada DataFrame to the ds datetime column
  forecast_canada = forecast_canada.set_index('ds')

  # Display the forecast_canada DataFrame
  forecast_canada.head()

  # Plot predictions for our forecast_canada DataFrame for the 52 week period
  forecast_canada[['yhat', 'yhat_lower', 'yhat_upper']].iloc[-52:,:].plot()

  # Set the index in the forecast_uruguay DataFrame to the ds datetime column
  forecast_uruguay = forecast_uruguay.set_index('ds')

  # Display the forecast_uruguay DataFrame
  forecast_uruguay.head()

  # Plot predictions for our forecast_uruguay DataFrame for the 52 week period
  forecast_uruguay[['yhat', 'yhat_lower', 'yhat_upper']].iloc[-52:,:].plot()
  ```

  The following image shows the plot of the forecast "hats" for Canada and the corresponding plot for Uruguay:

  ![A screenshot depicts the plots.](Images/11-3-forecast-hats.png)

* Finally, we use the `plot_components` function on the Prophet models to analyse the patterns of the Google Trends times series data for the Canada and Uruguay models, as the following code shows:

  ```python
  # Reset the index in the forecast_canada DataFrame
  forecast_canada = forecast_canada.reset_index()

  # Use the plot_components function to visualize the forecast results
  # for the forecast_canada DataFrame
  fig_canada = model_canada.plot_components(forecast_canada)

  # Reset the index in the forecast_uruguay DataFrame
  forecast_uruguay = forecast_uruguay.reset_index()

  # Use the plot_components function to visualize the forecast results
  # for the forecast_uruguay DataFrame
  fig_uruguay = model_uruguay.plot_components(forecast_uruguay)
  ```

  The following image shows the resulting plots:

  ![A screenshot depicts the plots.](Images/11-3-alpaca-trends-plot.png)

* We can observe that the seasonal patterns in both series exist in the forecasted scenario, with a similar trend in each country. So, it's reasonable to expect that the market opportunities in the future will resemble what they were in the previous years.

Explain that, regardless of the context, the students can use Prophet to understand and forecast data while using less than 10 lines of code from start to finish. In the Challenge assignment, they’ll apply Prophet to a new context. Specifically, they’ll use Prophet to understand and forecast Google search traffic for a publicly traded company. They’ll then correlate that search traffic with the company's stock price. The goal is to discover if the ability to predict search traffic can translate into the ability to profitably trade stock.

Answer any questions before moving on.

---

### 8. Break (40 minutes)

---

### 9. Student Do: Forecasting Bitcoin Prices by Using Prophet (40 minutes)

**Corresponding Activity:** [05-Stu_Forecasting_Bitcoin_Prices](Activities/05-Stu_Forecasting_Bitcoin_Prices)

**Files:**

* [Instructions](Activities/05-Stu_Forecasting_Bitcoin_Prices/README.md)

* [forecasting-bitcoin-prices.ipynb](Activities/05-Stu_Forecasting_Bitcoin_Prices/Unsolved/forecasting-bitcoin-prices.ipynb)

* [bitcoin_hourly.csv](Activities/05-Stu_Forecasting_Bitcoin_Prices/Resources/bitcoin_hourly.csv)

This mini project provides an opportunity for the students to gain practical experience with using Prophet to forecast Bitcoin prices.

Explain that the remaining activities will help them prepare for this module’s Challenge.

Ask the students to work in teams of two or three people. You and the TAs should engage with each team during the activity to check on their progress and answer any questions.

---

### 10. Instructor Do: Review Forecasting Bitcoin Prices by Using Prophet (20 minutes)

**Files:**

* [Instructions](Activities/05-Stu_Forecasting_Bitcoin_Prices/README.md)

* [forecasting-bitcoin-prices.ipynb (unsolved)](Activities/05-Stu_Forecasting_Bitcoin_Prices/Unsolved/forecasting-bitcoin-prices.ipynb)

* [forecasting-bitcoin-prices.ipynb (solved)](Activities/05-Stu_Forecasting_Bitcoin_Prices/Solved/forecasting-bitcoin-prices.ipynb)

* [bitcoin_hourly.csv](Activities/05-Stu_Forecasting_Bitcoin_Prices/Resources/bitcoin_hourly.csv)

Open Google Colab, import the unsolved version of the provided notebook, and live-code the solution.

Because the starter code provides the code for Steps 1 and 2, run these cells, and load the data.

Review each code cell while taking time to ask the students if they have questions or need something clarified.

Once you finish the review, be sure that the students have no questions before moving forward.

---

### End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
