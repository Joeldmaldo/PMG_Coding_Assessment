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
import CSV_Combiner_challenge


class TestCombiner(unittest.TestCase):

    # variables that will be used throught the test
    combine = CSV_Combiner_challenge
    combinerPath = "./CSV_Combiner_challenge.py"
    clothesPath = "./fixtures/clothes.csv"
    accessoriesPath = "./fixtures/accessories.csv"
    outputPath = "./testOutput.csv"
    testOutput = open(outputPath, "w+")

    def classSetup():

        self.output = StringIO()
        sys.stdout = self.output
        self.testOutput = open(self.OutputPath)
        # redirect output

    def testNoArgumentsPassed():
        argv = [self.combinerPath]
        self.combine.fileCombiner(argv)

        self.assertIn("No file paths were passed as arguments", self.output.getValue())

    def testFindingFiles():
        argv = [self.combinerPath, "fake.csv"]
        self.combine.fileCombiner(argv)

    def testAllValuesCombined(self):
        argv = [self.combinerPath, self.clothesPath, self.accessoriesPath]
        self.combine.fileCombiner(argv)

        self.testOutput.write(self.output.getvalue())
        self.testOutput.close()

        clothesDataFrame = pandas.read_csv(clothesPath, lineterminator="\n")
        accessoriesDataFrame = pandas.read_csv(accessoriesPath, lineterminator="\n")

        with open(self.OutputPath) as file:
            jointDataFrame = pandas.read_csv(file, lineterminator="\n")
        self.assertEqual(
            len(jointDataFrame.merge(clothesDataFrame)),
            len(jointDataFrame.drop_duplicates()),
        )
        self.assertEqual(
            len(jointDataFrame.merge(accessoriesDataFrame)),
            len(jointDataFrame.drop_duplicates()),
        )
