## 14.1 Lesson Plan: Introduction to Algorithmic Trading

---

### Overview

Today's class will introduce students to **algorithmic trading** in Python. Traditional trading&mdash;the manual purchase and sale of assets, such as stocks&mdash;has shifted toward automated methods in recent years. This is because of advancements in technology, like network speed, computing power, and financial trading APIs. In this module, students will learn about a type of automated trading known as algorithmic trading.

**Algorithmic trading** uses technical indicators and conditional logic to identify signals for entering and exiting trades. First, students will learn how to build a simple trading algorithm. Later in the module, students will apply their knowledge of machine learning from earlier modules to evaluate the trading decisions of our algorithm. It's important to highlight to students that understanding how trading algorithms perform on past data offers insight into how they might behave in future market conditions. And, this ultimately leads to better trading decisions, improved portfolio performance, and increased profits.

By the end of this week, students will complete a Challenge assignment that uses machine learning to build an intelligent algorithmic trading system.

### Class Objectives

By the end of class, students will be able to:

* Delineate what algorithmic trading is, how it came to be, and why it's valuable.

* Deconstruct the process for algorithmic trading: obtaining the data, making a trading decision, and evaluating the results.

* Understand how technical indicators, like simple moving averages (SMAs), identify the trading signals that instruct a trading algorithm.

* Compare the differences between technical analysis and fundamental analysis.

* Define what a trading signal is, how it is used, and why it's important.

* Write their own simple trading algorithm based on technical indicators.

### Instructor Notes

* Today's lesson will consist of elements taught in the Pandas and PyViz units; the lesson will include data analysis and the visualisation of trading performance and transaction analysis using Matplotlib and hvPlot.

* **Note:** hvPlot requires Pandas version `0.23.4` to `0.24.2`. If errors occur in notebooks, be sure to verify package dependencies as a first step in troubleshooting.

* The goal of this unit is to educate students on trading, as well as how to use code to automate trading. Trading may be new for many students, so it is important that adequate information is provided regarding what trading is and all of the steps involved in creating entry and exit strategies for automated trading.

* Not everyone will have a background in trading, so be thorough when explaining specific trading terminology, concepts, and strategies. Instead of painting the entire picture for students, focus on the individual steps required to execute a trade, and then apply coding concepts (i.e., iterations) to illustrate how the step can be automated using Python code. Definitions for key trading terminology will be provided.

* Review sessions will be geared towards allowing students to ask as many questions as possible. Questions should be prioritized over instructor posed review questions. While we want to provide as much opportunity as possible for students to ask questions, it is also important that the class is paced so that all material is covered.

* Encourage students to review supplementary resources, to reach out to TAs individually for assistance, and to attend office hours to address any unanswered questions or confusion.

