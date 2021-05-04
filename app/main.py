from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

###########################################
#--------Подключение к базе данных--------#
###########################################

engine = create_engine("postgresql://postgres:1908@localhost/microarch")
db = scoped_session(sessionmaker(bind=engine))

app.secret_key = 'microarch-lab2'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

###########################################
#--------Переходы между страницами--------#
###########################################

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/addteam')
def teams():
    return render_template("addteam.html")

@app.route('/addplayer')
def players():
    return render_template("addplayer.html")
    
@app.route('/delete')
def delete():
    return render_template("delete.html")

###########################################
#-----------------Функции-----------------#
###########################################

@app.route('/addplayer', methods=['POST']) # Добавление игрока
def addPlayer():
    firstname = request.form.get("firstname")
    secondname = request.form.get("secondname")
    patronname = request.form.get("patronname")
    birthdate = request.form.get("birthdate")
    teamname = request.form.get("teamname")
    db.execute("INSERT INTO players (firstname, secondname, patronname, birthdate, teamname) VALUES (:firstname, :secondname, :patronname, cast(:birthdate as date), :teamname)",
            {"firstname":firstname, "secondname":secondname, "patronname":patronname, "birthdate":birthdate, "teamname":teamname})
    db.commit()
    return render_template("addplayer.html") 

@app.route('/addteam', methods=['POST']) # Добавление команды  
def addTeam():
    teamname = request.form.get("teamname")
    homecity = request.form.get("homecity")
    sponsors = request.form.get("sponsors")
    db.execute("INSERT INTO teams (teamname,homecity,sponsors) VALUES (:teamname,:homecity,:sponsors)", 
            {"teamname":teamname, "homecity":homecity, "sponsors":sponsors})
    db.commit()
    return render_template("addteam.html")

@app.route('/delete', methods=['POST']) # DELETE Удаление игрока
def delPlayer():
    idplayer = request.form.get("idplayer")
    db.execute("DELETE FROM players WHERE playerid = (:idplayer)", {"idplayer":idplayer})
    db.commit()
    return render_template("delete.html")


@app.route('/delete', methods=['POST']) # DELETE Удаление команды
def delTeam():
    idteam = request.form.get("idteam")
    db.execute("DELETE FROM teams WHERE teamid = (:idteam)", {"idteam":idteam})
    db.commit()
    return render_template("delete.html")

if __name__ == "__main__":
    app.run(debug=True)