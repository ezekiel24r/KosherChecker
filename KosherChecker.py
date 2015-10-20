"""
    KosherChecker, written by Eric Rensel
    Class: 375-01 Computers & Society with Sander Eller
    Info: Given a filename, KosherChecker looks for any words in the file that are considered not kosher,
        and returns the Kosher-status of the text
"""

import re  # used for search function

# create a list of non-kosher items
notKosher = ["pig", "pigs", "pork", "ham", "hams", "bacon", "swine", "swines", "hog", "hogs", "boar", "boars"]

# infinitely look for program input
while True:
    # grab filename from user
    filename = input("Enter the name of the file you would like to analyze: ")

    notKosherFlag = False  # flag used for conditional statement later on

    # try loop used so that if the file is not found the program will still run
    try:
        with open(filename, "r") as file:
            fileData = file.read()  # file is loaded into fileData string
        file.close()
    except FileNotFoundError:
        print("File Not Found")
        continue  # continue brings the program to the start of the while loop

    # string is put into lower case for comparison
    fileData = fileData.lower()

    found = ""
    for term in notKosher:  # for each term in notKosher list
        """
        this next line searches for the term and ensures it isn't part of a bigger word (i.e. boar vs board)
        """
        if re.search(r"\b" + re.escape(term) + r"\b", fileData):
            found = term # save the term that matched
            notKosherFlag = True  # file is not kosher
            break  # stop searching

    if notKosherFlag:
        print("NOT KOSHER, CONTAINS: " + found.upper())  # uppercase for dramatic effect
    else:
        print("CERTIFIED KOSHER")