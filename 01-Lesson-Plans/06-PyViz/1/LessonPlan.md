## 6.1 Lesson Plan: Making and Understanding Interactive Plots

### Overview

The goal of this lesson is to educate students on how revolutionary interactive plots are, as well as enable them to create their own interactive visualisations that can be used to provide self-service data analysis and data exploration. Most importantly, today's class will teach students how to tell and interpret stories through data.

By the end of today’s class, students will be comfortable using hvPlot to create interactive visualisations for data exploration and analysis. The lesson will introduce students to PyViz, a visualisation ecosystem built for Python development, and it will focus on the differences and advantages of using interactive plotting technologies (like hvPlot) over technologies that provide static plots (e.g., Pandas and Matplotlib).

### Class Objectives

By the end of this class, students will be able to:

* Explain the importance of data visualisations in the current business environment

* Explain the advantages of the PyViz ecosystem.

* Use hvPlot widgets for data exploration.

* Create different style interactive charts using hvPlot, including line, bar, and scatter plots.

* Customize and interpret data visualisations.

* Create visualisations that consist of multiple plots.

---

### Instructor Notes

* As a reminder, slack out the [PyViz Installation Guide](../Supplemental/PyVizInstallationGuide.md). Tell students that they need to have PyViz installed prior to class today and to use office hours to debug any problems.

* Welcome to the first day of programming with PyViz and interactive plotting! You will be guiding students through a series of increasingly complex activities, which serve as the foundation for the next class as well as the homework. The class should feel like an evenly paced introduction to PyViz that provides a challenge and engages students with relatable use cases.

* Today's class will introduce students to fundamental PyViz concepts, including what PyViz is, technologies included within the ecosystem, and factors that make interactive plotting different from static plotting.

* Look for opportunities to include real-world examples in your lectures to make concepts more concrete and relatable for students. Feel free to draw upon your own experience using interactive visualisation technologies in the professional world.

* The financial focus for this unit is the real estate market. Real estate is a great domain for this type of lesson because real estate data is easily visualised with map charts. Visualisations can also help analysts scour through listings to find ideal property locations and sales.

  * Make sure to emphasise the real-world use cases of visualising real estate, such as finding the best place to move to, since some students may not find the real estate market as exciting as the stock market.

* A key to today's class is getting students to create and explore their visualisations using widgets. Therefore, each assignment will serve two purposes: coding the visualisation and analysing the visualisation to make key insights about the data.

* Remember that the purpose of this class is not just to teach students how to make interactive plots. Rather, the focus is to teach students how to tell stories through interactive plots, stories that users can deep dive into using the interactive widgets provided by PyViz's technologies.

