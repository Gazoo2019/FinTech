## 6.3 Lesson Plan: Plotting Geospatial Data

### Overview

This lesson introduces students to plotting geospatial data, which is an important component of the week’s homework. The goal of this lesson is to build student confidence in working with hvPlot and GeoViews so that they’re prepared for the homework assignment.

### Class Objectives

By the end of this class, students will be able to:

* Compose visualisations using hvPlot and GeoViews.

* Construct map plot visualisations.

* Interact with the geospatial visualisations created with hvPlot and GeoViews.

---

### Instructor Notes

* This lesson builds on what students have learned in the previous visualisation lessons by having students prepare data by using Pandas and create visualisations by using hvPlot. The key difference is that they will be plotting geospatial data using GeoViews.

* After you discuss why plotting geospatial data is important and demonstrate how to do it by using hvPlot with GeoViews, students will complete several activities that are very similar to the homework.

* Before closing the class, take some time to review the homework with the students. Emphasise the similarities between the activities they completed in class and what they will do in the homework.

* Have your TAs keep track of the time with the [Time Tracker](TimeTracker.xlsx).

---

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 6.3 Slides](https://docs.google.com/presentation/d/1vcWcfTqhTVzjCXHSpNLlGMx_wOH2UxWM9XkWDh_aW8w/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The Time Tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome (5 min)

Welcome the students to their third visualisation class, and explain that today’s focus is on visualising location data. Cover the following points to motivate the class:

* In the fintech industry, location often plays a critical role in understanding financial and economic data.

* For example, fintech lenders use mapping technologies to define geographic regions. Specifically, they define geographic regions where demographics and economic factors indicate both the need for loans and the best opportunities for repayment.

* Ride-share car services use similar location-based technologies to identify the areas where they’ll most likely encounter individuals needing a ride.

* Understanding how potential opportunities, resources, and clients are geographically distributed&mdash;from the neighbourhood level to the entire globe&mdash;is key to establishing a successful business.

* Technology allows businesses to target markets well beyond their immediate locations. Access to almost-infinite amounts of data means that businesses can scour the globe for opportunities.

* With location-based technologies, firms can visualise the distribution of data and pinpoint the locations where the best business opportunities exist.

* Previously, you used interactive visualisations to explore the patterns and relationships in your data&mdash;without using a lot of code. Today, you’ll create interactive maps for geospatial or location-based data by using the PyViz library GeoViews.

---

### 2. Instructor Do: Using Geographic Data (15 min)

Now you’ll explain more about what geospatial data is and how it is used.

* **Geospatial data** is another term for location-based data. Geospatial data typically includes coordinates (longitudes and latitudes), addresses, and zip codes. It also typically includes information like cities, counties, states, provinces, or countries/regions.

* By basing visualisations on geospatial data, we can observe how the data is distributed across a specified location. For example, if you knew the nominal gross domestic product GDP as a whole but were curious how different states contributed to that number, a map of the United States that distinguishes states by nominal gross domestic product (GDP) would help you make quick comparisons.

  ![A screenshot depicts the map.](Images/6-2-states-by-gdp.png)

* Both businesses and consumers use geospatial data. Businesses use this data to target consumer hot spots, identify trends, or get economic information. Consumers use geospatial data and services to estimate travel times, determine traffic patterns, and find missing devices.

* So, how do we make plots like this? There is a range of different methods, but today we’ll use the PyViz library [GeoViews](https://geoviews.org/) to build your geospatial visualisations.

* GeoViews is a powerful visualisation library that can produce advanced charts and interactive visualisations. We’ll use the GeoViews option built into hvPlot to create interactive maps for our geospatial data.

Slack out to students the URL of the GeoViews libraries for further reference. Answer any questions before moving on.

---

### 3. Instructor Do: GeoViews Demo (15 min)

**Corresponding Activity:** [01-Ins_GeoViews_Demo](Activities/01-Ins_GeoViews_Demo)

In this section, you will demonstrate how to use hvPlot with GeoViews, and students will observe.

Data for this activity was retrieved from [catalog.data.gov](https://catalog.data.gov/).

**Files:**

* [geoviews_demo.ipynb](Activities/01-Ins_GeoViews_Demo/Unsolved/geoviews_demo.ipynb)

Start the demonstration of using GeoViews with hvPlot.

Open the starter file and demonstrate how to create a map scatter plot using the hvPlot `point` function.

* The `point` function can be used to create a scatter plot that is overlaid on top of a map that is provided by GeoViews. This allows for scatter-plot data to be analysed in reference to geographical location.

Talk the students through each of the sections of code that follows. Be sure to explain the parameters included within the points function.

```python
## Read in the population_counts.csv file into a DataFrame
population_df = pd.read_csv(
    Path("../Resources/population_counts.csv")
).drop_duplicates()

# Filter the DataFrame to include only New York state data
ny_data = population_df[population_df["StateDesc"] == "New York"]

# Create a DataFrame consisting of the CityName, PopulationCount, Latitude, and Longitude columns
ny_plot_df = ny_data[["CityName", "PopulationCount", "Latitude", "Longitude"]]

# Group the DataFrame by CityName and sum PopulationCount
ny_plot_df.groupby('CityName').PopulationCount.sum()

# Plot the data using hvPlot and GeoViews
map_plot = ny_plot_df.hvplot.points(
    'Longitude',
    'Latitude',
    geo=True,
    size = 'PopulationCount',
    scale = .02,
    color='CityName',
    alpha=0.8,
    tiles='OSM',
    frame_width = 700,
    frame_height = 500
    )

# Display the map
map_plot
```

  ![scatter_map_plot.png](Images/scatter_map_plot.png)

* Map plots often require more memory than the plots we are used to.

  * Datasets should be filtered and aggregated to the highest level of granularity possible (without jeopardising reporting context) so that plots do not take long to load.

  * Sampling techniques (e.g., visualising only top *n* items) should be used to help reduce the amount of data reflected in the visualisation.

  * These approaches will preserve reporting integrity.

Explain that when datasets become too large to manage or reduce, technologies like [Datashader](http://datashader.org) can be considered. Datashader specialises in turning large volumes of data into visualisations. Encourage students to look into technologies like Datashader outside of class.

Ask if there are any questions before moving on to the next activity.

---

### 4. Everyone Do: Geospatial Data in Real-Estate Analysis (20 min)

**Corresponding Activity:** [02-Evr_Geospatial_Real-Estate](Activities/02-Evr_Geospatial_Real-Estate)

In this section, have the students code along with you as you work through another example.

* Let’s work through one more example to show how we can use hvPlot with GeoViews to create dynamic visualisations for real-estate data.

* Say that we want to identify the three or four most densely populated cities in California. We want to launch our company’s long-term housing rental initiative and corresponding ad campaign in these cities.

* We have access to the 2016 population data for the state of California that’s broken down by city and by latitude and longitude. With this information, we can determine the relative population of each city in California and how the population is distributed across the state.

* Run the code to load the data into the `california_population_data` DataFrame and display the first five rows (the head) and the last five rows (the tail). As you can see, we have columns for Year, StateAbbr (state abbreviation), StateDesc (state name), CityName, PopulationCount, Latitude, and Longitude.

  ![A screenshot depicts the first five rows and the last five rows of the DataFrame.](Images/6-2-cali-pop-density-dataframe.png)

* Notice that the DataFrame lists the coordinates for each city’s latitude and longitude. With this information, hvPlot can render the map with incredible accuracy.

* Additionally, by aggregating these latitude and longitude points by city name, hvPlot can render the scatter plot points by city name and colour.

* Now, let’s take a look at the code to generate the visualisation:

  ```python
  # Plot data in a scatter plot using hvPlot with GeoViews enabled
  california_population_data.hvplot.points(
      'Longitude',
      'Latitude',
      geo=True,
      size='PopulationCount',
      scale=.04,
      color='CityName',
      tiles='OSM',
      frame_width=700,
      frame_height=500
      )
  ```

* Once again, we are telling hvPlot which data we are plotting, with longitude listed first and latitude listed second. Then we are enabling GeoViews and setting the size of the points to vary with our `PopulationCount` data. The scale setting helps the data fit into the size of our plot, the colour of our points will vary according to our `CityName` data, the `tiles` parameter specifies the look of our map, and `frame_width` and `frame_height` determine the size of the plot.

* Take a moment to vary each of these parameters and see what happens. For example, you could try changing the tiles parameter to `CartoDark` or have the colour vary by `StateAbbr`.

Give the students some time to play around with different options. Then ask them to take a look at the plot that they have created and answer some questions.

* What is the most densely populated city in California?

    **Answer:** Los Angeles.

* Which is bigger in terms of population, San Diego or San Francisco?

   **Answer:** They are about the same size.

Now ask the students if they know how to see the exact population numbers for these cities to determine which one is bigger. If someone knows, have them demonstrate.

If no one volunteers, show students how to zoom in on specific areas of the state by using hvPlot's "Box Zoom" tool, accessed by the magnifying glass icon. Then show how to hover the mouse over any point to see detailed information about that datapoint. With the “Pan” tool, an icon with arrows pointing in four directions, we can navigate from one part of the map to the other.

Now that students know how to explore the map, ask some additional questions geared toward using this information to make decisions for the company’s ad campaign.

* Where are the four largest cities in California located?

    **Answer:** The map shows that the four largest cities in California are somewhat distant from each other. Two are located in the northern half of the state, and the other two are located in the southern half.

* Given the distance between the cities, how would you recommend the company approach advertising in California?

    **Answer:** The company should create two ad campaigns, each geared campaign toward the specific interests, industries, and economic conditions of the state region (north or south). For example, ads for the San Francisco and San Jose markets might focus on the software industry, San Francisco sports teams, or outdoor activities (like hiking and camping). Ads for the Los Angeles and San Diego markets might focus on the entertainment industry or water sports (like surfing and sailing).

* We’d find it difficult to think of campaign ideas for these markets based on the location-based tabular data alone. We need the map and the plot to understand the relationships among the most densely populated cities.

Answer any questions before moving on.

---

### 5. Student Do: Mapping Adventure (20 min)

**Corresponding Activity:** [03-Stu_Mapping_Adventures](Activities/03-Stu_Mapping_Adventures)

In this activity, students will create scatter plots by using GeoViews. Break students into groups of three or four people.

Explain to students that data for this activity was retrieved from [catalog.data.gov](https://catalog.data.gov/).

**File:** [mapping_adventures.ipynb](Activities/03-Stu_Mapping_Adventures/Unsolved/mapping_adventures.ipynb)

**Instructions** [README.md](Activities/03-Stu_Mapping_Adventures/README.md)

---

### 6. Instructor Do: Mapping Adventure Review (10 min)

Review the code solution step by step. If you have time, you’ll facilitate a discussion about the activity, and ask students to share the top places they would go on their trip.

**Files:**

* [mapping_adventures.ipynb](Activities/03-Stu_Mapping_Adventures/Solved/mapping_adventures.ipynb)

Open the solution file and review each step, highlighting the following:

* The “marriage” of hvPlot and GeoViews has enabled developers to create interactive map visualisations.

* Using GeoViews, hvPlot can render geographic plots, such as the points plot. The points plot is the classic scatter plot overlaid on top of a map.

* The code for plotting the places of interest by name is as follows:

  ```python
  # Plot all of the NYC places of interest
  # Set the color parameter to Name
  # Set alpha to 0.8
  # Set tiles to 'OSM'
  # Set frame_width = 700
  # Set frame_height = 500
  places_of_interest_by_name = places_of_interest.hvplot.points(
      'Longitude',
      'Latitude',
      geo=True,
      color='Name',
      alpha=0.8,
      tiles='OSM',
      frame_width = 700,
      frame_height = 500
      )

  # Show the plot
  places_of_interest_by_name
  ```

* The following is the visualisation created by this code:

  ![plotting_adventures.png](Images/plotting_adventures.png)

* To create the visualisations based on `PlaceType` and `Borough`, change the value assigned to the `color`parameter inside the  `points` function.

* To plot the parks, gardens, and squares of interest, we must first create a slice of the original `places_of_interest` DataFrame.

Ask if any group would like to volunteer their solution for this plot. Then, continue reviewing the code.

* The code to visualise a map of the parks of interest is as follows:

  ```python
  # Create a DataFrame that slices the places_of_intereset DataFrame to include only parks
  parks = places_of_interest[places_of_interest["PlaceType"] == "Park"]

  # Plot all of the parks in NYC
  # What column should color be set equal to?
  # Keep all other parameters the same as the previous plot

  parks_of_interest = parks.hvplot.points(
      'Longitude',
      'Latitude',
      geo=True,
      color='Name',
      alpha=0.8,
      tiles='OSM',
      frame_width = 700,
      frame_height = 500
      )
  # Show the plot
  parks_of_interest
  ```

Review the Bonus question. Students will need to understand how to use `isin` in order to complete the next activity.

Ask for volunteers to provide the code for the Bonus. Be sure to discuss the use of the following two functions with the students:

* [Pandas `str.contains` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.contains.html) allows students to capture a location that contains part of the provided word in its name.

* [Pandas **`isin`** function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isin.html) is a way to reference the specific locations. (Highlight the use of the "Name" column from the DataFrame, the `isin` function, and  the list of the two location names that you would like to visit.

Explain the use of `|` as a separator between parameters.

* Once the new DataFrame is created, the locations are plotted using the `points` function as usual. The code is as follows:

  ```python
  # Slice the name of two places from the places_of_interest DataFrame
  # Use the Pandas isin function to reference the specific name of a location
  two_places = places_of_interest[(
      places_of_interest["Name"].str.contains("Airport"))
      | (places_of_interest["Name"].isin(["Aqueduct Race Track"])
  )]

  # Create the plot for just the two places
  two_places_route = two_places.hvplot.points(
      'Longitude',
      'Latitude',
      geo=True,
      color='Name',
      alpha=0.8,
      tiles='OSM',
      frame_width = 700,
      frame_height = 500
      )
  # Show the plot
  two_places_route
  ```

Ask for any remaining questions. If time allows, facilitate a discussion about the activity, and ask students to share the top places they would go on their trip. Otherwise, move on to the next activity.

---

### 7. BREAK (15 min)

---

### 8. Student Do: A Cartographer's Expedition (20 min)

**Corresponding Activity:** [04-Stu_Mapping_Adventures](Activities/04-Stu_Cartographers_Expedition)

In this activity, students will create map plots to embark on a virtual expedition to various places of interest in New York City.

Break students into groups of three or four people.

**File:**

* [cartographers_expedition.ipynb](Activities/04-Stu_Cartographers_Expedition/Unsolved/cartographers_expedition.ipynb)

**Instructions:**

* [README.md](Activities/04-Stu_Cartographers_Expedition/README.md)

---

### 9. Instructor Do: A Cartographer’s Expedition Review (5 min)

In this activity, students will present the maps and expeditions they created in the previous activity.

**Files:**

* [cartographers_expedition.ipynb](Activities/04-Stu_Cartographers_Expedition/Solved/cartographers_expedition.ipynb)

Ask the class if any group would like to present first. If time remains, ask for a second group to present. Ask each group the questions that follow the code block below.

The code for plotting all of the possible points in the excursion is as follows:

```python
# Plot the course for all of the stops in your excursion, including the airport
all_stops = places_of_interest[
    (places_of_interest["Name"].str.contains("Airport"))
    | (
        places_of_interest["Name"].isin(
            [
              "Aqueduct Race Track",
              "Juniper Valley Park",
              "Madison Square",
              "Liberty Island",
              "Ellis Island"
            ]
        )
    )
]

# Create the plot that shows all of your stops
plot_all_stops = all_stops.hvplot.points(
    'Longitude',
    'Latitude',
    geo=True,
    color='Name',
    alpha=0.8,
    size = 300,
    tiles='OSM',
    frame_width = 700,
    frame_height = 500
    )

# Show the plot
plot_all_stops
```

All other plots will be variations on this syntax.

* Given the location of the stops on your excursion, what is the order in which you should visit them to get you back to the airport most efficiently?

  * **Answer:** One possible answer is: Airport, Juniper Valley Park, Madison Square Garden, Ellis Island, Liberty Island, Aqueduct Race Track

* Sometimes, it's difficult to determine whether two locations are in close proximity to one another. What are some programmatic approaches to making sure locations are close to each other?

  * **Answer:** The data could be sorted by latitude and longitude. Another possible approach is to first slice the data by borough, and then choose locations.

* What factors guided your final decision on locations?

  * **Answer:** Locations were chosen based on categorical type and proximity. Locations of type garden, park, and square were chosen for a specific experience.

* Were the geographic scatter plots helpful in understanding the distribution of places of interest throughout New York City? How did the visual help cement the image?

  * **Answer:** Yes, the plots were helpful. By colour-coding by `PlaceType`, it was easy to observe the clusters of each type of place. This helped outline the trek through the boroughs. It was also helpful for noticing trends in the positioning of certain locations (e.g., Ellis and Liberty islands are in the same place, and the forts all seem to be north of Manhattan).

Ask if there are any questions before moving on to the next section.

---

### 10. Student Do: Plotting Foreclosures (25 min)

**Corresponding Activity:** [05-Stu_Plotting_Foreclosures](Activities/05-Stu_Plotting_Foreclosures)

In this activity, students will use hvPlot with GeoViews to visualise and explore real-estate data.

**File:** [plotting_foreclosures.ipynb](Activities/05-Stu_Plotting_Foreclosures/Unsolved/plotting_foreclosures.ipynb)

**Instructions:** [README.md](Activities/05-Stu_Plotting_Foreclosures/README.md)

---

### 11. Instructor Do: Plotting Foreclosures Review (10 min)

Open [plotting_foreclosures.ipynb](Activities/05-Stu_Plotting_Foreclosures/Solved/plotting_foreclosures.ipynb) in the Solved folder and review the solution with the students.

Cover the following points as you walk through the solutions file:

* We begin by reading in our data to Pandas and confirming that it was imported correctly. Next, there is a function provided for you that creates a subset of the dataframe that only includes specific lenders. Does anyone have any questions about this provided code?

* Now, we can use hvPlot with GeoViews to take a closer look at our new dataframe, which includes the largest lenders in Los Angeles. The parameters are set so that the colour of the points varies by the lenders in the list. This helps us compare where different lenders have properties.

* If we want to look more closely at the different types of properties, we can change the setting of our `color` parameter to vary by the “Property Type” column in our dataframe.

* Similarly, we can explore the different council districts by resetting the `color` parameter to vary by the “Council District” column in our dataframe

After you finish the solution walkthrough, call on students to share their answers to the questions in part 6 of the activity:

* After reviewing the visualisations, what insights can you gain about the foreclosures in Los Angeles in 2018? Which lender owns the most foreclosed properties? Do the lenders tend to focus on one area or council district in the city, or do they evenly distribute their properties throughout the region?

* **Possible answers:** Reviewing the plots, Ocwen Loan Servicing LLC seems to be the biggest lender associated with foreclosed properties in the area. They are primarily associated with Single Family dwellings with some Multi-Family included. Additionally, their dwellings are spread out around the region rather than being focused in any single council district. If there was a new real estate firm looking to enter the LA foreclosure market, Ocwen might be willing to make a deal where they could sell some properties at below-market prices to get them off of their books.

Facilitate a discussion around these answers, and around the students’ experiences using the plots to analyse the real estate market.

Answer any questions before moving on.

---

### 12. Instructor Do: Review Homework (10 min)

This activity involves a quick demo and a review of the homework.

**Files:**

* [Homework Instructions](../../../02-Homework/06-PyViz/Instructions/README.md)

* [Homework Solution](../../../02-Homework/06-PyViz/Solution/san_francisco_housing.ipynb)

Navigate to the Unit 6 Homework Instructions, and communicate the following to the students:

* This week’s homework focuses on visualising and analysing real estate data to identify the best properties in the San Francisco region.

* The homework includes using hvPlot with GeoViews to create interactive data visualisations of geographic data.

* In an investment scenario, offering a way to explore the real estate market interactively gives the investor the power to find properties that are of particular interest to them. In scenarios like these, it is the visualisations that help users make decisions.

Demo the homework solution by giving the students a preview of the solution.

Ask the students for any questions before moving forward.

---

### 13. Instructor Do: Recap (5 min)

* Congratulations on finishing the visualisation week! After today’s lesson, you should have everything you need to be successful on this week’s homework.

* You should also feel much more comfortable creating visualisations and interacting with them in order to gain insight about different markets and scenarios.

* There are lots of interesting datasets that include latitude and longitude data. Try finding a dataset you’re interested in and using hvPlot with GeoViews to explore it.

Ask for any remaining questions before ending the class.

## End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
