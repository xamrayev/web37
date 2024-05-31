from flask import Flask, render_template, request, redirect, url_for
app=Flask(__name__)

cities = {
    "namangan": "Namangan is beautiful city",
    "andijan": "Bobur was born in Andijan"
}

@app.route('/')
def index():
    list_cities = list(cities.keys())
    return render_template(
        "index.html",
        cities = list_cities
        )

@app.route('/<city_name>')
def hello_name(city_name):
    about_city = cities[city_name]
    return render_template(
        "hello.html",
        c_name = city_name,
        a_city = about_city)

@app.route('/create_city', methods = ['GET', 'POST'])
def create_city():
    if request.method == 'POST':
        c_name = request.form['city_name']
        a_city = request.form['about_city']
        new_city = {c_name: a_city}
        cities.update(new_city)
        return render_template(
            'create_city.html', cities=cities)
    else:
        return render_template(
            'create_city.html', cities=cities)

@app.route('/delete_city/<name>')
def delete_city(name):
    del cities[name]
    return redirect(url_for('create_city'))
        


    


if __name__=='__main__':
    app.run(debug=True)
