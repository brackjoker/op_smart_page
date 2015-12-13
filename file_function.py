def make_tensor_file(message):
    filename = "openstack_csv/test1.csv"
#    writecsv = csv.writer(file(filename, 'w'), lineterminator='\n')
#    writecsv.writerow([1, 'nova', "message"])
    f = open(filename,"w")
    f.write('1, "nova", "'+make_tensor_file+'"')
