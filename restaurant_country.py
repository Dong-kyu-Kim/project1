#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os


# In[2]:


# Load the restaurant data
csv_file = os.path.join("resources", "restaurant_data.csv")

restaurant_df = pd.read_csv(csv_file, encoding = 'utf-8')
restaurant_df.head(10)


# In[3]:


# Check for missing data
restaurant_df.count()


# In[4]:


# Check data types
restaurant_df.dtypes


# In[5]:


# Create a country list for x-axis
country_list = ["American", "French", "Indian", "Italian", "Japanese", "Mexican"]


# 1. Average "Revenue" comparison by each country's "Cuisine"

# In[6]:


# Group with "Cuisine" by each countries with average "Revenue"
group0 = restaurant_df.groupby(["Cuisine"])
group0 = group0[["Revenue"]].mean()
group0


# In[7]:


# Create a "Revenue" list 
revenue = group0["Revenue"].tolist()
revenue


# In[8]:


# Create a bar chart comparing average "Revenue" by each countries
plt.figure(figsize = (8, 4))
plt.bar(country_list, revenue, color = 'blue', alpha = 0.25)

plt.title("Comparison between countries (Average Revenue)")
plt.xlabel("Cuisine by each countries")
plt.ylabel("Average Revenue")

revenue_bar_path = os.path.join("result_country", "avg_revenue_bar_comparison.png")
plt.savefig(revenue_bar_path)


# In[9]:


# Create a line graph comparing average "Revenue" by each countries
plt.figure(figsize = (8, 4))
plt.plot(country_list, revenue, marker = 'o', color = 'red', label = "Average Revenue", alpha = 0.5)

plt.title("Comparison between countries (Average Revenue)")
plt.xlabel("Cuisine by each countries")
plt.ylabel("Average Revenue")
plt.legend(loc = 'best')

revenue_line_path = os.path.join("result_country", "avg_revenue_line_comparison.png")
plt.savefig(revenue_line_path)


# 2. Average "Rating" by each country's "Cuisine"

# In[10]:


# Group with "Cuisine" by each countries with average "Rating" scores
group1 = restaurant_df.groupby(["Cuisine"])
group1 = group1[["Rating"]].mean()
group1


# In[11]:


# Create a "Rating" list
rating = group1["Rating"].tolist()
rating


# In[12]:


# Create a bar chart comparing average "Rating" by each countries
plt.figure(figsize = (8, 4))
plt.bar(country_list, rating, color = 'blue', alpha = 0.25)

plt.title("Comparison between countries (Average Rating)")
plt.xlabel("Cuisine by each countries")
plt.ylabel("Average Rating Scores")

rating_path = os.path.join("result_country", "avg_rating_bar_comparison.png")
plt.savefig(rating_path)


# In[13]:


# Create a line graph comparing average "Rating" by each countries
plt.figure(figsize = (8, 4))
plt.plot(country_list, rating, marker = 'o', color = 'red', label = "Average Rating Score", alpha = 0.5)

plt.title("Comparison between countries (Average Rating)")
plt.xlabel("Cuisine by each countries")
plt.ylabel("Average Rating Scores")
plt.legend(loc = 'best')

rating_path = os.path.join("result_country", "avg_rating_line_comparison.png")
plt.savefig(rating_path)


# 3. Average "Service Quality Score" by each country's "Cuisine"

# In[14]:


# Group with "Cuisine" by each countries with average "Service Quality Score"
group2 = restaurant_df.groupby(["Cuisine"])
group2 = group2[["Service Quality Score"]].mean()
group2


# In[15]:


# Create a "Service Quality Score" list
service_quality_score = group2["Service Quality Score"].tolist()
service_quality_score


# In[16]:


# Create a bar chart comparing average "Service Quality Score" by each countries
plt.figure(figsize = (8, 4))
plt.bar(country_list, service_quality_score, color = 'blue', alpha = 0.25)

plt.title("Comparison between countries (Average Service Quality Score)")
plt.xlabel("Cuisine by each countries")
plt.ylabel("Average Service Quality Scores")

