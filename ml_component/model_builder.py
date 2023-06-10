# ml_component/model_builder.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def build_model(csv_file, target_column):
    # Load CSV data
    data = pd.read_csv(csv_file)
    
    # Split the data into features (X) and target (y)
    X = data.drop(target_column, axis=1)
    y = data[target_column]
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Evaluate the model
    score = model.score(X_test, y_test)
    
    return model, score
