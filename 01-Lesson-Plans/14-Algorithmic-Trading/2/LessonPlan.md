## 14.2 Lesson Plan: Backtesting in Algorithmic Trading

---

### Overview

Algorithmic trading has become common and widely available across the financial world. But, we have a potentially enormous number of trading algorithms that use different strategies, make different decisions, and return different results. So, how does an analyst decide which strategy to incorporate into an algorithm or which trading algorithm to use for a particular portfolio? The answer is to backtest trading algorithms.

In this class, students will learn how to backtest a trading algorithm and then use the backtesting data to quantify various metrics.

In this week's Challenge, students will use backtesting to evaluate the performance of a trading algorithm based on historical stock pricing data.

### Class Objectives

By the end of class, students will be able to:

* Describe what implies to backtest an algorithmic trading strategy.

* Construct a dual moving average crossover trading signal strategy for both a long and short-position strategy.

* Evaluate the performance of a trading algorithm by using backtesting and risk/reward characteristics.

* Use the FinTA Python library to incorporate different technical indicators as trading signals in an algorithm.

### Instructor Notes

* Recall to students the legal disclaimer that is shared in the welcome activity. Warn students that the content contained in the FinTech Boot Camp is for informational and learning purposes only.

* This class includes different financial concepts related to assess the performance of a trading algorithm, reinforce the students comprehension of theses concepts by including some of your professional insights and experiences that could be share on the class.

* The final section of the class will cover trading signals as they relate to the FinTA Python library. Recall students that they should have this library installed on their virtual environment.

* In the next unit, students will start with Amazon Web Services (AWS). During this week, ask students to create an AWS account, if they don't have one, by following the "AWS Account Setup" guide that they can find in Unit 15's "Supplemental" folder.

### Class Slides and Time Tracker

The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1hQVdcF4RZivN_QOgO5ThGgHZF-eu5hTxmc8f_HRJ0AA/edit?usp=sharing).

To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

Note: Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

The time tracker for this lesson can be viewed here: [Time Tracker.xlsx](TimeTracker.xlsx)

---

### 1. Instructor Do: Welcome Class! (10 min)

Welcome students to the second day of the algorithmic trading unit, open the lesson slides and move to the "Legal Disclaimer" slide, and recall to students the educational nature of the skills that they will learn this week.

Explain to students that in Today's class they will learn how to evaluate the performance of a trading algorithm using backtest the backtesting data to quantify various metrics.

Continue on the lesson slides, move to the "Introduction to Backtesting" section and highlight the following:

* Algorithmic trading has become common and widely available across the financial world. But deciding what strategy to use may be a challenging task for financial analyst due to the enormous number of trading algorithms that can be used.

* To help on deciding what algorithmic trading strategy could be the best for a particular portfolio, we can use backtesting.

* Backtesting is a method that allows us to assess how well a strategy works retrospectively, using historical data to validate how accurately the strategy would have predicted the actual results.

Explain to students, that although we can backtest and apply a trading algorithm to essentially anything that's tradeable&mdash;whether it's stocks, bonds, or crypto&mdash;, no single trading strategy works for every individual or situation.

Ask the following question and spend a couple of minutes listening to students insights.

* **Question:** What’s an optimal trading algorithm?

  * **Possible Answer:** At a glance, the optimal trading algorithm is the one that fits the investor's risk tolerance; as its name suggests, it is the level of risk that an investor is willing to tolerate.

Explain to students, that measuring the risk an investor can tolerate may depend on each individual. However, at a glance, individuals who are more **risk averse** want more-conservative trading strategies, or those with less potential profit but also less risk of loss. By contrast, **risk tolerant** individuals are willing to take on more-speculative trading strategies, or those with the potential for great profit but also for great loss. An individual might also feel more risk averse in one situation and more risk tolerant in another.

Use the following example to illustrate risk tolerance:

* You might treat your retirement account differently than the short-term account that you use to fund your day-to-day living expenses.

* You may want to take more risk with your retirement account if a long time will elapse until you’ll need the funds. By contrast, if you need the funds from your short-term account to pay the mortgage or rent next month, you won’t have time to make up for potential investment losses.

Explain to students that in the financial world, **risk-averse individuals** are often categorised as investors who want low-risk, low-volatility investments, which should gain gradual profits over the long term. **Risk-loving individuals** are often categorised as investors who want high-risk, high-volatility investments, which should profit from short-term price fluctuations.

Present to students the "Risk Tolerance Scale" and highlight the following:

![Risk tolerance scale](Images/15-2-risk-tolerance-scale.png)

* The Risk Tolerance Scales illustrate the concept of risk tolerance on a continuum from low risk to high risk.

* This scale summarises the  characteristics of each type of investor, from conservative to aggressive as follows:

  * Conservative: Primarily focused on capital preservation. Willing to forgo potentially higher returns in exchange for protecting current assets.

  * Moderately Conservative: Willing to accept a small measure of risk in exchange for potentially higher returns, but still primarily focused on protecting the current principal balance.

  * Moderate: Demonstrates an equal interest in reducing risk and providing higher returns.

  * Moderately Aggressive: Primarily focused on long-term returns for the portfolio, and willing to accept significant levels of risk to achieve them.

  * Aggressive: Primarily focused on maximising portfolio returns and performance. The risk level is extremely high, and the loss of capital is likely.

Explain to students that a financial advisor usually discovers a customer's risk tolerance and then determines a trading strategy appropriate for the customer’s needs. We can take similar steps for algorithmic trading. We first evaluate a trading algorithm to determine its risk/reward characteristics. Based on this information, we then determine whether the algorithm meets our needs.

Be sure that there are no questions before moving forward.

---

### 2. Instructor Do: Backtesting a Trading Algorithm (20 min)

In this activity students will learn how to backtest a trading algorithm using Python.

Open the `Unsolved` folder in Jupyter Notebook for activity 1.

#### DMAC Trading Algorithm Review

**Files:**

* [Backtesting a Trading Algorithm](Activities/01-Ins_Backtesting_a_Trading-Algorithm/Unsolved/Backtesting_a_Trading-Algorithm.ipynb)

Begin the class discussing the steps to implement a trading algorithm with risk vs. reward. Open the lesson slides, move to the section "Risk Vs. Reward" and highlight the following:

* Backtesting helps gauge an algo strategy's risk/reward characteristics. To determine whether it suits your personal risk tolerance (or that of your client).

* It also supplies a standardised baseline for assessing the relative performance of different trading algorithms.

* In order to backtest a trading algorithm, we feed it historical stock data to analyse its trading performance and its risk/reward characteristics for a hypothetical portfolio. In our example our portfolio that we are going to test, we will give it a value of $100,000.

* This will help students prepare for the homework this week, which will involve comparing the performance of multiple algorithm trading models over the same historical time period.

* Traders use backtesting to compare the viability of trading strategies that they might employ, as well as to tweak successful strategies.

* Analysts for major companies also use backtesting as a way to test and compare various trading techniques that might be used in a large investment portfolio.

* In summary, backtesting involves applying a strategy or predictive model to historical data to determine its accuracy.

Explain to students that this activity will introduce them to backtesting, by using the DMAC (Dual Moving Average Crossover) trading algorithm that we developed in the previous lesson, but then backtesting this algorithm with a specific amount of investment capital.

Open the starter file provided above, and live code the following.

First, we’ll review how to create the DMAC algorithm, and then we’ll backtest it.

#### Re-Create the DMAC Algorithm

* Let's start importing the required libraries.  We then read historical stock data for AAPL from a CSV file into a Pandas DataFrame.

``` python
# Import the required libraries and dependencies
import numpy as np
import pandas as pd
import hvplot.pandas
from pathlib import Path

# Read the stock file to a dataframe
# Set the date column as the DataTimeIndex
aapl_df = pd.read_csv(
    Path("../Resources/aapl.csv"),
    index_col="date",
    parse_dates=True,
    infer_datetime_format=True)

# Review the DataFrame
aapl_df.head()
```

Display the dataframe for the class:
![Apple stock dataframe](Images/15-2-aapl-stock-dataframe.png)

* Next, we need to regenerate the trading signals that specify when our algorithm should enter or exit a trade. For now, we'll slice to just the `close` column:

```python
# Slice to just the `close` column
signals_df = aapl_df.loc[:,["close"]]
```

* Create long-window (100-day) and short-window (50-day) SMAs (Simple Moving Averages). Start by setting the short and long window parameters.

```python
# Set the short window and long windows
short_window = 50
long_window = 100
```

* With the long and short windows defined, we can create the simple moving averages. While we're here, we'll also pre-populate a `Signal` column for trading.

```python
# Generate the short and long moving averages (50 and 100 days, respectively)
signals_df['SMA50'] = signals_df['close'].rolling(window=short_window).mean()
signals_df['SMA100'] = signals_df['close'].rolling(window=long_window).mean()
# Prepopulate the `Signal` for trading
signals_df['Signal'] = 0.0
```

* After that, use the `where` function from `numpy` to specify the points in time when the algorithm should enter or exit a trade.

* We will use a value of `1` to indicate an entry (buy) and a value of `0` to indicate an exit (sell).

    ```python
    # Generate the trading signal 0 or 1,
    # where 1 is when short-window (SMA50) is greater than the long (SMA 100)
    # and 0 otherwise
    signals_df['Signal'][short_window:] = np.where(
        signals_df['SMA50'][short_window:] > signals_df['SMA100'][short_window:], 1.0, 0.0
    )
    ```

* By running the `diff` (difference) function on this new `Signal` column, we can mark changes in opportunities to buy or sell.