service_q_score_bar_path = os.path.join("result_country", "avg_service_quality_bar_comparison.png")
plt.savefig(service_q_score_bar_path)


# In[17]:


# Create a line graph comparing average "Service Quality Score" by each countries
plt.figure(figsize = (8, 4))
plt.plot(country_list, service_quality_score, marker = 'o', color = 'red', label = "Average Service Quality Score", alpha = 0.5)

plt.title("Comparison between countries (Average Service Quality Score)")
plt.xlabel("Cuisine by each countries")
plt.ylabel("Average Service Quality Scores")
plt.legend(loc = 'best')

service_q_score_line_path_ = os.path.join("result_country", "avg_service_quality_line_comparison.png")
plt.savefig(service_q_score_line_path_)


# 4. Average "Weekend Reservations", "Weekday Reservations", and "Weekend Reservations" by each country's "Cuisine"

# In[18]:


# Group with "Cuisine" by each countries with average "Weekend Reservations" and "Weekday Reservations"
group3 = restaurant_df.groupby(["Cuisine"])
group3 = group3[["Weekend Reservations", "Weekday Reservations"]].mean()
group3


# In[19]:


# Create a "Weekend Reservations" list
weekend = group3["Weekend Reservations"].tolist()
weekend


# In[20]:


# Create a "Weekday Reservations" list
weekday = group3["Weekday Reservations"].tolist()
weekday


# In[21]:


# Create a line graph comparing average "Weekend Reservations" and average "Weekday Reservations" by each countries
plt.figure(figsize = (8, 4))
plt.plot(country_list, weekend, marker = 'o', color = 'red', label = 'Average Weekend Reservation', alpha = 0.5)
plt.plot(country_list, weekday, marker = 'o', color = 'blue', label = 'Average Weekday Reservation', alpha = 0.5)

plt.title("Comparison between countries (Average Weekdays and Weekend Reservations)")
plt.xlabel("Cuisine by each countries")
plt.ylabel("Average Reservations")
plt.legend(loc = 'best')

weekend_weekday_path = os.path.join("result_country", "avg_weekend_weekday_line_comparison.png")
plt.savefig(weekend_weekday_path)


# In[22]:


group3["Week Reservations"] = group3["Weekend Reservations"] + group3["Weekday Reservations"]
group3


# In[23]:


# Create a "Week Reservations" list
week = group3["Week Reservations"].tolist()
week


# In[24]:


# Create a line graph comparing average "Week Reservations" by each countries
plt.figure(figsize = (8, 4))
plt.plot(country_list, week, marker = 'o', color = 'red', label = "Average Week Reservation", alpha = 0.5)

plt.title("Comparison between countries (Average Week Reservations)")
plt.xlabel("Cuisine by each countries")
plt.ylabel("Average Reservations")
plt.legend(loc = 'best')

week_path = os.path.join("result_country", "avg_week_line_comparison.png")
plt.savefig(week_path)


# 5. Average "Marketing Budget" by each country's "Cuisine"

# In[25]:


# Group with "Cuisine" by each countries with average "Marketing Budget"
group4 = restaurant_df.groupby(["Cuisine"])
group4 = group4[["Marketing Budget"]].mean()
group4


# In[26]:


# Create a "Marketing Budget" list
marketing_budget = group4["Marketing Budget"].tolist()
marketing_budget


# In[27]:


# Create a bar chart comparing average "Marketing Budget" by each countries
plt.figure(figsize = (8, 4))
plt.bar(country_list, marketing_budget, color = 'blue', alpha = 0.25)

plt.title("Comparison between countries (Marketing Budget)")
plt.xlabel("Cuisine by each countries")
plt.ylabel("Marketing Budget")

marketing_budget_bar_path = os.path.join("result_country", "avg_marketing_budget_bar_comparison.png")
plt.savefig(marketing_budget_bar_path)


# In[28]:


# Check the maximum value
max(marketing_budget)


# In[29]:


# Create a line graph comparing average "Marketing Budget" by each countries
plt.figure(figsize = (8, 4))
plt.plot(country_list, marketing_budget, marker = 'o', color = 'red', label = "Marketing Budget", alpha = 0.5)

