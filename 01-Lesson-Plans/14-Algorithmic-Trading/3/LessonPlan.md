## 14.3 Lesson Plan: Algorithmic Trading with Machine Learning

---

### Overview

The goal of this session is to apply many of the existing skills students have acquired in algorithmic trading to a framework involving machine learning. Thus far, students have acquired the ability to generate technical trading indicators, and to backtest the potential profit from deploying a long-short trading strategy on any one of those indicators. In this class, they will take their ability to generate those indicators one step further, by feeding them into a machine learning model, and backtesting the trading predictions of that machine learning model. In this way, students will learn to combine multiple trading indicators together in a systematic and mathematically optimal fashion.

### Class Objectives

By the end of class, students will be able to:

* Build a machine learning model that takes in technical indicators and makes predictions about the daily direction of stock returns.

* Evaluate the quality of that machine learning model, and improve model performance using scaling and resampling techniques.

* Build training and testing datasets based on `DatetimeOffset` Pandas functionality.

* Backtest a machine learning model to see how it would fare in terms of economic trading performance (i.e., cumulative percentage trading returns).

### Instructor Notes

* Students may be at or near their learning capacity by this point in the course, but encourage them to use today's material as a guide for incorporating machine learning models into an algorithmic trading strategy. These ideas can potentially be used in their projects.

* The last activity of Today's lessons involves a demo going live with an algorithmic trading strategy using the Alpaca API. Be sure to corroborate that the demo works—as well as your API keys—before class.

* It's crucial to remind students of the educational nature of the trading strategies covered in this course.

* Explain to students that the homework for this unit is optional. However, working on this assignment, will help them to enhance their FinTech professional skills.

* In the next unit, students will start with Amazon Web Services (AWS). During this week, ask students to create an AWS account, if they don't have one, by following the "AWS Account Setup" guide that they can find in Unit 15's "Supplemental" folder.

### Class Slides and Time Tracker

The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1_5dttV2XOJS0wwfFZGopQ46lGYVa3vMLLyObtztnmu8/edit?usp=sharing).

To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

Note: Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

The time tracker for this lesson can be viewed here: [Time Tracker.xlsx](TimeTracker.xlsx)

---

### 1. Instructor Do: Welcome Class! (10 min)

**Corresponding Activity:** [01-Ins_Welcome](Activities/01-Ins_Welcome)

**Files:**

* [Legal Disclaimer](Activities/01-Ins_Welcome/legal-disclaimer.pdf)

Welcome students back for the third class session on algorithmic trading. Emphasise that in this class they're going to be applying machine learning models to trading algorithms.

Open the lesson slides and move to the "Legal Disclaimer" slide. Explain to students that finance is an industry that has become driven by Legal and Compliance departments, as they may or not be aware. In that light, reiterate for students that any of the trading algorithms demonstrated are only demonstrations. They should not be considered as actual investment or trading advice. Any actual trading done using these algorithms is at their own risk.

Continue on the lesson slides, move to the "Algorithmic Trading with Machine Learning" section and highlight the following:

* Until now, we’ve learned how to translate the process of a trading strategy into a Python program.

* Specifically, in the previous lessons, we generated signals, backtested our trading strategies, and evaluated the results. Now, it’s time to incorporate intelligence and automation into our trading strategies by using machine learning.

Continue with the lesson slides, and facilitate a discussion in class by asking the following question:

* **Question:** Based on your professional experience, and considering what we learned about machine learning in the course, what can be the advantages of using machine learning in algorithmic trading strategies?

* **Possible Answer:** Computer systems driven by machine learning are disrupting the financial market. They allow investors to manage and automatically trade assets in highly dynamic and volatile environments by reducing human errors or the emotional bias on making trading decisions.

* **Possible Answer:** Machine learning systems can evaluate multiple factors that influence investment decisions (such as changing economic, political, and fundamental company conditions) even more efficiently than humans—resulting in more accurate trading decisions. Additionally, machine learning systems can quickly analyse the data that generates the trade signals used to both enter and exit a trade at its most profitable price points.

Close the discussion by explaining to students that using machine learning for trading requires combining a trader’s experience to assess the performance of a model with the technical experience of a FinTech professional, who can translate a trading process into code. The trading industry has not yet fully adopted machine learning. But, the industry is gradually accepting it. This is because it’s showing that it can generate more profitable trading strategies.

Continue with the lesson slides and highlight the following:

* The use of machine learning models makes trading decisions more efficient. The reason is that with these models, we can focus our attention on which variables move markets on the front end.

* Once we find the right features and adapt the correct model, we can delegate the rest of the trading process to automation. That frees us to spend more time creating new strategies—rather than maintaining existing ones on a day-to-day basis.

* We can create new trading strategies more easily. That’s because machine learning algorithms work by getting as much predictive information as possible from each variable that the model includes.

Finally, explain to students that the homework for this unit is an optional assignment. If they decide to work on it, they'll create an algorithmic trading bot that learns and adapts to new data and evolving markets.

Be sure that there are no questions before moving forward.

---

### 2. Instructor Do: Performance Metrics (10 min)

**Corresponding Activity:** [02-Ins_Perf_Metrics](Activities/02-Ins_Perf_Metrics)

In this activity, students will learn how to use the annualised volatility, the non-compounded returns, and the Sharpe Ratio to assess the performance of an algorithmic trading strategy on options. These metrics will also be helpful to assess machine learning powered trading strategies.

**Files:**

* [Unsolved](Activities/02-Ins_Perf_Metrics/Unsolved/performance_metrics.ipynb)

* [Solved](Activities/02-Ins_Perf_Metrics/Solved/performance_metrics.ipynb)

* [GOOG_implied_vol.csv](Activities/02-Ins_Perf_Metrics/Resources/GOOG_implied_vol.csv)

Explain to students that, before going into using machine learning in our trading strategies, we will cover a few more methods to evaluate an algorithm's trading performance, but this time we are backtesting an algorithmic trading strategy on options. Comment to students that we will use Google stock historical data for this demo.

#### Backtest with Options

Open the lesson slides, move to the "Backtesting with Options" section and highlight the following:

* Backtesting and trading options is somewhat more complex than equities. While options are derivatives that are based on equities, there are many more of them. There are more than 20,000 unique options trading on Google at any given time, for example.

* The sheer number of options available as well as other factors, such as how much any single option moves in response to an equity, means that trading in them can get complicated quickly.

* One way to simplify algorithmic options trading, however, is to backtest the implied volatility of a given stock.

* The **implied volatility** of a stock is a standardised measure of the price of all the options currently trading on the stock. This is a way to backtest options on a stock by using only a single column. This gives us an approximate measure of backtest option returns.

* In this class, we will use implied volatility to predict whether options on a stock will go up or down over the next day.

* Implied volatility is calculated by feeding an option's trading price into an option trading model, usually by using Black-Scholes models. It tells us the relative cheapness or expensiveness of the option, and allows us to compare one option from another on the same stock, or sometimes across stocks.

* In the next coding demonstration, the implied volatility is a single column because it's an average daily implied volatility across several options written on the same stock.

