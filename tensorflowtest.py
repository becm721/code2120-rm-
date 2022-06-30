from flask import Flask, request
app = Flask(__name__)

@app.route('/tensorflow')
def tensorflow_test():
    #Import Data
    import pandas as pd
    from sklearn.model_selection import train_test_split

    df = pd.read_csv('Churn.csv')

    X = pd.get_dummies(df.drop(['Churn', 'Customer ID'], axis=1))
    y = df['Churn'].apply(lambda x: 1 if x=='Yes' else 0)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

    y_train.head()

    #Import Dependencies
    from keras.models import Sequential, load_model
    from keras.layers import Dense

    from sklearn.metrics import accuracy_score

    #Build and Compile Model
    model = Sequential()
    model.add(Dense(units=32, activation='relu', input_dim=len(X_train.columns)))
    model.add(Dense(units=64, activation='relu'))
    model.add(Dense(units=1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='sgd', metrics='accuracy')

    #Fit, Predict and Evaluate
    model.fit(X_train, y_train, epochs=200, batch_size=32)

    y_hat = model.predict(X_test)
    y_hat = [0 if val < 0.5 else 1 for val in y_hat]

    accuracy_score(y_test, y_hat)

    #Saving and Reloading
    #model.save('tfmodel')
    #del model 
    model = load_model('tfmodel')
    return model

def main():
    app.run()

if __name__ == '__main__':
    main()