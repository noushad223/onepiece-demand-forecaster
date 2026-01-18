import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("onepiece_tracker.csv")
df_lr = df.dropna().copy()  # use non 0 rows for prediction

# Using independent variables to predict member count
X = df_lr[["scored_by_change", "favourites_change"]]
y = df_lr[["member_change"]]

# 80-20 train,test split
if len(df_lr) > 4:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = LinearRegression()
    model.fit(X_train, y_train)
else:
    model = LinearRegression()
    model.fit(X, y)

current_engagement = pd.DataFrame(
    [[df_lr["scored_by_change"].iloc[-1], df_lr["favourites_change"].iloc[-1]]],
    columns=["scored_by_change", "favourites_change"],
)
predicted_growth = model.predict(current_engagement)[0][0]
print(f"Based on engagement, expected growth was: {predicted_growth:.2f}")
print(f"Actual growth was: {df_lr['member_change'].iloc[-1]}")