* If students have issues with plots rendering blank in the Jupyter Lab preview, have them refer to the [troubleshooting section](../Supplemental/PyVizInstallationGuide.md#troubleshooting-guide-for-blankplots) of the PyViz Installation Guide.

* Please refer to our [Student FAQ](../../../06-Instructor-Resources/README.md) for answers to questions frequently asked by students of this program. If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

* Have your TAs keep track of the time with the [Time Tracker](TimeTracker.xlsx).

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 6.1 Slides](https://docs.google.com/presentation/d/1xEMm46SKvonVMQZ1lgcPkKiS1kqCmPazaOswuUYE2vo/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The Time Tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome (5 min)

Welcome to Unit 6! Unit 6 is dedicated to introducing and teaching students all they need to know about data visualisation using the PyViz visualisation platform.

​​Navigate to the 6.1 slides, and highlight the following:

* Visualisations have already been used in class (Matplotlib plots). However, these visualisations have been static. While static visualisations are helpful in displaying data, the data cannot be interacted with or explored in the same way. For this reason, students will learn how to create interactive plots.

* To create interactive plots, users need to be able to access visualisation libraries and packages that offer interactive visualisations. Otherwise, the visualisations would have to be coded manually, which can be extremely cumbersome.

* PyViz is a data visualisation ecosystem made specifically for Python. PyViz itself works as a wrapper around these various technologies.

  * Example visualisation technologies included with PyViz are hvPlot, GeoViews, Plotly Express, and Panel. In this unit, we’ll use hvPlot and GeoViews.

* PyViz aims to provide a single stop-and-shop space for all data visualisation needs.

* The creators of PyViz recognise that one technology or package cannot solve all data visualisation needs, and so, the creators have created PyViz as a means to provide developers with a platform that enables more than one data visualisation package being used for a project.

Transition into a demonstration of the types of visualisations that can be made using PyViz:

* Interactive visualisations allow data to be explored and analysed in the most efficient and effective manner for human eyes.

* Interactive visualisations give users the ability to pan, zoom, and filter data elements and values.

* Interactive visualisations also include functionality that allows data to be sorted off different values based on a simple click.

End the module communicating to students that gone are the days where simple line, bar, and histogram charts satisfied data visualisation and data analysis needs. Students will now learn how to create interactive and innovative visualisations.

Ask for any questions before proceeding.

---

### 2. Student Do: Exploring Visualisations (15 min)

**Corresponding Activity:** [01-Stu_Exploring_visualisations](Activities/01-Stu_Exploring_visualisations/)

In this activity, students will explore visualisation websites and present their findings.

First, break students into groups of five. Each group will be provided with the [PyViz Examples page](https://examples.pyviz.org/) as well as a link to one of the following websites:

* [Visual Captialist](https://www.visualcapitalist.com/)
* [FlowingData](https://flowingdata.com/)
* [Data Sketch](https://www.datasketch.es/)
* [Information is beautiful](https://informationisbeautiful.net/)

Groups will review the content and take notes on the visualisations that they find to be the most interesting and informative.

Be sure to tell students they’ll need to share their findings with the rest of the class.

**Files:**

[Instructions](Activities/01-Stu_Exploring_visualisations/README.md)

---

### 3. Everyone Do: Group Discussion on visualisations (15 min)

This section is an interactive group discussion about PyViz and the importance of visualisations.

The discussion will focus on the following:

* The importance of visualisations in the current business environment

* How the results of an analysis are communicated through visualisations

* How factors such as chart type, size, zoom, interactivity, and colours affect the visualisation and the information being communicated to your audience

Use the information that students gathered during the previous activity to start the discussion. For example, try the following approach:

* Choose one group to share their favourite visualisation from either the [PyViz Examples page](https://examples.pyviz.org/) or the visualisation website that they were assigned.

* Ask one team member to share their visualisation with the class and explain what aspects they found to be interesting and informative.

* Where possible, combine students’ insights with your personal experience with visualisations in the real world.

* Ask students how the visualisation communicates information to the audience (the person digesting the information from the visualisation). How might the visualisation be changed for a different audience?

* Ask someone from a different group to share a different visualisation. What makes the visualisation interesting and informative?

Continue the discussion until you have reviewed a variety of chart types on the various websites provided.

Transition to the next section of the lesson by saying something like the following:

> "With these different data visualisations in mind, let's begin our formal introduction to the PyViz ecosystem and one of its visualisation libraries, hvPlot."

---

### 4. Instructor Do: Introduction to PyViz (10 min)

In this section, you’ll discuss the advantages of using PyViz over other technologies (for example, HoloViews, Matplotlib, and D3.js).

Explain that the Python environment comes with a number of visualisation technologies that are wrapped together in a single platform called PyViz.

Have a TA slack out the image of the [overview of the PyViz ecosystem](https://pyviz.org/overviews/index.html).

Explain the following:

* PyViz is a data visualisation ecosystem that gives developers an easy way to access multiple data visualisation libraries like Matplotlib, HoloViews, and D3.js at once.

* Each visualisation technology in the PyViz ecosystem can provide stand-alone visualisations. Each technology has its strengths and weaknesses, which will be explored later.

* When it comes to fintech, using PyViz means you have access to standard plots as well as finance-specific plots. Another benefit of PyViz is that the sheer number of plotting technologies means that there's a greater chance of users finding the visualisations they need.

Facilitate a discussion by asking the following questions:

* Let’s say you need to use Matplotlib and HoloViews. What is the benefit of installing PyViz rather than downloading just these technologies?

  * **Answer:** Matplotlib and HoloViews may not satisfy all of the visualisation tools required. For example, Matplotlib and HoloViews provide visualisations, but they do not offer a way to create a dashboard. Installing PyViz will ensure all viable technologies are accessible.

  * **Answer:** Installing PyViz instead of just the individual technologies means that you get access to the individual technologies as well as the integration architecture that PyViz uses to integrate the libraries.

* What other environments we have worked in that resemble the PyViz environment?

  * **Answer:** The Anaconda environment. Anaconda is an environment that provides convenient access to all of the individual Python libraries, which is similar to the way that the PyViz ecosystem relates to the individual visualisation libraries.

Ask if there are any questions.

---

### 5. Everyone Do: Interactive Graphs with hvPlot (15 min)

**Corresponding Activity:** [02-Evr_hvPlot_Demo](Activities/02-Evr_hvPlot_Demo)

Explain to students that hvPlot, which is related to the HoloViews library, is a technology that brings plots to life.

* hvPlot abstracts over Python visualisation libraries like Matplotlib and Pandas. The abstraction allows hvPlot to utilise the stand-alone plotting mechanisms of these technologies.

* hvPlot provides the fintech industry with a new way of interacting with financial data. Instead of analysing ledgers or examining sections of a Pandas DataFrame, finance professionals can just explore interactive plots and digest large datasets visually.

* This abstraction also allows hvPlot to transform the static plots (e.g., Matplotlib plots) into interactive sandboxes for data exploration and analysis. hvPlots allow for:

  * Panning

  * Zooming

  * Hovering

  * Clicking

  * Filtering

Encourage students to review some of the [hvPlot examples](https://hvplot.pyviz.org/) on their own time. (Be sure to slack out the link.)

```text
https://hvplot.pyviz.org/
```

Open up the [hvPlot activity file](Activities/02-Evr_hvPlot_Demo/Unsolved/hvPlot.ipynb) and ask students to do the same. Review some of the hvPlot charts and their interactive features and have students follow along with you and ask questions.

* The hvPlot library must be imported into the Python environment. hvPlot offers a library called `hvplot.pandas` that integrates hvPlot with Pandas. This allows Pandas DataFrames to be visualised by using hvPlot. We use the following code to import hvPlot:

  ```python
  import hvplot.pandas
  ```

* Because hvPlot is integrated with Pandas, the two technologies share plotting interfaces. This makes it easy to repurpose code you’ve written to plot with Pandas in order to create plots with hvPlot.

  * Emphasize to students that even though hvPlot uses the function `hvplot` and not Pandas `plot`, the `hvplot` function makes reference to the Pandas `plot` interface. This allows for hvPlots to be created and manipulated in the same ways as Pandas plots (including plot attributes), but with an interactive component.

* The `hvPlot` function is used to create a standard hvPlot chart. For example, when used to visualise a DataFrame containing cumulative returns for five different tickers, hvPlot would create a visualisation using the metadata and data from the DataFrame. The user doesn’t need any additional configuration. The following code prepares the DataFrame and creates a line plot of the DataFrame by using `hvPlot`.

  ```python
  # Prepare the DataFrame
  idx = pd.date_range("1/1/2018", periods=52)

  df = pd.DataFrame(
      np.random.randn(52, 4), index=idx, columns=("APPL", "GOGLE", "AMMD", "BCOIN")
      ).pct_change()

  # Use hvplot.line to create line plot of the DataFrame
  df.hvplot.line(
    xlabel="Year",
    ylabel="Daily Return"
  )
  ```

  ![hvplot_line.png](Images/hvplot_line.png)

* Similar to Pandas `plot`, the `hvPlot` function has a `line` attribute. The `line` attribute tells hvPlot that the visualisation should be a line chart, as demonstrated in the following code.

  ```python
  # Use hvplot.line to create line plot
  df.hvplot.line(
      xlabel="Year",
      ylabel="Daily Return"
  )
  ```

* Similar to the Matplotlib plot functionality, if an attribute is not specified, hvPlot will choose the best plot for the data. In the following code, hvPlot will select a line plot, even though no plot type has been specified.

  ```python
  # Calculate the cumulative sum of the plot
  idx = pd.date_range("1/1/2017", periods=1000)

  df_cumsum = pd.DataFrame(np.random.randn(1000, 4), index=idx, columns=list('ABCD')).cumsum()

  # visualise the cumulative sum using a line plot
  # Like the plot function, hvPlot will select the plot that best displays the data
  df_cumsum.hvplot()
  ```

* The `hvPlot` function also has a `bar` attribute to visualise categorical data. It works the same as the `line` attribute, but it creates a bar chart rather than a line chart. Bar plots require categorical data, not just time series data. Bar plots need to compare the x-axis against the y-axis. The following code creates the DataFrame for the bar chart, and then creates the bar chart that visualises the daily return amount for each of the investments:

  ```python
  # Create the DataFrame for the bar chart
  df = pd.DataFrame(
    {'ticker':['APPL','GOGLE', 'AMMD','BCOIN'],
    'daily_return':(4.50,10,33.0,55.25)}
  )

  # Use hvplot.bar to create bar chart with categorical data
  df_bar.hvplot.bar(
    x="ticker",
    y="daily_return",
    xlabel="Ticker",
    ylabel="Daily Return",
    rot=90
  )
  ```

  ![hvplot_bar.png](Images/hvplot_bar.png)

With either the line or bar visualisation, demonstrate how to use hvPlot's interactive features. Be sure to show each feature while explaining the following:

* Hovering allows users to hone in on the plot value being observed.

* Panning allows for data to be analysed across time. To pan, click and drag the visualisation.

* Select an element on the legend to filter it out. This feature allows data to be hidden and curated as needed.

Explain that this interactivity is difficult with standard plotting packages like Pandas and Matplotlib. Having this kind of functionality with hvPlot is both powerful and groundbreaking. Rather than writing code to create a filter, a user can simply click the legend to visualise a filtered version of the dataset.

Indicate to students that these are just two ways to interact with hvPlots. hvPlot also provides widgets to interact with the data. These will be reviewed later in this lesson.

Ask students if they have any questions before moving on to the next activity.

---

### 6. BREAK (15 min)

---

### 7. Student Do: Plotting a Visual Takeover (20 min)

**Corresponding Activity:** [03-Stu_Plotting_Visual_Takeover](Activities/03-Stu_Plotting_Visual_Takeover)

In this activity, students will revisit the plots they made earlier in the class, and then recreate them as hvPlots. This activity aims to demonstrate the similarities between the hvPlot plot API and Pandas `.plot`, which uses Matplotlib's API.

Create breakout rooms of three or four students. Be sure to slack out the necessary files to the class.

**Files:**

* [plotting_visual_takeover.ipynb](Activities/03-Stu_Plotting_Visual_Takeover/Unsolved/plotting_visual_takeover.ipynb)

**Instructions**

* [README.md](Activities/03-Stu_Plotting_Visual_Takeover/README.md)

---

### 8. Instructor Do: Plotting a Visual Takeover Activity Review (10 min)

**Files:**

* [plotting_visual_takeover.ipynb](Activities/03-Stu_Plotting_Visual_Takeover/Solved/plotting_visual_takeover.ipynb)

Open the solved file and go over the code while explaining the following:

* The hvPlot library can be used to create many interactive plot visualisations.

* hvPlot has attributes that can be used to create line, bar, and scatter plots. If an explicit declaration is not desired, the `hvplot` function can be used.

The following code demonstrates several different plotting options:

  ```python
  # Plot an hvplot bar chart of the top 20 market cap companies
  top_20_market_cap.hvplot(title='Top 20 Market Cap Companies (in billions)')

  top_20_market_cap.hvplot.line(title='Top 20 Market Cap Companies (in billions)')

  top_20_market_cap.hvplot.bar(title='Top 20 Market Cap Companies (in billions)')

  sp500_companies_csv.hvplot.scatter(
    title='Top 20 Market Cap Companies (in billions) - EPS versus Price',
    x='Earnings/Share',
    y='Price'
  )

  sp500_companies_csv.hvplot(
    kind='scatter',
    title='Top 20 Market Cap Companies (in billions) - EPS versus Price',
    x='Earnings/Share',
    y='Price'
  )
  ```

  ![hvplot_plot.png](Images/hvplot_plot.png)

  ![hvplot_bar_market_cap.png](Images/hvplot_bar_market_cap.png)

If time remains, do a brief review of what was covered in the lesson so far. Ask the following questions:

* How does hvPlot differ from Pandas and Matplotlib?

  * **Answer:** hvPlot visualisations are interactive rather than static. They are equipped with widgets that allow users to manage how they want to interact with the data.

* What are some ways that a user can interact with an hvPlot visualisation?

  * **Answer:** Zooming, panning, hovering, filtering

* What is the relationship between the hvPlot API and the Pandas.plot API that you have previously used?

* **Answer:** hvPlot works with the existing Pandas.plot API, using its code as a foundation, building additional features and interactivity on top.

Ask if there are any questions before moving on.

---

### 9. Instructor Do: hvPlot Widgets (10 min)

**Corresponding Activity:** [04-Ins_hvPlot_Widgets](Activities/04-Ins_hvPlot_Widgets)

This section explores the different types of interactivity available with hvPlots. Students may have used some of the widgets already, but this section serves as a formal review of each button and interaction.

**Files:**

* [hvplot_widgets.ipynb](Activities/04-Ins_hvPlot_Widgets/Solved/hvplot_widgets.ipynb)

Explain to students that plot interactions occur via the hvPlot widget bar.

* The widget bar includes several buttons for different user interactions.

* The widget bar will be present for all plots that are created by using the `hvplot` function.

  ![hvplot_widget.png](Images/hvplot_widget.png)

Demonstrate how to use the widget bar. Open the solution file and highlight the following:

* The hvPlot widget bar gives users the ability to choose how they want to interact with the data.

* The widget bar includes buttons for the following interactions:

  * Panning

  * Box zoom

  * Wheel zoom

  * Save visualisation

  * Hover

Explain to the students that these tools will allow them to explore subsets of the data in detail more efficiently. Prior to the interactive plotting functionality, students would have had to create a subset of the DataFrame using either `loc` or `iloc` and then plot the resulting subset. hvPlot's widgets allow students to interact with and examine subsets of the data right inside the visualisation.

Use the bar plot that is generated based on the random flight data to demonstrate how each widget included in the toolbar allows you to interact with sections of the data.

  ```python
  # Use hvplot and the bar attribute to visualise the flight data
  flight_data.hvplot.bar(rot=90)
  ```

* **Panning** allows users to move the data on the screen in all directions. This is particularly valuable when trying to view data across time, outlying data points, or even high volume. Instead of having to zoom out to see all data, panning brings data into the forefront of the visualisation as needed. This is shown in the following image.

  ![hvplot_pan.gif](Images/hvplot_pan.gif)

* The **box zoom** interaction zooms into data points based on a selection:

  ![hvplot_box_zoom.gif](Images/hvplot_box_zoom.gif)

* **Wheel zoom** works like box zoom; however, the click wheel is used to magnify data points.

  ![hvplot_wheel_zoom.gif](Images/hvplot_wheel_zoom.gif)

* Another way to interact with visualisations is to **save** them. hvPlot allows visualisations to be saved as PNG files for later use.

  ![hvplot_save.gif](Images/hvplot_save.gif)

* **Hovering** is also a key interaction. Hovering over a value in a visualisation shows the actual value for that data point.

  ![hvplot_hover.gif](Images/hvplot_hover.gif)

* hvPlot also includes a **reset** widget button, which resets all visualisation interactions. If the visualisation was previously zoomed in at 110%, the reset would bring the zoom percentage back to 100%.

  ![hvplot_reset.gif](Images/hvplot_reset.gif)

* Widget activities can be **combined**. Clicking pan, wheel, and hover buttons enables users to pan, zoom, and get details by hovering all at the same time.

  * Note to students that certain widgets cannot be used with other widgets. For example, users cannot pan and box zoom at the same time. One action must occur first, and then the second widget option can be chosen.

  ![hvplot_all_actions.gif](Images/hvplot_all_actions.gif)

In addition to the widgets along the toolbar, using the **`groupby`** function will generate a widget that allows the user to visualise the information aggregated by category.

Explain that the Pandas `groupby` function allows users to numerically aggregate data. When using the `groupby` function, users must also chain one of the numerical aggregator functions like `sum`, `mean`, `min`, or `max`.

Demonstrate numerical aggregation for the flight data by grouping by `Status`, as shown in the following code.

  ```python
  # Use sum to find the total number of passengers by flight status
  flight_data.groupby('Status').sum()

  # Use sum to find the average number of passengers per flight by flight status
  flight_data.groupby('Status').mean()
  ```

Explain that `groupby` also works with hvPlot, allowing the user to visualise the data by category.

* Using the `groupby` function with hvPlot results in another widget.

* If the data being grouped is categorical in nature, the widget is a **dropdown menu**. If the data is numerical, the widget is a **slider**.

Group the flight data by `status` to demonstrate this widget, as the following code shows.

  ```python
  # Using groupby with hvPlot generates a dropdown menu widget
  flight_data.hvplot.bar(groupby='Status')
  ```

* The toolbar widgets can also be used in conjunction with the dropdown menu to further analyse the data.

  ![hvplot_dropdown.gif](Images/hvplot_dropdown.gif)

Ask if there are any questions before moving on to the next activity.

---

### 10. Student Do: hvPlot Widgets (20 min)

**Corresponding Activity:** [05-Stu_hvPlot_Widgets](Activities/05-Stu_hvPlot_Widgets)

In this activity, students will explore the hvPlot widgets to become familiar with the different types of interactions supported by hvPlots. Students will use hvPlot visualisations to explore hospital claims data and answer a few basic questions about the data.

Create breakout rooms of three or four students and share the following files.

**Files:**

* [hvplot_widgets.ipynb](Activities/05-Stu_hvPlot_Widgets/Unsolved/hvplot_widgets.ipynb)

**Instructions**

* [README.md](Activities/05-Stu_hvPlot_Widgets/README.md)

---

### 11. Instructor Do: hvPlot Widgets Activity Review (10 min)

In this section, you’ll review the previous activity on hvPlot widgets. Focus on what each widget does and how widgets can be used in conjunction with one another.

Data for this activity was retrieved from [data.cms.gov](https://data.cms.gov/).

**Files:**

* [hvplot_widgets.ipynb](Activities/05-Stu_hvPlot_Widgets/Solved/hvplot_widgets.ipynb)

Facilitate a discussion about the previous activity. Begin by reviewing the DataFrame that’s generated from running the starter code.

Review Step 2: Group the filtered hospital data by Average Total Payments and Provider State. Then, sum by Average Total Payments. The code is as follows:

  ```python
  # Using the procedure_638_charges DataFrame, group data by state and average total payments
  payment_by_state = procedure_638_charges[["Average Total Payments", "Provider State"]]

  # Aggregate the sum of payments by Provider State
  total_payment_by_state = payment_by_state.groupby("Provider State").sum()

  # visualise the DataFrame
  total_payment_by_state.head()
  ```

Review Step 3: Plot the aggregated data using the `hvplot.bar` function. Explore the unsorted data by using the pan and zoom widgets to find the costs for the state of New Jersey. Zoom in and out of the data to get a better understanding of costs for different states. The code for this step is as follows:

  ```python
  # visualise the data using an hvPlot bar chart
  total_payment_by_state.hvplot.bar(
      rot=90
  ).opts(
      yformatter='%.0f'
  )
  ```

Next, explain how the [hvPlot customisation option](https://hvplot.holoviz.org/user_guide/Customization.html) yformatter makes the values along the x-axis easier to view. Tell students that this information is covered in Lesson 3 of the module. Slack out the link to the hvPlot customisation page.

  ```text
  https://hvplot.holoviz.org/user_guide/Customization.html
  ```

Review the following question:

**Question:** How does the total cost of diabetes payments in New Jersey compare to that of surrounding states like New York, Connecticut, Delaware, and Pennsylvania?

* **Answer:** The cost of diabetes treatments in New Jersey are higher than some of the surrounding states but lower than others. Payments in New Jersey total 379,875. Of the surrounding states,the cost is lowest in Delaware, at 29,633. The cost is highest in New York, at 871,073. Pennsylvania comes in at 490,962, and Connecticut at 131,976.

Review Step 4: Sort the underlying visualisation data from lowest to highest total payments, as the following code shows.

  ```python
  # Sort the total payment by state data by Average Total Payments
  # and visualise the values in a bar chart
  total_payment_by_state.sort_values("Average Total Payments").hvplot.bar(
      rot=90
  ).opts(
      yformatter='%.0f'
  )
  ```

The remaining steps involve using the widgets and answering the following questions:

* List the 10 states with the lowest total payments for diabetes care.

  * **Answer:** The 10 states are: WY, HI, AK, SD, VT, MT, ND, ID, DE, and NE.

* How many states have total diabetes payments of less than 200,000?

  * **Answer:** There are 33 states with total diabetes payments of less than 200,000.

* What is the approximate difference in the total payments for diabetes services between the state with the tenth-highest payments and the state with the highest payments?

  * **Answer:** California has the highest total payments at 1,201,241. The state with the tenth- highest payments is Michigan at 345,449. The difference in payments between those two states is 855,792.

When you’re done reviewing the activity, ask students the following questions to confirm their understanding of hvPlot and the widgets:

* hvPlots have six standard widgets, one of which is pan. What are the other five widgets?

  * **Answer:** Box zoom, wheel zoom, save, refresh, and hover.

* What are some of the advantages of using hvPlot over a plotting API like Matplotlib or Pandas.plot?

  * **Answer:** Visualisations are interactive rather than static.

  * **Answer:** hvPlot dynamically handles the data in order to create more advanced visualisations. The `hvPlot` function automatically selects a plot to best fit the data, if none is specified.

* Sometimes, the text on display is hard to read. The labels can become illegible, depending on the amount of data being plotted. How can you improve the clarity of the plot?

  * **Answer:** Use the zoom widgets. This will limit the amount of data displayed on the screen, which will magnify the x-axis and y-axis values. This differs from static plots because static plots would require the width of the plot to be manipulated.

Ask if there are any questions before moving on.

---

### 12. Instructor Do: Composing Plots (10 min)

**Corresponding Activity:** [06-Ins_Composing_Plots](Activities/06-Ins_Composing_Plots)

In this section, you’ll demonstrate how to combine two plot objects in order to create a plot with subplots. The goal is for students to learn how to create plot layouts and overlay visualisations in order to create a centralised location for comparative data analysis.

**Files:**

* [composing_plots.ipynb](Activities/06-Ins_Composing_Plots/Solved/composing_plots.ipynb)

Explain to the students that the idea behind composing plots is to include more than one plot, called **subplots**, in a visualisation.

* One of the most powerful and valuable features of hvPlot is the ability to compose visualisations that include more than one plot called **subplots**.

* Composing plots is a quick and easy way to create a plot with subplots.

* Plots can be composed and overlaid by using the `+` and `*` operators. hvPlot handles the formatting and creates the layout for the new visualisation based on the type of data.

Open the starter file and demonstrate how to create plots using the `+` and `*` operators.

* One way to make composite plots, is to use the `+` layout operator. The layout operator places two plots side by side. hvPlot is so powerful and cutting edge that plots of different types can be composed. Here’s the code:

  ```python
  # Make a composite plots using + operator.
  total_payments_by_state.hvplot.bar() + sorted_total_payments_by_state.hvplot()
  ```

  ![compose_layout_bad_x.png](Images/compose_layout_bad_x.png)

Point out that, in this code, hvPlot automatically assigns the x-axis values on the second subplot to align with the x-axis values of the first subplot. There’s a way to overcome this issue by renaming the index of one of the DataFrames before creating the composite plots, as the following code shows.

  ```python
  # Rename the index of one of the DataFrames before they are plotted
  sorted_total_payments_by_state.index.names = ['Provider State Sorted']

  total_payments_by_state.hvplot.bar() + sorted_total_payments_by_state.hvplot()
  ```

  ![compose_layout.png](Images/compose_layout.png)

* Plots can also be overlaid using the `*` operator, which places the two plots along the same axis. For example, if one wanted to analyse Average Total Payments in relation to Average Medicare Payments, plots representing both per state could be composed in one plot.

* Labels should be used when overlaying plots in order to identify them.

* Plots of different types can be overlaid (e.g., line and bar). hvPlot will align the data from both plots along the same axis, as the following code shows.

  ```python
  # Overlay plots of different type using * operator
  sorted_total_payments_by_state.hvplot.line(label="Average Total Payments") * sorted_total_medicare_by_state.hvplot.bar(label="Average Medicare Payments")
  ```

  ![compose_overlay_different.png](Images/compose_overlay_different.png)

* Plots of the same type can also be overlaid (e.g., bar and bar). The following code shows how hvPlot automatically generates the overlaid plot in a different colour.

  ```python
  # Overlay plots of the same type using * operator
  sorted_total_payments_by_state.hvplot.bar(label="Average Total Payments") * sorted_total_medicare_by_state.hvplot.bar(label="Average Medicare Payments")
  ```

  ![compose_overlay_same.png](Images/compose_overlay_same.png)

* Once the plots have been composed, users can interact with both subplots by using a single widget bar.

  ![single_widget_bar.gif](Images/single_widget_bar.gif)

Answer any questions before moving on to the next activity.

---

### 13. Student Do: Composing Masterpieces (15 min)

**Corresponding Activity:**

[07-Stu_Composing_Masterpieces](Activities/07-Stu_Composing_Masterpieces)

In this activity, students will compose and overlay hvPlots. They will work individually rather than in groups, as there are only 10 minutes allotted for this activity.

Should students need assistance, encourage them to ask questions in the chat. Ask your TAs to monitor the chat closely.

If you notice a student who completes the activity quickly, or who helps others with the activity, ask them to review the solution step by step for the class.

Encourage any students who finish early to help their classmates.

**Files:**

* [composing_masterpieces.ipynb](Activities/07-Stu_Composing_Masterpieces/Unsolved/composing_masterpieces.ipynb)

* [README.md](Activities/07-Stu_Composing_Masterpieces/README.md)

---

### 14. Instructor Do: Composing Masterpieces Review (5 min)

In this section, the class will review the solution to the previous activity.

**Files:**

*
[composing_masterpieces.ipynb](Activities/07-Stu_Composing_Masterpieces/Solved/composing_masterpieces.ipynb)

To conduct this review, you can either ask a student volunteer to review the code solution, or do it yourself.

Either way, the following points should be covered:

* The `+` operator is used to create plots that are adjacent to each other. This creates a single plot that contains more than one visualisation.

  ```python
  # Create a composite plot to visualise the Q1 data side-by-side
  q1_2018_plot + q1_2019_plot + q1_2020_plot
  ```

* The overlay plot is created with the `*` operator. This creates a single plot with only one visualisation. The order in which the plots are listed affects the visualisation.

* Because the plots are overlaid, it is difficult to see the specific value for each of the three years. The exact values can be observed when the hover widget is used.

  ```python
  # Create an overlay plot to visualise the Q1 data
  q1_2018_plot * q1_2019_plot * q1_2020_plot
  ```

* This is the order of the plots that results in a correct visualisation. The plots with the largest values should be listed first.

  ```python
  # Create an overlay plot to visualise the Q1 data
  q1_2020_plot * q1_2019_plot * q1_2018_plot
  ```

**Note:** If a student is conducting this review and needs guidance, ask the following questions.

* How many different ways can you make composite plots? What are the operators?

  * **Answer:** There are two operators, `+` and `*`.

* What does the `+` operator do?

  * **Answer:** Create a layout where each plot is placed adjacent to another.

* What does the `*` operator do?

  * **Answer:** The `*` operator overlays plots where each plot is placed along the same axis.

* How many widget bars are created when plotting—one total, or one for each plot?

  * **Answer:** A single widget bar is created. This single bar can be used to control each of the plots.

Ask for any remaining questions before moving on.

---

### 15. Instructor Do: Recap (5 min)

Review and discuss the concepts covered in the lesson, especially as they relate to the lesson's learning objectives.

* Explain the importance of data visualisations in the current business environment

* Explain the advantages of the PyViz ecosystem.

* Create different style interactive charts using hvPlot, including line, bar, and scatter plots.

* Use hvPlot widgets for data exploration.

* Customize and interpret data visualisations.

If time permits, review the homework assignment with the students.

---
Ask for any remaining questions before ending the class.

## End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
