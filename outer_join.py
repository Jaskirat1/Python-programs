#outer join :-
""" in this join all the records from the 
first dataframw will be displayed, irrespective  
of whether the keys in the first dataframe can be found 
in the second dataframe. Whereas the second dataframe, 
only the records with the keys in the second dataframe that 
can be found in the first dataframe will be displayed."""
import pandas as pd


a = pd.DataFrame()
b =pd.DataFrame()



customers = {
    'Name' : ['Aman', 'Boby', 'Dolly','Fatima','Gauri'],
    'age' : [21,22,23,21,22.5],
    'Domain': ['CSE','CSE','ECE','CE','IT']
}

cust_details ={
    'Name':['Aman', 'Boby','Dolly','Fatima','Gauri'],
    'Phone_no':['4565151','5423145','7845215','87946532','541265478'],
    'Country' : ['India','France','Japan', 'South Africa','Canada']

}

a = pd.DataFrame(customers)
b = pd.DataFrame(cust_details)


out = pd.merge(a,b , on='Name', how='outer')

print(out)