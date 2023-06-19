# Data Analysis Project - CoffeeShops


In this project, we will be conducting a data analysis for coffeeshops. The data will be collected from fidilo.ir, including point of sale systems, customer feedback, and other relevant data sources. The main objective of this project is to gain insights into the coffee shop's operations and identify areas for improvement.

The analysis will cover various aspects of the coffee shop's operations including sales, customer behavior, and marketing effectiveness. We will also be analyzing customer feedback to gain insights into their preferences and identify areas for improvement in terms of product offerings, customer service, and overall customer experience.

By conducting this analysis, we aim to provide actionable insights that can be used to optimize the coffee shop's operations, increase revenue, and enhance the overall customer experience.

This Project is made of a greate teamwork with Ehsan Rajabi and Mobin Mohseni in Quera Data Anlysis Team. The main following Steps for this project are:

## Step 1: Scraping Websites

The first step in any data analysis project is to gather data. In this case, we will be scraping fidilio.ir to collect relevant data.This project involve using web scraping tools such as Beautiful Soup and Scrapy. Once the data has been scraped, it should be cleaned and stored in a structured format.

## Step 2: Implementing Data into Database

The next step is to implement the data into a database. This involves creating a schema that will accommodate the data and writing queries to insert the data into the database. The database should be optimized for fast retrieval of data.

## Step 3: Visualizing Data with Power BI

The final step is to visualize the data using the Power BI platform. Power BI is a powerful data visualization tool that can be used to create interactive dashboards, reports, and charts. The data can be connected directly to Power BI or exported from the database in a format that can be easily imported.

By following these steps, you can create a successful data analysis project for GitHub. Good luck!
=======
## Quera Team - group 4 - Project 1
In this project, we are about to crawl fidilio.com to extract coffeeshops data. then we are going to clean the data and implement it in a dedicated database. and finally, do some analysis and visualize them in Microsoft Power BI.

    Root.
        ├── src     # Source files Scripts for web scraping using tools like BeautifulSoup, requests, logging, and etc.
        |    ├── Coffee.csv
        |    ├── Coffee_Clean.csv
        |    ├── fidilio.log
        |    └─  fidilio.py
        |    
        ├── database 
        |    ├── img
        |    ├── DB_interface_and_implementing.ipynb
        |    └── Er_diagram.pdf
        ├── dashboard
        |   ├── data
        |   ├── img
        |   ├── Interface_of_Dashboard.py
        |   ├── report.pbix
        |   └── report.pdf
        |
        ├── requirements.txt
        └── README.md # Explanation of project structure, tools used, and instructions for executing each part of the project.
___
### Dashboard first page:
![Screenshot](dashboard/img/dashboard_view.png)
