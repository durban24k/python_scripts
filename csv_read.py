import csv
with open("test.csv","w",newline='') as f:
     fieldnames=['column1','column2','column3']
     thewriter=csv.DictWriter(f,fieldnames=fieldnames)

     thewriter.writeheader()
     for i in range(1,100):
          thewriter.writerow({'column1':'one','column2':'two','column3':'three'})