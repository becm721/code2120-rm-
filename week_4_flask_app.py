# A very simple Flask Hello World app for you to get started with...

from logging import exception
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask! and testing'

@app.route('/np_addMatrix')
def np_addMatrix():
    import numpy as np
    import pandas as pd
    from ast import Lambda

    args=request.args
    variables = dict(args) 

    #Deserialisation
    variables["m1"]=variables["m1"].split(",")
    variables["m2"]=variables["m2"].split(",") 

    variables["m1"]=list(map(lambda x:float(x), variables["m1"]))
    variables["m2"]=list(map(lambda x:float(x), variables["m2"])) 
        
    matrix1=np.array(variables["m1"]).reshape((int(variables["m1_y"]),int(variables["m1_x"])))
    matrix2=np.array(variables["m2"]).reshape((int(variables["m2_y"]),int(variables["m2_x"])))
    #print(matrix1)
    #print(matrix2) 

    #ACTUAL FUNCTION
    result=np.add(matrix1,matrix2) 

    #Serialisation
    data=pd.DataFrame(result)

    data.to_csv() 
    return str(data)




def main():
    app.run()

if __name__ == '__main__':
    main()

