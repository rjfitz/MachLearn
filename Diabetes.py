#!/usr/bin/env python3

###		IMPORT PACKAGES
import numpy as np
import os.path
from pandas import read_csv


###		USER DEFINE FUNCTIONS
def resultFileSetup(modelName):
	#Set up result file 
	resultDir = os.path.dirname(os.path.realpath(__file__)) + "/results"
	modelName = "/" + modelName +"_results"
	if not os.path.lexists(resultDir):
		os.makedirs(resultDir)
	ResultFile = open(resultDir+modelName+".txt", "w+")
	ResultFile.write("!	---	"+ modelName + "	---	!")
	return ResultFile

def processDataFile(filePath):
	#takes a csv file name in then reads it and seperates the datasets
		#need to make change to check that file exists or through error
	Data = np.array(read_csv(filePath))
	X = Data[:,:-1]
	y = Data[:,-1:]
	X_train, X_test, y_train, y_test = train_test_split(X, y)
	#remove dimension of y vectors
	y_test = np.squeeze(y_test)
	y_train = np.squeeze(y_train)
	return X_train, X_test, y_train, y_test


###		MAIN
def main():
	#Set Necassary Variables
	modelName = 'Diabetes_SVM'  # (datsetName)+(structure)+[class/regr]
	dataFilePath = '~/Personal/MachLearn/Data/Diabetes-Data'	#create file path to data
	ResultFile = resultFileSetup(modelName)	#load results file

	#load data
	#X_train, X_test, y_train, y_test = processDataFile(dataFilePath)

	Data = np.array(read_csv(dataFilePath))

	#start model
	print(Data)
	

	#evaluate model


	#Print that program ran successfully
	print("Program Ran successfully")
	
###		CALL MAIN
if __name__ == '__main__':
	main()

###END		END		END		END		END