
import csv

DELIMITER = ' '
QUOTECHAR = '|'

def get():

    try:
        with open('session.csv', newline='') as csvfile:
            csvfile.seek(0)
            sreader = csv.reader(csvfile, delimiter=DELIMITER, quotechar=QUOTECHAR)
            return sreader
            """ out = []
            for row in spamreader:
                #print(', '.join(row))
                out.append(row)
            return out """
    
    except:
        print("No session file")
        open('session.csv', 'a', newline='')
        return []


def add(newrow):

    with open('session.csv', 'a', newline='') as csvfile:
        seswriter = csv.writer(csvfile, delimiter=DELIMITER,quotechar=QUOTECHAR, quoting=csv.QUOTE_MINIMAL)
        seswriter.writerow(newrow)


""" def sessionTest():
r
    add(['test',0,0,0,0,'test file name'])

    with open('session.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=DELIMITER,quotechar=QUOTECHAR, quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['test',0,0,0,0,'test file name']) """
        #spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        #spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])