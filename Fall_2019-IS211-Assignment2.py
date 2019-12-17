"""
=====================
part 0 - Prerequisite
=====================
1. create github repository called IS211_Assignment2
2. Clone to local repository
==========================
Part 1 - Download the Data
==========================
1. Think about how to handle the problem.
    a. What is the goal?
    b. What is the best structure for the program?
    c. How will ou break the program into smaller steps?
==========================
Part 2 - Download the Data
==========================
1. Create function called downloadData that takes string called 'url.'
    a. Use urllib2 to download content at the url and return it to the
     caller.
==========================
part 3 - Process Data
==========================
1. Write a function called processData that takes the file's contents as the
 first parameter,
process it line by line, and returns a dictionary.
2. It should return a tuple consisting of the name and birthday.
    a. The birthday should be converted into a Datetime object
     ('dd/mm/yyy' format)
3. If the data is missing or incorrect (e.g. invalid date), it should be
placed on a log called assignment 2'
4. The log mess should sent an error level message which states error processing
line # for ID #."
==========================
part 4 - Display/User Input
==========================
1. Write a function called displayPerson that takes the first parameter, id as an integer
 and the second parameter as a dictionary called personData.
2. The function should return the name and birthday of the given user or
 display a message: Person # is <name>  with a birthday of <date>.
"""

import argparse
import datetime
import logging
import pprint
import urllib.request

logging.basicConfig(filename='error.log', level=logging.ERROR)
assignment2 = logging.getLogger()


# Reads and downloads data from url
def downloadData(url):
    return urllib.request.urlopen(url).readlines()


# Reads Data line by line, creates birthday datetime objects and returns a dictionary.
def processData(data):
    line_number = 0
    persons = {}
    for line in data:
       line_number += 1
       line = str(line)
       line = line.lstrip('b\'').rstrip('\\n\'')
       line = line.split(',')
       try:
           person_id, name = line[0], line[1]
           birthday = datetime.datetime.strptime(line[2], "%d/%m/%Y")
           persons[person_id] = (name, birthday)
       except ValueError:
            error_message ="Error processing line #{} for ID #{}.".format(line_number, person_id)
            logging.error(error_message)
            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint(error_message)
            continue
       return persons


def displayPerson(id, personData):
    found = 0
    for key,values in personData:
        if int(key) == id:
            print("Person #{} is {} with a birthday of {}.".format(personData['person_id'], personData['birthday']))
            found = 1
    if found == 0:
            print("No user found with that id.")


def main():
    csvData = ''
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', required=True, help='Provide URL of csv file.')
    args = parser.parse_args()
    try:
        csvData = downloadData(args.url)
    except Exception as e:
        print('Error: ', str(e))
    personData = processData(csvData)
    while True:
        choice = int(input('Enter ID to lookup: '))
        if choice == 0 or choice < 0:
            break
        else:
            displayPerson(choice, personData)


if __name__ == '__main__':
    main()