Explain to the students that when we use implied volatility to proxy for option returns, we're skimming over some more complicated option issues (we're assuming "greeks" are held constant). This allows us to demonstrate to the students how to backtest by using option data, but it comes with the caveat that our backtest returns are only an approximation of the returns to option trading. A step beyond this would be to calculate option greeks and how they change each day.

#### Build a Simple Trading Algorithm

Open the provided unsolved version of the Jupyter notebook. Run the initial code that loads and plots the data, calculates returns, builds the initial simple trading algorithm, and defines a simple momentum strategy (in this case, buying tomorrow if the day is positive, shorting if the day is negative).

To get the students on the same page, spend a minute or two reviewing this code before live coding. Let the students know that the performance metrics code we're about to write applies to the trading strategies in the previous session, but that it just as easily applies to some of the machine learning trading strategies that we'll learn next.

Continue to the "Risk and Performance" section of the starter Jupyter notebook, live code the demo, and highlight the following:

* First, we will code the annualised volatility of the option returns for Google.

    ```python
    # Annualised volatility of the option returns for Google
    annualized_volatility = round(signals_df["Actual Returns"].std() * np.sqrt(252) * 100, 2)

    # Display results
    print("Annualised Volatility:", annualized_volatility, '%')
    ```

    ```text
    Annualised Volatility: 240.41 %
    ```

* We have an annualised volatility of 240.41%! This is an extremely volatile option price, even for a company as large as Google. This extreme risk is both the peril and the potential when it comes to trading options.

* Whether we're trading options or stocks, the `Signal` is a `1` or `-1` (long or short).

* Remember that when backtesting, we need to lag our signal by `1` period relative to the returns. Otherwise, in the backtest, we'd be acting upon information that wasn't actually available to us at the time. To do so, we calculate the strategy returns and add them to the `signals_df` DataFrame by using the Pandas `shift()` function, as the following code shows:

    ```python
    # Calculate the strategy returns and add them to the signals_df DataFrame
    signals_df["Strategy Returns"] = signals_df["Actual Returns"] * signals_df["Signal"].shift()
    ```

* Let's plot the total strategy performance to see how it looks. There's one difference in how we do this, because we're looking at options. Here, we need to look at non-compounded returns. That is, we're testing what happens when we don't continually re-invest any profits.

* Non-compounded returns can be plotted using the Pandas `cumsum()` (cumulative sum) function.

  ```python
  # Calculate the strategy's returns
  strategy_returns = signals_df["Strategy Returns"].cumsum()

  # Plot Strategy Returns to examine performance
  strategy_returns.plot()
  ```

  ![Strategy Returns](Images/15-3-cumulative_strategy_returns_options.png)

#### Add Transaction Costs to a Backtest

Explain to students that trading U.S. equities is close to costless these days, with most brokerages charging no commissions. The same can't be said for trading options though, particularly when using an option broker that provides an API to do the trading.

Continue the demo, live code the "Add Transaction Cost to a Backtest" section and highlight the following:

* The code below can keep track of the number of trades. It uses the `Signal` column, which takes the value of `-1` or `1`. This means if the algorithm switches from short to long, or from `-1` to `1`, the number of trades will be equal to two: one trade to close the short option, and one trade to buy the long option.

  ```python
  # Every time we change from long to short, or vice-versa, 2 trades occur
  signals_df['Trades'] = np.abs(signals_df['Signal'].diff())

  # Display sample data
  signals_df.head()
  ```

  ![Tracking the number of trades](Images/15-3-signals-df-with-trades.png)

* Let's assume a cost per trade of one-half of one percent per trade. Multiplying this by the total number of trades per day gives us our total daily trade costs in percentage form.

  ```python
  # Calculate total daily trade costs
  cost_per_trade = 0.005
  daily_trade_costs = signals_df["Trades"] * cost_per_trade

  # Display sample data
  daily_trade_costs.head()
  ```

  ```text
  date
  2014-04-07     NaN
  2014-04-08    0.01
  2014-04-09    0.00
  2014-04-10    0.01
  2014-04-11    0.00
  Name: Trades, dtype: float64
  ```

* The strategy itself doesn't change: what changes is the cost to achieve those returns. So let's calculate the strategy returns after costs by adding a new column to our DataFrame, which is the `Strategy Returns`, less the `daily_trade_costs` (in percent).

  ```python
  # Calculate strategy returns after costs
  signals_df["Strategy Returns (After Costs)"] = signals_df["Strategy Returns"] - daily_trade_costs
  ```

* Next, we can then plot the strategy, both before and after transaction costs, to determine whether the strategy is still viable.

  ```python
  # Compute total strategy returns after costs
  strategy_returns_after_costs = signals_df["Strategy Returns (After Costs)"].cumsum()

  # Plot strategy returns before and after costs
  strategy_returns_after_costs.plot(label="Strategy Returns (After Costs)")
  strategy_returns.plot(label="Strategy Returns (Before Costs)")
  plt.legend()
  ```

  ![Plot of strategy returns before and after costs](Images/15-3-stratregy-costs.png)

Explain to students that, as they can appreciate in the plot, transaction costs matter. While performance in option trading is still strong; it's only about a third of it's level (4 versus 12) after considering transaction costs.

#### Other Performance Metrics

Continue the demo and move to the "Other Performance Metrics" section of the notebook. Explain to students that as we learned before, we can calculate the Sharpe Ratio, or the ratio of investment performance relative to investment risk, to assess a trading strategy.

Now, we will take a look at the Sharpe Ratio of this option trading strategy. Highlight the following:

* The Sharpe ratio is the ratio of returns, relative to the amount of risk. Both are usually expressed on an annualised basis.

* Notice in our previous plot we had huge returns (10-12X!), but the Sharpe ratio is 0.7, which isn't much better than the S&P 500's long-run Sharpe (0.56). This tells us that the outsized option strategy return comes with an outsized amount of risk.

  ```python
  # Calculate Sharpe Ratio
  annualized_return = signals_df["Strategy Returns"].mean() * 252
  annualized_std = signals_df["Strategy Returns"].std() * np.sqrt(252)
  sharpe_ratio = round(annualized_return/annualized_std, 3)

  # Display results
  print("Sharpe Ratio:", sharpe_ratio)
  ```

  ```text
  Sharpe Ratio: 0.688
  ```

* Another way to assess risk is to observe the best and worst week returns. We can get a measure of best-case and worst-case weekly performance by grouping the strategy returns by year and by week, and then adding up returns within each week, as the following code shows:

  ```python
  # Calculate weekly returns
  weekly_returns = signals_df["Strategy Returns"].groupby(
          by=[
              signals_df.index.year,
              signals_df.index.week
          ]
      ).sum()

  # Display results
  weekly_returns.head()
  ```

  ```text
  date  date
  2014  1       0.008679
        15     -0.195647
        16     -0.206601
        17      0.228056
        18      0.026974
  ```