plt.title("Comparison between countries (Marketing Budget)")
plt.xlabel("Cuisine by each countries")
plt.ylabel("Marketing Budget")
plt.legend(loc = 'best')

marketing_budget_line_path_ = os.path.join("result_country", "avg_marketing_budget_line_comparison.png")
plt.savefig(marketing_budget_line_path_)


# 6. Relationship between "Marketing Budget" and "Social Media Followers"

# In[30]:


# Load a dataset
restaurant_df[["Marketing Budget", "Social Media Followers"]].head()


# In[31]:


# Create a scatter plot to see relationship between "Marketing Budget" and "Social Media Followers"
x_values = restaurant_df["Marketing Budget"]
y_values = restaurant_df["Social Media Followers"]

(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope, 2)) + "x + " + str(round(intercept, 2))

plt.scatter(x_values, y_values, color = 'blue', alpha = 0.1)
plt.plot(x_values, regress_values, color = 'red')
plt.annotate(line_eq, (5000, 20000), fontsize = 15, color = "red")

plt.title("Relationship between Marketing Budget and Social Media Followers")
plt.xlabel("Marketing Budget")
plt.ylabel("Social Media Followers")

print(f"r-squared: {rvalue ** 2}")

marketing_followers_scatter_path = os.path.join("result_country", "marketing_followers_scatter.png")
plt.savefig(marketing_followers_scatter_path)


# 7. Relationship between "Rating" and "Revenue"

# In[32]:


# Load a dataset
restaurant_df[["Rating", "Revenue"]].head()


# In[33]:


# Create a scatter plot to see relationship between "Rating" and "Revenue"
x_values = restaurant_df["Rating"]
y_values = restaurant_df["Revenue"]

(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope, 2)) + "x + " + str(round(intercept, 2))

plt.scatter(x_values, y_values, color = 'blue', alpha = 0.1)
plt.plot(x_values, regress_values, color = 'red')
plt.annotate(line_eq, (3.75, 1470000), fontsize = 15, color = "red")

plt.title("Relationship between Rating and Revenue")
plt.xlabel("Rating")
plt.ylabel("Revenue")

print(f"r-squared: {rvalue ** 2}")

rating_revenue_scatter_path = os.path.join("result_country", "rating_revenue_scatter.png")
plt.savefig(rating_revenue_scatter_path)


# 8. Relationship between "Marketing Budget" and "Revenue"

# In[34]:


# Load a dataset
restaurant_df[["Marketing Budget", "Revenue"]].head()


# In[35]:


# Create a scatter plot to see relationship between "Marketing Budget" and "Revenue"
x_values = restaurant_df["Marketing Budget"]
y_values = restaurant_df["Revenue"]

(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope, 2)) + "x + " + str(round(intercept, 2))

plt.scatter(x_values, y_values, color = 'blue', alpha = 0.1)
plt.plot(x_values, regress_values, color = 'red')
plt.annotate(line_eq, (5000, 200000), fontsize = 15, color = "red")

plt.title("Relationship between Marketing Budget and Revenue")
plt.xlabel("Marketing Budget")
plt.ylabel("Revenue")

print(f"r-squared: {rvalue ** 2}")

marketing_revenue_scatter_path = os.path.join("result_country", "marketing_revenue_scatter.png")
plt.savefig(marketing_revenue_scatter_path)


# 9. Relationship between "Rating" and "Service Quality Score"

# In[36]:


# Load a dataset
restaurant_df[["Rating", "Service Quality Score"]].head()


# In[37]:


# Create a scatter plot to see relationship between "Rating" and "Service Quality Score"
x_values = restaurant_df["Rating"]
y_values = restaurant_df["Service Quality Score"]

(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope, 3)) + "x + " + str(round(intercept, 3))

plt.scatter(x_values, y_values, color = 'blue', alpha = 0.1)
plt.plot(x_values, regress_values, color = 'red')
plt.annotate(line_eq, (4.1, 10), fontsize = 15, color = "red")

