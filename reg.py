# -*- coding: utf-8 -*-

from datetime import datetime
start_time = datetime.now()
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
import json
def get_data(file_name):
	
        x_parameter=[]
	y_parameter=[]
	f = open('try1.json')
	data = json.load(f)
	for key in data.keys(): 
		print key
		x_parameter.append(int(key))
		

	print x_parameter


	for key,value in data.items():
		print value
		y_parameter.append(int(value))

	print y_parameter
        	
	x=np.array(x_parameter).astype(np.float)
	print x
	x = np.array(x).reshape((len(x), 1))
	#x = scaler.transform(x)
	y=np.array(y_parameter).astype(np.float)
	print y
	y = np.array(y).reshape((len(y), 1))
	#y = scaler.transform(y)

	return x,y

def linear_model_main(X_parameters,Y_parameters,predict_value):
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    predict_outcome = regr.predict(predict_value)
    predictions = {}
    predictions['intercept'] = regr.intercept_
    predictions['coefficient'] = regr.coef_
    predictions['predicted_value'] = predict_outcome
    return predictions

def show_linear_line(X_parameters,Y_parameters):
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    plt.scatter(X_parameters,Y_parameters,color='blue')
    plt.plot(X_parameters,regr.predict(X_parameters),color='red',linewidth=4)
    plt.xticks(())
    plt.yticks(())
    plt.show()

x1,y1 = get_data('try1.json')
predict_value = 35
result = linear_model_main(x1,y1,predict_value)
print "Intercept value " , result['intercept']
print "coefficient" , result['coefficient']
print "Predicted value: ",result['predicted_value']

#end_time = datetime.now()
#print('Duration: {}'.format(end_time - start_time))
show_linear_line(x1,y1)