* Running describe gives us a high level view of that weekly performance. In the best week, we made 61%. Nice! But our worst week was -620%. If we had been reinvesting all our gains and losses (i.e., cumulative product returns), this one week would have completely wiped us out.

  > **Note:** Our backtest involves going long (buying) and short (selling) options. When we go short, we can lose *more* than our original investment--that is, greater than a `100%` loss.

    ```python
    # Fetch descriptive statistics
    weekly_returns.describe()
    ```

    ```text
    count    363.000000
    mean       0.031288
    std        0.363318
    min       -6.149959
    25%       -0.048737
    50%        0.027361
    75%        0.128409
    max        0.611968
    Name: Strategy Returns, dtype: float64
    ```

Finally, explain to students that when we plot the raw strategy returns to visualise that kind of risk, most of the time, risk is high, but not that high. But just one day of jump risk is enough to effect our performance. This is one reason why options trading can be so much more risky than equity trading.

```python
# Plot weekly returns
weekly_returns.plot(rot=45)
```

![Weekly returns](Images/15-3-daily_returns_plot.png)

Be sure that there are no questions before moving forward.

---

### 3. Students Do: Evaluating Algorithmic Strategy Performance (15 min)

**Corresponding Activity:** [03-Stu_Perf_Metrics](Activities/03-Stu_Perf_Metrics)

**Files:**

* [Instructions](Activities/03-Stu_Perf_Metrics/README.md)

* [Unsolved](Activities/03-Stu_Perf_Metrics/Unsolved/algo_trading_performance.ipynb)

* [equity_algos.csv](Activities/03-Stu_Perf_Metrics/Resources/equity_algos.csv)

* [equity_trades.csv](Activities/03-Stu_Perf_Metrics/Resources/equity_trades.csv)

* [option_algos.csv](Activities/03-Stu_Perf_Metrics/Resources/option_algos.csv)

* [option_trades.csv](Activities/03-Stu_Perf_Metrics/Resources/option_trades.csv)

In this activity, students will utilise the various performance metrics to consider the performance and investment tradeoffs to various algorithmic strategies.

---

### 4. Instructor Do: Review Evaluating Algorithmic Strategy Performance (10 min)

**Corresponding Activity:** [03-Stu_Perf_Metrics](Activities/03-Stu_Perf_Metrics)

**Files:**

* [Instructions](Activities/03-Stu_Perf_Metrics/README.md)

* [Solved](Activities/03-Stu_Perf_Metrics/Unsolved/algo_trading_performance.ipynb)

* [equity_algos.csv](Activities/03-Stu_Perf_Metrics/Resources/equity_algos.csv)

* [equity_trades.csv](Activities/03-Stu_Perf_Metrics/Resources/equity_trades.csv)

* [option_algos.csv](Activities/03-Stu_Perf_Metrics/Resources/option_algos.csv)

* [option_trades.csv](Activities/03-Stu_Perf_Metrics/Resources/option_trades.csv)

Start by reviewing the four different DataFrames that the starter code is reading in. This contains the actual daily trading performance of a trading algorithm for three different stocks (`equity_algos`) and on options on those stocks (`option_algos`), as well the number of trades that each strategy generates each day (`equity_trades` and `option_trades`).

#### Plotting Performance

Plot the non-compounded performance of the option returns using cumulative sum. Explain to students that, using `cumsum` simulates a strategy in which we essentially "take profits off the table"--i.e., we don't reinvest them. However, it also means that we finance any ongoing losses.

```python
# Plot non-compounded returns (`cumsum`) to the three option strategies.
(option_returns).cumsum().plot()
```

![total-option-returns.png](Images/15-3-total-option-returns.png)

Explain to students that we can plot cumulative performance for the equity strategies using compounded returns, like we've done before.

```python
# Plot compounded returns (1+`cumprod`) to the three equity strategies.
(1+equity_returns).cumprod().plot()
```

![cumulative-equity-returns.png](Images/15-3-cumulative-equity-returns.png)

#### Adding Transaction Costs

Start by illustrating transaction costs for equities and highlight the following:

* Trading equities are cheap (or even free). Here we can assume every time we trade, it costs 0.10% (one tenth of one percent) of the shares bought or shorted.

  ```python
  # Trading Costs
  cost_per_trade = 0.001
  daily_trade_costs_equity = equity_trades * cost_per_trade
  daily_trade_costs_equity.head(2)
  ```

  ![daily_equity_trade_costs.png](Images/15-3-daily_equity_trade_costs.png)

* Equity returns can then be adjusted downward by the cost to trade:

  ```python
  equity_returns_after_cost = equity_returns - daily_trade_costs_equity
  equity_returns_after_cost.head()
  ```

  ![after_cost_equity_returns.png](Images/15-3-after_cost_equity_returns.png)

* While we're at it, let's do the same thing for options. Options are more expensive to trade, so let's say 0.50% per trade (half a percent).

  ```python
  # Trading Costs
  cost_per_trade = 0.005
  daily_trade_costs_options = option_trades*cost_per_trade
  option_returns_after_cost = option_returns - daily_trade_costs_options
  option_returns_after_cost.head()
  ```

  ![option_returns_after_cost.png](Images/15-3-option_returns_after_cost.png)

#### Plotting Performance After Transaction Costs

Start plotting the cumulative performance of the after transaction costs equity returns.

```python
# Plot cumulative performance of after costs equity returns
(1+equity_returns_after_cost).cumprod().plot()
```

![after_cost_cumulative_equity_returns.png](Images/15-3-after_cost_cumulative_equity_returns.png)

Continue the review and highlight the following:

* When we compare this result to the pre-transaction equity returns, performance is reduced by a fair bit. That's the reality of algorithmic trading: results are very sensitive to trading costs.

* Let's take a similar look at option returns. Remember that with options, we're looking at non-compounded (non-reinvesting of profits) returns. (Basically, this approach helps us avoid losing everything when, invariably, the option strategy "blows up").

  ```python
  # Plot total performance of the option returns
  (option_returns_after_cost).cumsum().plot()
  ```

  ![after_cost_option_returns.png](Images/15-3-after_cost_option_returns.png)

#### Calculate Sharpe Ratios

Explain to students that, at this point, the following may arise: So which is better? Trading in the equity, or trading in the option?

Explain to students that one way to answer this is to compare Sharpe Ratios. Highlight the following:

* First we calculate Sharpe Ratios for the equity strategies, using returns *after* transaction costs:

  ```python
  annualized_return = equity_returns_after_cost.mean()*252
  annualized_std = equity_returns_after_cost.std()*np.sqrt(252)
  annualized_return/annualized_std
  ```

  ```python
  ANTM    0.802410
  SPY     0.487163
  EWJ     0.052008
  ```

* Then we calculate Sharpe Ratios for the options strategies, again using returns *after* transaction costs:

  ```python
  annualized_return = option_returns_after_cost.mean()*252
  annualized_std = option_returns_after_cost.std()*np.sqrt(252)
  annualized_return/annualized_std
  ```

  ```python
  ANTM    0.686211
  SPY     1.146813
  EWJ     0.715246
  ```

#### Calculate Weekly Returns

Explain to students that, another way to compare trading in the equity or option is to look at maximum risk. Highlight the following:

