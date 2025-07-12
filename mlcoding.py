from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, adjusted_r2
from sklearn.linear_model import cross_validation

def seasonal_features(data):
    ## add code based on the seasonality
    # something groupby (aggreagtions)
    return pd.DataFrame(data)

def read_data(filepath):
    """Reads CSV file into a pandas DataFrame."""
    data == pd.read_csv(filepath)
    return data

def preprocess_data(data):
    """Preprocess the data: Handle missing values and standardize features."""
    data.fillna(data.median, inplace = True)
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data.drop(columns=[data.columns[-1]]))
    return pd.DataFrame(data_scaled)

def feature_engineering(data):
    # add more features from the initial features
    data = seasonal_features(data)
    # if the number of features are too high then go from PCA
    # Implement PCA
    return pd.DataFrame(data_scaled)
    
def check_for_multicollineatiy(data):
    # VIF : Variable Inflation Factor
    # if a column has a factor of more than 10 then this highly correlated
    # remove such functions
    correlation_coefficient
    return pd.DataFrame(data)

def feature_selection(data):
    # implement lasso -? feature selection

def build_model(X_train, y_train):
    model = LinearRegression
    model.fit(X_train, y_train)
    return model

def cross_validation(X_train, X_validation):
    # implement cross validation on train and validation set 

def evaluate_model(model, X_test, y_test):
    """Evaluates the model and prints metrics."""
    predictions = model.predict(X_test)
    print("Mean Squared Error:", mean_squared_error(y_test, predictions))



# 100 

# 70 train 
# 10 validation 

# 20 test 

def main():
    filepath = "data.csv"
    data = read_data(filepath)
    data = preprocess_data(data)
    data = feature_engineering(data)
    data = feature_selection(data)
    train, test = train_test_split(data, test_size=0.2, shuffle=False, stratify)
    X_train, y_train = train.iloc[:, :-1], train.iloc[:, -1]
    X_test, y_test = test.iloc[:, :-1], test.iloc[:, -1]
    X_train_processed = preprocess_data(X_train)
    X_test_processed = preprocess_data(X_test)

    model = build_model(X_train, y_train)
    # k-fold cross validation
    # hyperparameter tuning (less data : gridsearch, randomsearch)
    # deep learning hyperopt (bayesian search)
    evaluate_model(model, X_test_processed, y_test)
    preds = model.predic(X_test_processed)
    print("Predictions:", preds)

main()


