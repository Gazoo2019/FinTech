## 6.2 Lesson Plan: Customised Visualisations and Data Aggregation

### Overview

Today’s class will focus on building professional and compelling visualisations. Students will continue where they left off in the last lesson by customising visualisations by using the different options that hvPlot provides. Students will also explore techniques for data aggregation, first by using the Pandas `groupby` function to prepare data for visualisations, then by using visualisations.

### Class Objectives

By the end of this class, students will be able to:

* customise visualisations by using hvPlot attributes and options

* Aggregate data by using the Pandas `groupby` function

* Explore data by using visual aggregation techniques

* Tell a story by using custom visualisations

---

### Instructor Notes

* This lesson encourages students to professionalise their plots by adding details such as axis labels and colours. Be sure to share your perspective on what makes a visualisation effective and clear. Stories and anecdotes from your work experience can help emphasise why these details matter.

* Students will also use Pandas to prepare data for visualisations in this lesson. Although students will have some experience with data aggregation from previous lessons, their comfort level with this will vary. Make sure to provide opportunities for students to ask questions about these aggregation techniques.

* The lesson ends with an activity in which students can create their own custom visualisations and use them to tell stories. Encourage students to be creative with this activity!

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 6.2 Slides](https://docs.google.com/presentation/d/1r9zUWXvZTBMQo0HChhfjqKf9VgglFEZ6ReMEONMjU9o/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The Time Tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome (5 min)

In this section, you will provide an overview of today’s lesson. Start by welcoming students to their second day of visualisation. Review the class objectives, and explain the focus of the class.

* In the last class, you learned how to use hvPlot to make visualisations. Today we’re going to build on that work to create more complex and more professional visualisations.

* visualisations serve many purposes in our work. Sometimes we may use one line of code to make a quick plot to explore our data. That’s fine, but if we’re making a plot to share with others, it’s important to make it as clear and easy to interpret as possible.

* Today we’ll learn how to add titles, axes, legends, colours, and other details to our plots. These are all important elements that you will need to use any time you create a professional visualisation.

* We’ll also work on **data aggregation**, which is the process of preparing and summarising data. We’ll do this two ways: by using the Pandas `groupby` function, and by using visualisation tools to aggregate data.

* At the end of class, you’ll use these tools to create a visualisation that you can use to tell a story. Visualisations are important communication tools, so we’ll talk about strategies for data storytelling with visualisations.

---

### 2. Instructor Do: visualisation Options (15 min)

**Corresponding Activity:** [01-Ins_Viz_Options](Activities/01-Ins_Viz_Options)

In this section, you’ll demonstrate how to use hvPlot attributes and options in order to customise the look and feel of visualisations. Students will learn how to add detail to their visualisations, such as axis labels, colour themes, and effects.

**Files:**

* [viz_options.ipynb](Activities/01-Ins_Viz_Options/Solved/viz_options.ipynb)

**Note:** This section is based on part of the solution for the “Composing Masterpieces” activity.

Open the starter file and highlight the following:

* hvPlots do not always turn out perfectly. The values on the y-axis are unreadable, and the labels along the x-axis are crammed together. Customisation options give users the ability to tailor their visualisations to the information they are presenting. The plot created in the following code is challenging to read and interpret with the default settings:

  ```python
  # Create a DataFrame that slices the subscriber data for Q1 - 2018.
  q1_2020 = subscribers_df.loc[subscribers_df['Years'] == 'Q1 - 2020']

  # Set the index of the DataFrame to Area
  q1_2020 = q1_2020.set_index('Area')

  # Create a bar chart of the Q1 - 2018 data
  q1_2020['Subscribers'].hvplot.bar()
  ```

  ![hvplot_issues.png](Images/hvplot_issues.png)

* Without customisation, visualisations of large datasets often have axis labels that are difficult to read. The `rot` attribute allows users to customise label angles in order to make labels more readable. The `rot` attribute accepts an integer value that indicates the angle at which x-axis labels should be rotated, as shown in the following code.

  ```python
  # Update the Q1 - 2018 data with rotation, x- and y-axis labels
  q1_2020['Subscribers'].hvplot.bar(
    xlabel="International Region",
    ylabel="Number of Subscribers",
    rot=30
  )
  ```

  ![plot_with_rot_labels.png](Images/plot_with_rot_labels.png)

* Axes labels can be formatted in a specific way. The `opts(xformatter)` and `opts(yformatter)` allow users to specify strings or numbers (e.g., `%.2f`).

  ```python
  # Update the Q1 - 2018 data with yformatter
  q1_2020['Subscribers'].hvplot.bar(
      xlabel="International Region",
      ylabel="Number of Subscribers",
      rot=30
  ).opts(yformatter='%.0f')
  ```

  ![hvplot_formatter.png](Images/hvplot_formatter.png)

* You can add a title to a visualisation by using the `opts(title)` parameter.

* You can also add a title to the plot with a label parameter, as the following code shows. A title added in this manner is reflected in the legend of a composed or overlay plot.

  ```python
  # Update the Q1 - 2018 data with a title
  q1_2020['Subscribers'].hvplot.bar(
      xlabel="International Region",
      ylabel="Number of Subscribers",
      rot=30
  ).opts(
      yformatter='%.0f',
      title="Subscriber Numbers by Region - Q1 2020"
  )
  ```

  ![opt_title.png](Images/opt_title.png)

  ```python
  # Update the Q1 - 2018 data replacing the title with the label parameter
  q1_2020['Subscribers'].hvplot.bar(
      label="Subscriber Numbers by Region - Q1 2020",
      xlabel="International Region",
      ylabel="Number of Subscribers",
      rot=30
  ).opts(
      yformatter='%.0f',
  )
  ```

  ![opt__no_title.png](Images/opt_no_title.png)

If time remains, discuss how to use the `opts` function to switch the x- and y-axes.

Highlight the `colour` and `hover_color` options, as shown in the following code. Explain that `hover_color` is especially useful in a bar plot with a lot of bars.

  ```python
    # The Q1 - 2018 data with color and hover_color
  q1_2020['Subscribers'].hvplot.bar(
      xlabel="International Region",
      ylabel="Number of Subscribers",
      rot=30
  ).opts(
      yformatter='%.0f',
      title="Subscriber Numbers by Region - Q1 2020",
      color="purple",
      hover_color="orange"
  )
  ```

  ![hvplot_color.png](Images/hvplot_color.png)

Slack out the [hvPlot customization](http://holoviews.org/user_guide/Customizing_Plots.html) link.The site lists all of the options available in hvPlot. Encourage students to review the list of options.

```text
http://holoviews.org/user_guide/Customizing_Plots.html
```

Ask if there are any questions before moving on to the next activity.

---

### 3. Student Do: Picture Perfect (15 min)

**Corresponding Activity:** [02-Stu_Picture_Perfect](Activities/02-Stu_Picture_Perfect)

In this activity, students will use hvPlot customisation attributes and options to add details to their visualisations.

**Note:** The data used in this section is similar to the dataset used in the “Composing Masterpieces” activity from the previous lesson, but it focuses on revenue rather than subscriber information.

Depending on the time available and students’ comfort level with the material, students can work either in groups or individually. Have TAs support students as needed.

Be sure to slack out the [hvPlot customisation](https://hvplot.pyviz.org/user_guide/Customization.html) documentation so that students have a complete list of all options available.

**File:**

* [picture_perfect.ipynb](Activities/02-Stu_Picture_Perfect/Unsolved/picture_perfect.ipynb)

**Instructions:**

* [README.md](Activities/02-Stu_Picture_Perfect/README.md)

------

### 4. Instructor Do: Picture Perfect Review (10 min)

In this section, the class will review the solution to the previous activity, and students will present their final, customised visualisations.

**Files:**

* [picture_perfect.ipynb](Activities/02-Stu_Picture_Perfect/Solved/picture_perfect.ipynb)

Ask for volunteers to demo their customised visualisations. Encourage students to share any tricks or shortcuts they learned in the process of building their visualisation, as well as give constructive criticism to their peers regarding how to make their visualisations more appealing and insightful.

When students present, ask them how they used the `opts` function and other customisation attributes to perfect their visualisations.

Review the solution to the activity by highlighting the following points:

* The code for the stylised plot for the revenue figures for the United States and Canada region is as follows:

  ```python
  # Create a DataFrame that slices the subscriber data for the United States and Canada region
  us_canada_revenue = regional_revenue_df.loc[regional_revenue_df['Area'] == 'United States and Canada']

  # Set the index of the DataFrame to Years
  us_canada_revenue = us_canada_revenue.set_index('Years')

  # Save the United States and Canada revenue plot to a variable
  us_canada_plot = us_canada_revenue['Revenue'].hvplot(
      xlabel='Revenue Periods',
      ylabel='Revenue',
      rot=45,
      label='United States and Canada Revenue - Q1 2018 through Q2 2020',
  ).opts(
      yformatter='%.0f',
      line_color="blue",
      hover_line_color="yellow"
  )

  # Show the plot
  us_canada_plot
  ```

* The code for the stylised plot for the revenue figures for Europe, the Middle East, and Africa is as follows:

  ```python
  # Create a DataFrame that slices the subscriber data for the Europe, Middle East, and Africa region
  emea_revenue = regional_revenue_df.loc[regional_revenue_df['Area'] == 'Europe, Middle East and Africa']

  # Set the index of the DataFrame to Years
  emea_revenue = emea_revenue.set_index('Years')

  # Create a styled line plot for the Europe, Middle East, Africa region.
  # Make the line_color orange and be sure to set the plot equal to a variable.
  emea_plot = emea_revenue['Revenue'].hvplot(
      xlabel='Revenue Periods',
      ylabel='Revenue',
      rot=45,
      label='Europe, Middle East and Africa - Q1 2018 through Q2 2020'
  ).opts(
      yformatter='%.0f',
      line_color="orange",
      hover_line_color="yellow"
  )

  # Show the plot
  emea_plot
  ```

* The code for the composite plot for these two visualisations is as follows:

  ```python
  # Adjust the title, height, width and background color of the overlay plot
  (us_canada_plot * emea_plot).opts(
      title="Revenue - US and Canada versus Europe, Middle East and Africa",
      bgcolor="lightgrey",
      height=500,
      width=1000,
  )
  ```

Here is the composite visualisation:

![overlay_styled.png](Images/overlay_styled.png)

If time remains, ask the following review questions:

* What are the different types of customisations we covered today?

  * **Answer:** Labels, axes, and colour.

* What is the argument of the `rot` function?

  * **Answer:** The angle of the x-axis labels. This could be 90, 45, and so on.

* Can composite plots be customised?

  * **Answer:** Yes. Composite plots can be customised with the `opts` function. The composing operation should be placed within parentheses in order for the `opts` function to work.

Answer any questions before moving on.

---

### 5. Instructor Do: Data Aggregation (15 min)

**Corresponding Activity:** [03-Ins_Data_Aggregation](Activities/03-Ins_Data_Aggregation)

Now you’ll begin discussing data aggregation with students. Begin by covering the following points:

* Now that we’ve made some beautiful, professional plots, let’s switch gears and talk about **data aggregation**, which is often the first step to creating a visualisation.

* Data storytelling often involves numerical, written, and visual explanations of the data. We combine all these elements to communicate what we understand about the data.

* Working in fintech, you’ll need to do analyses that rely on the relationships among multiple variables. For example, a real-estate analyst determines a property’s sale or rental price based on various factors: the square footage, number of rooms, property size, neighbourhood, school district, taxes, and more.

* The job of an analyst is to determine how these factors relate to one another and how those relationships affect the price. These relationships often help us tell a powerful or convincing story about the data that might inform financial decisions within markets.

* One powerful technique for exploring and understanding data relationships is aggregation. We already used aggregation to summarise data in previous lessons.

Now ask the students to recall the types of aggregation they have done in the past:

* What techniques have we used to describe or summarise data in the past?

  * **Answer:** Functions like `mean`, `count`, `sum`, `min`, and `max`. Each of these functions can summarise, or **aggregate**, a sequence of values.

* We can also use aggregation to explore the relationships in data by combining, or grouping, related data. We’ll use these techniques in two ways: numerically and visually. Let's start by exploring related groups of data with numerical aggregation.

Now, open the notebook in the Solved folder and begin to demonstrate some numerical aggregation techniques.

**File:** [03-Ins_Data_Aggregation](Activities/03-Ins_Data_Aggregation/Solved/data_aggregation.ipynb)

* **Numerical aggregation** involves evaluating a group of numbers to compile and summarise information about the group.

* For example, we have used the Pandas `describe` function to summarise a DataFrame. The `describe` function uses many aggregates, such as the mean, count, and minimum and maximum values. Each of these aggregates give us new ways to summarise and display the data.

  ```python
  df = pd.DataFrame({
      'prices': np.random.randint(0, 100, 100)
  })
  df.describe()
  ```

* We can also directly use aggregate functions, such as `mean` and `sum`, to summarise our data:

  ```python
  df.mean()
  df.sum()
  ```

* Now, say that we have a dataset consisting of prices for houses in different zip codes. The following code creates a DataFrame of randomly generated housing prices that are quoted in thousands of dollars. The code also randomly chooses between two zip codes:

  ```python
  houses_df = pd.DataFrame({
      'prices (in thousands))': np.random.randint(100, 1000, 100),
      'zip': np.random.choice([90210, 60606], 100)
  })
  display(houses_df.head())
  display(houses_df.tail())
  ```

* Now let’s inspect the first and the last five rows of our DataFrame by using `head` and `tail`:

* Say that we want to estimate the average housing price for each zip code. One way to do this is to filter out all the other zip codes and then calculate the summary statistics for just one neighbourhood. The following code shows doing this for zip code 90210:

  ```python
  prices_90210 = houses_df.loc[houses_df['zip'] == 90210]
  prices_90210.mean()
  ```

* The output gives the average price (in thousands of dollars) for housing in the zip code 90210, which is 610.05 (rounded two decimal places).

* This method works fine for one zip code, but what if we want to calculate the average housing price for each zip code in a state or even in a country or region? This means hundreds or even thousands of zip codes! There’s a better way to calculate the summary statistics for a group&mdash; by using the `groupby` function.

* The `groupby` function groups the data by the values in any column. In this case, we’ll group all the data by zip code. By default, the `groupby` function creates a **`groupby` object**. This object consists of the collection of elements from the original DataFrame that the characteristic you want defines. (The characteristic you want is the one that you’re using to create the groups.)

Run the following code to group the housing data by `zip`:

```python
houses_df.groupby('zip')
```

* If we try to display the output that results from this code, we’ll get a message that the code results in a `groupby` object.

* Running the Pandas `groupby` function results in a `groupby` object message rather than in a new DataFrame. This is because Pandas expects the `groupby` function to be followed by a function that aggregates the grouped data in some way. That is, Pandas expects to do something with the grouped data. So, Pandas expects an aggregate function such as `mean`, `sum`, or `std`.

* For example, let's calculate the mean of the prices grouped by zip code:

  ```python
  houses_df.groupby('zip').mean()
  ```

* This simple line of code calculates the mean value of the housing prices for each zip code. You can use any of the Pandas aggregate functions with the `groupby` object.

* Now let’s move on to an activity where you’ll use numerical aggregation to gain better insight into the relationships that exist in your data.

Keep the notebook open, as you will be reviewing the “Visual Aggregation” section with students later in the class.

---

### 6. Student Do: Group Dynamics (20 min)

**Corresponding Activity:** [04-Stu_Group_Dynamics](Activities/04-Stu_Group_Dynamics)
In this activity, students will use the Pandas `groupby` function to calculate the aggregate statistics of a DataFrame.

**File:** [group_dynamics.ipynb](Activities/04-Stu_Group_Dynamics/Unsolved/group_dynamics.ipynb)

**Instructions:** [README.md](Activities/04-Stu_Group_Dynamics/README.md)

As students work on the activity, circulate the room with the TAs to offer assistance to students who need it. Some students will be able to finish this more quickly than others. Let students know that their break follows this activity, and they can take additional time to complete it if needed.

---

### 7. BREAK (15 min)

---

### 8. Instructor Do: Group Dynamics Activity Review (10 min)

Open [group_dynamics.ipynb](Activities/04-Stu_Group_Dynamics/Solved/group_dynamics.ipynb) in the Solved folder and go over the code while explaining the following:

* To make our dataframe easy to work with, it’s important to load any columns that include dates or durations correctly. To do this, use the `parse_dates` and `infer_date_time_format` parameters in the Pandas `read_csv` function as you import your data.

* Always review the first few rows of your dataframe after loading it to make sure everything is as expected. To do this, use the Pandas `head` function. You can also use the `dtypes` function to confirm that Pandas correctly parsed your datetime columns.

* Clean your data before using it by dropping columns you will not need, as well as rows that have missing values. For this dataset, we will not need the `data_time` or the `timestamp` columns. Drop these first, then remove any rows that have missing values in our remaining columns by using the `dropna` function. Again, use `head` to check your work here.

* Now that our dataframe is clean, we can start aggregating. We want to group the dataframe by cryptocurrency, which will enable us to compare the values over time of the different cryptocurrencies in our dataset.

* First group the dataset by using the `groupby` function, then specify the `data_priceUsd` column, then use the Pandas `plot` function to create a plot.

* We can use the same `groupby` approach to calculate the mean of the cryptocurrency prices that we just plotted for each of our cryptocurrencies. To do this, use the same groupby object with the Pandas `mean` function.

* The calculation for the maximum price is similar. We apply the Pandas `max` function to our groupby object to determine this value.

* To determine the minimum value, we apply the `min` function.

* As you can see, we can quickly calculate values by using our `groupby` object! To make this process even easier, you can save your `groupby` object to a variable, and then apply the functions to that variable.

* Let’s take a moment to think about the results that we found in these steps and in our plot.

Call on students to answer the questions in step 7:

    * Which cryptocurrency had the largest swings in prices?

    * Which cryptocurrency do you recommend investing in?

Ask students to share if they had any issues with the activity, or if they found anything interesting as they explored the data.

---

### 9. Instructor Do: Visual Aggregation (10 min)

Now you’ll move on to discuss how to use similar aggregation approaches using visual methods. You’ll do this by continuing with the same notebook you used to discuss numerical aggregation.

**File:** [03-Ins_Data_Aggregation](Activities/03-Ins_Data_Aggregation/Unsolved/data_aggregation.ipynb)

Open the file and begin to work through the second section entitled “Visual Aggregation.”  Be sure to cover the following points:

* We can explore data relationships in various ways. For instance, certain plot types highlight different aspects of the data or allow you to compare one data point with another.

* Let’s look at an example of how we can compare data points. To do this, we’ll generate a DataFrame that contains a direct relationship between two data elements, AK and CA. (AK is the abbreviation for Alaska, and CA is the abbreviation for California.) In the data that the following code generates, the CA data mathematically relates to the AK data:

  ```python
  ak_data = np.arange(100)
  bias = np.random.uniform(0, 10, 100)
  ca_data = 2*ak_data + bias
  df = pd.DataFrame({
      "AK": ak_data,
      "CA": ca_data
  })
  ```

* Next, we plot this data by using an hvPlot scatter plot with AK on the x-axis and CA on the y-axis, as the following code demonstrates:

  ```python
  df.hvplot.scatter(x="AK", y="CA")
  ```

* The resulting plot shows that AK increases as CA increases&mdash;indicating a relationship between the two.

A simple plot like this can prove effective in illustrating patterns and relationships between distinct values. However, when the data involves groups, we might need to manipulate the plot or the DataFrame to correctly format the data for plotting.

* hvPlot helps us automatically visualise groups with widgets. **Widgets** are functional elements in a plot that allow us to easily change the visualisation. This way, we can highlight how each group affects the overall plot, the relationships among different groups, and how the analysis might change if we change the groups.

* As an example, let’s use the hvPlot widgets to interactively explore housing prices by zip code.
To apply the hvPlot widgets to groups, we need to add the `groupby` parameter to the `hvplot` function call. This tells hvPlot to group the prices by zip code. The following code shows this:

  ```python
  houses_df.hvplot(groupby="zip")
  ```

* We can use this widget to change the zip code that we want to explore. To change the zip code, we toggle, or drag, the slider to its left side to access data for zip code 60606, or its right side to access data for zip code 90210. This is a quick way to explore the data in each group, which will help us uncover patterns and relationships within a particular group.

* Notice that grouping the data by state creates a different type of widget - a dropdown menu rather than a slider.

* Because a zip code is a series of numbers, hvPlot selected the slider widget. Because a state abbreviation has a different data type, it selected a dropdown menu. It automatically customises the plot and widget type for the data that we’re working with. However, options exist for overriding its selections.

* You can read more about Widgets in the official hvPlot documentation.

Have a TA slack out the following link to do the documentation:
<https://hvplot.holoviz.org/user_guide/Widgets.html>

Next, you’ll use visual aggregation with hvPlot to explore real financial data.

---

### 10. Student Do: Exploring Medical Payments (20 min)

**Corresponding Activity:** [05-Stu_Exploring_Medical_Payments](Activities/05-Stu_Exploring_Medical_Payments)

In this activity, you’ll explore medical payments for diabetes by state. You’ll do so by using interactive visualisations, numerical and visual aggregation, and analysis.

**File:** [exploring_medical_payments.ipynb](Activities/05-Stu_Exploring_Medical_Payments/Unsolved/exploring_medical_payments.ipynb)

**Instructions:** [README.md](Activities/05-Stu_Exploring_Medical_Payments/README.md)

---

### 11. Instructor Do: Exploring Medical Payments Review (10 min)

Open [exploring_medical_payments.ipynb](Activities/05-Stu_Exploring_Medical_Payments/Solved/exploring_medical_payments.ipynb) in the Solved folder and review the solution with the students.
As you walk through the different sections of the activity, call on students to answer the questions that they should have answered as they worked through the steps of the activity.

Cover the following points in your walkthrough:

* As always, we’ll start by reading in the data and taking a look at it. Note that there are no dates in this dataset, so we are able to use the `read_csv` function without any additional parameters.

* We can use `.loc` to filter our data to only include costs with the definition code “638 - DIABETES W CC". There are other ways to filter datasets; did anyone do this a different way?

Ask students to share any different methods that they used. If time allows, you can mention filtering by column value, as in `hospital_data[(hospital_data["DRG Definition"] == "638 - DIABETES W CC")` or by query, as in hospital_data.query("DRG Definition" == "638 - DIABETES W CC")`.

* Regardless of how you filter, be sure to use the `head` and `tail` functions to confirm your filter worked as intended. This is always best practice after performing an operation on a dataframe.

* Next we’ll create a new dataframe that only includes the `Provider State` and `Average Total Payments` column. To do this, we will save a subset of the dataframe with these columns to a new name, `average_total_payments_by_state`. This is a good alternative to dropping columns you don’t need, should you want to retain access to the full dataframe.

* Now that we’ve done some filtering and created a subset of the dataframe, let’s explore the dataset by using data aggregation. We’ll begin by summing up the average total payments for each state, by grouping our dataframe by state and applying the `sum` function to the grouped dataset.

* We can sort this table using the `sort_values` function. The default sort for this function is ascending, so we’ll have our lowest average payments first. Then we can use our friend the `head` function to take a look at the states with the 5 lowest average total payments. We can use the `tail` function to look at the states with the highest payments.

* That was numerical aggregation; now let’s visually aggregate the data by using hvPlot, which allows us to quickly create a bar plot that lets us visually compare the payments in each state. We can use hvPlot widgets to take a closer look at California.

Ask the students to share their answers to the following questions:

* What patterns do you notice in the data?

* **Answer:** We can see from the interactive visualisation that there are some average total payments that stand above the majority.

* Do any data points influence the total payments amount?

* **Answer:** There are three spikes that stand out above the rest. These spikes may indicate outliers or anomalies that may need to be explored further. We may want to use numerical aggregation for the California data to investigate how these 3 outliers influence the overall payment information.

* Now we can do some numerical aggregation to look closer at these outliers we found. To do this, we’ll filter our dataframe to show California only, then sort the results to view the outlier payments. We can then plot this dataframe to look at the patterns.

Ask students to share their answer to the following question:

* How many payments appear to be outliers? What’s the approximate value of those payments?

* **Answer:** Zooming in on the data, it appears that there are 3 payments that appear to be outliers. The approximate value of these outliers are: a payment of approximately 15,570 at index position 127678; a payment of approximately 15,730 at index position 127746; and a payment of approximately 19,510 at index position 127735.

* We can now explore the outliers we found further. We’ll start by using the `describe` function, which is a quick way to review some statistics about California’s average total payments.

* Next we’ll filter out the outliers that are above 15,000, and plot the results in by using the hvPlot `bar` function.

* We can also use the `describe` function to compare our statistics from the filtered dataset with the statistics from the original dataset that includes outliers.

Ask the students to share their answers to the following questions:

* How much do the outliers change the mean value of the California average total payments for diabetes?

* **Answer:** Including the three outlier payments, the mean of California's average total diabetes payment is 7507.76. Removing the three outlier payments, the average becomes 7327.59. The outlier payments lower the mean payments value by 180.17.

Ask students to share if they had any issues with the activity, or if they found anything else that was interesting as they explored the data.

---

### 12. Student Do: Storytelling with Custom visualisations (20 min)

In this activity, Students will enhance a basic plot by using the visualisation options that the hvPlot library makes available.

**Corresponding Activity:** [06-Stu_Storytelling_with_Custom_visualisations](Activities/06-Stu_Storytelling_with_Custom_Visualisations)

In this activity, you’ll explore medical payments for diabetes by state. You’ll do so by using interactive visualisations, numerical and visual aggregation, and analysis.

**File:** [storytelling_with_custom_visualisations.ipynb](Activities/06-Stu_Storytelling_with_Custom_Visualisations/Unsolved/storytelling_with_custom_visualisations.ipynb)

**Instructions:** [README.md](Activities/06-Stu_Storytelling_with_Custom_Visualisations/README.md)

---

### 13. Instructor Do: Storytelling with Custom Visualisations Review (10 min)

Open [storytelling_with_custom_visualisations.ipynb](Activities/06-Stu_Storytelling_with_Custom_Visualisations/Solved/storytelling_with_custom_visualisations.ipynb) in the Solved folder and review the solution with the students. As you walk through the different sections of the activity, call on students to answer the questions that they should have answered as they worked through the steps of the activity.

Cover the following points as you walk through the solution file:

* Our process for creating visualisations should be familiar to you now. We start by importing the data, looking at it to confirm the import was successful, and then using the `.loc` function, or any method of your choice, to filter the dataset to values of interest.

* In this case, we’ll look at home sales between January and March 2019. Again, always look at your dataframe to confirm your filtering method worked as intended.

* Now we’ll use `groupby` to find the sale amount by the sell date for the first three months of 2019. This can show us how the average sale price varied by day.

* Note that I’m doing several things at once here. First I’m subsetting the dataset to only show the columns “saleAmt” and “saleDate”, then I’m grouping by “saleDate”, then I’m taking the mean the columns that I did not group by, in this case, just “saleAmt”, and finally I’m sorting the values by “saleDate”.

* You can do all of these operations in steps, or you can nest them together like this. It’s fine if your solution is written a bit differently than mine.

* Now we’ll use hvPlot to quickly create some plots. First we’ll use hvPlot’s default line plot. Then we’ll specify the `bar` function.

* hvPlot lets us create these plots very quickly, but we need to use additional parameters to make them more readable and professional.

Walk through the different steps in the solution to customise the plots. Ask students if they did anything differently in their customisation. Then, ask students to share their version of the data story they found for the tread of the real-estate commission.

If no one volunteers, you can share this story:

* Based on the information depicted in the visualisations, the trend for real estate commissions for 2019 is not great. The average sales per date in March is definitely down from that seen in January and February.

* March has only recorded 1 date with sales over 1 million while January and February recorded 8 days over the 1 million threshold. Additionally, March exhibited two consecutive dates of the lightest sales recorded.

* Just based on these initial observations, there is some cause for concern regarding the Arlington, Virginia real estate market.

Ask students to share if they had any issues with the activity, or if they found anything interesting as they explored the data.

---

### 15. Instructor Do: Recap (5 min)

Before beginning the recap, ask students if they have any questions about what they learned in class today. Take time to answer any questions that come up, then cover the following points.

* visualisations are an important part of working in any business that uses data. They are a critical way to summarise information to share with others.

* If a visualisation can’t be understood by others, it’s not worth sharing. Make sure to label and style your plots. Even if you do not need to share them with anyone, this will be good practice for you when you return to your work.

* Data aggregation, whether numerical or visual, will help you generate insights from data. Make sure that you are comfortable with both methods of aggregation.

Ask for any remaining questions before ending the class.

---

## End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
