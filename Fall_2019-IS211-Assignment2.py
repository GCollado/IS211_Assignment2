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

import datetime
import logging
import pprint
import urllib.request

LOG_FILENAME = 'assignment2.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.ERROR)


def downloadData(url):
    return urllib.request.urlopen(url).readlines()

#row needs to be
def processData(contents):
    line_number = 0
    file = downloadData(contents)
    persons = {'person_id': ('name', 'birthday')}
    for line in file:
        line_number += 1
        line = str(line)
        line = line.lstrip('b\'').rstrip('\\n\'')
        line = line.split(',')
        persons['person_id'], persons['name'], persons['birthday'] = line[0], line[1], line[2]
        try:
           persons['birthday'] = datetime.datetime.strptime(persons['birthday']+' 00:00:00','%m/%d/%Y %H:%M:%S')
        except ValueError:
            error_message ="Error processing line #{} for ID #{}.".format(line_number, persons['person_id'])
            logging.error(error_message)
            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint(error_message)


def displayPerson(id, personData):
    pass

if __name__ == '__main__':
    blah='https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'
    processData(blah)