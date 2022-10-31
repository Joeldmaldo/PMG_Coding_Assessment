
# PMG Programming Challenge

Program that will take several CSV files as arguments on the command line. 
This script will output a new CSV file to stdout that will contain all of 
the rows from each of the files and will additionally include a column filename
which will contain the name of the file where the row was added from.


Given two input files it will generate the following:

## File#1
|email_hash|category|
|----------|--------|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Shirts|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Pants|
|166ca9b3a59edaf774d107533fba2c70ed309516376ce2693e92c777dd971c4b|Cardigans|

## File#2
|email_hash|category|
|----------|--------|
|176146e4ae48e70df2e628b45dccfd53405c73f951c003fb8c9c09b3207e7aab|Wallets|
|63d42170fa2d706101ab713de2313ad3f9a05aa0b1c875a56545cfd69f7101fe|Purses|


## Output
|email_hash|category|filename|
|----------|--------|--------|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Shirts|clothing.csv|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Pants|clothing.csv|
|166ca9b3a59edaf774d107533fba2c70ed309516376ce2693e92c777dd971c4b|Cardigans|clothing.csv|
|176146e4ae48e70df2e628b45dccfd53405c73f951c003fb8c9c09b3207e7aab|Wallets|accessories.csv|
|63d42170fa2d706101ab713de2313ad3f9a05aa0b1c875a56545cfd69f7101fe|Purses|accessories.csv|


# Language and tools used:
- Python 3.10.7 
- Libraries:
    - pandas
    - os
    - unittest
    - sys

## Usage/Examples

### CSV_Combiner_challenge.py:

python CSV_Combiner_challenge ./fixtures/clothing.csv ./fixtures/accessories.csv >combined.csv

### CSVCombinerTester

python -m unittest CSVCombinerTester.py 