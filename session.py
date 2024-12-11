
import csv

DELIMITER = ' '
QUOTECHAR = '|'

def get():

    try:
        with open('session.csv', newline='') as csvfile:
            sreader = csv.reader(csvfile, delimiter=DELIMITER, quotechar=QUOTECHAR)
            return sreader
            """ out = []
            for row in spamreader:
                #print(', '.join(row))
                out.append(row)
            return out """
    
    except:
        print("No session file")
        return []


def add(newrow):

    with open('session.csv', 'a', newline='') as csvfile:
        seswriter = csv.writer(csvfile, delimiter=DELIMITER,quotechar=QUOTECHAR, quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(newrow)


def sessionTest():

    with open('session.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=DELIMITER,quotechar=QUOTECHAR, quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['test',0,0,0,0,'none'])
        #spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        #spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

test = get()

for row in test:
    print(row)

#sessionTest()