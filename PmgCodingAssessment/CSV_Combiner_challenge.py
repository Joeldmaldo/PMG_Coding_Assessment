""" 
Author: Joel Maldonado
Filename: CSV_Combiner_challenge.py
Code purpose:
Program which will take csv files given as command line arguments
and will output a new CSV file on the console, 
which will contain a new column with the filename.
This can be used as well to generate a new csv file containing the merged and added information.

"""


# import the libraries we'll be using

import os
import sys
import pandas

""" 
Create our CSVFileCombiner class which will have two main functions:

    verifyFilePath:
    This function will take itself and the arguments that were passed on the command line.
    This will be used in order to verify 
    1) if csv files were passed as arguments
    2) if the csv file or file path is valid
    
    If any of these fail and error message will be displayed

    fileCombiner: 
    Will take itself and the list of arguments that were passed in the command line.
    Here we will use the pandas library to read and work with the csv files.

"""


class CSVFileCombiner:
    def fileCombiner(self, argv: list):

        # get the file arguments given in the command line

        # flag for the use of our header
        header = True

        # list which will hold the data our new combined CSV will have
        newCSV = []

        # value to use in the chunksize value of .read_csv to prevent memory problems
        handleMemory = 10**7

        # call our funtion in order to verify if files are found
        if self.verifyFilePath(argv):

            """
            Nested for loop for each file that was passed.
            Inner loop will read file data,get the filenames and
            append the data to our list
            """
            # get the file arguments given in the command line
            inputFiles = argv[1:]
            
            for files in inputFiles:

                for data in pandas.read_csv(files, chunksize=handleMemory):
                    fileName = os.path.basename(files)
                    data["filename"] = fileName
                    newCSV.append(data)

            # final for loop in order to print out our data in a csv format
            for paths in newCSV:
                print(
                    paths.to_csv(index=False, header=header, lineterminator="\n",chunksize=handleMemory),
                    end="",
                )
                header = False

        else:
            #print("Error while running code")
            return

    def verifyFilePath(self, arguments):

        # if to verify if any inputs were passed. Starts at 0 because argv was modified
        if len(arguments) <= 1:
            print("No file paths were placed as arguments.")
            #print("Code runs as so: ")
            #print("python csvCombiner.py ./fixtures/accessories.csv >combined.csv")

            return False

        # Now we want to verify if we can find the files that were passed as arguments

        for paths in arguments:
            if os.path.exists(paths) == False:
                print("The file was not found")
                return False

        return True


combiner = CSVFileCombiner()
combiner.fileCombiner(sys.argv)
