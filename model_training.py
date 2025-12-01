from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def train_model(df):
    X=df[['Quantity','Discount','BasePrice']]
    y=df['Sales']
    X_train,X_test,y_train,y_test=train_test_split(X,y)
    model=RandomForestRegressor().fit(X_train,y_train)
    return model