plt.title("Relationship between Rating and Service Quality Score")
plt.xlabel("Rating")
plt.ylabel("Service Quality Score")

print(f"r-squared: {rvalue ** 2}")

rating_service_score_scatter_path = os.path.join("result_country", "rating_service_score_scatter.png")
plt.savefig(rating_service_score_scatter_path)


# 10. Relationship between "Rating" and "Ambience Score"

# In[38]:


# Load a dataset
restaurant_df[["Rating", "Ambience Score"]].head()


# In[39]:


# Create a scatter plot to see relationship between "Rating" and "Ambience Score"
x_values = restaurant_df["Rating"]
y_values = restaurant_df["Ambience Score"]

(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope, 2)) + "x + " + str(round(intercept, 2))

plt.scatter(x_values, y_values, color = 'blue', alpha = 0.1)
plt.plot(x_values, regress_values, color = 'red')
plt.annotate(line_eq, (4.25, 10), fontsize = 15, color = "red")

plt.title("Relationship between Rating and Ambience Score")
plt.xlabel("Rating")
plt.ylabel("Ambience Score")

print(f"r-squared: {rvalue ** 2}")

rating_ambience_score_scatter_path = os.path.join("result_country", "rating_ambience_score_scatter.png")
plt.savefig(rating_ambience_score_scatter_path)


# 11. Relationship between "Social Media Followers" and "Revenue"

# In[40]:


# Load a dataset
restaurant_df[["Social Media Followers", "Revenue"]].head()


# In[41]:


# Create a scatter plot to see relationship between "Social Media Followers" and "Revenue"
x_values = restaurant_df["Social Media Followers"]
y_values = restaurant_df["Revenue"]

(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope, 2)) + "x + " + str(round(intercept, 2))

plt.scatter(x_values, y_values, color = 'blue', alpha = 0.1)
plt.plot(x_values, regress_values, color = 'red')
plt.annotate(line_eq, (54000, 200000), fontsize = 15, color = "red")

plt.title("Relationship between Social Media Followers and Revenue")
plt.xlabel("Social Media Followers")
plt.ylabel("Revenue")

print(f"r-squared: {rvalue ** 2}")

follower_revenue_scatter_path = os.path.join("result_country", "follower_revenue_scatter.png")
plt.savefig(follower_revenue_scatter_path)


# 12. Relationship between "Service Quality Score" and "Revenue"

# In[42]:


# Load a dataset
restaurant_df[["Service Quality Score", "Revenue"]].head()


# In[43]:


# Create a scatter plot to see relationship between "Service Quality Score" and "Revenue"
x_values = restaurant_df["Service Quality Score"]
y_values = restaurant_df["Revenue"]

(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope, 2)) + "x + " + str(round(intercept, 2))

plt.scatter(x_values, y_values, color = 'blue', alpha = 0.1)
plt.plot(x_values, regress_values, color = 'red')
plt.annotate(line_eq, (4, 1480000), fontsize = 15, color = "red")

plt.title("Relationship between Service Quality Score and Revenue")
plt.xlabel("Service Quality Score")
plt.ylabel("Revenue")

print(f"r-squared: {rvalue ** 2}")

service_score_revenue_scatter_path = os.path.join("result_country", "service_score_revenue_scatter.png")
plt.savefig(service_score_revenue_scatter_path)


# 13. Relationship between "Ambience Score" and "Revenue"

# In[44]:


# Load a dataset
restaurant_df[["Ambience Score", "Revenue"]].head()


# In[45]:


# Create a scatter plot to see relationship between "Ambience Score" and "Revenue"
x_values = restaurant_df["Ambience Score"]
y_values = restaurant_df["Revenue"]

(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope, 2)) + "x + " + str(round(intercept, 2))

plt.scatter(x_values, y_values, color = 'blue', alpha = 0.1)
plt.plot(x_values, regress_values, color = 'red')
plt.annotate(line_eq, (4, 1480000), fontsize = 15, color = "red")

plt.title("Relationship between Ambience Score and Revenue")
plt.xlabel("Ambience Score")
plt.ylabel("Revenue")

print(f"r-squared: {rvalue ** 2}")

