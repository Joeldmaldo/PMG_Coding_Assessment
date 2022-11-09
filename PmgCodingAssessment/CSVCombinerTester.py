""" 
Author: Joel Maldonado
Filename: CSV_Combiner_challenge.py
Code purpose:
Program which will take the CSV_Combiner_challenge.py file and test its fucntionality.

"""


# import the libraries we'll be using

import os
import sys
import pandas
import unittest
from io import StringIO
from CSV_Combiner_challenge import CSVFileCombiner

""" 
Create our TestCombiner class which will do the follwoing:

    startClass():
    This function will be used to redirect the given output to our designated testOutput.csv
    
    If any of these fail and error message will be displayed

    fileCombiner(): 
    Will take itself and the list of arguments that were passed in the command line.
    Here we will use the pandas library to read and work with the csv files.

    tearDownClass():
    Is a method that is used for unittest. This class method will be called after
    test in an individual class have finished executing. It also has to be decorated
    as a classmethod() in order for it to work.

    setUp():
    Method used for unittest. It is used to prepare the test fixtures and is called before
    calling the test method.

    tearDown():
    Method used for unittest which is called after the test method in order to clean up after
    the testing concludes.

    testNoArgumentsPassed():
    Is used as to test whether arguments were passed on the command line or not against our funciton in our CSVCombinerTester

    testFindingFiles():
    Is used to test whether the files that are being passed as arguments actually exists.

    testAllValuesCombined():
    Verifies if all the values were passed on to the final csv file

"""
class TestCombiner(unittest.TestCase):

    # variables that will be used throught the test which contain testing file paths and file we will create for testing
    combine = CSVFileCombiner()
    combinerPath = "./CSV_Combiner_challenge.py"
    clothesPath = "./fixtures/clothing.csv"
    accessoriesPath = "./fixtures/accessories.csv"
    outputPath = "./testOutput.csv"
    emptyFile = "./test_fixtures/empty.csv"
    testOutput = open(outputPath, "w+")

    backup = sys.stdout

    #our startClass that is decorated as a classmethod since this is our setUpClass method which will set up our class
    @classmethod
    def startClass(cls):
        sys.stdout = cls.testOutput

    #Must also be decorated and is called after test in an individual class have run.    
    @classmethod
    def tearDownClass(cls):
        cls.testOutput.close()

   #we define our function that is used to prepare the test fixtures and this is called
   # immediately before calling the method.
    def setUp(self):

        self.output = StringIO()
        sys.stdout = self.output
        self.testOutput = open(self.outputPath,"w+")
        # redirect output

    def tearDown(self):
        self.testOutput.close()
        self.testOutput = open(self.outputPath,"w+")
        sys.stdout = self.backup
        self.testOutput.truncate(0)
        self.testOutput.write(self.output.getvalue())
        self.testOutput.close()


    def testNoArgumentsPassed(self):
        argv = [self.combinerPath]
        self.combine.fileCombiner(argv)

        self.assertIn("No file paths were placed as arguments", self.output.getvalue())

    def testFindingFiles(self):
        argv = [self.combinerPath, "fake.csv"]
        self.combine.fileCombiner(argv)


    def testAllValuesCombined(self):
        argv = [self.combinerPath, self.clothesPath, self.accessoriesPath]
        self.combine.fileCombiner(argv)

        self.testOutput.write(self.output.getvalue())
        self.testOutput.close()

        clothesDataFrame = pandas.read_csv(filepath_or_buffer=self.clothesPath, lineterminator='\n')
        accessoriesDataFrame = pandas.read_csv(filepath_or_buffer=self.accessoriesPath, lineterminator='\n')

        with open(self.outputPath) as file:
            jointDataFrame = pandas.read_csv(file, lineterminator='\n')
        self.assertEqual(len(jointDataFrame.merge(clothesDataFrame)),len(clothesDataFrame))
        self.assertEqual(len(jointDataFrame.merge(accessoriesDataFrame)),len(accessoriesDataFrame))