* Let's look at the best and worst weekly returns. First for the equity returns.

  ```python
  weekly_returns = equity_returns_after_cost.groupby(
      by=[
          equity_returns_after_cost.index.year,
          equity_returns_after_cost.index.week
      ]
  ).sum()
  weekly_returns.describe()
  ```

  ![weekly_returns_equities.png](Images/15-3-weekly_returns_equities.png)

* Then the same for option returns.

  ```python
  weekly_returns = option_returns_after_cost.groupby(
      by=[
          option_returns_after_cost.index.year,
          option_returns_after_cost.index.week
      ]
  ).sum()
  weekly_returns.describe()
  ```

  ![weekly_options_equities.png](Images/15-3-weekly_options_equities.png)

* Based on the output of our code, the option returns are much more risky. The worst week for this strategy ranged from -68% (ANTM) to -279% (EWJ). Yikes! The worst equity week ranged from -8% (SPY and EWJ) to -10% (ANTM), which is pretty good by comparison.

Conclude that option returns were, by comparison, unambiguously better. However, consider the real risk of loss: with options, you can lose three times your initial investment in as little as a week. By contrast, with equities, the worst week was a loss of about 10%. Before trading any algorithm, consider which loss you can really tolerate.

Before moving on, however, ask students if they have any questions.

---

### 5. Instructor Do: Data Preparation for a Machine Learning Trading Strategy (15 min)

**Corresponding Activity:**[04-Ins_Data_Prep_for_ML](Activities/04-Ins_Data_Prep_for_ML)

In this activity, students will review the process of collecting and preparing data for algorithmic trading with machine learning; they will learn that this process is similar to the process that we followed in the previous lessons.

**Files:**

* [Unsolved](Activities/04-Ins_Data_Prep_for_ML/Unsolved/data_prep_for_ml.ipynb)

* [Solved](Activities/04-Ins_Data_Prep_for_ML/Solved/data_prep_for_ml.ipynb)

* [ohlcv.csv](Activities/04-Ins_Data_Prep_for_ML/Resources/ohlcv.csv)

Explain to the students that, before incorporating machine learning into a trading algorithm, we will review the data preparation process that is required in order to run an algorithmic trading strategy with machine learning. The process of collecting and preparing data for algorithmic trading with machine learning is the same process that we followed in the previous lessons; however, there are some nuances that are worth highlighting.

Open the unsolved version of the provided Jupyter notebook and highlight the following:

* Recall that before fitting a machine learning algorithm, we need to make sure that all the features (variables) are numeric. Also, we need to select a set of features that might have predictive power.

* For this demo, we'll import a financial dataset that contains the open, high, low, close, and volume (OHLCV) values for a stock.

* The following code imports the dataset into a Pandas DataFrame and sets the `date` column as the `DatetimeIndex`.

  ```python
  # Import the OHLCV dataset into a Pandas Dataframe
  trading_df = pd.read_csv(
      Path("../Resources/ohlcv.csv"),
      index_col="date",
      infer_datetime_format=True,
      parse_dates=True
  )

  # Display sample data
  trading_df.head()
  ```

  ![Load OHLCV Stock data](Images/15-3-load-ohlcv-data.png)

