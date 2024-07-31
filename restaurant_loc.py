#!/usr/bin/env python
# coding: utf-8

# In[49]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# In[50]:


# Load the restaurant data
csv_file = os.path.join("resources", "restaurant_data.csv")

restaurant_df = pd.read_csv(csv_file, encoding = 'utf-8')
restaurant_df.head(10)


# In[51]:


# Check for missing data
restaurant_df.count()


# In[52]:


# Check data types
restaurant_df.dtypes


# In[53]:


# Create a location list for x-axis
location_list = ["Downtown", "Rural", "Suburban"]


# 1. Average "Revenue" comparison by each "Location"

# In[54]:


# Group with "Location" by each countries with average "Revenue"
group0 = restaurant_df.groupby(["Location"])
group0 = group0[["Revenue"]].mean()
group0


# In[55]:


# Create a "Revenue" list 
revenue = group0["Revenue"].tolist()
revenue


# In[56]:


# Create a bar chart comparing average "Revenue" by "Location"
plt.bar(location_list, revenue, color = 'blue', alpha = 0.25)

plt.title("Comparison between location (Average Revenue)")
plt.xlabel("Cuisine by location")
plt.ylabel("Average Revenue")

revenue_bar_path = os.path.join("result_loc", "avg_revenue_bar_comparison.png")
plt.savefig(revenue_bar_path)


# In[57]:


# Create a pie chart comparing average "Revenue" by "Location"
colors = ["lightblue", "orange", "pink"]
explode = (0.1, 0, 0)
figure = revenue

plt.pie(figure, labels = location_list, colors = colors, explode = explode, 
        shadow = True, autopct = '%.1f%%', startangle = 320)
plt.title("Comparison between location (Average Revenue)")

revenue_pie_path = os.path.join("result_loc", "avg_revenue_pie_comparison.png")
plt.savefig(revenue_pie_path)


# In[58]:


# Create a line graph comparing average "Revenue" by "Location"
plt.figure(figsize = (8, 4))
plt.plot(location_list, revenue, marker = 'o', color = 'red', label = "Revenue", alpha = 0.5)

plt.title("Comparison between location (Revenue)")
plt.xlabel("Cuisine by location")
plt.ylabel("Average Revenue")
plt.legend(loc = 'best')

revenue_line_path = os.path.join("result_loc", "avg_revenue_line_comparison.png")
plt.savefig(revenue_line_path)


# 2. Average "Ambience Score" comparison by each "Location"

# In[59]:


# Group with "Location" by each countries with average "Ambience Score"
group1 = restaurant_df.groupby(["Location"])
group1 = group1[["Ambience Score"]].mean()
group1


# In[60]:


# Create a "Ambience Score" list 
ambience = group1["Ambience Score"].tolist()
ambience


# In[61]:


# Create a bar chart comparing average "Ambience Score" by "Location"
plt.bar(location_list, ambience, color = 'blue', alpha = 0.25)

plt.title("Comparison between location (Average Ambience Score)")
plt.xlabel("Cuisine by location")
plt.ylabel("Average Ambience Score")

ambience_bar_path = os.path.join("result_loc", "avg_ambience_bar_comparison.png")
plt.savefig(ambience_bar_path)


# In[62]:


# Create a pie chart comparing average "Ambience Score" by "Location"
colors = ["lightblue", "orange", "pink"]
explode = (0, 0.1, 0)
figure = ambience

plt.pie(figure, labels = location_list, colors = colors, explode = explode, 
        shadow = True, autopct = '%.1f%%', startangle = 220)
plt.title("Comparison between location (Average Ambience Score)")

ambience_pie_path = os.path.join("result_loc", "avg_ambience_pie_comparison.png")
plt.savefig(ambience_pie_path)


# In[63]:


# Create a line graph comparing average "Ambience Score" by "Location"
plt.figure(figsize = (8, 4))
plt.plot(location_list, ambience, marker = 'o', color = 'red', label = "Average Ambience Score", alpha = 0.5)

plt.title("Comparison between location (Average Ambience Score)")
plt.xlabel("Cuisine by location")
plt.ylabel("Average Ambience Score")
plt.legend(loc = 'best')

ambience_line_path = os.path.join("result_loc", "avg_ambience_line_comparison.png")
plt.savefig(ambience_line_path)


# 3. Average "Service Quality Score" comparison by each "Location"

# In[64]:


# Group with "Location" by each countries with average "Service Quality Score"
group2 = restaurant_df.groupby(["Location"])
group2 = group2[["Service Quality Score"]].mean()
group2


# In[65]:


# Create a "Service Quality Score" list 
service_score = group2["Service Quality Score"].tolist()
service_score


# In[66]:


# Create a bar chart comparing average "Service Quality Score" by "Location"
plt.bar(location_list, service_score, color = 'blue', alpha = 0.25)

plt.title("Comparison between location (Average Service Quality Score)")
plt.xlabel("Cuisine by location")
plt.ylabel("Average Service Quality Score")

service_score_bar_path = os.path.join("result_loc", "avg_service_score_bar_comparison.png")
plt.savefig(service_score_bar_path)


# In[67]:


# Create a pie chart comparing average "Service Quality Score" by "Location"
colors = ["lightblue", "orange", "pink"]
explode = (0, 0.1, 0)
figure = service_score

plt.pie(figure, labels = location_list, colors = colors, explode = explode, 
        shadow = True, autopct = '%.1f%%', startangle = 220)
plt.title("Comparison between location (Average Service Quality Score)")

service_score_pie_path = os.path.join("result_loc", "avg_service_score_pie_comparison.png")
plt.savefig(service_score_pie_path)


# In[68]:


# Create a line graph comparing average "Service Quality Score" by "Location"
plt.figure(figsize = (8, 4))
plt.plot(location_list, service_score, marker = 'o', color = 'red', label = "Average Service Quality Score", alpha = 0.5)

plt.title("Comparison between location (Average Service Quality Score)")
plt.xlabel("Cuisine by location")
plt.ylabel("Average Service Quality Score")
plt.legend(loc = 'best')

service_score_line_path = os.path.join("result_loc", "avg_service_score_line_comparison.png")
plt.savefig(service_score_line_path)


# In[71]:


# Group with "Location" by each countries with average "Service Quality Score" and "Ambience Score"
group3 = restaurant_df.groupby(["Location"])
group3 = group3[["Service Quality Score", "Ambience Score"]].mean()
group3


# In[72]:


# Create a line graph comparing average "Service Quality Score" and "Ambience Score" by "Location"
plt.figure(figsize = (8, 4))
plt.plot(location_list, service_score, marker = 'o', color = 'red', label = "Average Service Quality Score", alpha = 0.5)
plt.plot(location_list, ambience, marker = 'o', color = 'blue', label = "Average Ambience Score", alpha = 0.5)

plt.title("Comparison between location (Average Service Quality Score VS Average Ambience Score)")
plt.xlabel("Cuisine by location")
plt.ylabel("Average Score")
plt.legend(loc = 'best')

service_ambience_score_line_path = os.path.join("result_loc", "avg_service_ambience_score_line_comparison.png")
plt.savefig(service_ambience_score_line_path)


# In[ ]:




