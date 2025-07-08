# train_model.py

import pandas as pd
import numpy as np
import pickle
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression

# Sample dataset
data = {
    'age': [25, np.nan, 35, 28, 52],
    'salary': [50000, 60000, np.nan, 58000, 62000],
    'city': ['New York', 'Los Angeles', 'New York', np.nan, 'Chicago'],
    'purchased': ['Yes', 'No', 'Yes', 'No', 'Yes']
}
df = pd.DataFrame(data)

# Split X and y
X = df.drop(columns='purchased')
y = df['purchased'].map({'Yes': 1, 'No': 0})  # encode labels

# Preprocessing
categorical_cols = X.select_dtypes(include='object').columns.tolist()
numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()

num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])
cat_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer([
    ('num', num_pipeline, numerical_cols),
    ('cat', cat_pipeline, categorical_cols)
])

# Full pipeline
model_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression())
])

# Train
model_pipeline.fit(X, y)

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model_pipeline, f)

print("Model trained and saved as model.pkl")
