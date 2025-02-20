import csv

def read_csv(path):
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)
        #file1 = next(reader)
        #print(reader)
        #print("ES ES EL HEADER=>>>>", header)
        #print("ES ES EL FILE1=>>>>", file1)
        data = []
        
        for row in reader:
            #print(row)
            iterable = zip(header, row)
            #print("CONVERSION A DICCIONARIO********************************************")
            country_dict = {key: value for key, value in iterable}
            #print(country_dict)
            #print("CONVERSION A LISTA********************************************")
            data.append(country_dict)
        return data


"""
[('Rank', '36'), ('CCA3', 'AFG'), ('Country/Territory', 'Afghanistan'), ('Capital', 'Kabul'), ('Continent', 'Asia'), ('2022 Population', '41128771'), ('2020 Population', '38972230'), ('2015 Population', '33753499'), ('2010 Population', '28189672'), ('2000 Population', '19542982'), ('1990 Population', '10694796'), ('1980 Population', '12486631'), ('1970 Population', '10752971'), ('Area (kmÂ²)', '652230'), ('Density (per kmÂ²)', '63.0587'), ('Growth Rate', '1.0257'), ('World Population Percentage', '0.52')]
"""

lista1 = ["n1", 1, "n2" , 2]

lista2 = [["adm", 200], ["omb", 89]]

data = []

for i in lista2:
    tupla1 = tuple(i)
    #my_dict = {key: value for key, value in tupla1}
    print(tupla1)
    data.append(tupla1)
    print(data)
    #my_dict = {key: value for key, value in tupla1}
    
    #data.append(tupla1)
#print(data)
print("Esta es la data =>>>", data)
my_dict = {key: value for key, value in data}
print(my_dict)

data2 = []

#my_dict2 = {llave:valor for llave, valor in my_dict}


price = [100, 300, 200]
price_2 = list(map(lambda x : x["price"], data2))
print(price_2)

if __name__ == "__main__":
    data = read_csv("./app/data.csv")
    #print(data[0])