* In the next class, students will use the [FinTA](https://pypi.org/project/finta/) Python library. Ask students to follow the ["Algorithmic Trading Install Guide"](../Supplemental/algorithmic-trading-install-guide.md) to install this library in their virtual environments to be ready to use this library in the next class.

* Highlight to students the legal disclaimer that is shared in the welcome activity. Warn students that the content contained in the FinTech Boot Camp is for informational and learning purposes only.

* In the next unit, students will start with Amazon Web Services (AWS). During this week, ask students to create an AWS account, if they don't have one, by following the "AWS Account Setup" guide that they can find in Unit 15's "Supplemental" folder.

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1wx5vODCNAlK2cazdvSvPn0OoFHEAZDboFpTsVplsOZ4/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (10 min)

**Corresponding Activity:** [01-Ins_Welcome](Activities/01-Ins_Welcome)

**Files:**

* [Legal Disclaimer](Activities/01-Ins_Welcome/legal-disclaimer.pdf)

Welcome students to the algorithmic trading unit of the Bootcamp. Congratulate students on reaching this important milestone as they have learned several skills that will allow them to build algorithmic trading strategies.

Open the lesson slides and move to the "Legal Disclaimer" slide, read it along with the class and highlight the educational nature of the skills that they will learn this week.

Slack out the "Legal Disclaimer" PDF file to students

Continue on the lesson slides, move to the "Welcome to Algorithmic Trading" section and highlight the following:

* Not long ago, algorithmic trading disrupted the financial sector. It did so by introducing computer algorithms that could buy and sell faster than human traders.

* Although the speed of these transactions gave the algorithmic trading systems a competitive advantage, people had to specifically program the systems. So, their ability to adapt to new data was limited.

* To improve these systems, FinTech companies developed machine learning algorithms that could adapt to new data. Now, algorithmic trading systems&mdash;which are driven by machine learning &mdash;are disrupting the financial market again. This is because investors can use them to automatically trade and manage assets in highly dynamic environments.

* In this lesson, you’ll use your knowledge of Python, Pandas, and NumPy to build programs that both analyse the pricing data of stocks and make decisions about when to buy and sell shares.

Answer any questions before continuing to the next activity.

---

### 2. Instructor Do: Introduction to Algorithmic Trading (15 min)

**Corresponding Activity:** [02-Ins_Intro_Algo_Trading](Activities/02-Ins_Intro_Algo_Trading)

In this activity, students will learn what algorithmic trading is and how they can build a simple trading algorithm using Python.

**Files:**

* [intro_algo_trading.ipynb](Activities/02-Ins_Intro_Algo_Trading/Unsolved/intro_algo_trading.ipynb)

Open the lesson slides, move to the "Introduction to Algorithmic Trading" and highlight the following:

* Normally, a typical day for traders involves the following:

  * Manually tracking the transactional history of many stocks.

  * Identifying the best opportunity to buy, sell, and hold.

  * Maintaining knowledge about the highs and lows for each individual stock, as well as their overall portfolio value and profit/loss.

  * Keeping emotions in check.

* The sheer number of moving parts and details that need to be considered can make it difficult for the human mind to consistently make performant trades.

* This is where algorithmic trading comes in.

* **Algorithmic trading** consists of an established set of rules that first tell a system when to buy or sell an asset and then execute that trading strategy. Algorithmic trading is logic based. This means that it’s based on a set of conditions that, when triggered, initiate a buy or sell action.

* The key difference between human traders and algorithmic trading is that computers can make decisions and predictions much more efficiently and effectively than humans, and they can do so without human emotions getting in the way.

Open the unsolved version of the code provided for this activity and explain to students that now you will demonstrate how a simple trading algorithm can be coded using Python. Live code the solution and highlight the following:

* We can build a trading algorithm just by using Python and the Pandas and NumPy libraries.

* So, let’s do that. Our algorithm will first analyse a list of stock prices. Based on the information, it will then determine whether to buy or sell shares of stock.

* First, we need to import the required libraries&mdash;in this case, Pandas and NumPy&mdash;into a Jupyter notebook, as the following code shows:

  ```python
  # Import required libraries
  import pandas as pd
  import numpy as np
  ```

* Next, we need to determine the kind of data that we’ll work with. By analysing the market data, we can form a trading strategy.

* For this example, we’ll analyse the following 10 days of closing prices for a fictional stock, FNTK:

  ```python
  # Create a list with closing prices for 10 days
  fntk_data = [30.05, 30.36, 30.22, 30.52, 30.45, 31.85, 30.47, 30.60, 30.21, 31.30]
  ```

* Next, we create a Pandas DataFrame named `fntk_df` and assign the closing prices to the “close” column, as the following code shows:

  ```python
  # Create a Pandas DataFrame containing closing prices for stock FNTK
  fntk_df = pd.DataFrame(
      {"close": fntk_data}
  )

  # Review the DataFrame
  fntk_df
  ```

  ![A screenshot depicts the DataFrame.](Images/15-1-fntk-dataframe.png)

* With the data in a DataFrame, we can set the index to a set of `datetime` objects, starting from `2019-09-09`. To do so, we use the `bdate_range` function to generate the index only for the business days, as the following code shows:

  ```python
  # Set the index as datetime objects starting from 2019-09-09, but only for business days
  fntk_df.index = pd.bdate_range(start='2019-09-09', periods=10)

  # Review the DataFrame
  fntk_df
  ```

  ![A screenshot depicts the updated DataFrame.](Images/15-1-fntk-dataframe-with-index.png)

Explain to students that trading days are business days, which run from Monday to Friday. When setting the index for this stock price data, we therefore use the `bdate_range` function to account for only the business dates. By contrast, the `date_range` function provides the dates for all the days, which run from Monday to Sunday. This wouldn’t work as well for our trade-focused DataFrame.

* We now have a DataFrame consisting of 10 trading days of FNTK stock prices. The next step is to plot the stock prices. With a plot, we can examine the price action, or behaviour, of the FNTK stock during this time frame. Here’s the code:

  ```python
  # Use the plot function to plot the closing prices for FNTK
  fntk_df.plot()
  ```

  ![A screenshot depicts the line plot, with the date along the x-axis and the closing value along the y-axis.](Images/15-1-fntk-plot.png)

* Based on this plot, we can observe that the stock price fluctuates on a day-to-day basis. However, it has a slightly upward trend over the course of the 10-day trading session.

* How might we form a trading strategy based on this data? As the mantra goes, the goal of any trading strategy is to buy low and sell high!

Explain to students that you will create a trading algorithm using conditionals to decide whether to buy or sell stocks. Highlight the following:

* At a glance, we might base a trading algorithm on the following conditions:

  * When the closing price of the current day is less than that of the previous day, we should buy.

  * When the closing price of the current day is greater than that of the previous day, we should sell.

* To incorporate these conditions into our code, we need to add a “trade_type” column to the DataFrame. We then need to loop through each index value to set the appropriate “buy” or “sell” trade. Let’s go through the code step by step.

* First, we add the new column, named “trade_type”, to the DataFrame to track buys and sells. We set the values in this column to `NaN` by default, as the following code shows:

  ```python
  # Add the trade_type column to track buys and sells
  fntk_df["trade_type"] = np.nan
  ```

* Now, we can begin to define our trading logic. Specifically, we need to track the closing price for the previous day. We store this value in a variable named `previous_price`, as the following code shows:

  ```python
  # Initialize variable to hold previous day's trading price
  # Set the initial value of the previous_price to 0
  previous_price = 0
  ```

* Our DataFrame contains each row’s index value and data. So, we can use a `for` loop along with the [Pandas `iterrows` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iterrows.html) to loop through each row in the DataFrame. Inside the loop, we’ll access each row’s `DatetimeIndex` and data to evaluate the trading condition.

* The following code sets up our `for` loop:

  ```python
  # Loop through the Pandas DataFrame and initiate a trade each iteration
  for index, row in fntk_df.iterrows():
  ```

* Now, inside the `for` loop, we need to use an `if` statement to check if `previous_price` is set to 0. If it is, we know that it’s the first day of trading&mdash;so we need to buy. Therefore, in the `if` statement, we pass the index value to the `loc` function to change that row and set the trade type to ”buy”, as the following code shows:

  ```python
  # buy if the previous price is 0, in other words, buy on the first day
  if previous_price == 0:
      fntk_df.loc[index, "trade_type"] = "buy"
  ```

* Next, we use an `elif` statement inside the loop to check if the price of the current day is less than that of the previous day. If it is, we need to buy.

  ```python
  # buy if the current day’s price is less than the previous day’s price
  elif row["close"] < previous_price:
      fntk_df.loc[index, "trade_type"] = "buy"
  ```

* Now, we need to create an `elif` statement to check if the price of the current day is greater than that of the previous day. If it is, we should sell, as the following code shows:

  ```python
  # sell if the current day’s price is greater than the previous day’s price
  elif row["close"] > previous_price:
      fntk_df.loc[index, "trade_type"] = "sell"
  ```

* Next, we write an `else` statement to account for a situation that doesn’t meet either condition. (That is, the price of the current day is neither less than nor greater than that of the previous day.) If this is the case, we should hold, as the following code shows:

  ```python
  # hold if the current day’s price is equal to the previous day’s price
  else:
      fntk_df.loc[index, "trade_type"] = "hold"
  ```

* Finally, we need to update `previous_price` to the price of the current row. We do this so that during the next iteration, we’ll check it against the new current price. We then use another `if` statement to check if we’ve reached the final day of trading. If so, we’ll sell, as the following code shows:

  ```python
  # update the previous_price to the current row's price
  previous_price = row["close"]

  # if the index is the last index of the DataFrame, sell
  if index == fntk_df.index[-1]:
      fntk_df.loc[index, "trade_type"] = "sell"
  ```

* Nice! We now have the following completed algorithm.

  ```python
  # Loop through the Pandas DataFrame and initiate a trade each iteration
  for index, row in fntk_df.iterrows():

    # buy if the previous_price is 0, in other words, buy on the first day
    if previous_price == 0:
      fntk_df.loc[index, "trade_type"] = "buy"

    # buy if the current day's price is less than the previous day's price
    elif row["close"] < previous_price:
      fntk_df.loc[index, "trade_type"] = "buy"

    # sell if the current day's price is greater than the previous day's price
    elif row["close"] > previous_price:
      fntk_df.loc[index, "trade_type"] = "sell"

    # hold if the current day's price is equal to the previous day's price
    else:
      fntk_df.loc[index, "trade_type"] = "hold"

    # update the previous_price to the current row's price
    previous_price = row["close"]

    # if the index is the last index of the DataFrame, sell
    if index == fntk_df.index[-1]:
      fntk_df.loc[index, "trade_type"] = "sell"
    ```

* As usual, we also want to review the DataFrame. Notice that the DataFrame now has the “trade_type” column. It shows when the algorithm decided to buy, sell, or hold FNTK stock during the 10-day trading session.

  ```python
  # Review the DataFrame
  fntk_df
  ```

  ![A screenshot depicts the DataFrame, with the index values and the “close” and “trade_type” columns.](Images/15-1-fntk-trading-dataframe.png)

Explain to students that using conditionals to set trading rules is a simple approach. Still, it can be powerful since it can represent an expert trader's logic and mental process.

Now, it's time for students to create their simple trading algorithms. Be sure that there are no questions before moving forward.

---

### 3. Students Do: Getting Started with Algorithmic Trading (15 min)

**Corresponding Activity:** [03-Stu_Algo_Trading](Activities/03-Stu_Algo_Trading)

**Files:**

* [Instructions](Activities/03-Stu_Algo_Trading/README.md)

* [Unsolved](Activities/03-Stu_Algo_Trading/Unsolved/algo_trading.ipynb)

In this activity, students will write a trading algorithm that uses Python to represent the conditions of a simple trading strategy.

---

### 4. Instructor Do: Review Getting Started with Algorithmic Trading (10 min)

**Corresponding Activity:** [03-Stu_Algo_Trading](Activities/03-Stu_Algo_Trading)

**Files:**

* [Solved](Activities/03-Stu_Algo_Trading/Solved/algo_trading.ipynb)

* [Unsolved](Activities/03-Stu_Algo_Trading/Unsolved/algo_trading.ipynb)

Open the unsolved version of the provided Jupyter notebook, live code the solution and highlight the following:

* To create a trading algorithm, we can use pure Python. So that, for this activity, we start by importing Pandas and NumPy only.

  ```python
  # Import the required libraries
  import pandas as pd
  import numpy as np
  ```

* For this activity, we used AMD stock closing prices. Let's continue by creating a DataFrame with the provided closing prices.

  ```python
  # Closing prices for AMD stock
  amd_data = [28.99, 28.76, 28.31, 28.68, 29.01, 28.93, 28.23, 28.46, 28.38, 29.75,]

  # Create the Pandas DataFrame using the price information supplied
  amd_df = pd.DataFrame(
      {"close": amd_data}
  )

  # Review the DataFrame
  amd_df
  ```

  ![Closing prices of AMD stock](Images/15-1-amd-closing-prices.png)

* To analyze closing prices along time, the next step is to set the index of the DataFrame as DateTime objects. To do so, we use the `bdate_range` Pandas function.

  ```python
  # Set the index as datetime objects starting from 2019-09-09 and onwards (but only business days)
  amd_df.index = pd.bdate_range(start='2019-09-30', periods=10)

  # Review the DataFrame
  amd_df
  ```

  ![Setting the DataFrame index as DateTime objects using the bdate_range Pandas function](Images/15-1-set-amd-datetime-index.png)

* After setting the DataFrame index as DateTime, we can plot the AMD closing prices to visualise the closing price over time.

  ```python
  # Visualize the DataFrame using the plot function
  amd_df.plot()
  ```

  ![AMD closing price plot](Images/15-1-amd-price-plot.png)

* Once the data is ready, we continue by coding the trading algorithm. We loop through the rows using the `iterrows` Pandas function by following the conditions defined for this algorithm.

  ```python
  # Initialize trade_type column for buys and sells
  amd_df['trade_type'] = np.nan

  # Initialize variable to hold the previous_price
  previous_price = 0

  # Loop through the Pandas DataFrame and code the conditions of the trading strategy
  for index, row in amd_df.iterrows():

      # buy if the previous price is 0, in other words, buy on the first day
      if previous_price == 0:
          amd_df.loc[index, "trade_type"] = "buy"

      # buy if the current day price is less than the previous day price
      elif row["close"] < previous_price:
          amd_df.loc[index, "trade_type"] = "buy"

      # sell if the current day price is greater than the previous day price
      elif row["close"] > previous_price:
          amd_df.loc[index, "trade_type"] = "sell"

      # else hold if the current day price is equal to the previous day price
      else:
          amd_df.loc[index, "trade_type"] = "hold"

      # set the previous_price variable to the close price of the current row
      previous_price = row["close"]

      # if the index is the last index of the Dataframe, set the trade_type to sell
      if index == amd_df.index[-1]:
          amd_df.loc[index, "trade_type"] = "sell"
  ```

Run the trading algorithm; next, review the resulting DataFrame and explain to students that this is a simple trading strategy based on conditions; though these conditions look simple, they represent the primary mental process of trading to buy, sell, or hold. Using pure Python code, they can describe any cognitive process that a trader may do.

Be sure that there are no questions before moving forward.

---

### 5. Instructor Do: Assessing Trading Algorithms (20 min)

**Corresponding Activity:** [04-Ins_Assessing_Trading_Algos](Activities/04-Ins_Assessing_Trading_Algos)

In this activity, students will learn how they can assess a trading algorithm using cost and proceeds of each trade, as well as the return on investment (ROI).

**Files:**

* [Unsolved](Activities/04-Ins_Assessing_Trading_Algos/Unsolved/assessing_trading_algos.ipynb)

Open the lesson slides, move to the "Assessing Trading Algorithms" section and highlight the following:

* Now that we built a simple trading algorithm, it's time to calculate the profit that a trading algorithm generates&mdash;valuable information for most investors!

* For this profit-calculation demonstration, we’ll slightly adjust the trading strategy of our algorithm.

* Specifically, we’ll change the code so that it only buys (and doesn’t sell) shares during the trading period. Then, it will sell all the shares on the final day of the period.

* The new algorithm will accumulate stock shares on those days when the stock price of the current day is less than that of the previous day, hold on to the stock when the price of the current day is greater than that of the previous day, and then sell all the accumulated shares on the final day of the period. We’ll calculate the profit by subtracting the cost of the shares for each buy from the proceeds that we make by selling our shares on the final day.

Explain to students that we will start by exploring the calculations for determining the cost and the proceeds of each trade in more detail.

#### Calculate the Cost and the Proceeds of Each Trade

Continue with the lesson slides, move to the "Cost and Proceeds" section and highlight the following:

* We calculate the cost of each trade by multiplying the closing price of the stock by the number of shares that we bought.

* We calculate the proceeds by multiplying the closing price of the stock by the total number of shares that we accumulated over the period.

* Finally, we calculate the profit or loss by subtracting the total cost of the shares that we bought from the total proceeds that we made from selling the shares.

* Let's see how we can do this using Python.

Open the starter code provided. You will note that the code is the trading algorithm that we created before. Live code the algorithm modifications and highlight the following:

* After the code that initializes the “trade_type” column, we'll add a line of code that initialises a new “cost/proceeds” column. We’ll record our trade metrics in this column. Here’s the new line of code:

  ```python
  # Initialize a cost/proceeds column for recording trade metrics
  fntk_df["cost/proceeds"] = np.nan
  ```

* Just after this line, we add the code that creates variables to track the share size and the accumulated shares, as the following code shows:

  ```python
  # Initialize share size and accumulated shares
  share_size = 100
  accumulated_shares = 0
  ```

* Next, inside the `for` loop, we change the `buy` conditional statements to calculate the cost values for the current row. We calculate each cost value by multiplying the price of the current day by the number of shares that we buy. Note that we calculate the negative of this expression, because buying shares requires money to leave an account in order to pay for them. The following code shows all these changes:

  ```python
  # Loop through the Pandas DataFrame and initiate a trade at each iteration
  for index, row in fntk_df.iterrows():

      # buy if the previous_price is 0, in other words, buy on the first day
      if previous_price == 0:
          fntk_df.loc[index, "trade_type"] = "buy"

          # calculate the cost of the trade by multiplying the current day's price
          # by the share_size, or number of shares purchased
          fntk_df.loc[index, "cost/proceeds"] = -(row["close"] * share_size)

          # add the number of shares purchased to the accumulated shares
          accumulated_shares += share_size

      # buy if the current day's price is less than the previous day's price
      elif row["close"] < previous_price:
          fntk_df.loc[index, "trade_type"] = "buy"

          # calculate the cost of the trade by multiplying the current day's price
          # by the share_size, or number of shares purchased
          fntk_df.loc[index, "cost/proceeds"] = -(row["close"] * share_size)

          # add the number of shares purchased to the accumulated shares
          accumulated_shares += share_size
  ```

* As mentioned, we no longer sell our shares until the last day of the period. To accommodate this new condition, we change the trading algorithm in the following way: if the price of the current day is greater than that of the previous day, we set the value in the “trade_type” column to “hold", as the following code shows:

  ```python
  # hold if the current day's price is greater than the previous day's price
  elif row["close"] > previous_price:
      fntk_df.loc[index, "trade_type"] = "hold"
  ```

* Finally, we change our trading algorithm to sell our accumulated shares on the final day of the period and to calculate the proceeds. We calculate the proceeds by multiplying the number of accumulated shares by the final closing price. Note that we represent the proceeds with a positive number, because a sale of shares leads to money coming into an account. The following code shows our changes:

  ```python
  # if the index is the last index of the DataFrame, sell
  if index == fntk_df.index[-1]:
      fntk_df.loc[index, "trade_type"] = "sell"

      # calculate the proceeds by multiplying the last day's price by the accumulated shares
      fntk_df.loc[index, "cost/proceeds"] = row["close"] * accumulated_shares
  ```

* The completed for loop should look as follows:

```python
# Loop through the Pandas DataFrame and initiate a trade at each iteration
for index, row in fntk_df.iterrows():

    # buy if the previous_price is 0, in other words, buy on the first day
    if previous_price == 0:
        fntk_df.loc[index, "trade_type"] = "buy"

        # calculate the cost of the trade by multiplying the current day's price
        # by the share_size, or number of shares purchased
        fntk_df.loc[index, "cost/proceeds"] = -(row["close"] * share_size)

        # add the number of shares purchased to the accumulated shares
        accumulated_shares += share_size

    # buy if the current day's price is less than the previous day's price
    elif row["close"] < previous_price:
        fntk_df.loc[index, "trade_type"] = "buy"

        # calculate the cost of the trade by multiplying the current day's price
        # by the share_size, or number of shares purchased
        fntk_df.loc[index, "cost/proceeds"] = -(row["close"] * share_size)

        # add the number of shares purchased to the accumulated shares
        accumulated_shares += share_size

    # hold if the current day's price is greater than the previous day's price
    elif row["close"] > previous_price:
        fntk_df.loc[index, "trade_type"] = "hold"

    # hold if the current day's price is equal to the previous day's price
    else:
        fntk_df.loc[index, "trade_type"] = "hold"

    # update the previous_price to the current row's price
    previous_price = row["close"]

    # if the index is the last index of the DataFrame, sell
    if index == fntk_df.index[-1]:
        fntk_df.loc[index, "trade_type"] = "sell"

        # calculate the proceeds by multiplying the last day's price by the accumulated shares
        fntk_df.loc[index, "cost/proceeds"] = row["close"] * accumulated_shares
```

* The following image shows our final DataFrame, which now has a “cost/proceeds” column:

  ![A screenshot depicts the DataFrame.](Images/15-1-fntk-algo-cost-proceeds.png)

Ask students if there is any question before continuing with the next step. After answering all the questions, explain to students that now we can compute the total profit or loss generated by our algorithm along the trading period.

#### Calculate the Total Profit or Loss for the Trading Period

Explain to students that now that our DataFrame contains the cost and proceeds information for our trading strategy, we can assess our trading algorithm by computing the total profit or loss. Continue live coding the demo and highlight the following:

* According to our new trading strategy, we bought 100 shares every time “trade_type” signalled a buy, and we didn’t sell until the last day of the period.

* With this information, we can calculate the total profit or loss that this strategy generated by summing the values in the “cost/proceeds” column, as the following code shows:

  ```python
  # Calculate the total profit/loss for 100 share size orders
  total_profit_loss = round(fntk_df["cost/proceeds"].sum(), 2)

  # Print the profit/loss metrics
  print(f"The total profit/loss of the trading strategy is ${total_profit_loss}.")
  ```

  ```text
  The total profit/loss of the trading strategy is $510.0.
  ```

* As you can see, our simple trading algorithm returned a profit of $510! Now, let's calculate this profit as a percentage of our investment, or return on investment (ROI).

#### Calculate the Return on Investment

Explain to students that to calculate our ROI, we first calculate the total cost of all the buy trades&mdash;which is known as the **invested capital**. We then divide that into the `total_profit_loss` value, as the following code shows:

```python
# Initialize the variable to hold the value of the invested capital
invested_capital = 0

# Calculate the invested capital by adding the cost of all buy trades
for index, row in fntk_df.iterrows():
    if row["trade_type"] == "buy":
        invested_capital = invested_capital + row["cost/proceeds"]


# Calculate the return on investment (ROI)
roi = round((total_profit_loss / -(invested_capital)) * 100, 2)

# Print the ROI
print(f"The trading algorithm resulted in a return on investment of {roi}%")
```

```text
The trading algorithm resulted in a return on investment of 3.37%
```

Explain to students that after calculating the ROI, our trading algorithm gave us an ROI of 3.37%&mdash;which isn’t bad for only 10 business days of trading. On an annualised basis (252 trading days divided by 10), this ROI amounts to 84.9% (`252/10 * 3.37% = 84.9`).

Highlight to students that, as it was demonstrated, algorithmic trading consists of the two parts mentioned earlier. First, we establish a set of rules that indicate when to buy, sell, or hold an asset. Second, we execute based on those rules.

Now it's time for students to write a new trading algorithm by themselves, but first, be sure that there are no questions before moving forward.

---

### 6. Students Do: Profitable Algorithmic Trading (20 min)

**Corresponding Activity:** [05-Stu_Profitable_Algo_Trading](Activities/05-Stu_Profitable_Algo_Trading)

**Files:**

* [Instructions](Activities/05-Stu_Profitable_Algo_Trading/README.md)

* [Unsolved](Activities/05-Stu_Profitable_Algo_Trading/Unsolved/profitable_algo_trading.ipynb)

In this activity, you’ll write a trading algorithm that buys 100 shares of AMD stock on the days when the price decreases and that sells the accumulated shares on the last day of the trading period.

---

### 7. Instructor Do: Review Profitable Algorithmic Trading (10 min)

**Corresponding Activity:** [05-Stu_Profitable_Algo_Trading](Activities/05-Stu_Profitable_Algo_Trading)

**Files:**

* [Solved](Activities/05-Stu_Profitable_Algo_Trading/Solved/profitable_algo_trading.ipynb)

* [Unsolved](Activities/05-Stu_Profitable_Algo_Trading/Unsolved/profitable_algo_trading.ipynb)

Congratulate students on creating a trading algorithm that follows a defined set of rules to successfully complete trades!

Open the unsolved version of the provided Jupyter notebook, live code the solution and highlight the following.

* A trading algorithm based on conditions, can do more that simply buy, hold, and sell shares. We can also assess the profitability of a trading action while trading.

* In this activity, we modified the simple trading algorithm that we created before, to include the calculation of the cost and proceeds metrics for buys of 100 shares.

  ```python
  # Loop through the Pandas DataFrame and code the conditions of the trading strategy
  for index, row in amd_df.iterrows():

      # buy if the previous price is 0, in other words, buy on the first day
      # set the cost/proceeds column equal to the negative value of the row close price
      # multiplied by the share_size
      if previous_price == 0:
          amd_df.loc[index, "trade_type"] = "buy"
          amd_df.loc[index, "cost/proceeds"] = -(row["close"] * share_size)
          accumulated_shares += share_size

      # buy if the current day price is less than the previous day price
      # set the cost/proceeds column equal to the negative value of the row close price
      # multiplied by the share_size
      elif row["close"] < previous_price:
          amd_df.loc[index, "trade_type"] = "buy"
          amd_df.loc[index, "cost/proceeds"] = -(row["close"] * share_size)
          accumulated_shares += share_size

      # sell if the current day price is greater than the previous day price
      elif row["close"] > previous_price:
          amd_df.loc[index, "trade_type"] = "sell"

      # else hold if the current day price is equal to the previous day price
      else:
          amd_df.loc[index, "trade_type"] = "hold"

      # set the previous_price variable to the close price of the current row
      previous_price = row["close"]

      # if the index is the last index of the Dataframe, sell
      # set the cost/proceeds column equal to the row close price multiplied
      # by the accumulated_shares
      if index == amd_df.index[-1]:
          amd_df.loc[index, "trade_type"] = "sell"
          amd_df.loc[index, "cost/proceeds"] = row["close"] * accumulated_shares
  ```

* By computing the cost and proceeds on every buy and sell operation, we will be able to understand the costs of each trade and the money that our trading algorithm is able to make.

* After modifying and running the trading algorithm, we can calculate the total profit or loss of our trading strategy. To do so, we use the `sum` Pandas function to sum all the values of the `cost/proceeds` column.

  ```python
  # Calculate the total profit/loss for 100 share size orders
  total_profit_loss = round(amd_df["cost/proceeds"].sum(), 2)

  # Print the profit/loss metrics
  print(f"The total profit/loss of the trading strategy is ${total_profit_loss}.")
  ```

  ```text
  The total profit/loss of the trading strategy is $690.0.
  ```

* Based on the above, it looks like this algorithmic trading strategy had a profit of $690.00.

* Next, we calculate the ROI for the trades to validate how profitable our strategy was as a proportion of the invested capital.

* To calculate the invested capital, we loop through the DataFrame by adding the cost of all the buy trades.

  ```python
  # Initialize the variable to hold the value of the invested capital
  invested_capital = 0

  # Calculate the invested capital by adding the cost of all buy trades
  for index, row in amd_df.iterrows():
      if row["trade_type"] == "buy":
          invested_capital = invested_capital + row["cost/proceeds"]
  ```

* Finally, we calculate the ROI as a percentage.

  ```python
  # Calculate the return on investment (ROI)
  roi = round((total_profit_loss / -(invested_capital)) * 100, 2)

  # Print the ROI
  print(f"The trading algorithm resulted in a return on investment of {roi}%")
  ```

  ```text
  The trading algorithm resulted in a return on investment of 4.02%
  ```

* We can see that our trading strategy resulted in an ROI of 4.02%, not bad for a trading journey of ten days.

Explain to students that thus far, we've only built an algorithm with a single rule: buy if the price was lower than the day before, and sell it all after ten days. But we can also create much more complex trading algorithms that learn from and even predict short-term price movements. This is where trading signals come into play. Highlight that we’ll explore how to generate these signals after the break, which are more sophisticated indicators for trading.

Be sure that there are no questions before moving forward.

---

### 8. BREAK (15 min)

---

### 9. Instructor Do: Forming Trading Signals (20 min)

**Corresponding Activity:** [06-Ins_Trading_Signals](Activities/06-Ins_Trading_Signals)

In this activity, students will learn how to generate trading signals based on simple moving averages (SMA) and the dual moving average crossover (DMAC) trading strategies. Also, students will identify the differences between fundamental analysis and technical analysis.

**Files:**

* [trading_signals.ipynb](Activities/06-Ins_Trading_Signals/Unsolved/trading_signals.ipynb)

Open the lesson slides, move to the "Trading Signals" section and highlight the following:

* A trading algorithm requires proper **trading signals**, which are point-in-time indications of when to buy a stock (enter a trade) or sell the stock (exit a trade). For example, in the case of our simple trading algorithm, we chose to buy FNTK stock when the price of the current day was less than that of the previous day. That is, the signal to enter the trade occurred when the price of the current day was less than that of the previous day.

* Such a strategy is appropriate if we assume that the stock price will continue to fluctuate each day. That is, the price might go up on one day, go down the next day, and so on. But, what if the stock price continues to slide? We don’t want to buy the stock if we expect the price to continually decrease in the short term.

* To make intelligent trades, we therefore need to form trading signals that can identify underlying price trends and thus refine our trade entry and exit strategies.

* The trading industry has a common saying: the trend is your friend! This means that one good trade often proves better than many trades back and forth, buying and selling. This "trend following" is one approach, and when the trend breaks, this signals it's time to close out the position.

* However, for volatile stocks, it may be more profitable to be continually buying and selling, rather than following a longer term trend. An algorithm that makes many trades over a very short period of time (e.g., every 30 seconds, or even shorter) is known as a **high-frequency trading (HFT)** algorithm.

Explain to students that to determine which buy and sell trading signals to deploy in a stock trading algorithm, we need to understand whether there are any repeatable patterns in a stock's price movements. To accomplish this, we’ll analyse both the fundamental and the technical metrics of the stock.

Continue on with the slides, presenting the definitions of fundamental and technical analysis. Highlight the following:

* To define a trading strategy, we need to understand how a stock price might trend in either the short or the long term.

* There are two schools of thought that exist in the investment world for how to do so: fundamental analysis and technical analysis.

* **Fundamental analysis** focuses on the long-term health of a company. This includes its historical cash flow, debt-to-equity ratio, and management quality. The healthier the financial outlook for a company, the higher we expect its stock price to trend.

* We can implement fundamental analysis in algorithmic trading. But doing so usually requires analysing three financial statements from a company: income, balance sheet, and cash flow.

* **Technical analysis** focuses on the price action of a company’s stock&mdash;that is, its behaviour as shares are bought and sold. Because technical analysis is quantitative in nature, algorithmic trading often leans toward this philosophy when determining when to buy or sell.

* When using technical analysis, traders often rely on price-derived calculations known as **technical indicators** to gauge short-term price trends.

Explain to students that because of the lucrative nature of trading, stock traders have developed many technical indicators that signal when to buy or sell a stock. Traders can base these indicators on a wide variety of factors, which involve varying amounts of complexity, historical pricing information, and computing power. One of the most popular technical indicators&mdash;and the one that we’ll focus on in today's class&mdash;is the simple moving average (SMA).

Present the SMA slide to the class and explain the following:

* The **SMA** calculates the average price of a stock over a rolling period of a specific number of days. Examples of these periods include 30 days, 50 days, 100 days, and 200 days.

* When trading, we can consider using both a long-window SMA (say, for 100 or 200 days) and a short-window SMA (say, for 30 or 50 days).

* When the short-window SMA is greater than the long-window SMA, we can assume that the price trend is positive over the short term. When the opposite is true&mdash;when the short-window SMA is less than the long-window SMA&mdash;we can likewise assume a negative price trend.

* The following image shows a plot of a short-window (50-day) SMA and long-window (200-day) SMA for the closing price of a stock.

  ![A short-window (50-day) SMA and long-window (200-day) SMA for the closing price of a stock](Images/15-1-long-short-sma.png)

Explain to students that points exist on the plot where the two SMA lines cross one another. These **crossover points** indicate when the short-term price trend changes. We consider such changes as opportunities to either enter or exit a trade. Highlight the following about the crossover points:

* Consider the point on the plot where the short-window SMA crosses below the long-window SMA (that is, where the short-window SMA now has a lower value than the long-window SMA). That point indicates that the asset price is expected to trend lower, so we should sell our stock before the price decreases further.

* Now, consider the point on the plot where the short-window SMA crosses above the long-window SMA (that is, where the short-window SMA has a higher value than that of the long-window SMA). Such a point indicates that the asset price is trending higher, so we should start buying stock before the price increases too much.

* These crossover points become the trading signals that define the entry and exit points for our trading algorithm. This particular strategy is known as **dual moving average crossover (DMAC)** trading.

#### Writing an Algorithm that Uses DMAC Trading

Time to code! Explain to students that now, you will demonstrate how DMAC trading works by writing a trading algorithm from scratch that uses this trading strategy. Open the starter file provided, live code the solution and highlight the following:

* As always, we first need to import the required libraries&mdash;Pandas, NumPy, hvPlot, and pathlib.

  ```python
  # Import the required libraries
  import numpy as np
  import pandas as pd
  import hvplot.pandas
  from pathlib import Path
  ```

* Next, we read historical stock data from a CSV file into a Pandas DataFrame and set the “date” column as the `datetime` index. For this demo, we will use stock data from Apple.

  ```python
  # Read the aapl.csv file into a Pandas DataFrame
  # Set the date column as the DateTimeIndex
  aapl_df = pd.read_csv(
      Path("../Resources/aapl.csv"),
      index_col="date",
      parse_dates=True,
      infer_datetime_format=True
  )

  # Review the DataFrame
  aapl_df.head()
  ```

  ![A screenshot depicts the head of the DataFrame.](Images/15-1-apple-stock-dataframe.png)

* For our trading algorithm, we care only about Apple's (ticker symbol "AAPL") closing prices. So, we need to filter the DataFrame to only the `close` column. We thus create a new DataFrame, named `signals_df`, from the `close` column of the original `apple_df` DataFrame, as the following code shows.

  ```python
  # Filter the date index and close columns
  signals_df = aapl_df.loc[:,["close"]]

  # Review the DataFrame
  signals_df.head()
  ```

  ![A screenshot depicts the head of the new DataFrame, which consists of only the date index and the “close” column.](Images/15-1-aapl-signals-dataframe.png)

* When working with stock prices, we also want to visualise how the values change over time. We thus plot the DataFrame by using the `hvplot` function, as the following code shows.

  ```python
  # Use hvplot to visualize the data
  signals_df.hvplot()
  ```

  ![A screenshot depicts the plot.](Images/15-1-apple-price-chart.png)

##### SMA for the Short and Long Windows Calculation

Explain to students that they can notice from the plot that the stock price generally trends higher over the course of the time period from 2015 to 2019. However, during a period in late 2018, the price did drop before it recovered.

Now that we have created and visualised our DataFrame, explain to students that we’ll turn our attention to creating the short- and long-window SMA metrics.

Continue the live coding demo and highlight the following:

* With the AAPL closing prices, we can calculate the metrics for the short-window (50-day) SMA and the long-window (100-day) SMA.

* First, we define two new variables, `short_window` and `long_window`, with the values of 50 and 100, respectively, as the following code shows.

  ```python
  # Set the variables for short window and long window periods
  short_window = 50
  long_window = 100
  ```

* Next we define two new DataFrame columns, named “SMA50” and “SMA100”. To fill these columns with the SMA metrics for the AAPL closing prices, we use both the `rolling` function with the `window` parameter and the `mean` function, as the following code shows.

  ```python
  # Generate the short and long window simple moving averages (50 and 100 days, respectively)
  signals_df["SMA50"] = signals_df["close"].rolling(window=short_window).mean()
  signals_df["SMA100"] = signals_df["close"].rolling(window=long_window).mean()

  # Review the DataFrame
  display(signals_df.head())
  display(signals_df.tail())
  ```

  ![A screenshot depicts the head and the tail of the DataFrame.](Images/15-1-apple-sma-metrics.png)

Explain to students that they can notice that the first five rows of the DataFrame contain `NaN` values in the “SMA50” and “SMA100” columns. This is because we need 50 and 100 trading days' worth of data, respectively, before we can calculate the SMA. The last five rows of the DataFrame do have the SMA values in the “SMA50” and “SMA100” columns.

With the short- and long-window SMA values in place, explain to students that it’s time to use these technical indicators to identify the trading signals, or the opportunities to either buy or sell AAPL stock.

##### Trading Signals Identification

Explain to students that if we want the trading algorithm to identify the trading signals that indicate opportunities to buy AAPL stock, we’ll need to identify the times when the short-window SMA is greater than the long-window SMA. Remember that when this happens, the price trend for AAPL stock is moving upward in the short term. (That is, the price is increasing). So, we want to own AAPL stock during this time.

Continue the live coding demo and highlight the following:

* To identify trading signals, first, we'll create a “Signal” column in the DataFrame to hold a value that identifies the trading signal. We set this column to initially hold a value of 0.0, as the following code shows.

  ```python
  # Create a column to hold the trading signal
  signals_df["Signal"] = 0.0
  ```

* Next, we change the trading algorithm in the following way: We set the value of the “Signal” column to 1 when the condition to buy AAPL is met (that is, when the short-window SMA is greater than the long-window SMA). We set the value of this column to 0 when the condition isn’t met, indicating that the algorithm shouldn’t buy. We use the [NumPy `where` function](https://numpy.org/doc/stable/reference/generated/numpy.where.html) to check the condition. The following code shows these changes.

  ```python
  # Generate the trading signal 0 or 1,
  # where 1 is the short-window (SMA50) greater than the long-window (SMA100)
  # and 0 is when the condition is not met
  signals_df["Signal"][short_window:] = np.where(
      signals_df["SMA50"][short_window:] > signals_df["SMA100"][short_window:], 1.0, 0.0
  )

  # Review the DataFrame
  signals_df.tail(10)
  ```

  ![A screenshot depicts the tail of the DataFrame, with the “date” index and “close”, “SMA50”, “SMA100”, and “Signal” columns.](Images/15-1-apple-trade-signals.png)

Explain to students that now that we established the trading signal for buying AAPL stock, it’s time to find the crossover points. Remind students that these points appear when the values of the “SMA50” and “SMA100” columns match, which indicates a change in the short-term pricing trend of AAPL stock.

##### Find the Crossover Points

Explain to students that to find the crossover points for the “SMA50” and “SMA100” values, we'll use the [Pandas `diff` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.diff.html) on the “Signal” column. Specifically, we'll use this function to identify the dates when the value in the “Signal” column changes from 0 to 1 or from 1 to 0.

Continue the live coding demo and highlight the following:

* One example of this signal change occurs on Day 100 in the dataset. On this date, `2015-02-12`, the algorithm starts calculating the “SMA100” value. And on this date, the “SMA50” value is greater than the “SMA100” value. So, the algorithm sets the signal with a value of 1. We can confirm the signal by reviewing a slice of the DataFrame around the date in question, as the following code shows.

  ```python
  # Slice the DataFrame to confirm the Signal
  signals_df.loc["2015-02-09":"2015-02-17"]
  ```

  ![A screenshot depicts the slice of the DataFrame.](Images/15-1-confirm-signal.png)

* Notice that the value in the “Signal” column does change from 0 to 1 on `2015-02-12`, which is the first date when the “SMA50” value is greater than the “SMA100” value.

* Notice further that in our slice, the value in the “Signal” column starts as 0, changes from 0 to 1 on `2015-02-12`, and then continues as `1` on the subsequent dates.

* Now, to identify all the crossover points, we use the Pandas `diff` function on the “Signal” column as described earlier in this section. Remember that the crossover points define the trade entry and exit points.

* The `diff` function returns 1 when the “Signal” value changes from 0 to 1, &minus;1 when the “Signal” value changes from 1 to 0, and 0 when the “Signal” value doesn’t change from one day to the next. Therefore, a returned value of 1 tells the algorithm to enter the trade (that is, buy the AAPL stock). A returned value of &minus;1 tells the algorithm to exit (that is, sell the AAPL stock). And, a returned value of 0 tells the algorithm to hold the current position. We add a new “Entry/Exit” column to our DataFrame to hold these returned values, as the following code shows.

  ```python
  # Calculate the points in time when the Signal value changes
  # Identify trade entry (1) and exit (-1) points
  signals_df["Entry/Exit"] = signals_df["Signal"].diff()

  # Review the DataFrame
  signals_df.loc["2015-02-09":"2015-02-17"]
  ```

  ![A screenshot depicts the same slice of the DataFrame with the addition of the “Entry/Exit” column.](Images/15-1-apple-entry-exit.png)

Explain to students that they can notice that the “Entry/Exit” column contains a value of 1 for the `2015-02-12` date. This is the same date from our earlier example when the “Signal” value changes from 0 to 1.

Now that we defined the entry and exit points, explain to students that now we can plot them against the AAPL closing prices. By creating a plot, we can then observe each buy or sell order that the algorithm would make.

Continue the live coding demo and highlight the following:

* To visualise the behaviour and performance of our algorithm, we’ll plot our trade entry and exit points relative to the stock closing prices, the stock closing prices over time, and the “SMA50” and “SMA100” values.

* We’ll use hvPlot so that we can make enhancements, such as changing the colour and direction (up or down) of the markers.

* The following plot shows the exit points across the period of time. These points represent the dates when the "SMA50" value became less than, or crossed below, the "SMA100" value.

  ```python
  # Visualize exit position relative to close price
  exit = signals_df[signals_df['Entry/Exit'] == -1.0]['close'].hvplot.scatter(
    color='yellow',
    marker='v',
    size=200,
    legend=False,
    ylabel='Price in $',
    width=1000,
    height=400)

  # Show the plot
  exit
  ```

  ![A screenshot depicts the plot.](Images/15-1-apple-exit.png)

* The following image shows the entry points across the period of time. These points represent the dates when the “SMA50” value became greater than, or crossed above, the “SMA100” value.

  ```python
  # Visualize entry position relative to close price
  entry = signals_df[signals_df['Entry/Exit'] == 1.0]['close'].hvplot.scatter(
      color='purple',
      marker="^",
      size=200,
      legend=False,
      ylabel='Price in $',
      width=1000,
      height=400)

  # Show the plot
  entry
  ```

  ![A screenshot depicts the plot.](Images/15-1-apple-entry.png)

* The following image shows the plot of the AAPL closing prices over the time period:

  ```python
  # Visualize close price for the investment
  security_close = signals_df[['close']].hvplot(
      line_color='lightgray',
      ylabel='Price in $',
      width=1000,
      height=400)

  # Show the plot
  security_close
  ```

  ![A screenshot depicts the plot.](Images/15-1-apple-close.png)

* The following image shows the plot of the “SMA50” and “SMA100” values over the time period:

  ```python
  # Visualize moving averages
  moving_avgs = signals_df[['SMA50', 'SMA100']].hvplot(
      ylabel='Price in $',
      width=1000,
      height=400)

  # Show the plot
  moving_avgs
  ```

  ![A screenshot depicts the plot.](Images/15-1-apple-sma50-sma100.png)

Explain to students that although we just individually visualised each basic plot, the information really comes together when we create an overlay plot, as the following code shows:

```python
# Create the overlay plot
entry_exit_plot = security_close * moving_avgs * entry * exit

# Show the plot
entry_exit_plot.opts(
    title="Apple - SMA50, SMA100, Entry and Exit Points"
)
```

![A screenshot depicts the overlay plot.](Images/15-1-apple-overlay.png)

Explain to students that they can notice that with the preceding visualisation, we can identify the trading signals from the algorithm. Specifically, the purple, upward-pointing arrows indicate the entry points, and the yellow, downward-pointing arrows indicate the exit points. With this visualisation, we can identify these signals, along with the “SMA50”, “SMA100”, and closing price information.

Move back to the lesson slides, navigate to the "What Are Long and Short Positions?" section and highlight the following:

* The algorithm that we just design is able to recognise the crossover points of the long- and short-window SMAs. We further designed it to enter a trade when the “SMA50” value crossed above the “SMA100” value and to exit the trade when the “SMA50” value crossed below the “SMA100” value.

* This trading strategy is called a **long position** or **going long**. This is because it focuses on first buying the stock, then holding it, and then selling it only when the short-term price trend turns lower. A trader who buys and holds a stock thus creates a long position. The trader makes a profit in the traditional mode of “buy low, sell high.”

* But, what if we want to apply a **short position** trading strategy? That is, say that we want to make a profit by first selling the stock, also called **going short**, and then buying back the stock when the price goes down? With a short position, the trader makes a profit by selling high and then buying low.

Slack out the following articles to students, and encourage them to review them to learn more about these trading strategies.

1. [Short (Short Position)](https://www.investopedia.com/terms/s/short.asp) from Investopedia.

2. [The Difference Between Long and Short Trades](https://www.thebalance.com/long-and-short-trading-term-definitions-1031122) from The Balance.

Be sure that there are no questions before moving forward.

---

### 10. Students Do: Create a Short-Position Algorithm (30 min)

**Corresponding Activity:** [07-Stu_Short_Position_Algorithm](Activities/07-Stu_Short_Position_Algorithm)

**Files:**

* [Instructions](Activities/07-Stu_Short_Position_Algorithm/README.md)

* [create_a_short_position_algorithm.ipynb](Activities/07-Stu_Short_Position_Algorithm/Unsolved/create_a_short_position_algorithm.ipynb)

In this activity, students will create an algorithm to identify the entry and exit points for a short-position trading strategy. The algorithm will still use a short-window (50 days) SMA and a long-window (100 days) SMA.

This is a mini-project activity intended to be done by groups of two or three people.

---

### 11. Instructor Do: Review Create a Short-Position Algorithm (15 min)

**Corresponding Activity:** [07-Stu_Short_Position_Algorithm](Activities/07-Stu_Short_Position_Algorithm)

**Files:**

* [Solved](Activities/07-Stu_Short_Position_Algorithm/Solved/create_a_short_position_algorithm.ipynb)

* [Unsolved](Activities/07-Stu_Short_Position_Algorithm/Unsolved/create_a_short_position_algorithm.ipynb)

Congratulate students on creating a brand new trading algorithm that includes trading signals!

Open the unsolved version of the provided Jupyter notebook, live code the solution and highlight the following.

* Using trading signals, we can build more robust trading algorithms that can predict short-term price movements that are either increasing or decreasing. Now you have the tools to make profits from these price movements.

* In this activity, we started by loading trading data from a three years period from the VNQ stock into a Pandas DataFrame.

  ```python
  # Read the vnq.csv file from the Resources folder into a Pandas DataFrame
  # Set the `Date` column as the DateTimeIndex
  vnq_df = pd.read_csv(
      Path("../Resources/vnq.csv"),
      index_col="Date",
      parse_dates=True,
      infer_datetime_format=True
  )

  # Review the DataFrame
  vnq_df.head()
  ```

  ![VNQ stock historical data](Images/15-1-vnq-historical-data.png)

* Next, we create and plot a new DataFrame called `signals_df` that contains the closing prices only. We will use this DataFrame to create the trading signals.

  ```python
  # Create a DataFrame filtering only the index and Close columns
  signals_df = vnq_df.loc[:,["Close"]]

  # Review the DataFrame
  signals_df.head()

  # Use hvplot to visualize the DataFrame
  signals_df.hvplot()
  ```

  ![VNQ stock historical closing prices](Images/15-1-vnq-closing-prices.png)

* Next, we add a couple of columns to our `signals_df` that contain the 50-day SMA and a 100-day SMA simple moving averages. We use the `rolling` and `mean` pandas functions to calculate the simple moving averages.

  ```python
  # Set the short_window (50) and long window (100) variables
  short_window = 50
  long_window = 100

  # Generate the short and long moving averages (50 and 100 days, respectively)
  signals_df['SMA50'] = signals_df['Close'].rolling(window=short_window).mean()
  signals_df['SMA100'] = signals_df['Close'].rolling(window=long_window).mean()

  # Review the DataFrame
  signals_df.tail()
  ```

  ![VNQ SMA50 and SMA100 columns](Images/15-1-vnq-sma50-sma100.png)

* After computing the simple moving averages, we use the NumPy `where` function to add a new column called `Signal` to our `signals_df` DataFrame that contains the trading signals.

  ```python
  # Initialize the new Signal column to hold the trading signal
  signals_df['Signal'] = 0.0

  # Generate the trading signal 0 or 1,
  # where 1 is the short-window (SMA50) is less than the long-window (SMA100)
  signals_df["Signal"][short_window:] = np.where(
      signals_df["SMA50"][short_window:] < signals_df["SMA100"][short_window:], 1.0, 0.0
  )

  # Review the DataFrame
  signals_df.iloc[95:105,:]
  ```

  ![VNQ trading signals](Images/15-1-vnq-trading-signals.png)

* Next, we add a new column called `Entry/Exit` to our `signals_df` DataFrame. We use the `diff` Pandas function on the `Signal` column to assign values of `1` or `-1` that indicate the trade entry and exit points respectively in time.

```python
# Calculate the points in time at which a position should be taken, 1 or -1
signals_df['Entry/Exit'] = signals_df['Signal'].diff()

# Review the DataFrame
signals_df.loc["2007-10-20":"2007-10-30",:]
```

![VNQ Entry/Exit signals](Images/15-1-vnq-entry-exit.png)

* Finally, we use hvPlot to plot the entry and exit points of the trading signal.

  ![VNQ trading signals plot](Images/15-1-vnq-trading-signals-plot.png)

Explain to students that in some cases, they’ll have several algorithms to experiment with so that they can measure their future profitability. This is where the concept of backtesting comes in. **Backtesting** is the process of testing an algorithm by using historical stock prices, which we’ll explore more deeply in the next class.

Be sure that there are no questions before ending the class.

---

End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
