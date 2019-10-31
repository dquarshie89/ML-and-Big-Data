import kaggle, zipfile
import pandas as pd, pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Imputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix

#This python file will use a user's Kaggle info to download the train and test files
#The user must have a Kaggle account and get the API token here: https://www.kaggle.com/<username>/account
#Aftet getting the token it must be moved to the /.kaggle folder. This was done using terminal and the mv command

#This command authenticates thr user's Kaggle account
kaggle.api.authenticate()

#This downloads the Titanic train and test data in a zip file
kaggle.api.competition_download_files('Titanic')


#Unzip the 2 CSVs
with zipfile.ZipFile("Titanic.zip", 'r') as zip_ref:
    zip_ref.extractall("")

#Save the train dataset as a dataframe and show the first 5 lines
train = pd.read_csv("train.csv")
print('\nSample of train data\n')
print(train.head(5))

#Save the test dataset as a dataframe and show the first 5 lines
print('\nSample of test data\n')
test = pd.read_csv("test.csv")
print(test.head(5))

#Random Forest Classification 
def RFC(X, y):
    try:
        #Set up RFC to imputate by setting missing values to the median for the population
        imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
        rfc = RandomForestClassifier(max_depth=10, min_samples_split=2, n_estimators=100, random_state=1)
        steps = [('imputation', imputer), ('random_forest', rfc)]
        pipeline = Pipeline(steps)

        #Create a 70-30 split 
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=55)
        X_test.to_csv('X_test.csv')
        y_test.to_csv('y_test.csv')

        #Build the model
        model = pipeline.fit(X_train, y_train)
    except:
        #Display if there's an error
        print("Error. Please check the data or RFC setup.")
    return(model)

#Read the train data
df = pd.read_csv("train.csv")
#Drop unneeded variables
df = df.drop(['Name', 'Cabin', 'Ticket'], axis=1)
#Drop nulls
df = df.dropna(subset=['Embarked'], how='all')

#Make categorical variables dummy variables 
dummies = pd.get_dummies(df)
#Drop unneeded columns from tbe dummy dataframe
dummies = dummies.drop(['Sex_female', 'Embarked_C'], axis=1)

# Assign X and y
y = dummies['Survived']
X = dummies.drop('Survived', axis=1)

#Run RFC and store in a pickle file
model = RFC(X,y)
p = open('model.pkl', 'wb')
pickle.dump(model, p)
p.close()

#Open pickle file
def read_pickle(file):
    try:
        p = open(file, 'rb')
        open_pickle = pickle.load(p)
    except:
        print("Cannot open file. Please run train_model.py first.", file)
    return(open_pickle)

#Make test data the same as train by removing columns and making categorical variables dummy variables 
def get_test_df(df):
    df = df.drop(['Name', 'Cabin', 'Ticket'], axis=1)
    dum = pd.get_dummies(df)
    dum = dum.drop(['Sex_female', 'Embarked_C'], axis=1)
    return(dum)



#Input test data and drop unneeded columns
test_df = pd.read_csv("test.csv")
X_test = pd.read_csv("X_test.csv")
y_test = pd.read_csv("y_test.csv")
X_test.drop(X_test.columns[[0]], axis=1, inplace=True)
y_test.drop(y_test.columns[[0]], axis=1, inplace=True)
X_test.drop(X_test.index[0], inplace=True)

#Input the pickle file 
model = read_pickle('model.pkl')

#Accuracy score of model
accuracy_score = model.score(X_test, y_test)

#Make the test data format be the same as training so that we can run the model
pred_df = get_test_df(test_df)

#Run prediction on X test
y_pred = model.predict(X_test)

#Run prediction on new test format
test_pred = model.predict(pred_df)
test_pred = pd.DataFrame(test_pred, columns = ['Survived']) 

#Add Predictions to test data
test_df = test_df.join(test_pred)

#Make theclassification report
class_report = classification_report(y_test, y_pred)

#Make the confusion matrix
confmatrix = confusion_matrix(y_test, y_pred)

#Final outputs
print("\nModel accuracy score:")
print(accuracy_score)
print("\nModel confusion matrix:")
print(confmatrix, sep = ' ')
print("\nClassification report:\n")
print(class_report)

#Export predictions to CSV
test_df.to_csv (r'Titanic_Predictions.csv', index = None, header=True)
