from flask import Flask, render_template, request, jsonify
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker
from json import dumps
import json
import psycopg2

app = Flask(__name__)

###########################################
#--------Подключение к базе данных--------#
###########################################

engine = create_engine("postgresql://postgres:1908@localhost/microarch")
db = scoped_session(sessionmaker(bind=engine))
Session = sessionmaker(bind=engine)
session = Session()

app.secret_key = 'microarch-lab2'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

###########################################
#-----------------Функции-----------------#
###########################################

# CREATE Добавление игрока
@app.route('/addplayer/<string:firstname>/<string:secondname>/<string:patronname>/<string:birthdate>/<string:teamname>', methods=['POST'])
def addPlayer(firstname,secondname,patronname,birthdate,teamname):
    db.execute("INSERT INTO players (firstname, secondname, patronname, birthdate, teamname) VALUES (:firstname, :secondname, :patronname, cast(:birthdate as date), :teamname)",
            {"firstname":firstname, "secondname":secondname, "patronname":patronname, "birthdate":birthdate, "teamname":teamname})
    db.commit()
    return "Success: firstname = " + str(firstname) + ", secondname = " + str(secondname) + ", patronname = "  + str(patronname) + ", birthdate = "  + str(birthdate) + ", teamname = "  + str(teamname) 

# CREATE Добавление команды  
@app.route('/addteam/<string:teamname>/<string:homecity>/<string:sponsors>', methods=['POST']) 
def addTeam(teamname,homecity,sponsors):
    db.execute("INSERT INTO teams (teamname,homecity,sponsors) VALUES (:teamname,:homecity,:sponsors)", 
            {"teamname":teamname, "homecity":homecity, "sponsors":sponsors})
    db.commit()
    return "Success: teamname = " + str(teamname) + ", homecity = " + str(homecity) + ", sponsors = "  + str(sponsors)

# READ Возвращение команды по id 
@app.route('/getteam/<int:teamid>', methods=['GET'])
def getTeam(teamid):
    result = db.execute("SELECT * FROM teams WHERE teamid = " + str(teamid))
    return json.dumps([dict(r) for r in result], default=str)

# READ Возвращение всех команд
@app.route('/getteams', methods=['GET'])
def getTeams():
    result = db.execute("SELECT * FROM teams")
    return json.dumps([dict(r) for r in result], default=str)

# READ Возвращение игрока по id 
@app.route('/getplayer/<int:playerid>', methods=['GET'])
def getPlayer(playerid):
    result = db.execute("SELECT * FROM players WHERE playerid = " + str(playerid))
    return json.dumps([dict(r) for r in result], default=str)

# READ Возвращение всех игроков 
@app.route('/getplayers', methods=['GET'])
def getPlayers():
    result = db.execute("SELECT * FROM players")
    return json.dumps([dict(r) for r in result], default=str)

# PUT Изменение игрока
@app.route('/editplayer/<int:playerid>/<string:firstname>/<string:secondname>/<string:patronname>/<string:birthdate>/<string:teamname>', methods=['PUT'])
def editPlayer(playerid, firstname,secondname,patronname,birthdate,teamname):
    db.execute("UPDATE players SET firstname = :firstname, secondname = :secondname, patronname = :patronname, birthdate = :birthdate, teamname = :teamname WHERE playerid = :playerid",
            {"playerid": playerid,"firstname":firstname, "secondname":secondname, "patronname":patronname, "birthdate":birthdate, "teamname":teamname})
    db.commit()
    return "Success: player with id = " + str(playerid) + "updated to firstname = " + str(firstname) + ", secondname = " + str(secondname) + ", patronname = "  + str(patronname) + ", birthdate = "  + str(birthdate) + ", teamname = "  + str(teamname) 

# PUT Изменение команды
@app.route('/editteam/<int:teamid>/<string:teamname>/<string:homecity>/<string:sponsors>', methods=['PUT']) 
def editTeam(teamid,teamname,homecity,sponsors):
    db.execute("UPDATE teams SET teamname = :teamname, homecity = :homecity, sponsors = :sponsors WHERE teamid = :teamid", 
            {"teamid":teamid, "teamname":teamname, "homecity":homecity, "sponsors":sponsors})
    db.commit()
    return "Success:  team with id = " + str(teamid) + " updated to teamname = " + str(teamname) + ", homecity = " + str(homecity) + ", sponsors = "  + str(sponsors)


# DELETE Удаление игрока
@app.route('/deleteplayer/<int:idplayer>', methods=['DELETE']) 
def delPlayer(idplayer):
    db.execute("DELETE FROM players WHERE playerid = (:idplayer)", {"idplayer":idplayer})
    db.commit()
    return "Success: player with id=" + str(idplayer) + " was deleted."

# DELETE Удаление команды
@app.route('/deleteteam/<int:idteam>', methods=['DELETE']) 
def delTeam(idteam):
    db.execute("DELETE FROM teams WHERE teamid = (:idteam)", 
            {"idteam":idteam})
    db.commit() 
    return "Success: team with id=" + str(idteam) + " was deleted."

# GET Возвращение команды и его игроков 
@app.route('/getplayerteam/<int:idplayer>', methods=['GET'])
def getPlayerTeam(idplayer):
    result = db.execute("SELECT p.*, t.* FROM players p RIGHT JOIN teams t ON p.teamName = t.teamName WHERE p.playerid = :idplayer",
            {"idplayer":idplayer})
    return json.dumps([dict(r) for r in result], default=str)

# GET Возвращение игрока и команды, в котороый он состоит 
@app.route('/getteamplayers/<int:idteam>', methods=['GET'])
def getTeamPlayers(idteam):
    result = db.execute("SELECT t.teamName, t.homecity, t.sponsors, json_agg(json_build_object('firstName', p.firstname, 'secondName', p.secondname, 'patronName', p.patronname, 'birthDate', p.birthdate)) AS players FROM teams t RIGHT JOIN players p ON p.teamName = t.teamName WHERE t.teamid = :idteam GROUP BY t.teamName, t.homecity, t.sponsors",
            {"idteam":idteam})
    res = json.dumps([dict(r) for r in result], default=str)
    return res

if __name__ == "__main__":
    app.run(debug=True)