* Next, we use the Pandas `pct_change` function to calculate the daily returns from the closing prices. We assign these values to a new column named "actual_returns". (We call them "actual_returns" so that it's easier to distinguish from returns predicted by an ML model later on.)

  ```python
  # Calculate the daily returns using the closing prices and the pct_change function
  trading_df["actual_returns"] = trading_df["close"].pct_change()

  # Display sample data
  trading_df.head()
  ```

  ![Calculating actual returns](Images/15-3-calculating-actual-returns.png)

* Notice the `NaN` value in the `actual_returns` column. Our trading strategy won’t find these values useful. So, we use the Pandas `drop_na` function to drop all the NaN values from the DataFrame.

```python
# Drop all NaN values from the DataFrame
trading_df = trading_df.dropna()

# Review the DataFrame
display(trading_df.head())
display(trading_df.tail())
```

![Dropping NAN values](Images/15-3-dropping-nan-values.png)

* Now that we have collected and prepared our data, it’s time to create the features and target sets to fit our machine learning model.

Explain to students that, regardless of whether we use a machine learning model in our trading strategy, we should always prepare our data. In practice, we can get financial data from an enterprise resource planning (ERP) system in the form of a CSV file or a database connection. We can also retrieve data from APIs, like the Alpaca API, as you learned before.

Continue the demo and explain to students that we will use supervised machine learning for our trading algorithms.

Remind students that supervised machine learning models require us to define a set of features (`X`) that will predict a target variable (`y`). Because we’ll build a trading algorithm that’s powered by machine learning, our features and target sets will use technical analysis indicators for the stocks that we want to trade.

Continue the demo, live code the creation of the features and target sets and highlight the following.

* Think back to the dual moving average crossover (DMAC) trading algorithm that we generated during the activities in the previous class.

* We used a single trading signal to determine the entry and exit points for the algorithm. (That trading signal was the crossover point between the short-window and long-window SMAs.) The lesson demonstrations used the data to generate trading signals for holding long positions. By contrast, the activities used the trading signals to initiate short-position trades—first selling stock and then buying it to cover the sale, ideally at a lower price.

* For our machine learning–powered trading algorithm, the trading signals will make up the features set.

* Our new trading algorithm will continue to use the same short- and long-window SMA logic, but with a slight difference. We’ll create an SMA column using a window size of 4 days, and name it `sma_fast`. We’ll create another SMA column using a window size of 100 days, and name it `sma_slow`.

* Let's start by creating the `sma_fast` column in our DataFrame.

  ```python
  # Define a window size of 4
  short_window = 4

  # Create an SMA that uses short_window, and assign it to a new column named “sma_fast”
  trading_df["sma_fast"] = trading_df["close"].rolling(window=short_window).mean()
  ```

* Similarly, we create the `sma_slow` column in our DataFrame.

  ```python
  # Define a window size of 100
  long_window = 100

  # Create an SMA that uses long_window, and assign it to a new columns named “sma_slow”
  trading_df["sma_slow"] = trading_df["close"].rolling(window=long_window).mean()
  ```

* Next, we drop all the NaN values by using the `dropna` function.

  ```python
  # Drop the NaNs using dropna()
  trading_df = trading_df.dropna()
  ```

* Finally, we create the `X` features set by copying the `sma_fast` and `sma_slow` columns from our original DataFrame into a new DataFrame named `X`.

```python
# Assign a copy of the `sma_fast` and `sma_slow` columns to a new DataFrame called `X`
X = trading_df[["sma_fast", "sma_slow"]].shift().dropna().copy()

# Display sample data
display(X.head())
display(X.tail())
```

![Create features set](Images/15-3-create-features-set.png)

Explain to the students that we want the model to learn a predictive relationship. (That is, we want to know how `sma_fast` and `sma_slow` will predict returns in the future.) That's why we used the shift function to shift the feature columns by 1. Doing so ensures that the model will use the current values to predict the outcome for the next period.

Continue the demo creating the target set and highlight the following:

* Since we’ll use a supervised learning algorithm, we need to create a target set of the values that we want to predict. In this case, we’ll predict a signal that indicates whether we should buy or sell.

* For this trading algorithm, we’ll set the signals as follows: If the actual returns are equal to or greater than zero, we’re earning money. Therefore, the signal will indicate that we should buy a position, or go long, on the stock. By contrast, if the actual returns are less than zero, we’re starting to lose money. Therefore, we want to short the stock—that is, sell it with the intention of buying it later, at a lower price, to cover the sale.

* Let’s return to our original DataFrame and create a new column named “signal”. For now, this column will contain zeros

  ```python
  # Create a new column in the `trading_df` called "signal" setting its value to zero.
  trading_df["signal"] = 0.0
  ```

* Using the Pandas `loc` function, we evaluate whether the actual returns are positive, negative, or zero. Where the `actual_returns` value is greater than or equal to zero, we set the `signal` value to 1. Where the `actual_returns` value is less than zero, we set the `signal` value to −1.

  ```python
  # Create the signal to buy
  trading_df.loc[(trading_df["actual_returns"] >= 0), "signal"] = 1

  # Create the signal to sell
  trading_df.loc[(trading_df["actual_returns"] < 0), "signal"] = -1
  ```

* Finally, we create the target set by copying the new `signal` column to a new Pandas Series named `y`.

  ```python
  # Copy the new "signal" column to a new Series called `y`.
  y = trading_df["signal"].copy()
  ```

Explain to students that now, the `y` target set includes the target signals that we want to predict. A value of 1 indicates that the algorithm will buy stock. A value of −1 indicates that the algorithm will sell.

Now that we have created the features and target sets, it’s time to split the data into training and testing datasets.

Explain to the students that, as we did with machine learning models in previous modules, we’ll split the prepared data into training and testing sets. We’ll use the training data to train the machine learning model to make buy and sell predictions. We’ll use the testing data to backtest the trained model—to find out how well it performs at algorithmic trading.

However, explain to students that rather than using `train_test_split` from Scikit-learn to create the training and testing sets, as we did in the previous modules, we’ll split the data into training and testing sets by using date windows.

Continue the demo by moving to the "Split the Data Into Training and Testing Sets" section of the notebook and highlighting the following.

* For this demo, our training data will contain only a portion of the entire dataset—specifically, three months’ worth.

* We therefore need to create a date offset of three months. To do so, we first need to import the `DateOffset` module from `pandas.tseries.offsets`.

  ```python
  # Import required libraries
  from pandas.tseries.offsets import DateOffset
  ```

* To define the training dataset, we need to define where we want the training data values to begin and end.

* We first define two new variables: `training_begin` and `training_end`. We use the Pandas `index.min` function to set the value of `training_begin` to the minimum index value in the `X` features DataFrame.

  ```python
  # Select the start of the training period
  training_begin = X.index.min()

  # Display the training begin date
  print(training_begin)
  ```

  ```text
  2018-10-24 15:15:00
  ```

* Next, we use the `DateOffset` module to set the value of `training_end` to the minimum index value plus a date offset of three months.

  ```python
  # Select the ending period for the training data with an offset of 3 months
  training_end = X.index.min() + DateOffset(months=3)

  # Display the training end date
  print(training_end)
  ```

  ```text
  2019-01-24 15:15:00
  ```

* Notice that the training period begins at the index labelled `2018-10-24 15:15:00` and ends at the index labelled `2019-01-24 15:15:00`. The training dataset thus begins on `2018-10-24` and ends three months later on `2019-01-24`.

* Now, we can generate our `X_train` and `y_train` datasets by using the `loc` function with our `training_begin` and `training_end` values.

  ```python
  # Generate the X_train and y_train DataFrames
  X_train = X.loc[training_begin:training_end]
  y_train = y.loc[training_begin:training_end]
  ```

* Now, we will create our testing datasets. The only difference when we create the `X_test` and `y_test` DataFrames occurs when we slice the data. We slice the index starting at the `training_end` value and ending at the last record of the datasets.

  ```python
  # Generate the X_test and y_test DataFrames
  X_test = X.loc[training_end:]
  y_test = y.loc[training_end:]
  ```

* Finally, as we did before with machine learning models, the next step is to standardise the data in the `X_train` and `X_test` DataFrames by using the `StandardScaler` module from Scikit-learn.

Explain to students that, right now, the values of our features (that is, the `X` data values that we’ll use to make predictions) aren’t standardised. If certain `sma_fast` and `sma_slow` values are very high, that might skew our model’s ability to develop accurate predictions. So, like with most machine learning applications, we should first standardise, or scale, our feature data.

Continue the demo, move to the "Standardize the Data" section in the notebook and highlight the following:

* As before, we use the `StandardScaler` module to transform our `X_train` and `X_test` datasets.

* To do so, we import the `StandardScaler` module from `sklearn.preprocessing`, instantiate a new `StandardScaler` instance, and then fit it to our `X_train` dataset.

  ```python
  # Import the required module
  from sklearn.preprocessing import StandardScaler

  # Create a StandardScaler instance
  scaler = StandardScaler()

  # Apply the scaler model to fit the X_train data
  X_scaler = scaler.fit(X_train)

  # Transform the X_train and X_test DataFrames using the X_scaler
  X_train_scaled = X_scaler.transform(X_train)
  X_test_scaled = X_scaler.transform(X_test)
  ```

Conclude this activity by explaining to the students that now our feature data is standardised, so any outlier data points shouldn’t influence the machine learning model. With our data finally prepared and ready to go, we can incorporate the machine learning model into our trading strategy. But first, it's time for students to practice the data preparation process.

Be sure that there are no questions before moving forward.

---

### 6. Students Do: Preparing Data for a Machine Learning Trading Strategy (15 min)

**Corresponding Activity:** [05-Stu_Preparing_Data](Activities/05-Stu_Preparing_Data)

**Files:**

* [Instructions](Activities/05-Stu_Preparing_Data/README.md)

* [Unsolved](Activities/05-Stu_Preparing_Data/Unsolved/preparing_data.ipynb)

In this activity, students will prepare training and testing data for fitting a machine learning-powered trading algorithm.

---

### 7. Instructor Do: Review Preparing Data for a Machine Learning Trading Strategy (10 min)

**Corresponding Activity:** [05-Stu_Preparing_Data](Activities/05-Stu_Preparing_Data)

**Files:**

* [Instructions](Activities/05-Stu_Preparing_Data/README.md)

* [Unsolved](Activities/05-Stu_Preparing_Data/Unsolved/preparing_data.ipynb)

* [Solved](Activities/05-Stu_Preparing_Data/Solved/preparing_data.ipynb)

Open the unsolved version of the provided Jupyter notebook, live code the solution and highlight the following:

* The data preparation process to use a machine learning model in a trading algorithm, is similar to the process we learned in previous units.

* Perhaps, the main difference is how we split the data into training and testing sets.

* For this demo, we use data that contains open, high, low, close, and volume information for a given stock.

* We read in the data into a Pandas DataFrame. In this case, we set as the DataFrame index the `date` column and we parse the dates in the `read_csv` function call.

  ```python
  # Import the OHLCV dataset into a Pandas Dataframe
  trading_df = pd.read_csv(
      Path("../Resources/ohlcv.csv"),
      index_col="date",
      infer_datetime_format=True,
      parse_dates=True
  )
  ```

* Next, as part of the data preparation process, we use the Pandas `pct_change` function to add a new column that contains the daily returns. Recall that it's important to drop the `NaN` values.

  ```python
  # Calculate the daily returns using the closing prices and the pct_change function
  trading_df["actual_returns"] = trading_df["close"].pct_change()

  # Drop all NaN values from the DataFrame
  trading_df = trading_df.dropna()
  ```

* We should also perform any data cleaning required, for this demo, we don't need to perform any additional data cleaning task since the data provided is in the appropriate shape and format.

* The next step is to generate the features set `X` and the target set `y`. For the features set, we compute the fast and the slow moving average with a window size of 4 and 100 days respectively.

  ```python
  # Define a window size of 4
  short_window = 4

  # Create a simple moving average (SMA) using the short_window and assign this to a new columns called sma_fast
  trading_df['sma_fast'] = trading_df['close'].rolling(window=short_window).mean()

  # Define a window size of 100
  long_window = 100

  # Create a simple moving average (SMA) using the long_window and assign this to a new columns called sma_slow
  trading_df['sma_slow'] = trading_df['close'].rolling(window=long_window).mean()

  # Drop the NaNs using dropna()
  trading_df = trading_df.dropna()

  # Assign a copy of the sma_fast and sma_slow columns to a new DataFrame called X
  X = trading_df[['sma_fast', 'sma_slow']].copy()
  ```

* Our trading algorithm will predict the trading signal to define whether or not we will buy or sell. We add a `signal` column to the DataFrame using the `loc` Pandas functions as follows: where the `actual_returns` value is greater than or equal to zero, we set the `signal` value to 1 (buy). Where the `actual_returns` value is less than zero, we set the `signal` value to −1 (sell).

  ```python
  # Create a new column in the trading_df called signal setting its value to zero.
  trading_df['signal'] = 0.0

  # Create the signal to buy
  trading_df.loc[(trading_df['actual_returns'] >= 0), 'signal'] = 1

  # Create the signal to sell
  trading_df.loc[(trading_df['actual_returns'] < 0), 'signal'] = -1

  # Copy the new signal column to a new Series called y.
  y = trading_df['signal'].copy()
  ```

* Next, we create the training and testing sets. This is where the data preparation process differs from what we learned before since we use the `DateOffset` module from Pandas to slice the data.

  ```python
  # Generate the X_train and y_train DataFrames
  X_train = X.loc[training_begin:training_end]
  y_train = y.loc[training_begin:training_end]

  # Generate the X_test and y_test DataFrames
  X_test = X.loc[training_end:]
  y_test = y.loc[training_end:]
  ```

* Finally, we use the `StandardScaler` from Scikit-learn to standardised the data.

  ```python
  # Imports
  from sklearn.preprocessing import StandardScaler

  # Create a StandardScaler instance
  scaler = StandardScaler()

  # Apply the scaler model to fit the X-train data
  X_scaler = scaler.fit(X_train)

  # Transform the X_train and X_test DataFrames using the X_scaler
  X_train_scaled = X_scaler.transform(X_train)
  X_test_scaled = X_scaler.transform(X_test)
  ```

Be sure that there are no questions before moving forward.

---

### 8. BREAK (15 min)

---

### 9. Instructor Do: Use Machine Learning in a Trading Strategy (20 min)

**Corresponding Activity:** [06-Ins_ML_Trading_Strategy](Activities/06-Ins_ML_Trading_Strategy)

In this activity, students will learn how to fit a machine learning model to predict the target trading signal. For this demonstration, we'll use the support vector machine (SVM) learning method from SKLearn, and its SVC classifier model.

**Files:**

* [Unsolved](Activities/06-Ins_ML_Trading_Strategy/Unsolved/ml_trading_strategy.ipynb)

* [Solved](Activities/06-Ins_ML_Trading_Strategy/Solved/ml_trading_strategy.ipynb)

* [ohlcv.csv](Activities/06-Ins_ML_Trading_Strategy/Resources/ohlcv.csv)

Explain to students that, in this section, we’ll use our training data to fit a machine learning model to predict the target trading signal. For this demonstration, we'll use the support vector machine (SVM) learning method from SKLearn, and its `SVC` classifier model. The reason is its ability to discriminate between two classes, and we want to predict whether the signal will be 1 or −1.

Open the provided unsolved Jupyter notebook. Move to the "Part 2 Using Machine Learning in a Trading Strategy" section (cell 20) and run all the cells above to load and clean the data while you explain to students that, for this demo, you will use the OHLCV data that you prepared in the previous instructor demo. (The already completed code in cells 1 through 20 in this notebook contains code identical to that of the previous instructor activity, except for changes to the size of the testing window and speed of the fast/slow parameters).

Live code the demo and highlight the following:

* We start by importing the SVM classifier model and the `classification_report` from Scikit-learn.

  ```python
  # Import the SVM model
  from sklearn import svm
  from sklearn.metrics import classification_report
  ```

* Next, we create an instance of the `SVM` model and fit it to the `X_train_scaled` and `y_train` data.

  ```python
  # Create the classifier model
  svm_model = svm.SVC()

  # Fit the model to the data using X_train_scaled and y_train
  svm_model = svm_model.fit(X_train_scaled, y_train)
  ```

* Now, as we did with other machine learning models, the model learns from the training dataset and can make predictions based on the testing dataset, which is `X_test_scaled` in this case. The `training_signal_predictions` variable will contain our predicted values, which will exist in an array of `1` and `−1` values.

  ```python
  # Use the trained model to predict the trading signals for the training data
  training_signal_predictions = svm_model.predict(X_train_scaled)

  # Display the sample predictions
  training_signal_predictions[:10]
  ```

  ```text
  array([-1., -1., -1., -1., -1., -1., -1., -1., -1., -1.])
  ```

* Once we have generated predictions from our training data, we evaluate the results by using the `classification_report` module from Scikit-learn.

  ```python
  # Evaluate the model using a classification report
  training_report = classification_report(y_train, training_signal_predictions)

  # Display report
  print(training_report)
  ```

  ```text
                precision   recall   f1-score   support

        -1.0       0.57      0.02      0.04      4487
         1.0       0.53      0.99      0.69      4968

    accuracy                           0.53      9455
   macro avg       0.55      0.50      0.36      9455
  ```

* Note that the precision values are similar for both classes; however, the recall for the `1` class is higher than the recall to the `-1` class. Based on the higher recall, it seems that the model (based on the training data) is better at predicting the `1` class than the `−1` class.

Explain to the students that before putting a model to work with new data, it’s important to test it. So in the next step, we use the testing data to backtest the trading algorithm.

Remind the students that with backtesting, we can assess the performance of a trading strategy by using historical data to find out how the model would have performed in the past.

Explain that, in order to backtest our model, we use the trained model to predict the trading signals for the testing data.

```python
# Use the trained model to predict the trading signals for the testing data.
testing_signal_predictions = svm_model.predict(X_test_scaled)
```

After using the testing data to backtest our model, explain to the students that now, we can evaluate the ability of the model to make predictions by using a classification report.

```python
# Evaluate the model's ability to predict the trading signal for the testing data
testing_report = classification_report(y_test, testing_signal_predictions)

# Display the report
print(testing_report)
```

```text
              precision    recall  f1-score   support

        -1.0       0.46      0.99      0.63      1192
         1.0       0.56      0.01      0.03      1401

    accuracy                           0.46      2593
   macro avg       0.51      0.50      0.33      2593
weighted avg       0.51      0.46      0.30      2593
```

Explain to the students that the overall performance of this trading algorithm, based on the accuracy score, is roughly similar for the training data (`0.46` versus `0.53`). But in the testing data, the recall is much higher for the `-1.0` values, and much lower for the `1.0` values. This is common in real world scenarios, in which the training and testing results can differ, especially when testing datasets are small.

For a different perspective on the model's performance, explain to students that we can also create a plot to visually compare the actual and predicted returns. Continue the demo and highlight the following.

* To visually compare the actual and predicted returns, we will create a new DataFrame with the actual and predicted returns.

  ```python
  # Create a predictions DataFrame
  predictions_df = pd.DataFrame(index=X_test.index)

  predictions_df["predicted_signal"] = testing_signal_predictions

  predictions_df["actual_returns"] = trading_df["actual_returns"]

  predictions_df["trading_algorithm_returns"] = (
      predictions_df["actual_returns"] * predictions_df["predicted_signal"]
  )

  # Review the DataFrame
  predictions_df.head()
  ```

  ![Actual and predicted returns](Images/15-3-ml-actual-predicted-returns.png)

* Notice that the DataFrame has `predicted_signal`, `actual_returns`, and `trading_algorithm_returns` columns.

* Now, we plot the cumulative returns. We can then compare the actual returns to those that our SVM model predicted by using the historical data.

  ```python
  # Calculate and plot the cumulative returns for the `actual_returns` and the `trading_algorithm_returns`
  (1 + predictions_df[["actual_returns", "trading_algorithm_returns"]]).cumprod().plot()
  ```

  ![Actual returns vs. predicted returns plot](Images/15-3-plot-actual-predicted-returns.png)

Explain that, for this particular dataset, it seems that by the end of the test period, our SVM model had underperformed somewhat, with the biggest divergence relative to a long-only strategy during the spring of 2020. This was a time when the market was strongly rebounding from a crash, so anything that wasn't long only at this time was a disadvantage. Testing this model out on additional time periods&mdash;additional test datasets&mdash;might give us a better picture about how the model will perform under a variety of market conditions.

Be sure that there are no questions before moving forward.

---

### 10. Students Do: Using a New Machine Learning Classifier for Algorithmic Trading (30 min)

**Corresponding Activity:**[07-Stu_New_ML_Classifier](Activities/07-Stu_New_ML_Classifier)

**Files:**

* [Instructions](Activities/07-Stu_New_ML_Classifier/README.md)

* [Unsolved](Activities/07-Stu_New_ML_Classifier/Unsolved/new_ml_classifier.ipynb)

* [ohlcv.csv](Activities/07-Stu_New_ML_Classifier/Resources/ohlcv.csv)

In this activity, the students will evaluate how our earlier trading strategy behaves when it uses a different machine learning classification model, and alternative moving average parameters and test windows. This is a mini project activity that can be done in teams of two students.

---

### 11. Instructor Do: Review Using a New Machine Learning Classifier for Algorithmic Trading (15 min)

**Corresponding Activity:** [07-Stu_New_ML_Classifier](Activities/07-Stu_New_ML_Classifier)

**Files:**

* [Solved](Activities/07-Stu_New_ML_Classifier/Solved/new_ml_classifier.ipynb)

* [Unsolved](Activities/07-Stu_New_ML_Classifier/Unsolved/new_ml_classifier.ipynb)

* [ohlcv.csv](Activities/07-Stu_New_ML_Classifier/Resources/ohlcv.csv)

Congratulate students on learning how to use machine learning to generate trading signals!

Open the unsolved version of the provided Jupyter notebook. Explain to the students that the main goal of this activity is to compare the performance of two machine learning models for a single trading strategy.

Explain that, in the first part of this activity we'll review the process of loading and preparing data to be used in a machine learning powered trading strategy. First, a SVM model is used, and then they are asked to run a new model by using the `LogisticRegression` classifier provided by Scikit-learn.

Live code the solution and highlight the following:

* To test a logistic regression model in our algorithmic trading strategy, first we import it from Scikit-learn and create an instance.

  ```python
  # Import LogisticRegression from sklearn
  from sklearn.linear_model import LogisticRegression

  # Create an instance of the LogisticRegression model
  logistic_regression_model = LogisticRegression()
  ```

* Next, it's important to train (fit) the new model using the same training data to have an identical point of comparison.

  ```python
  # Fit the LogisticRegression model
  logistic_regression_model.fit(X_train_scaled, y_train)
  ```

* After training the logistic regression model, we can make some predictions and assess the model performance using the training dataset.

  ```python
  # Use the trained LogisticRegression model to predict the trading signals for the training data
  lr_training_signal_predictions = logistic_regression_model.predict(X_train_scaled)

  # Display the predictions
  lr_training_signal_predictions
  ```

  ```text
  array([-1., -1., -1., ...,  1.,  1.,  1.])
  ```

  ```python
  # Generate a classification report using the training data and the logistic regression model's predications
  lr_training_report = classification_report(y_train, lr_training_signal_predictions)

  # Review the classification report
  print(lr_training_report)
  ```

  ```text
                precision    recall  f1-score   support

          -1.0       0.51      0.24      0.33       741
           1.0       0.52      0.77      0.62       776

      accuracy                           0.51      1517
     macro avg       0.51      0.51      0.47      1517
  weighted avg       0.51      0.51      0.48      1517
  ```

* We continue backtesting our model using the `fit` function and the testing data.

  ```python
  # Use the trained model to predict the trading signals for the testing data.
  lr_testing_signal_predictions = logistic_regression_model.predict(X_test_scaled)

  # Generate a classification report using the testing data and the logistic regression model's predictions
  lr_testing_report = classification_report(y_test, lr_testing_signal_predictions)
  ```

* Finally, to identify what model performs better between the SMV and the logistic regression, we use the classification report of each model.

  ```python
  # Print the classification report for the Logistic Regression model using the test data
  print("Logistic Regression Classification Report")
  print(lr_testing_report)
  ```

  ```text
  Logistic Regression Classification Report
                precision    recall  f1-score   support

          -1.0       0.52      0.07      0.12      4894
           1.0       0.54      0.94      0.68      5559

      accuracy                           0.53     10453
     macro avg       0.53      0.51      0.40     10453
  weighted avg       0.53      0.53      0.42     10453
  ```

  ``` python
  # Print the classification report for the SVM model using the test data
  print("SVM Classification Report")
  print(svm_testing_report)
  ```

  ```text
  SVM Classification Report
                  precision    recall  f1-score   support

           -1.0       0.47      0.37      0.42      4894
            1.0       0.53      0.64      0.58      5559

      accuracy                           0.51     10453
     macro avg       0.50      0.50      0.50     10453
  weighted avg       0.51      0.51      0.50     10453
  ```

Ask to students to share their insight about the final results. Facilitate an open discussion to listen to one or two teams.

Ultimately, the class consensus and your own conclusions will drive the conclusions that are reached in this dicsussion. Here are some suggested viewpoints that have emerged from previous class discussions:

* After reviewing the final results, the logistic regression model performs a bit better than the SVM model because it has a higher accuracy score. However, by observing the recall, we'll conclude that neither algorithm is great at predicting successful short trades (`-1.0`) compared to long trades. Of all the potential short opportunities (recall), the logistic model predicted only `7%` of them, and the SVM predicted only `37%`. If we care more about correctly identifying short opportunities, the SVM might be a better choice than the logistic regression, despite its lower overall accuracy.

* Low recall for one class doesn't necessarily mean that both models aren't usable—part of the underprediction of negative returns in the test data relates to the unprecedented stock market crash in 2020. Because the model was built on the training data, the model (and many market participants at the time) simply had no conception that this type of severe downturn, present in the test data, was possible. (For example, the unemployment rate in the U.S. during this time was fast approaching `15%` of the workforce, something that hadn't been observed since the 1920s). Systematic traders call this type of risk "out of model" risk because it's a rare enough event that the model simply wasn't built to capture. However, "out of model" risk doesn't mean we abandon building models; it means we acknowledge their limitations.

* Despite the low recall for the short positions, the plot of model cumulative returns versus long-only returns shows that the SVM model performed fairly well. While it tended to miss most short opportunities, it still got enough of the short predictions right when it really mattered during March of 2020. As a result, it performed spectacularly well when most of the market was tanking (providing diversification), and it outperformed a long-only investment in the same stock over the test period.

* If there's any takeaway here, it's that there is rarely only one metric to always focus on. Classification reports matter, but we need to consider which class (long or short) we're most concerned about getting right. And classification reports only tell part of the story. Ultimately, what matters may simply be whether the model outperforms, in terms of dollars, a long-only investment in the same security.

As a final conclusion, explain to the students that using machine learning models in trading algorithms increases their flexibility for both developing and backtesting their trading strategies. Machine learning models can better adapt to complex data and rapidly evolving situations than humans can. Additionally, they can now use the tools that they’ve learned to evaluate the performance of different machine learning models for the same trading strategy. They can then determine which model works best for the provided set of data.

Be sure that there are no questions before moving forward.

---

### 12. Instructor Do: Going Live with Algo Trading (15 min)

**Corresponding Activity:**[08-Ins_Live_Trade_Demo](Activities/08-Ins_Live_Trade_Demo)

To this point, we've looked at how to test out whether an algorithmic strategy would be profitable to trade, but we haven't yet covered *how* to actually trade live. This instructor demo represents a sort of "sneak-preview", if you will, of how that can be done and what websites students might visit if they want to apply an algorithmic trading system in real life.

> **Note**: You'll need to use your own API and Secret key here to run this code, remember to create a hidden `.env` file containing your keys.

**Files:**

* [Unsolved](Activities/08-Ins_Live_Trade_Demo/Unsolved/live_trade_demo.ipynb)

* [Solved](Activities/08-Ins_Live_Trade_Demo/Solved/live_trade_demo.ipynb)

Start this activity by introducing to the class two APIs which are commonly used for algorithmic trading.

* [Alpaca Trading](https://alpaca.markets/): Commission free, easy to use API.

* [InteractiveBrokers](https://www.interactivebrokers.com/en/trading/ib-api.php): Not commission free, but provides the ability to trade globally in all assets -- from equities, to futures and bonds, using a single API.

Visit the [Alpaca website](https://alpaca.markets/) and remind students that we used its Python SDK before. Explain to students that now, we will use Alpaca to demo the use of the buy/sell logic to place API calls. Live code the demo and highlight the following:

* In this demo, we will walk through the logic of the code to illustrate that the next step in algorithmic trading--actually doing the trading--is not all that more difficult than what we've done thus far.

* Recall that to use the Alpaca API, we need to import the `tradeapi` module and load our API keys.

  ```python
  import alpaca_trade_api as tradeapi

  API_KEY = os.getenv("ALPACA_API_KEY")
  API_SECRET = os.getenv("ALPACA_SECRET_KEY")
  ALPACA_API_BASE_URL = "https://paper-api.alpaca.markets"
  ```

* Once that's done, we establish a connection to Alpaca's servers.

  ```python
  # Create a connection to the API
  api = tradeapi.REST(API_KEY, API_SECRET, ALPACA_API_BASE_URL, api_version="v2")
  ```

* For this we will use a the trading logic for a single stock, at a single point in time. Extending this logic to multiple stocks or continuous trading requires a for loop, but the logic stays the same.

* A model predicts a `signal` -- either `1` if it wants to go long, or `-1` if it wants to short. For this demo, we will manually set the signal to equal `1`.

  ```python
  # Set signal variable
  signal = 1
  ```

* Next, we code the trading logic. If the signal is long (`1`), we need to translate that into `buy` (long), or `sell` (short) otherwise. The `buy` or `sell` information is what we'll send to the broker's server when we submit the order.

  ```python
  # Create buy signal, num shares and ticker
  if signal == 1:
      orderSide = "buy"
  else:
      orderSide = "sell"
  ```

* We continue by specifying the number of shares (for now, just one share), as well as the ticker.

  ```python
  # Set the ticket symbol and the number of shares to buy
  ticker = "TSLA"
  number_of_shares = 1
  ```

* Before we submit an order though, we should figure out what a good price would be to pay for that stock. We need to get the most recent trading history, measured at 1 minute intervals, and get the most recent price. We'll save that most recent `close` price for the most recent 1 minute interval as a `limit_amount` value. This is the maximum price we'd be willing to buy at, or the minimum price we'd be willing to sell at, depending on whether we are long or short.

  ```python
  # Make API call
  prices = api.get_bars(ticker, "1Min").df

  # Reorganize the DataFrame
  prices = pd.concat([prices], axis=1, keys=["TSLA"])

  # Get final closing price
  limit_amount = prices["TSLA"]["close"][-1]
  ```

* With our price set, we can now submit the order! And this is all there is to it. (By the way, "gtc" means "good til cancelled", which means that this order stays out there, either waiting to be filled or until we issue a cancellation on it).

  ```python
  api.submit_order(
      symbol="TSLA",
      qty=number_of_shares,
      side=orderSide,
      time_in_force="gtc",
      type="limit",
      limit_price=limit_amount
  )
  ```

* At this point, there are many parameters we can add to our orders to help manage risk or increase profits, such as "stop loss" orders, or "fill or kill" orders.

Explain to students that what we learned in this demo is just an illustration to get them started, but there's a lot more that we can do to improve it. For this reason, for any student interested in going further in algorithmic trading, it's strongly recommended that they learn and work out the bugs on a **paper** (not real money) portfolio first. At Alpaca, it's easy and quick to sign up for such a virtual portfolio and begin testing various ML trading strategies out.

Be sure that there are no questions before ending the class.

---

End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
