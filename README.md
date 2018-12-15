# Projects from Dataquest

This repository is for sharing some of my projects from Dataquest.  Each of the projects I completed is listed below along with some notes on the concepts and methods used.


## Project_01: [Numbers of Births](https://github.com/Frizzles7/Dataquest/blob/master/Project_01/Basics.ipynb)
This introductory project practices reading in a file, splitting data, creating a dictionary, and summarizing counts.


## Project_02: [Births](https://github.com/Frizzles7/Dataquest/blob/master/Project_02/Basics.ipynb)
This project continues with the births dataset and uses dictionaries, loops, creating functions, and calculating some summary statistics.


## Project_03: [Gun Deaths](https://github.com/Frizzles7/Dataquest/blob/master/Project_03/Basics.ipynb)
This project explores data on gun deaths and uses datetime, dictionaries, and loops to draw conclusions.


## Project_04: [eBay Car Sales](https://github.com/Frizzles7/Dataquest/blob/master/Project_04/Basics.ipynb)
This project investigates car sales on Germany's eBay website and uses NumPy and Pandas to summarize and clean the data.  Examples of methods used include info, head, describe, value_counts, and unique.


## Project_05: [Earnings by College Major](https://github.com/Frizzles7/Dataquest/blob/master/Project_05/Basics.ipynb)
This project looks at earnings by college major and explores different visualizations using Pandas and Matplotlib.  Examples of visualizations used include scatter plots, histograms, scatter matrix plots, bar graphs, grouped histograms, box plots, and hexagonal bin plots.


## Project_06: [Gender Gap in College Degrees](https://github.com/Frizzles7/Dataquest/blob/master/Project_06/Basics.ipynb)
This project looks at the degrees awarded by gender and uses different visualizations with more customizations.  Examples include using options to change the size, layout, labels, tick marks, colors, and other display parameters in the visualizations. 


## Project_07: [NYC High Schools](https://github.com/Frizzles7/Dataquest/blob/master/Project_07/Schools.ipynb)
This project incorporates data on New York City high schools.  Data is initially provided in multiple files, which I combine and convert data to numeric data, using regex as needed.  Data visualizations used include scatter plots, bar graphs, and a map using basemap.


## Project_08: [Star Wars Survey](https://github.com/Frizzles7/Dataquest/blob/master/Project_08/Basics.ipynb)
This project investigates survey data on Star Wars movies.  I cleaned and transformed the provided data into a usable format with usable columns.  I then compiled various statistics using NumPy and Pandas and created visualizations using bar graphs from Matplotlib and Seaborn.


## Project_09: [Working with Data Downloads](https://github.com/Frizzles7/Dataquest/tree/master/Project_09)
This project involved creating and manipulating files from the command line, rather than in Jupyter.  In this project, I created several scripts to read in the data, perform counts of some variables, create pivot tables, and create a dictionary of counts.  The results of the analysis performed were printed to the findings.txt file.


## Project_10: [Hacker New Submissions](https://github.com/Frizzles7/Dataquest/tree/master/Project_10)
This project continued my work from the command line, writing scripts to answer some questions about the data provided on submissions to Hacker News.  I created scripts to read in the data, determine the most common words in the headlines, determine which domains were submitted most frequently to Hacker News, and determine at what time of day submissions were most commonly made.


## Project_11: [CIA Factbook using SQLite](https://github.com/Frizzles7/Dataquest/blob/master/Project_11/Basics.ipynb)
This project looks at the CIA World Factbook database using SQLite.  I created SELECT queries to review the data, look for outliers, and calculate several different statistics.  I also created visualizations using Matplotlib and Seaborn.


## Project_12: [Answering Business Questions using SQL](https://github.com/Frizzles7/Dataquest/blob/master/Project_12/Basics.ipynb)
This project uses the chinook database of sales for a digital media store.  I used SQLite to run queries on the database and used Matplotlib to create visualizations of the results.  I use the results of the queries and visualizations to make business recommendations regarding which types of albums to add to the store, the performance of the different sales agents, which countries generate sales, and whether sales should be of individuals songs or full albums.


## Project_13: [Designing and Creating a Database](https://github.com/Frizzles7/Dataquest/blob/master/Project_13/Basics.ipynb)
This project uses SQLite to design and create a database on Major League Baseball statistics initially provided in several different files.  I review the data provided and create tables.  I also design the [schema](https://github.com/Frizzles7/Dataquest/blob/master/Project_13/my_schema.png) for the database.  I then build the database as outlined in my schema.


## Project_14: [Fandango Movie Ratings](https://github.com/Frizzles7/Dataquest/blob/master/Project_14/Basics.ipynb)
This project looks at whether Fandango movie ratings have changed since it was discovered that they were rounding up ratings.  Using Pandas, NumPy, and Matplotlib, I investigate the differences in ratings from before this discovery and after using calculated statistics and visualizations, including kernel density plots and grouped bar plots.


## Project_15: [Finding Advertising Markets](https://github.com/Frizzles7/Dataquest/blob/master/Project_15/Basics.ipynb)
This project looks at an e-learning company to determine the best markets in which to advertise.  I use NumPy, Pandas, and Matplotlib to compute different metrics, normalize the values, and create visualizations to make business recommendations.  I also handle missing values and outliers in the data.


## Project_16: [Jeopardy!](https://github.com/Frizzles7/Dataquest/blob/master/Project_16/Basics.ipynb)
This project uses a portion of the Jeopardy! dataset to look for patterns to help win the game.  I use regular expressions to clean text strings, write functions to determine whether the answer can be deduced from the question, and determine whether new questions are recycled old questions.  Finally, I used chi-squared tests to determine if any of the terms had a statistically significant difference between high and low value questions.


## Project_17: [Predicting Car Prices](https://github.com/Frizzles7/Dataquest/blob/master/Project_17/Basics.ipynb)
This project uses a data set on cars where I investigate using k-nearest neighbors to predict the market price of a car.  I use KNeighborsRegressor, mean_squared_error, cross_val_score, and KFold in the analysis.  I also create visualizations of the RMSEs calculated, determine the best features to use in the model, and tune the value of k in k-nearest neighbors.


## Project_18: [Predicting House Sale Prices](https://github.com/Frizzles7/Dataquest/blob/master/Project_18/Basics.ipynb)
This project looks at housing data for Ames, Iowa to perform several data preparation tasks and different linear regression techniques.  I create a pipeline of functions to transform the features, select specific features for the model, and train and test the model.  During the creation of these functions, I investigate the data more closely, deal with missing values, look at correlations, and create a heat map.  I also use holdout validation, simple cross validation, and k-fold cross validation.


## Project_19: [Predict Closing Stock Prices](https://github.com/Frizzles7/Dataquest/blob/master/Project_19/predict.py)
This project evaluates historical S&P 500 stock price data.  I create a script to predict closing prices, in which I create several features for the models to use, train a linear regression model, and evaluate the model based on root mean squared error.


## Project_20: [Predicting Bike Rentals in DC](https://github.com/Frizzles7/Dataquest/blob/master/Project_20/Basics.ipynb)
This project uses data on bike rentals in Washington, DC.  I use several different models to predict the count of bike rentals in a given hour.  I review the data and create visualizations, including a histogram of the count of bike rentals and heatmap of correlations.  I begin with linear regression.  Next, I use decision trees to improve signficantly over linear regression, and I tweak the model to make it perform even better.  Then, I use a random forest to improve even more over the best decision tree model, and tune the parameters of that model to make it perform even better.


