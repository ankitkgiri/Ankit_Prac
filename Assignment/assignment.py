import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df_meal=pd.read_csv("meal_info.csv")

df_meal.head()

df_center=pd.read_csv("fulfilment_center_info.csv")

df_center.head()


df_food= pd.read_csv("train.csv")
df_food.head()

df=pd.merge(df_center,df_food, on="center_id")
df=pd.merge(df,df_meal, on="meal_id")

table = pd.pivot_table(data=df,index='category',values='num_orders',aggfunc=np.sum)
#Create a dataframe having category and num_orders which has aggregated sum of each category


table.plot.bar()
plt.xticks(rotation=70) #rotates xticks by 70 deg
plt.xlabel("Food Items")
plt.ylabel("Quantity Sold")
plt.title("Most Popular Food")
fig=plt
fig.savefig("plot.png")
plt.show()


df["revenue"]=df["checkout_price"]*df["num_orders"]
df["month"]=df["week"]//4


month=[] 
month_order=[] 
month=df["month"]
month_order=df["revenue"]

week=[]
week_order=[]
week=df["week"]
week_order=df["revenue"]

d1={"week": week, "revenue" : week_order}
d1=pd.DataFrame(d1)
t1 = pd.pivot_table(data=d1,index='week',values='revenue',aggfunc=np.sum)
d1={"month": month, "revenue" : month_order}
d1=pd.DataFrame(d1)
t2 = pd.pivot_table(data=d1,index='month',values='revenue',aggfunc=np.sum)

fig, (ax1, ax2) = plt.subplots(1,2, figsize=(20,5))
ax1.set_title("Weekly revenue")
ax2.set_title("Monthly revenue")
ax1.xlabel=("Week")
ax2.xlabel=("month")
ax1.ylabel=("Revenue")
ax2.ylabel=("Revenue")
plt.tight_layout()
t1.plot(ax=ax1)
t2.plot(ax=ax2)