ambience_score_revenue_scatter_path = os.path.join("result_country", "ambience_score_revenue_scatter.png")
plt.savefig(ambience_score_revenue_scatter_path)


# 14. Relationship between "Average Meal Price" and "Revenue"

# In[46]:


# Load a dataset
restaurant_df[["Average Meal Price", "Revenue"]].head()


# In[47]:


# Create a scatter plot to see relationship between "Average Meal Price" and "Revenue"
x_values = restaurant_df["Average Meal Price"]
y_values = restaurant_df["Revenue"]

(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope, 2)) + "x + " + str(round(intercept, 2))

plt.scatter(x_values, y_values, color = 'blue', alpha = 0.1)
plt.plot(x_values, regress_values, color = 'red')
plt.annotate(line_eq, (30, 1480000), fontsize = 15, color = "red")

plt.title("Relationship between Average Meal Price and Revenue")
plt.xlabel("Average Meal Price")
plt.ylabel("Revenue")

print(f"r-squared: {rvalue ** 2}")

price_revenue_scatter_path = os.path.join("result_country", "price_revenue_scatter.png")
plt.savefig(price_revenue_scatter_path)


# 15. Relationship between "Weekday Reservations" and "Revenue"

# In[48]:


# Load a dataset
restaurant_df[["Weekday Reservations", "Revenue"]].head()


# In[49]:


# Create a scatter plot to see relationship between "Weekday Reservations" and "Revenue"
x_values = restaurant_df["Weekday Reservations"]
y_values = restaurant_df["Revenue"]

(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope, 2)) + "x + " + str(round(intercept, 2))

plt.scatter(x_values, y_values, color = 'blue', alpha = 0.1)
plt.plot(x_values, regress_values, color = 'red')
plt.annotate(line_eq, (36, 140000), fontsize = 15, color = "red")

plt.title("Relationship between Weekday Reservations and Revenue")
plt.xlabel("Weekday Reservations")
plt.ylabel("Revenue")

print(f"r-squared: {rvalue ** 2}")

weekday_revenue_scatter_path = os.path.join("result_country", "weekday_revenue_scatter.png")
plt.savefig(weekday_revenue_scatter_path)


# 16. Relationship between "Weekend Reservations" and "Revenue"

# In[50]:


# Load a dataset
restaurant_df[["Weekend Reservations", "Revenue"]].head()


# In[51]:


# Create a scatter plot to see relationship between "Weekend Reservations" and "Revenue"
x_values = restaurant_df["Weekend Reservations"]
y_values = restaurant_df["Revenue"]

(slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
line_eq = "y = " + str(round(slope, 2)) + "x + " + str(round(intercept, 2))

plt.scatter(x_values, y_values, color = 'blue', alpha = 0.1)
plt.plot(x_values, regress_values, color = 'red')
plt.annotate(line_eq, (36, 140000), fontsize = 15, color = "red")

plt.title("Relationship between Weekend Reservations and Revenue")
plt.xlabel("Weekend Reservations")
plt.ylabel("Revenue")

print(f"r-squared: {rvalue ** 2}")

weekend_revenue_scatter_path = os.path.join("result_country", "weekend_revenue_scatter.png")
plt.savefig(weekend_revenue_scatter_path)


# 17. Relationship between "Weekend Reservations", "Weekday Reservations" and "Revenue"

# In[52]:


# Create a scatter plot to see relationship between "Weekday Reservations", "Weekend Reservations" and "Revenue"
plt.scatter(restaurant_df["Weekend Reservations"], restaurant_df["Revenue"], color = 'blue', alpha = 0.05)
plt.scatter(restaurant_df["Weekday Reservations"], restaurant_df["Revenue"], color = 'red', alpha = 0.05)

plt.title("Relationship between Weekend, Weekday Reservations and Revenue")
plt.xlabel("Weekend, Weekday Reservations")
plt.ylabel("Revenue")

week_day_end_revenue_scatter_path = os.path.join("result_country", "week_day_end_revenue_scatter.png")
plt.savefig(week_day_end_revenue_scatter_path)


# In[ ]:




