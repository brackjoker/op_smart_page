from django.shortcuts import render
import csv

def test(req):
    filename = "openstack_csv/test1.csv"
#    writecsv = csv.writer(file(filename, 'w'), lineterminator='\n')
#    writecsv.writerow([1, 'nova', "message"])
    f = open(filename,"w")
    f.write('1, "nova", "message"')

    #f = open("openstack_csv/test1.csv", "r")
    #str = f.read()
    #print str