* Specifically, the `diff` function will specify the points in time when the algorithm should enter, exit, or hold the trade.

  * A value of `1` (when the signal changes from `0` to `1`) will indicate that the algorithm should enter a trade

  * A value of `-1` (when the signal changes from 1 to 0) indicates that we should exit the trade.

  * A value of `0` (when there's no change in the signal value) indicates that the algorithm should hold the position.

    ```python
    # Calculate the points in time when the Signal value changes
    # Identify trade entry (1) and exit (-1) points
    signals_df['Entry/Exit'] = signals_df['Signal'].diff()

    # Review the DataFrame
    signals_df.tail(10)
    ```

The following image shows the resulting signals_df DataFrame:

![APPL Signals Dataframe ](./Images/15-2-aapl-long-short-sma.png)

From the DataFrame columns, highlight the following to students:

* The DataFrame includes the `close`, `SMA50`, `SMA100`, `Signal`, and `Entry/Exit` columns.

* These contain the AAPL closing prices, the 50- and 100-day SMAs, the trading signals, and the flags for the entry and exit points of the trade.

* During the time period of the tail of this DataFrame, no such entry or exit points are flagged.

* Next, plot the entry and exit points against the closing price of AAPL stock. Note to students how each of these objects (`exit`, `entry`, and so forth) are individual plots. With `hvplot` we can easily combine them, overlaid onto each other into one plot, using the multiplication sign.

```python
# Visualize exit position relative to close price
exit = signals_df[signals_df['Entry/Exit'] == -1.0]['close'].hvplot.scatter(
    color='yellow',
    marker='v',
    size=200,
    legend=False,
    ylabel='Price in $',
    width=1000,
    height=400
)

# Visualize entry position relative to close price
entry = signals_df[signals_df['Entry/Exit'] == 1.0]['close'].hvplot.scatter(
    color='purple',
    marker='^',
    size=200,
    legend=False,
    ylabel='Price in $',
    width=1000,
    height=400
)

# Visualize close price for the investment
security_close = signals_df[['close']].hvplot(
    line_color='lightgray',
    ylabel='Price in $',
    width=1000,
    height=400
)

# Visualize moving averages
moving_avgs = signals_df[['SMA50', 'SMA100']].hvplot(
    ylabel='Price in $',
    width=1000,
    height=400
)

# Create the overlay plot
entry_exit_plot = security_close * moving_avgs * entry * exit

# Show the plot with a title
entry_exit_plot.opts(
    title="Apple - SMA50, SMA100, Entry and Exit Points"
)
```

The following image below shows the overlay plot:

![APPL Signals Overlay Plot](./Images/15-2-aapl-entry-exit-overlay-plot.png)

* Point out that the plot represents the entry points as upward-pointing purple markers and the exit points as downward-pointing yellow markers.  The plot also includes the “SMA50”, “SMA100”, and closing price lines.

#### Backtesting the Algorithm

* Now that we've built the algorithm, we can backtest its profitability.

* The first step is to set the initial capital investment to $100,000. Each time the algorithm trades, let's set the number of shares to trade to 500.

* This means that for each trade, we’ll buy or sell 500 shares of AAPL stock.

```python
# Set initial capital
initial_capital = float(100000)

# Set the share size
share_size = 500
```

* With our portfolio size constructed, we can then create columns in our DataFrame for calculating various backtesting metrics.

* The first metric keeps track of our stock position.

  * The `Position` column will contain the number of shares of AAPL stock that the algorithm holds.

  * This algorithm buys a 500-share position when the DMAC `Signal` column contains a value of `1` (that is, when the `SMA50` value is greater than the `SMA100` value).

  * The algorithm then holds these 500 shares until the `Signal` column reverts to a value of `0` (that is, when the `SMA50` value is less than the `SMA100` value), which triggers the sale.

* The number of shares traded (`Position`) is then found by multiplying the share size (here, 500) by the sign in the `Signal` column. Since `Signal` takes the value of `1` or `0`, values for the `Position` column with either be `500` or `0`.

```python
# Buy a 500 share position when the dual moving average crossover Signal equals 1
# Otherwise, `Position` should be zero (sell)
signals_df['Position'] = share_size * signals_df['Signal']
```

* The `Entry/Exit Position` column will be created using the Pandas `diff` function, to find the specific points in time when the algorithm either buys or sells the 500-share position (which it determines from the `Position` column).

  * This column can contain a value of `500` to mean entry (when the `Position` value changes from 0 to 500).

  * OR `-500` for exit (when the “Position” value changes from `500` to `0`), or `0` for hold (when no change occurs in the “Position” value from one day to the next).

```python
# Determine the points in time where a 500 share position is bought or sold
signals_df['Entry/Exit Position'] = signals_df['Position'].diff()

```

Next, create a `Portfolio Holdings` column.

* This column contains the dollar value of the AAPL shares that the algorithm holds. This column is used to determine the algorithm’s ROI.

* `Portfolio Holdings` is calculated by multiplying the AAPL price in the `close` column by the “Position” value, which is the number of shares that the algorithm holds at that time.

```python
# Multiply the close price by the number of shares held, or the Position
signals_df['Portfolio Holdings'] = signals_df['close'] * signals_df['Position']
```

* The `Portfolio Cash` column contains the amount of available cash that the portfolio holds. The first value in this column is the value of the initial capital investment—$100,000.

  * When the algorithm buys AAPL stock, the portfolio cash decreases by the cost of the trade (500 shares multiplied by the `close` price).

  * When the algorithm sells stock, the portfolio cash increases by the proceeds from the trade (−500 shares multiplied by the `close` price).

* The running value of cash in the portfolio, at any given time, can be calculated using the `cumsum` function.
  * If a trade entry or exit is triggered, this triggers a share sale at the prevailing closing price.
  * The running sum of these (`cumsum`) of this is then the current cumulative value of the portfolio--it's what the total equity position is worth.
  * If we subtract this current total equity position from our `initial_capital`, we have a running number for the amount of cash we have on hand each day.

```python
# Subtract the amount of either the cost or proceeds of the trade from the initial capital invested
signals_df['Portfolio Cash'] = initial_capital - (signals_df['close'] * signals_df['Entry/Exit Position']).cumsum()
```

* The `Portfolio Total` column contains the current value of the portfolio, which is the value of the held stock plus the value of the portfolio cash.

* Calculate this value by adding the portfolio cash to the portfolio holdings.

```python
# Calculate the total portfolio value by adding the portfolio cash to the portfolio holdings (or investments)
signals_df['Portfolio Total'] = signals_df['Portfolio Cash'] + signals_df['Portfolio Holdings']
```

* The `Portfolio Daily Returns` column contains the daily return percentage of the portfolio total, or the day-to-day change in the value of the portfolio expressed as a percentage.

* Calculate this by calling the `pct_change` function on the `Portfolio Total` value.

```python
# Calculate the portfolio daily returns
signals_df['Portfolio Daily Returns'] = signals_df['Portfolio Total'].pct_change()
```

* The `Portfolio Cumulative Returns` column calculates the cumulative return value of the portfolio, or the aggregate percentage amount that the portfolio has gained or lost over the period.

* Calculate this by calling the `cumprod` function on the `Portfolio Daily Returns`.

```python
# Calculate the portfolio cumulative returns
signals_df['Portfolio Cumulative Returns'] = (1 + signals_df['Portfolio Daily Returns']).cumprod() - 1
```

* Finally, we can print our DataFrame to get our results!

```python
# Print the DataFrame
signals_df.head(150)
```

* The parameter of the head function was to print the first 150 rows of the DataFrame. This is to show the changing backtest results over time. And, the long- and short-window SMAs require at least 100 and 50 points of data, respectively.

#### Visualizing the Backtested Results

* Explain to students that now that we've built all the columns we need to evaluate backtest performance, we can now visualise this performance using `hvPlot`.

* In particular, we'll plot the algorithm's entry and exit trades against the running portfolio total.

* The benefit to this is it is easier then to further visualise the performance of the trading algorithm in the context of our initial portfolio investment of $100,000.

* Live code the following three hvPlots. Remind students that all that is happening is that we're creating three individual line plots in hvPlot, saving them to variables (`exit`, `entry` and `total_portfolio_value`), and then overlaying all these plots into a single one using hvPlot notation.

```python
# Visualize exit position relative to total portfolio value
exit = signals_df[signals_df['Entry/Exit'] == -1.0]['Portfolio Total'].hvplot.scatter(
    color='yellow',
    marker='v',
    legend=False,
    ylabel='Total Portfolio Value',
    width=1000,
    height=400
)

# Visualize entry position relative to total portfolio value
entry = signals_df[signals_df['Entry/Exit'] == 1.0]['Portfolio Total'].hvplot.scatter(
    color='purple',
    marker='^',
    ylabel='Total Portfolio Value',
    width=1000,
    height=400
)

# Visualize the value of the total portfolio
total_portfolio_value = signals_df[['Portfolio Total']].hvplot(
    line_color='lightgray',
    ylabel='Total Portfolio Value',
    xlabel='Date',
    width=1000,
    height=400
)

# Overlay the plots
portfolio_entry_exit_plot = total_portfolio_value * entry * exit
portfolio_entry_exit_plot.opts(
    title="Apple Algorithm - Total Portfolio Value",
    yformatter='%.0f'
)
```

Resulting overlay plot:
![Apple backtesting plot](./Images/15-2-apple-backtest-overlay-plot.png)

***Interpreting Backtest Results from the Overlay Plot***

* Point out to students that a number of insights can be gained from this overlay plot.

* First, it highlights the fact that the total value of the portfolio changed with each entry and exit of a 500-share position in AAPL.

* Second, the trading algorithm made close to `$33,000` during the backtesting period overall, leaving us with a final portfolio value of `$132,975`.

* Notice, the gains didn’t remain consistent over time, which is our third insight. During the period that we measured, the value of the portfolio dropped as low as `$80,000`.

* Discuss visualising the potential upside (gains) and downside (risks) of an algorithm over time proves just as important (if not more so) than measuring the profitability of any particular trade.

* In this case, the backtest results show that the algorithm produced an upside cumulative return of about 30%. However, trade performance overall was quite volatile, with a downside of almost 20% at one point.

* Based on this visual information, it might not be wise to use this algorithm—or buy this stock for the portfolio of an investor who is risk averse or has a short-term time horizon, as there are lengthy periods when an investor in this algorithm would have experienced losses before eventually realising a profit.

Be sure that there are no questions before moving forward.

---

### 3. Student Do: Backtest Your Short-Position Algorithm (20 min)

**Corresponding Activity:**[02-Stu_Backtest_Your_Short-Position_Algorithm](Activities/02-Stu_Backtest_Your_Short-Position_Algorithm)

**Files:**

* [Instructions](Activities/02-Stu_Backtest_Your_Short-Position_Algorithm/README.md)

* [vnq.csv](Activities/02-Stu_Backtest_Your_Short-Position_Algorithm/Resources/vnq.csv)

* [Backtest Your Short-Position Algorithm (Unsolved)](./Activities/02-Stu_Backtest_Your_Short-Position_Algorithm/Unsolved/backtest_your_short_position_algorithm.ipynb)

In this activity, students will backtest an algorithm to determine both the changes to the overall portfolio values and the daily return and cumulative return metrics.

Specifically, they'll revisit the short-position DMAC trading algorithm that was developed in the previous lesson, but this time, they'll backtest the short-position strategy that it used in order to trade a real estate stock (`VNQ`) during the 2008 recession.

Be sure to check in with students that may need help throughout the activity.

---

### 4. Instructor Do: Review Backtest Your Short-Position Algorithm (10 min)

**Corresponding Activity:**[02-Stu_Backtest_Your_Short-Position_Algorithm](Activities/02-Stu_Backtest_Your_Short-Position_Algorithm)

**Files:**

* [Backtest Your Short-Position Algorithm (Unsolved)](./Activities/02-Stu_Backtest_Your_Short-Position_Algorithm/Unsolved/backtest_your_short_position_algorithm.ipynb)

* [Backtest Your Short-Position Algorithm (Solved)](./Activities/02-Stu_Backtest_Your_Short-Position_Algorithm/Solved/backtest_your_short_position_algorithm.ipynb)

* [vnq.csv](Activities/02-Stu_Backtest_Your_Short-Position_Algorithm/Resources/vnq.csv)

Open the solution and explain the following:

* The `signal` is constructed by looking at the difference between short and long term simple moving averages.

* Wherever the short term moving average is less than the long, the `signal` column has a value of `1`, and otherwise is `0`.

``` python
signals_df['Signal'][short_window:] = np.where(
   signals_df['SMA50'][short_window:] < signals_df['SMA100'][short_window:], 1.0, 0.0
)
```

* As before, entry and exit points are denoted by any change (`diff`) in the value of the `Signal`:

```python
# Calculate the points in time at which a position should be taken, 1 or -1
signals_df['Entry/Exit'] = signals_df['Signal'].diff()
```

* With Entry and Exit Points defined, we can plot them along with the stock price using `hvPlot`:

```python
# Visualize entry positions relative to close price
entry = signals_df[signals_df['Entry/Exit'] == 1.0]['Close'].hvplot.scatter(
   color='purple',
   marker='^',
   legend=False,
   ylabel='Price in $',
   width=1000,
   height=400)
​
# Visualize exit positions relative to close price
exit = signals_df[signals_df['Entry/Exit'] == -1.0]['Close'].hvplot.scatter(
   color='orange',
   marker='v',
   legend=False,
   ylabel='Price in $',
   width=1000,
   height=400)
​
# Visualize the close price for the investment
security_close = signals_df[['Close']].hvplot(
   line_color='lightgray',
   ylabel='Price in $',
   width=1000,
   height=400)
​
# Visualize the moving averages
moving_avgs = signals_df[['SMA50', 'SMA100']].hvplot(
   ylabel='Price in $',
   width=1000,
   height=400)
​
# Overlay the plots
entry_exit_plot = security_close * moving_avgs * entry * exit
entry_exit_plot.opts(
   title="VNQ - Short-Position Dual Moving Average Trading Algorithm"
)
```

* Finally, we can write the python code to keep track of investment performance if we were to allocated $100,000 to this investment strategy.

* Set an `initial_capital` variable to `100000` to represent the starting value (100,000) of your simulated portfolio. Create this variable as a floating point number.

```python
# Set the initial_capital to 100000
initial_capital = float(100000)
```

* Set a `share_size` variable to negative 500 shares (-500).

```python
# Set the share_size to -500
# In a short-position strategy, shares are sold before they are bought
share_size = -500
```

* Create a new column named `Position` by multiplying the `share_size` value by the values in the `Signal` column.

```python
# Create a column named "Position" by multiplying the share_size by the Signal
# Sell a position (-500 shares) when the dual moving average crossover Signal equals 1 (SMA50 is less than SMA100)
# Buy a position (500 shares) when the dual moving average crossover Signal equals 0 (SMA50 is greater than SMA100)
signals_df["Position"] = share_size * signals_df["Signal"]
​
# Review the DataFrame
signals_df.tail()
```

* Create a new column named `Entry/Exit Position` by calling the diff function on the `Position` column.

```python
# Find the points in time where a 500 share position is bought or sold
signals_df["Entry/Exit Position"] = signals_df["Position"].diff()
​
# Review the DataFrame
signals_df.tail()
```

* Create a new column named `Portfolio Holdings` by multiplying the `Close` prices of VNQ by the values in the `Position` column.

```python
# Create a Portfolio Holdings column by multiplying the Close price by the Position
signals_df["Portfolio Holdings"] = signals_df["Close"] * signals_df["Position"]
​
​
# Review the DataFrame
signals_df.tail()
```

* Create a new column named `Portfolio Cash` by subtracting the cumulative sum of the trades that the `Entry/Exit Position` column indicates from the `initial_capital` value.

```python
# To calculate Portfolio Cash, subtract the cumulative sum of the trade cost/proceeds from the initial_capital
# The trade cost proceeds are calculated by multiplying the Close price by Entry/Exit Position
signals_df["Portfolio Cash"] = (
   initial_capital - (signals_df["Close"] * signals_df["Entry/Exit Position"]).cumsum()
)
​
# Review the DataFrame
signals_df.tail()
```

* Create a new column named `Portfolio Total` by adding the values of the `Portfolio Cash` and `Portfolio Holdings` columns.

```python
# Calculate the Portfolio Total value by adding Portfolio Cash and Portfolio Holdings
signals_df["Portfolio Total"] = signals_df["Portfolio Cash"] + signals_df["Portfolio Holdings"]
​
# Review the DataFrame
signals_df.tail()
```

* Create a new column named `Portfolio Daily Returns` by calling the `pct_change` function on the `Portfolio Total` column to calculate the percent change.

```python
# Calculate the Portfolio Daily Returns based on the Portfolio Total
signals_df["Portfolio Daily Returns"] = signals_df["Portfolio Total"].pct_change()
​
# Preview the DataFrame
signals_df.tail()
```

* Create a new column named `Portfolio Cumulative Returns` by calling the `cum_prod` function on the `Portfolio Daily Returns` column.

```python
# Calculate the Portfolio Cumulative Returns based on the Portfolio Daily Returns
signals_df["Portfolio Cumulative Returns"] = (
   1 + signals_df["Portfolio Daily Returns"]
).cumprod() - 1
​
# Review the DataFrame
signals_df.tail()
```

* Use the hvplot function to plot the short-position DMAC trading strategy against its backtesting results.

```python
# Visualize the entry positions relative to the Portfolio Total
entry = signals_df[signals_df["Entry/Exit"] == 1.0]["Portfolio Total"].hvplot.scatter(
   color='purple',
   marker='^',
   legend=False,
   ylabel="Total Portfolio Value",
   width=1000,
   height=400
)
​
# Visualize the exit positions relative to the Portfolio Total
exit = signals_df[signals_df["Entry/Exit"] == -1.0]["Portfolio Total"].hvplot.scatter(
   color='orange',
   marker='v',
   legend=False,
   ylabel="Total Portfolio Value",
   width=1000,
   height=400
)
​
# Visualize Portfolio Total for the investment
total_portfolio_value = signals_df[["Portfolio Total"]].hvplot(
   line_color="lightgray",
   ylabel="Total Portfolio Value",
   width=1000,
   height=400
)
```

```python
# Overlay the entry, exit and total_portfolio_value plots
portfolio_entry_exit_plot = total_portfolio_value * entry * exit
portfolio_entry_exit_plot.opts(
   title="VAQ Short-Position Algorithm - Total Portfolio Value",
   yformatter='%.0f'
)
```

Close the activity review by posing the following question to students:

* **Question**: Does it appear that this algorithm suits a short-position trading strategy?

  * **Sample Answer**: Although the value of the portfolio did fall below the initial investment of 100,000, the drop in the stock price in 2008 and 2009 benefited the algorithm's short-position strategy and the portfolio did make money.

---

### 5. Instructor Do: Assessing the Risk/Reward Characteristics of a Trading Algorithm (20 min)

**Corresponding Activity:** [03-Ins_Assessing_Risk_Reward](Activities/03-Ins_Assessing_Risk_Reward)

In this activity, students will employ risk/reward metrics to assess a trading algorithm.

**Files:**

* [assessing_risk_reward.ipynb](Activities/03-Ins_Assessing_Risk_Reward/Unsolved/assessing_risk_reward.ipynb)

* [trading_signals.csv](Activities/03-Ins_Assessing_Risk_Reward/Resources/trading_signals.csv)

Explain to students that besides using historical data to backtest a trading algorithm, it's also essential to assess the risk/reward characteristics to determine whether it suits a particular portfolio. Also, we need to use metrics to analyse an algorithm at a more granular level quantitatively.

Open the lesson slides, move to the "Risk/Rewards Characteristics of a Trading Algorithm" section and explain to students that there are two considerations that should be done when we backtest a trading algorithm: past vs. future performance and risk/reward management.

Regarding considering past vs. future performance highlight the following:

* When we backtest a trading algorithm, the results are based on historical data. This means that backtesting might demonstrate that the algorithm would have been profitable in the past. However, it doesn’t guarantee how the algorithm will perform in the future.

* Just like a machine learning model can overfit to its training data and not perform well on the testing data, an algorithmic trading strategy that’s designed to succeed with past data might not work with future data.

As to considering risk/reward management, highlight the following:

* Due to the inherent uncertainty about future profitability, the golden rule of trading is to use risk/reward management.

* Since future market conditions are unknowable, traders should make investments only when they feel comfortable with the level of risk that’s required for achieving a certain level of profit. That is, traders need to consider the amount of money that they might lose in their pursuit of a certain amount of profit.

* Before deploying a trading algorithm, we need to analyse the algorithm's overall risk/reward characteristics at both the portfolio and per-trade level. This will help us understand how much money the trading algorithm might make. More importantly, it will help us understand how much it might lose relative to its overall profitability.

Finally, explain to students that at a glance, the risk/reward characteristics of a trading strategy can be understood as the amount of risk, or the potential loss, that a person assumes for an investment with the expectation of returning a gain, or an expected amount of profit.

Now, explain to students that you will demonstrate how the risk/reward evaluation metrics can be implemented to our trading algorithm using Python.

#### Generating the Risk/Reward Evaluation Metrics

Open the Jupyter notebook provided in the `Unsolved` folder. Explain to students that for this demo, they will use a CSV file that contains the information from the backtesting data that we did before using Apple stock data.

Start by loading the required libraries and reading the data into a DataFrame.

```python
# Import the required libraries and dependencies
import numpy as np
import pandas as pd
from pathlib import Path

# Read the trading_signals.csv file into a Pandas DataFrame
# Set the date column as the DateTimeIndex
signals_df = pd.read_csv(
    Path('../Resources/trading_signals.csv'),
    index_col="date",
    parse_dates=True,
    infer_datetime_format=True)

# Review the DataFrame
signals_df.tail(10)
```

The following image shows the resulting DataFrame.

![Sample backtest data](Images/15-2-aapl-backtest-dataframe-import.png)

Explain to students that in addition to the `close` column, this DataFrame has the columns that we created for the DMAC algorithm and for supporting the backtest analysis.

After loading the data, explain to students that now you will create a new DataFrame that will contain the portfolio-level metrics that will offer insight into the risk/reward characteristics of our trading algorithm.

Explain to students that the new DataFrame that you will create will consist of a single column, named `Backtest`, and will have the name of the metrics as the index values of the DataFrame.

Before creating the DataFrame, jump back to the lesson slides for a moment to explain the following metrics to students.

* `Annualized Return`: A metric that represents the expected ROI over a time period of one year. We calculate it by first averaging the daily return values over the time period of the dataset. We then multiply that average daily return value by 252, or the number of trading days in a year.

* `Cumulative Returns`: The aggregate percentage return (that is, the percentage gain or percentage loss) for an investment. We usually measure the cumulative return across the entire investment rather than for a particular time period.

* `Annual Volatility`: The amount that each daily return value differs from the asset's average daily return value (that is, the standard deviation of the asset’s daily return values), measured on an annualised basis. The annual volatility helps determine the amount that the stock will potentially gain or lose vs. the expected amount, over a single year.

* `Sharpe Ratio`”`: A measurement of an asset's outperformance as compared to the asset’s volatility. The outperformance is measured by the difference between the asset's ROI and the return expected from an asset assumed to have no risk, like a three-month US Treasury bill. (Because three-month Treasury bill returns are, these days, zero, we usually just exclude this last term from the formula). The asset's volatility is characterized by the standard deviation of its daily return values.

* `Sortino Ratio`: A variation of the Sharpe ratio that differentiates an asset’s harmful volatility from its overall volatility. The Sharpe ratio measures an investment’s ROI vs. its volatility, treating positive or negative results the same way. By contrast, the [Sortino ratio](https://www.investopedia.com/terms/s/sortinoratio.asp) focuses on the **downside standard deviation**, which measures the downside volatility of the asset. The distinction has relevance, because investors tend to have more concern about negative surprises than positive ones.

Remind students that we covered some of these metrics and their calculations, like the annualised return, annual volatility, and Sharpe ratio, in the initial units of the Bootcamp when we learned Pandas.

Go back to the Jupyter notebook, and live code the creation of the new DataFrame as follows.

```python
# Create a list for the column name
columns = ["Backtest"]

# Create a list holding the names of the new evaluation metrics
metrics = [
    "Annualized Return",
    "Cumulative Returns",
    "Annual Volatility",
    "Sharpe Ratio",
    "Sortino Ratio"]

# Initialize the DataFrame with index set to the evaluation metrics and the column
portfolio_evaluation_df = pd.DataFrame(index=metrics, columns=columns)

# Review the DataFrame
portfolio_evaluation_df
```

![A screenshot depicts the DataFrame.](Images/15-2-evaluation-dataframe-empty-metrics.png)

Now that we have structured the DataFrame, explain to students that we will to perform the calculations to fill in the values for each metric. Live code the calculation of each metric as it's explained next.

##### Annualised Return

For the annualised return metric, explain to students that we first use the mean function to calculate the average daily return of the asset over the time period of the dataset. We then multiply the result by 252, or the number of trading days in a year, as the following code shows:

```python
# Calculate annualised return
portfolio_evaluation_df.loc["Annualized Return"] = (
    signals_df["Portfolio Daily Returns"].mean() * 252
)

# Review the result
portfolio_evaluation_df
```

![A screenshot depicts the DataFrame.](Images/15-2-backtested-annualized-return.png)

##### Cumulative Returns

Recall to students that we already calculated the cumulative returns metric during our original backtesting process. So, in the following code we can thus use the last value in the `Portfolio Cumulative Returns` column of our `signals_df` DataFrame, as the following code shows.

```python
# Calculate cumulative return
portfolio_evaluation_df.loc["Cumulative Returns"] = signals_df["Portfolio Cumulative Returns"][-1]

# Review the result
portfolio_evaluation_df
```

![A screenshot depicts the DataFrame.](Images/15-2-backtested-cumulative-returns.png)

##### Annual Volatility

For the annual volatility metric, explain to students that we use the Pandas `std` function to calculate the standard deviation of the daily returns for our portfolio. We then multiply that value by the square root of 252 trading days, using the NumPy `np.sqrt` function to do so, as the following code shows.

```python
# Calculate annual volatility
portfolio_evaluation_df.loc["Annual Volatility"] = (
    signals_df["Portfolio Daily Returns"].std() * np.sqrt(252)
)

# Review the result
portfolio_evaluation_df
```

![A screenshot depicts the DataFrame.](Images/15-2-backtested-annual-volatility.png)

##### Sharpe Ratio

For the Sharpe ratio, explain to students that we compute it by dividing the annualised return metric by the annualised volatility metric, as the following code shows.

```python
# Calculate Sharpe ratio
portfolio_evaluation_df.loc["Sharpe Ratio"] = (
    signals_df["Portfolio Daily Returns"].mean() * 252) / (
    signals_df["Portfolio Daily Returns"].std() * np.sqrt(252)
)

# Review the result
portfolio_evaluation_df
```

![A screenshot depicts the DataFrame.](Images/15-2-backtested-sharpe-ratio.png)

##### Sortino Ratio

The last metric to compute is the Sortino ratio. Explain to students that this ratio is a metric that measures an asset's downside risk, so we will need a multi-part calculation as follows:

* First, we calculate the downside return values. To do so, we square each of the asset’s negative daily return values.

* Second, we calculate the annualised return value of the asset.

* Finally, to calculate the Sortino ratio, we divide the annualised returns by the annualised standard deviation of the downside return values.

Explain to students that to calculate the downside return values, we create a new DataFrame that consists of two columns. The first column contains the `Portfolio Daily Returns` values from the `signals_df` DataFrame. We name the second column `Downside Returns`. To fill the `Downside Returns` column, we find the dates when the `Portfolio Daily Returns` values are less than 0, square only those values, and then add the squared values to the column for those dates, as the following code shows.

```python
# Create a DataFrame that contains the Portfolio Daily Returns column
sortino_ratio_df = signals_df[['Portfolio Daily Returns']].copy()

# Create a column to hold downside return values
sortino_ratio_df.loc[:,'Downside Returns'] = 0

# Find Portfolio Daily Returns values less than 0,
# square those values, and add them to the Downside Returns column
sortino_ratio_df.loc[sortino_ratio_df['Portfolio Daily Returns'] < 0,
                     'Downside Returns'] = sortino_ratio_df['Portfolio Daily Returns']**2

# Review the DataFrame
sortino_ratio_df.tail()
```

![A screenshot depicts the DataFrame.](Images/15-2-sortino-ratio-downside-returns-dataframe.png)

Explain to students that as it can be seen on this DataFrame, where the `Portfolio Daily Returns` column contains a negative value, the `Downside Returns` column contains the square of the `Portfolio Daily Returns` value.

For the second part of our Sortino ratio calculation, explain to students that we start by determining the annualised return value of our portfolio. To do so, we average the `Portfolio Daily Returns` values, and multiply the average by the number of trading days in the year (252) as can be seen in the code below.

```python
# Calculate the annualized return value
annualized_return = (
    sortino_ratio_df["Portfolio Daily Returns"].mean() * 252
)

# Print the result
print(f"Annualized Return: {annualized_return}")
```

```text
Annualized Return: 0.06668285491297833
```

Next, explain to students that we calculate the annualised downside standard deviation of the portfolio. To do so, we find the square root of the average of our downside return values. Then, we multiply this number by the square root of the number of trading days in the year (252):

```python
# Calculate the annualised downside standard deviation value
downside_standard_deviation = (
    np.sqrt(sortino_ratio_df["Downside Returns"].mean()) * np.sqrt(252)
)

# Print the result
print(f"Annualised Downside STD: {downside_standard_deviation}")
```

```text
Annualised Downside STD: 0.09721151675996255
```

Explain to students that to calculate the Sortino ratio, we divide the annualised return value of the portfolio by the downside standard deviation of the portfolio as the following code shows.

```python
# The Sortino ratio is reached by dividing the annualized return value
# by the downside standard deviation value
sortino_ratio = annualized_return/downside_standard_deviation

# Add the Sortino ratio to the evaluation DataFrame
portfolio_evaluation_df.loc["Sortino Ratio"] = sortino_ratio

# Review the DataFrame
portfolio_evaluation_df
```

Finally, our evaluation metrics feature a Sortino ratio, the following image shows our `portfolio_evaluation_df` DataFrame with the completed `Backtest` column:

![A screenshot depicts the DataFrame.](Images/15-2-backtested-sortino-ratio.png)

At this point, students may feel confused; if needed, take a couple of minutes to ask the class if there are any questions. If no questions arise, explain to students that these metrics will make more sense next as you explain how to evaluate them.

#### Evaluate the Metrics

While presenting the evaluation metrics to the class, explain to students that we can estimate the following about the trading algorithm that we backtested:

* Annualized return: A portfolio that this trading algorithm manages should yield an annualised return of about 6.67%. That is, the dollar value of the portfolio should increase by about 6.67% each year.

* Cumulative returns: The dollar value of the portfolio increased by approximately 33% over the backtesting period. We can reasonably expect a similar growth trajectory for the future.

* Annual volatility: The annual volatility of the portfolio should have a spread of about 13.78% surrounding the annualised return. This means with reasonable likelihood that the portfolio might return as much as 20.45% (6.67% + 13.78%) or lose as much as &minus;7.11% (6.067% &minus; 13.78%) per year.

* Sharpe ratio: The Sharpe ratio, which evaluates the performance of a portfolio on a risk-adjusted basis, is 0.484. In general, a higher Sharpe ratio indicates a better risk/reward profile. We commonly get a Sharpe ratio of about 1.00 for a portfolio with a favourable risk-adjusted profile. However, a single Sharpe ratio doesn’t offer much insight. It’s best to compare it with the Sharpe ratios of other portfolios to determine which one offers the best profile.

* Sortino ratio: The Sortino ratio of our portfolio suggests a rate of about 0.685956 for the risk-adjusted annual profitability compared to the annual downside risk. As with the Sharpe ratio, a higher Sortino ratio is better. And, it’s best to compare it with the Sortino ratios of other portfolios.

At a glance, explain to students that we can conclude that alone, these annualised return and cumulative return values indicate overall profitability. However, we need to consider the annual volatility value and the Sharpe and Sortino ratios that compare the risk to the reward. From these metrics, the overall profitability of this portfolio doesn’t seem to outweigh its risks. For a risk-averse investor, we might need to adjust the assets that we include in the portfolio to generate a similar return profile, but with the Sharpe and Sortino ratios closer to 1.00. For an investor who is risk loving and has a longer-term time horizon, the potential of a 20% return might outweigh the downside risk of the portfolio.

Now, let's zoom in even further to discover the risk/reward characteristics that we can determine from the behaviour of our trading algorithm on a per-trade basis.

#### Set Up the Trade-Level Risk/Reward Evaluation Metrics

Explain to students that just as we created a new DataFrame to hold our portfolio-level evaluation metrics, we will now create a new DataFrame, named `trade_evaluation_df`, to hold our per-trade evaluation metrics.

Open the lesson slides and present to the class the columns that we will include in the `trade_evaluation_df` DataFrame.

* `Stock`: The name of the asset that we’re trading.

* `Entry Date`: The date that we entered (bought) the trade.

* `Exit Date`: The date that we exited (sold) the trade.

* `Shares`: The number of shares that we executed for the trade.

* `Entry Share Price`: The price of the asset when we entered the trade.

* `Exit Share Price`: The price of the asset when we exited the trade.

* `Entry Portfolio Holding`: The cost of the trade on entry (which is the number of shares multiplied by the entry share price).

* `Exit Portfolio Holding`: The proceeds that we made from the trade on exit (which is the number of shares multiplied by the exit share price).

* `Profit/Loss`: The profit or loss from the trade (which is the proceeds from the trade minus the cost of the trade).

Go back to the Jupyter notebook, and show the code that sets up the new DataFrame.

```python
# Initialize trade evaluation DataFrame with columns
trade_evaluation_df = pd.DataFrame(
    columns=[
        "Stock",
        "Entry Date",
        "Exit Date",
        "Shares",
        "Entry Share Price",
        "Exit Share Price",
        "Entry Portfolio Holding",
        "Exit Portfolio Holding",
        "Profit/Loss"]
)
```

Now it's time to populate this DataFrame. Explain to students that to do so we will loop through the backtesting results DataFrame by using the `iterrows` Pandas function to examine each index and its corresponding row of values. When the algorithm enters a trade, we record the trade entry values (such as the current portfolio holding value and entry share price) at that index. When the algorithm exits a trade, we record the trade exit values (such as the exit portfolio holding value and the exit share price) and calculate the profit/loss of the trade, as the following code shows.

```python
# Loop through signal DataFrame
# If `Entry/Exit` is 1, set entry trade metrics
# Else if `Entry/Exit` is -1, set exit trade metrics and calculate profit
# Then append the record to the trade evaluation DataFrame
for index, row in signals_df.iterrows():
    if row["Entry/Exit"] == 1:
        entry_date = index
        entry_portfolio_holding = row["Portfolio Holdings"]
        share_size = row["Entry/Exit Position"]
        entry_share_price = row["close"]

    elif row["Entry/Exit"] == -1:
        exit_date = index
        exit_portfolio_holding = abs(row["close"] * row["Entry/Exit Position"])
        exit_share_price = row["close"]
        profit_loss = exit_portfolio_holding - entry_portfolio_holding
        trade_evaluation_df = trade_evaluation_df.append(
            {
                "Stock": "AAPL",
                "Entry Date": entry_date,
                "Exit Date": exit_date,
                "Shares": share_size,
                "Entry Share Price": entry_share_price,
                "Exit Share Price": exit_share_price,
                "Entry Portfolio Holding": entry_portfolio_holding,
                "Exit Portfolio Holding": exit_portfolio_holding,
                "Profit/Loss": profit_loss
            },
            ignore_index=True)

# Print the DataFrame
trade_evaluation_df
```

The following image shows the DataFrame:

![A screenshot depicts the DataFrame.](Images/15-2-per-trade-metrics-dataframe.png)

Explain to students that as they can see our trading algorithm made six trades. Three were profitable, and three were unprofitable. This gives us a **trade accuracy**, or percentage of profitable trades to total trades, of 50%. Also, it can be seen that the maximum loss on any trade was `-$9,115`. The maximum gain was `$32,130`. That’s pretty good! Conversely, the minimum loss was `-$3,810`, and the minimum gain was `$2,890`.

As a conclusion, explain to students that we can say that overall, it seems that our DMAC trading algorithm produces a profit. However, when we dive more deeply into the risk/reward characteristics of the algorithm, the portfolio and per-trade metrics show the potential for inconsistent performance. Highlight the following as general insights from the metrics evaluation:

* Both the portfolio-level and the trade-level evaluation metrics reveal the risk/reward characteristics of this portfolio and algorithmic strategy.

* In this demonstration, we can observe that the portfolio-level evaluation metrics give us an annual volatility of 13.7% and a Sharpe ratio of 0.484. The per-trade metrics show that only one trade turned the overall profit of the portfolio from negative to positive.

* With real money, we might hesitate to use this trading algorithm&mdash;unless we have quite a high risk tolerance.

* As a general rule, we often consider a trading algorithm to be good if it consistently maximises its gains while minimising its losses. A Sharpe ratio that’s greater than 1 and a trading accuracy that’s greater than 80% are popular baselines.

Be sure that there are no questions before moving forward.

---

### 6. Student Do: Evaluating Your Short-Position Algorithm (25 min)

**Corresponding Activity:** [04-Stu_Evaluating_Your_Short_Position_Algorithm](Activities/04-Stu_Evaluating_Your_Short_Position_Algorithm)

**Files:**

* [Instructions](Activities/04-Stu_Evaluating_Your_Short_Position_Algorithm/README.md)

* [evaluating_your_short_position_algorithm.ipynb (Unsolved)](Activities/04-Stu_Evaluating_Your_Short_Position_Algorithm/Unsolved/evaluating_your_short_position_algorithm.ipynb)

* [vnq.csv](Activities/04-Stu_Evaluating_Your_Short_Position_Algorithm/Resources/vnq.csv)

In this activity, students will evaluate the risk/reward characteristics of the short-position strategy that they created before.

---

### 7. Instructor Do: Review Evaluating Your Short-Position Algorithm (10 min)

**Corresponding Activity:** [04-Stu_Evaluating_Your_Short_Position_Algorithm](Activities/04-Stu_Evaluating_Your_Short_Position_Algorithm)

**Files:**

* [Solved](Activities/04-Stu_Evaluating_Your_Short_Position_Algorithm/Solved/evaluating_your_short_position_algorithm.ipynb)

* [Unsolved](Activities/04-Stu_Evaluating_Your_Short_Position_Algorithm/Unsolved/evaluating_your_short_position_algorithm.ipynb)

* [vnq.csv](Activities/04-Stu_Evaluating_Your_Short_Position_Algorithm/Resources/vnq.csv)

Congratulate students on learning how to deploy an end-to-end algorithmic trading strategy! Get them excited about the fact that now they are able to create and backtest a trading algorithm, and also, they learned the skills to evaluate its risk/reward characteristics at both the portfolio and per-trade levels.

Since this is a large activity, you are invited to conduct a dry walkthrough of the solution to explain to students each line of code while you share your professional insights about the solution and the obtained results.

Explain to students that backtesting and evaluation can help them gauge the potential profitability of the algorithm but offers no guarantees. They need to assess their risk tolerance for a particular portfolio and then choose an appropriate trading algorithm based on that assessment.

No matter how much risk they can tolerate, highlight to students that knowing how to evaluate a trading algorithm is a valuable skill. This ensures that when they develop an algorithmic trading strategy, they’ll be able to train it with a viable trading algorithm that adheres to their (or their client’s) personal risk tolerance.

Be sure that there are no questions before moving forward. Remind students that after the break they will use the `FinTA` Python library, and that they can use part of the break time to install it if they haven't already using the following command:

```python
pip install finta
```

---

### 8. BREAK (15 min)

---

### 9. Instructor Do: Alternative Technical Indicators (15 min)

**Corresponding Activity:** [05-Ins_Alternative_Technical_Indicators](Activities/05-Ins_Alternative_Technical_Indicators)

**Instructor Notes:**

The following section will focus on creating trading algorithms with alternative trading signals. The code used in this demo replaces SMA with EMA (Exponential Moving Average), and eventually with trading signals generated from the Python library [FinTA](https://pypi.org/project/finta/).

Before the lesson begins, please be sure that you have installed the FinTA library in your development environment.

```shell
pip install finta
```

**Files:**

* [Unsolved](Activities/05-Ins_Alternative_Technical_Indicators/Unsolved/alternative_technical_indicators.ipynb)

* [Solved](Activities/05-Ins_Alternative_Technical_Indicators/Solved/alternative_technical_indicators.ipynb)

* [blk_ohlcv.csv](Activities/05-Ins_Alternative_Technical_Indicators/Resources/blk_ohlcv.csv)

Explain to students that in addition to altering the values associated with the short and long windows, it is also possible to incorporate different technical indicators into a trading algorithm.

Open the unsolved version of the Jupyter notebook provided, and import the provided data set as follows.

```python
# Import required libraries
import pandas as pd
import numpy as np
import hvplot.pandas
from pathlib import Path

# Setting these options will allow for reviewing more of the DataFrames
pd.set_option("display.max_rows", 2000)
pd.set_option("display.max_columns", 2000)
pd.set_option("display.width", 1000)

# Read in CSV file in from the resources folder into a Pandas DataFrame
# Set the date as the DateTimeIndex
blk_df = pd.read_csv(
    Path("../Resources/blk_ohlcv.csv"),
    index_col = "date",
    parse_dates = True,
    infer_datetime_format = True
)

# Review the DataFrame
blk_df.head()
```

![Sample data](Images/15-2-adv-indicators-df.png)

Explain to students that a close relative to the simple moving average (SMA) technical indicators that were just utilised is the **Exponential Moving Average (EMA)**. Highlight the following:

* The EMA technical indicator weights the recent prices more heavily than prices further in the past. The idea is that an asset's near-term future price behaviour is more likely to mimic its near-term past behaviour than its distant past behaviour.

* Because EMA's place more weight on recent prices, they react to short-term price volatility more quickly. As a result, a short-window EMA is often described as having a **faster** price action.

Illustrate a comparison of a short-window SMA versus a short-window EMA using the following code and visualisation. Highlight that the line depicting the EMA values hugs the line depicting the closing price just a little more closely.

```python
# Create a DataFrame with the index and Close column from the dataset
signals_df = blk_df.loc[:, ["close"]].copy()

# Set the short window and long windows
short_window = 50

# Create a short window SMA
signals_df["SMA50"] = signals_df["close"].rolling(window=short_window).mean()

# Create a short window EMA
signals_df["EMA50"] = signals_df["close"].ewm(span=short_window).mean()

# Review the DataFrame
signals_df.iloc[45:55, :]

# Visualize close price for the investment
security_close = signals_df[["close"]].hvplot(
    line_color='lightgray',
    ylabel='Price in $',
    width=1000,
    height=400
)

# Visualize moving averages
moving_avgs = signals_df[["SMA50", "EMA50"]].hvplot(
    ylabel='Price in $',
    width=1000,
    height=400
)

# Overlay plots
sma_ema_plot = security_close * moving_avgs
sma_ema_plot
```

![short-window SMA versus EMA](Images/15-2-short-window-sma-ema.png)

If possible, zoom in on a section of the plot to highlight the difference in the two lines' trajectory versus the closing price as it's shown in the image below.

![short-window SMA versus EMA zoomed](Images/15-2-short-window-sma-ema-zoom.png)

Explain to students that a long-position dual moving average crossing over trading algorithm can be built by simply replacing the SMA technical indicators with EMA technical indicators as is shown in the code below.

```python
# Create a DataFrame with the index and Close column from the dataset
ema_signals_df = blk_df.loc[:, ["close"]].copy()

# Set the short window and long windows
short_window = 50
long_window = 100

# Generate the short and long moving averages (50 and 100 days, respectively)
ema_signals_df["EMA50"] = signals_df["close"].ewm(span=short_window).mean()
ema_signals_df["EMA100"] = signals_df["close"].ewm(span=long_window).mean()

# Review the DataFrame
ema_signals_df.head()
```

![EMA long-position](Images/15-2-ema-long-position.png)

Highlight that the algorithmic strategy would work the same, that entry position would be generated when the short-window EMA value was greater than the long-window EMA, and vice versa for the exit position as the following code and plot show.

```python
# Set the Signal column
ema_signals_df["Signal"] = 0.0

# Generate the trading signal 1 or 0,
# where 1 is when the EMA50 is greater than (or crosses over) the EMA100
# where 0 is when the EMA50 is under the EMA100
ema_signals_df["Signal"][short_window:] = np.where(
    ema_signals_df["EMA50"][short_window:] > ema_signals_df["EMA100"][short_window:], 1.0, 0.0
)

# Calculate the points in time at which a position should be taken, 1 or -1
ema_signals_df["Entry/Exit"] = ema_signals_df["Signal"].diff()

# Review the DataFrame
ema_signals_df.head()
```

![EMA signals](Images/15-2-ema-signals.png)

```python
# Visualize entry position relative to close price
entry = ema_signals_df[ema_signals_df["Entry/Exit"] == 1.0]["close"].hvplot.scatter(
    color='purple',
    marker='^',
    size=200,
    legend=False,
    ylabel='Price in $',
    width=1000,
    height=400
)

# Visualize exit position relative to close price
exit = ema_signals_df[ema_signals_df["Entry/Exit"] == -1.0]["close"].hvplot.scatter(
    color='orange',
    marker='v',
    size=200,
    legend=False,
    ylabel='Price in $',
    width=1000,
    height=400
)

# Visualize close price for the investment
security_close = ema_signals_df[["close"]].hvplot(
    line_color='lightgray',
    ylabel='Price in $',
    width=1000,
    height=400
)

# Visualize moving averages
moving_avgs = ema_signals_df[["EMA50", "EMA100"]].hvplot(
    ylabel='Price in $',
    width=1000,
    height=400
)

# Overlay plots
entry_exit_plot = security_close * moving_avgs * entry * exit
entry_exit_plot
```

![EMA DMAC plot](Images/15-2-ema-dmac-plot.png)

Stress that, once the dual moving average trading algorithm is built, it is almost as easy to evaluate alternative moving average technical indicators to evaluate a trading algorithm for different short and long-window periods.

In fact, explain to students that this is made even easier by the existence of Python libraries that specialise in generating technical indicators like [**FinTA** from Pypi](https://pypi.org/project/finta/).

If possible, have a TA Slack the link to the `FinTA` Python library out to the students: [**FinTA** from Pypi](https://pypi.org/project/finta/).

Highlight the following about the `FinTA` Python library:

* Although still in development, `FinTA` is a Python library that assists in the generation of the technical indicators that are used to design trading algorithms.

* Incorporating the `FinTA` library starts with the import statement once it's installed in your virtual environment.

  ```python
  from finta import TA
  ```

* From the `FinTA` documentation, we know that this library requires a dataset that includes the open, high, low, close, and volume metrics, often referenced as **ohlcv** data. Also, the column headers should be specified with lowercase labels.

* To demonstrate how to use the `FinTA` library, we will start by loading again the ohlcv data to create a fresh DataFrame.

  ```python
  # Read in CSV file in from the resources folder into a Pandas DataFrame
  # Set the date as the DateTimeIndex
  blk_df = pd.read_csv(
      Path("../Resources/blk_ohlcv.csv"),
      index_col = "date",
      parse_dates = True,
      infer_datetime_format = True
  )

  # Review the DataFrame
  blk_df.head()
  ```

  ![ohlcv dataframe](Images/15-2-ohlcv-dataframe.png)

* The FinTA library requires that the open, high, low, close, and volume columns be left in place, so we no longer create a `signals_df` DataFrame.

* The short and long-window periods are defined as they are previously, but the generation of the technical indicators is accomplished by referencing the **TA** module from FinTA and then calling the desired technical indicator function. For example, the EMA technical indicator is generated with the following code:

  ```python
  # Set the short window and long windows
  short_window = 50
  long_window = 100

  # Add the EMA technical indicators for the short and long windows
  blk_df["Short"] = TA.EMA(blk_df, short_window)
  blk_df["Long"] = TA.EMA(blk_df, long_window)

  # Review the DataFrame
  blk_df.iloc[45:105, :]
  ```

  ![Sample EMA data creating using the FinTA library](Images/15-2-ema-data-finta.png)

* Once the short and long windows are generated, the remainder of the code stays the same, and the entry and exit points are generated.

  ```python
  # Set the Signal column
  blk_df["Signal"] = 0.0

  # Generate the trading signal 1 or 0,
  # where 1 is when the Short window is greater than (or crosses over) the Long Window
  # where 0 is when the Short window is under the Long window
  blk_df["Signal"][short_window:] = np.where(
      blk_df["Short"][short_window:] > blk_df["Long"][short_window:], 1.0, 0.0
  )

  # Calculate the points in time at which a position should be taken, 1 or -1
  blk_df["Entry/Exit"] = blk_df["Signal"].diff()

  # Review the DataFrame
  blk_df.iloc[95:105, :]
  ```

  ![Trading signals generated using the EMA indicator](Images/15-2-ema-trading-signals.png)

  * We can also easily plot the results using hvPlot.

  ```python
  # Visualize entry position relative to close price
  entry = blk_df[blk_df["Entry/Exit"] == 1.0]["close"].hvplot.scatter(
      color="purple",
      marker="^",
      size=200,
      legend=False,
      ylabel="Price in $",
      width=1000,
      height=400
  )

  # Visualize exit position relative to close price
  exit = blk_df[blk_df["Entry/Exit"] == -1.0]["close"].hvplot.scatter(
      color="orange",
      marker="v",
      size=200,
      legend=False,
      ylabel="Price in $",
      width=1000,
      height=400
  )

  # Visualize close price for the investment
  security_close = blk_df[["close"]].hvplot(
      line_color="lightgray",
      ylabel="Price in $",
      width=1000,
      height=400
  )

  # Visualize moving averages
  moving_avgs = blk_df[["Short", "Long"]].hvplot(
      ylabel="Price in $",
      width=1000,
      height=400
  )

  # Overlay plots
  entry_exit_plot = security_close * moving_avgs * entry * exit
  entry_exit_plot
  ```

  ![FinTA EMA plot](Images/15-2-finta-ema-plot.png)

Explain to students that, with this code in place, evaluating another technical indicator is as easy as changing the function assigned to the TA module.

Demo how easy it is to compute an alternative technical indicator using the FinTA library. Start with the smoothed moving average (SMMA) and explain to students that the SMMA indicator has been developed to smooth out the market noises and show the overall trends more clearly. It does this by averaging the price values of the periods over which it is calculated.

```python
# Read in CSV file in from the resources folder into a Pandas DataFrame
# Set the date as the DateTimeIndex
blk_df = pd.read_csv(
    Path("../Resources/blk_ohlcv.csv"),
    index_col = "date",
    parse_dates = True,
    infer_datetime_format = True
)

# Add the SMMA technical indicators for the short and long windows
blk_df["Short"] = TA.SMMA(blk_df, short_window)
blk_df["Long"] = TA.SMMA(blk_df, long_window)
blk_df.head()
```

![FinTA SMMA data](Images/15-2-smma-data-finta.png)

After computing the SMMA technical indicator, explain to students that the algorithmic trading strategy can be executed and plotted again. Highlight how the signal flags are in different positions as the following plot shows.

![FinTA SMMA plot](Images/15-2-finta-smma-plot.png)

Next, demo evaluating the DMAC algorithm with the volume-adjusted moving average (VAMA). Explain to students that this moving average takes into account the price movements over the period and the volumes associated with each given period. Days with higher volumes are given more importance than other days.

```python
# Add the VAMA technical indicators for the short and long windows
blk_df["Short"] = TA.VAMA(blk_df, short_window)
blk_df["Long"] = TA.VAMA(blk_df, long_window)
```

Run the trading algorithm using VAMA as technical indicator, an highlight the differences on the signals in the plot.

![FinTA VAMA plot](Images/15-2-finta-vama-plot.png)

Let students know that, in addition to moving averages, there are many technical indicators available from the FinTA library to build trading algorithm strategies. One such additional indicator is called **Bollinger Bands**. Highlight the following:

* A Bollinger Band is a technical indicator defined by a set of trend lines plotting two standard deviations, both positive and negative, away from the running simple moving average of a security's price.

* Bollinger Bands help to identify when an asset is either overbought (i.e., at an unusually high price) or oversold (unusually low). The closer the stock price moves to the lower Bollinger band, the more oversold the stock is, presenting a buying opportunity. The closer the stock price moves to the upper band, the more overbought a stock is, indicating a possible time to sell.

* Using the FinTA library, Bollinger Bands can be created using the function `TA.BBANDS`, passing the DataFrame in as the parameter.

  ```python
  # Determine the Bollinger Bands for the Dataset
  bbands_df = TA.BBANDS(blk_df)

  # Review the DataFrame
  bbands_df.iloc[17:25, :]
  ```

  ![Bollinger bands DataFrame](Images/15-2-bollinger-bands-dataframe.png)

* In the DataFrame created with the `TA.BBANDS` function, the column identified as `BB_Middle` is the 20-day simple moving average of the stock.

* To create a visualisation that shows the stock's close price and the Bollinger bands, we must concatenate the Bollinger bands DataFrame with the original ohlcv Dataframe.

  ```python
  # Concatenate the Bollinger Bands to the DataFrame
  blk_df = pd.concat([blk_df, bbands_df], axis=1)

  # Review the DataFrame
  blk_df.head()
  ```

  ![Bollinger bands concatenated DataFrame](Images/15-2-bollinger-bands-concatenated-dataframe.png)

* From there, a visualisation of the close price integrated with the Bollinger bands can be created using hvPlot.

  ```python
  # Visualize close price for the investment
  security_close = blk_df[["close"]].hvplot(
      line_color="lightgray",
      ylabel="Price in $",
      width=1000,
      height=400
  )

  bb_upper = blk_df[["BB_UPPER"]].hvplot(
      line_color="purple",
      ylabel="Price in $",
      width=1000,
      height=400
  )


  bb_middle = blk_df[["BB_MIDDLE"]].hvplot(
      line_color="orange",
      ylabel="Price in $",
      width=1000,
      height=400
  )

  bb_lower = blk_df[["BB_LOWER"]].hvplot(
      line_color="blue",
      ylabel="Price in $",
      width=1000,
      height=400
  )


  # Overlay plots
  bbands_plot = security_close * bb_upper * bb_middle * bb_lower
  bbands_plot
  ```

  ![Bollinger bands plot](Images/15-2-bollinger-bands-plot.png)

Explain to students that, from here, we can begin to construct a trading algorithm with the information we have about Bollinger bands. Highlight the following.

* If the stock price is less than the lower Bollinger band, the stock might be oversold, and there is a potential buying opportunity

* If the stock price is greater than the upper Bollinger band, the stock might be overbought

Continue the demo by showing to the class the trading algorithm that uses the Bollinger Bands translated into code.

```python
# Create a trading algorithm using Bollinger Bands
# Set the Signal column
blk_df["Signal"] = 0.0

# Generate the trading signals 1 (entry) or -1 (exit) for a long position trading algorithm
# where 1 is when the Close price is less than the BB_LOWER window
# where -1 is when the Close price is greater the the BB_UPPER window
for index, row in blk_df.iterrows():
    if row["close"] < row["BB_LOWER"]:
        blk_df.loc[index, "Signal"] = 1.0
    if row["close"] > row["BB_UPPER"]:
        blk_df.loc[index,"Signal"] = -1.0

# Review the DataFrame
blk_df
```

Highlight the following about this trading algorithm:

* This particular trading algorithm combines aspects of the two trading algorithms that have been demonstrated  in this lesson:

  * Using the if statement and the `iterrows` function to evaluate the pricing information and technical indicators.

  * Identifying our trading signal with a designator of 1 for an entry trade and -1 for an exit trade

  * Because we are already flagging the `Signal` column as 1 and -1, we do not need to utilise the  `diff` function and generate an `Entry/Exit` column.

* From there, we can overlay the possible entry and exit positions with Bollinger bands and visualise the algorithm.

  ```python
  # Visualize entry position relative to close price
  entry = blk_df[blk_df["Signal"] == 1.0]["close"].hvplot.scatter(
      color="green",
      marker="^",
      size=200,
      legend=False,
      ylabel="Price in $",
      width=1000,
      height=400
  )

  # Visualize exit position relative to close price
  exit = blk_df[blk_df["Signal"] == -1.0]["close"].hvplot.scatter(
      color="red",
      marker="v",
      size=200,
      legend=False,
      ylabel="Price in $",
      width=1000,
      height=400
  )

  # Visualize close price for the investment
  security_close = blk_df[["close"]].hvplot(
      line_color="lightgray",
      ylabel="Price in $",
      width=1000,
      height=400
  )

  bb_upper = blk_df[["BB_UPPER"]].hvplot(
      line_color="purple",
      ylabel="Price in $",
      width=1000,
      height=400
  )


  bb_middle = blk_df[["BB_MIDDLE"]].hvplot(
      line_color="orange",
      ylabel="Price in $",
      width=1000,
      height=400
  )

  bb_lower = blk_df[["BB_LOWER"]].hvplot(
      line_color="blue",
      ylabel="Price in $",
      width=1000,
      height=400
  )


  # Overlay plots
  bbands_plot = security_close * bb_upper * bb_middle * bb_lower * entry * exit
  bbands_plot
  ```

  ![Bollinger bands entry exit plot](Images/15-2-bollinger-bands-entry-exit-plot.png)

Explain to students that this is by no-means a perfect trading algorithm, but it is a solid start, and that with a bit of refinement, it could yield some results.

Highlight to the class that by incorporating the `FinTA` Python library into the process, we have access to a multitude of new technical indicators around which we can begin to design different trading algorithms.

Ask students if they have any questions before moving forward.

---

### 10. Student Do: Using FinTA for Trading Signals (25 min)

**Corresponding Activity:** [06-Stu_Using_Finta_for_Trading_Signals](Activities/06-Stu_Using_Finta_for_Trading_Signals)

**Files:**

* [Instructions](Activities/06-Stu_Using_Finta_for_Trading_Signals/README.md)

* [Unsolved](Activities/06-Stu_Using_Finta_for_Trading_Signals/Unsolved/using_finta_for_trading_signals.ipynb)

* [ixn_ohlcv.csv](Activities/06-Stu_Using_Finta_for_Trading_Signals/Resources/ixn_ohlcv.csv)

In this activity, students will utilise the `FinTA` Python library to generate the technical indicator values used in several trading algorithms. The activity will begin by asking them to open a terminal instance and install the `FinTA` library into their Python `dev` virtual environment. Though this is not expected to cause any issues, please have the TA's troubleshoot the process as necessary.

---

### 11. Instructor Do: Review Using FinTA for Trading Signals (10 min)

**Corresponding Activity:** [06-Stu_Using_Finta_for_Trading_Signals](Activities/06-Stu_Using_Finta_for_Trading_Signals)

**Files:**

* [Solved](Activities/06-Stu_Using_Finta_for_Trading_Signals/Solved/using_finta_for_trading_signals.ipynb)

* [Unsolved](Activities/06-Stu_Using_Finta_for_Trading_Signals/Unsolved/using_finta_for_trading_signals.ipynb)

* [ixn_ohlcv.csv](Activities/06-Stu_Using_Finta_for_Trading_Signals/Resources/ixn_ohlcv.csv)

Review the previous student activity, focusing on the ease of incorporating various technical indicators into the process of designing a trading algorithm.

The students are asked to import the FinTA library into their starter notebook. They might have to reference the documentation to find the import phrasing.

```python
from finta install TA
```

This activity will use pricing data from the iShares Global Tech ETF (ticker: IXN). As always, it starts with the import from a CSV file into a Pandas DataFrame, the DataFrame review, and a quick plot.

```python
# Read in CSV file in from the resources folder into a Pandas DataFrame
# Set the date as the DateTimeIndex
ixn_df = pd.read_csv(
    Path("../Resources/ixn_ohlcv.csv"),
    index_col = "date",
    parse_dates = True,
    infer_datetime_format = True
)

# Review the DataFrame
ixn_df.head()

# Plot the DataFrame with hvplot
ixn_df["close"].hvplot()
```

![IXN plot](Images/15-2-ixn-plot.png)

The first part of the activity asks the students to re-create the dual moving average crossover algorithm (DMAC) using the finta syntax for determining the short and long-window moving averages.

* The code is as simple as referencing the `TA` module and then the `SMA` function, both from the `FinTA` library.
* The values of 15 and 50 are specified for the short and long windows.

```python
# Create a signals_df DataFrame that is a copy of the ixn_df Dataframe
signals_df = ixn_df.copy()

# Set the short window and long windows
short_window = 15
long_window = 50

# Add the SMA technical indicators for the short and long windows
signals_df["Short"] = TA.SMA(signals_df, short_window)
signals_df["Long"] = TA.SMA(signals_df, long_window)

# Review the DataFrame
signals_df.iloc[95:105, :]
```

From there, they are asked to recreate the DMAC trading algorithm. This should not be too difficult as they should have the code from the prior activity.

```python
# Set the Signal column
signals_df["Signal"] = 0.0

# Generate the trading signal 1 or 0,
# where 1 is when the Short window is greater than (or crosses over) the Long Window
# where 0 is when the Short window is under the Long window
signals_df["Signal"][short_window:] = np.where(
    signals_df["Short"][short_window:] > signals_df["Long"][short_window:], 1.0, 0.0
)

# Calculate the points in time at which a position should be taken, 1 or -1
signals_df["Entry/Exit"] = signals_df["Signal"].diff()

# Review the DataFrame
signals_df.iloc[95:105, :]
```

The code for the visualisation is provided for them.

```python
# Visualize entry position relative to close price
entry = signals_df[signals_df["Entry/Exit"] == 1.0]["close"].hvplot.scatter(
    color='purple',
    marker='^',
    size=200,
    legend=False,
    ylabel='Price in $',
    width=1000,
    height=400
)

# Visualize exit position relative to close price
exit = signals_df[signals_df["Entry/Exit"] == -1.0]["close"].hvplot.scatter(
    color='orange',
    marker='v',
    size=200,
    legend=False,
    ylabel='Price in $',
    width=1000,
    height=400
)

# Visualize close price for the investment
security_close = signals_df[["close"]].hvplot(
    line_color='lightgray',
    ylabel='Price in $',
    width=1000,
    height=400
)

# Visualize moving averages
moving_avgs = signals_df[["Short", "Long"]].hvplot(
    ylabel='Price in $',
    width=1000,
    height=400
)

# Overlay plots
entry_exit_plot = security_close * moving_avgs * entry * exit
entry_exit_plot
```

![IXN SMA signals plot](Images/15-2-ixn-sma-signals-plot.png)

Next, they are asked to replace the moving average calculations with a different moving average technical indicator from the FinTA library. There are several from which to choose. The key is to point out how easy it is to swap out the code. The solution file provided uses the Double Exponential Moving Average indicator.

```python
# Replace the SMA moving average calculations with an alternative moving average
# calculation from the finta library
signals_df["Short"] = TA.DEMA(signals_df, short_window)
signals_df["Long"] = TA.DEMA(signals_df, long_window)
```

![IXN double EMA signals plot](Images/15-2-ixn-double-ema-signals-plot.png)

If time permits, also highlight how the information changes when the short and long window values are adjusted.

Part 2 of this activity asks students to create a new trading algorithm using Bollinger bands as the technical indicator. This is the same technical indicator that you reviewed in the original demo, so the students should have some reference for what they are coding. The difference is that, in the last step, they are asked to add code that simplifies the entry and exit flags so that only one is displayed per entry/exit cycle.

They start by creating a copy of the original `ixn_df` DataFrame. This is then passed into the `BBANDS` function from finta. Highlight that the resulting DataFrame consists of 3 columns of data. Upper and Lower are used to indicate the overbought and oversold positions, and the middle band is the 20-day SMA of the closing price.

Again, point out how many different technical indicators there are available for them to explore. Bollinger bands is only one possibility. The web is full of information on what each of these different technical indicators means and how they are utilized to evaluate trading signals.

```python
# Create a new clean copy of the signals_df DataFrame
bb_signals_df = ixn_df.copy()

# Review the DataFrame
bb_signals_df.head()

# Determine the Bollinger Bands for the Dataset
bbands_df = TA.BBANDS(bb_signals_df)

# Review the DataFrame
bbands_df.iloc[17:25, :]
```

![ixn bollinger bands dataframe](Images/15-2-ixn-bollinger-bands-dataframe.png)

Remind students that the Bollinger bands DataFrame has to be concatenated with the original DataFrame in order to generate the visualisations properly.

```python
# Concatenate the Bollinger Bands to the DataFrame
bb_signals_df = pd.concat([bb_signals_df, bbands_df], axis=1)

# Review the DataFrame
bb_signals_df.iloc[17:25, :]
```

The code for visualising the Bollinger bands and the close price is provided for the students.

![ixn bollinger bands plot](Images/15-2-ixn-bollinger-bands-plot.png)

Next, a new trading algorithm is created.

The Pandas `iterrows` function is used to loop through each row of data. If the "close" value is less than the `BB_LOWER` value (indicating an oversold postion), the `Signal` column is updated to `1`. If the `close` value is greater than `BB_UPPER` (indicating an overbought position), the `Signal` column is updated to `-1`.

```python
# Create a trading algorithm using Bollinger Bands
# Set the Signal column
bb_signals_df["Signal"] = 0.0

# Generate the trading signals 1 (entry) or -1 (exit) for a long position trading algorithm
# where 1 is when the Close price is less than the BB_LOWER window
# where -1 is when the Close price is greater the the BB_UPPER window
for index, row in bb_signals_df.iterrows():
    if row["close"] < row["BB_LOWER"]:
        bb_signals_df.loc[index, "Signal"] = 1.0
    if row["close"] > row["BB_UPPER"]:
        bb_signals_df.loc[index,"Signal"] = -1.0

# Review the DataFrame
bb_signals_df
```

The students are asked to add the code for visualising the entry and exit positions. The other code is provided for them.

```python
# Visualize entry position relative to close price
entry = bb_signals_df[bb_signals_df["Signal"] == 1.0]["close"].hvplot.scatter(
    color='green',
    marker='^',
    size=200,
    legend=False,
    ylabel='Price in $',
    width=1000,
    height=400
)

# Visualize exit position relative to close price
exit = bb_signals_df[bb_signals_df["Signal"] == -1.0]["close"].hvplot.scatter(
    color='red',
    marker='v',
    size=200,
    legend=False,
    ylabel='Price in $',
    width=1000,
    height=400
)
```

![ixn bollinger bands multiple entry exit points](Images/15-2-ixn-bollinger-bands-multiple-entry-exit-points.png)

Point out that the current trading algorithm identifies multiple points for entry and exit trading possibilities. This does not make for a very functional trading algorithm. That number of trades would result in a lot of fees. Additionally, it appears you are being asked to sell more shares than you might possibly own. All in, the algorithm, the way it is currently written, is not very user-friendly.

The final step in the activity asks students to update the trading algorithm so that only the first entry and first exit flags are identified.

Ask students if anyone would like to volunteer their solution before working through the code updates.

Explain to students that creating a variable called `trade_signal` and incorporating that into the trading algorithm works to solve the issue. The variable is incorporated as a conditional in the if-statement and is updated inside the code body.

```python
# Update the trading algorithm using Bollinger Bands

# Set the Signal column
bb_signals_df["Signal"] = 0.0

# Create a value to hold the initial trade signal
trade_signal = 0

# Update the DataFrame Signal column 1 (entry) or -1 (exit) for a long position trading algorithm
# where 1 is when the Close price is less than the BB_LOWER window
# where -1 is when the Close price is greater the the BB_UPPER window
# Incorporate a conditional in the if-statement, to evaluate the value of the trade_signal so the algorithm
# plots only 1 entry and exit point per cycle.
for index, row in bb_signals_df.iterrows():
    if (row["close"] < row["BB_LOWER"]) and (trade_signal < 1):
        bb_signals_df.loc[index, "Signal"] = 1.0
        trade_signal += 1

    if (row["close"] > row["BB_UPPER"]) and (trade_signal > 0):
        bb_signals_df.loc[index, "Signal"] = -1.0
        trade_signal = 0


# Review the DataFrame
bb_signals_df
```

Highlight how the `trade_signal` variable is used in the if-statement as part of the entry/exit signal evaluation process, and it is updated inside the body of the code.

* Once the first entry signal is flagged, the `trade_signal` variable is updated to one, and no other entry trading signal will be flagged until the variable is reset.

* When the first exit signal is detected and flagged, the `trade_signal` variable is reset to 0, allowing for the next entry position to be created.

Running the visualisation results in the following:

![ixn bollinger bands single entry exit points](./Images/15-2-ixn-bollinger-bands-single-entry-exit-points.png)

Highlight how this new trading algorithm could be applied to different stocks by simply importing a new `ohlcv` DataFrame. Python libraries like FinTA make technical indicators easy to generate. The fun is in designing the trading algorithm.

Pose the following question:

* **Question:** Now that we are able to create a variety of trading algorithms using different technical indicators, how do we go about evaluating them?

* **Answer:** The next step in the process is to backtest the various trading algorithms using evaluation metrics such as per-trade profit and loss as well as risk metrics like annualised volatility and the Sharpe/Sortino ratio.

Be sure that there are no questions before ending the class.

---

End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
