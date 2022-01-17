import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model



def predict():
    data = pd.read_csv("hr_data.cvs", sep=";")
    # removed =
    data = data[["resting_heart_rate", "injury", "activity", "day", "sick", "sleep", "sleep_score", "body_battery", "stress", "heart_rate_high", "calories_burnt"]]

    predict = "resting_heart_rate"

    x = np.array(data.drop([predict], 1))
    y = np.array((data[predict]))

    x_test, x_train, y_test, y_train = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)

    print(acc * 100,"% accuracy")
    predictions = linear.predict(x_test)
    print("----------------------------------------------")
    print("----------------------------------------------")
    print("Prediction      Result          Difference")
    for x in range(len(predictions)):
        print(int(predictions[x]), "            ", y_test[x], "            ", y_test[x] - int(predictions[x]))
    print("----------------------------------------------")
    print("----------------------------------------------")

def log():

    #User input
    activity = input("Have you done activity today (Yes[1]/No[0])\n>")
    if activity == "Yes":
        activity = "1"
    elif activity == "No":
        activity = "0"
    elif activity == "0":
        activity = activity
    elif activity == "1":
        activity = activity
    else:
        print("Enter a valid option")
        log()
    day = input("How many days since you last physical activity?\n>")
    injury = input("Are you currently injured (Yes/No)?\n>")
    if injury == "Yes":
        injury = "1"
    elif injury == "No":
        injury = "0"
    elif injury == "0":
        injury = injury
    elif injury == "1":
        injury = injury
    else:
        print("Enter a valid option")
        log()
    sick = input("Are you currently feeling Sick (Yes/No)?\n>")
    if sick == "Yes":
        sick = "1"
    elif sick == "No":
        sick = "0"
    elif sick == "0":
        sick = sick
    elif sick == "1":
        sick = sick
    else:
        print("Enter a valid option")
        log()
    sleep = input("How many hours did you sleep last night?\n>")
    sleep_score = input("What sleep score did you achieve last night?\n>")
    body_battery = input("What body battery did you achieve?\n>")
    stress = input("What was your stress level?\n>")
    heart_rate_high = input("What was you max HR?\n>")
    resting_heart_rate = input("What was your resting HR\n>")
    calories_burnt = input("How many calories have you burnt actively?\n>")

    #Update Data
    f = open("hr_data.cvs", "a")
    f.write(activity + ";" + day + ";" + injury + ";" + sick + ";" + sleep + ";" + sleep_score + ";" + body_battery + ";" + stress + ";" + heart_rate_high + ";" + resting_heart_rate + ";" + calories_burnt)

    #Completion
    print("-----------------------")
    print("-----------------------")
    print("Data Updated")
    exit()

def main():
    log_predict = input("Would you like to Log data or predict your resting HR (Log/Predict)\n>")
    if log_predict == "Log":
        log()
    elif log_predict == "L":
        log()
    elif log_predict == "l":
        log()
    elif log_predict == "log":
        log()
    elif log_predict == "Predict":
        predict()
    elif log_predict == "P":
        predict()
    elif log_predict == "p":
        predict()
    elif log_predict == "predict":
        predict()
    else:
        print("Enter a valid option")
        main()

if __name__ == '__main__':
    main()





"""

Description

activity;day;injury;sick;sleep;sleep_score;body_battery;stress;heart_rate_high;resting_heart_rate;calories_burnt

day = days since last exercised
activity = yes(1) or no (0)
injury = yes(1) or no (0)
sick = yes(1) or no (0)
sleep = hours
sleep_score = garmin sleep score
body_battery = garmin body battery
stress = garmin stress reading
heart_rate_high = highest HR in day
resting_heart_rate = resting HR for that day
calories_burnt = calories burnt activily

"""