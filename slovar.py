cities = {
    "namangan": "Namangan is beautiful city",
    "andijan": "Bobur was born in Andijan",    
}

def read_c(city_name):
    c_name = city_name
    a_city = cities[c_name]
    print(c_name, a_city)

def create_c(city_name, about_city):
    c_name = city_name
    a_city = about_city
    new_city = {c_name: a_city}
    cities.update(new_city)
    print(cities)

def delete_c(city_name):
    c_name=city_name
    del cities[c_name]
    print(cities)

def update_c(city_name, new_about):
    c_name = city_name
    a_city = new_about
    cities[c_name] = a_city
    print(cities)

create_c("Fergana", "Fergane is beautiful city")
print(20*"*")
delete_c("andijan")
print(20*"*")
update_c("namangan", "Namangan is here")