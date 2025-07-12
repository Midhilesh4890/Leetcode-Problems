# # # # import bisect

# # # # def solve(input, sorted_stream, target):
# # # #     # Insert element while maintaining sorted order
# # # #     bisect.insort(sorted_stream, input)

# # # #     # Check the entire sorted stream for any triplet that meets the simplified distance condition
# # # #     i = 0
# # # #     while i < len(sorted_stream) - 2:
# # # #         # Extract the potential triplet
# # # #         a, c = sorted_stream[i], sorted_stream[i + 2]
        
# # # #         # Check if the distance between the first and last in the triplet is less than target
# # # #         if abs(a - c) < target:
# # # #             # Triplet found that meets the condition
# # # #             triplet = sorted_stream[i:i+3]
# # # #             print("Triplet found:", triplet)

# # # #             # Remove these elements from the sorted stream
# # # #             del sorted_stream[i:i+3]
# # # #             # Continue checking from the current index as the list has been modified
# # # #             continue
        
# # # #         i += 1

# # # # # Main program loop
# # # # sorted_stream = []
# # # # target_distance = 3

# # # # while True:
# # # #     try:
# # # #         # Accept input from the user
# # # #         data = input("Enter a floating-point number (or type 'exit' to quit): ")
# # # #         if data.lower() == 'exit':
# # # #             break
# # # #         data = float(data)
# # # #         solve(data, sorted_stream, target_distance)
# # # #         print("Current stream state:", sorted_stream)
# # # #     except ValueError:
# # # #         print("Please enter a valid floating-point number or 'exit'.")

# # # # # Output the remaining elements in the stream after processing
# # # # print("Remaining elements in the stream after exit:", sorted_stream)


# # # Decompress Strings
# # # "3[b]2[bc]" -> "bbbbcbc"
# # # "3[x2[c]]" -> "xccxccxcc"
# # # "2[ab]3[cd]hf" -> ababcdcdcdhf"

# # # step1 : ']'

# # # stack = [(value , string)]

# # # pop the stack 

# # # res = ''

# # def solve(s):

# #     res = ''
# #     val = 0
# #     stack = [] # (val, res)

# #     for i in s:
# #         if i.isdigit(): val = 10 * val + int(i)
# #         elif i == ']': res = stack.pop() + stack.pop() * res
# #         elif i == '[':
# #             stack.extend([val, res])
# #             val = 0
# #             res = ''
# #         else:
# #             res += i 
# #     return res 
# # s = '3[x2[c[2][c][c[c[c[c[c]]]]]]]'
# # print(solve(s))


# # roman to integer 

# # I - 1, II - 2, IV, LIV IX X, XC, C, XL, CM

# def solve(s):
#     d = {"I" : 1, "V": 5, 'X': 10} # assume its already there 
#     res = 0

#     for a, b in zip(s, s[1:]):
#         if d[a] >= d[b]:
#             res += d[a]

#         else:
#             res -= d[a]
#         res += d[b]





















# # topological sort 

# # C depends on A and B (i.e., A and B must be installed before C).
# # B depends on D (i.e., D must be installed before B).
# # A depends on E (i.e., E must be installed before A).
# # D depends on E (i.e., E must be installed before D).

# # A, B, C, D, E 



# # # graph = [[]]

# # # C --> B --> D
# # # |           |
# # # A --> E ----

# # from collections import defaultdict
# # def solve(arr):
# #     graph = defaultdict(list)

# #     for a, b in arr:
# #         graph.append((a, b))

# #     print(graph)





# # arr = [[A, E], [D, E], [B, D], [C, A], [C, B]]
# # print(solve(arr))



# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score, adjusted_r2
# from sklearn.linear_model import cross_validation

# def seasonal_features(data):
#     ## add code based on the seasonality
#     # something groupby (aggreagtions)
#     return pd.DataFrame(data)

# def read_data(filepath):
#     """Reads CSV file into a pandas DataFrame."""
#     data == pd.read_csv(filepath)
#     return data

# def preprocess_data(data):
#     """Preprocess the data: Handle missing values and standardize features."""
#     data.fillna(data.median, inplace = True)
#     scaler = StandardScaler()
#     data_scaled = scaler.fit_transform(data.drop(columns=[data.columns[-1]]))
#     return pd.DataFrame(data_scaled)

# def feature_engineering(data):
#     # add more features from the initial features
#     data = seasonal_features(data)
#     # if the number of features are too high then go from PCA
#     # Implement PCA
#     return pd.DataFrame(data_scaled)
    
# def check_for_multicollineatiy(data):
#     # VIF : Variable Inflation Factor
#     # if a column has a factor of more than 10 then this highly correlated
#     # remove such functions
#     correlation_coefficient
#     return pd.DataFrame(data)

# def feature_selection(data):
#     # implement lasso -? feature selection

# def build_model(X_train, y_train):
#     model = LinearRegression
#     model.fit(X_train, y_train)
#     return model

# def cross_validation(X_train, X_validation):
#     # implement cross validation on train and validation set 

# def evaluate_model(model, X_test, y_test):
#     """Evaluates the model and prints metrics."""
#     predictions = model.predict(X_test)
#     print("Mean Squared Error:", mean_squared_error(y_test, predictions))



# # 100 

# # 70 train 
# # 10 validation 

# # 20 test 

# def main():
#     filepath = "data.csv"
#     data = read_data(filepath)
#     data = preprocess_data(data)
#     data = feature_engineering(data)
#     data = feature_selection(data)
#     train, test = train_test_split(data, test_size=0.2, shuffle=False, stratify)
#     X_train, y_train = train.iloc[:, :-1], train.iloc[:, -1]
#     X_test, y_test = test.iloc[:, :-1], test.iloc[:, -1]
#     X_train_processed = preprocess_data(X_train)
#     X_test_processed = preprocess_data(X_test)

#     model = build_model(X_train, y_train)
#     # k-fold cross validation
#     # hyperparameter tuning (less data : gridsearch, randomsearch)
#     # deep learning hyperopt (bayesian search)
#     evaluate_model(model, X_test_processed, y_test)
#     preds = model.predic(X_test_processed)
#     print("Predictions:", preds)

# main()

# # aaina.bajaj@salesforce.com
# # varun.2@salesforce.com


