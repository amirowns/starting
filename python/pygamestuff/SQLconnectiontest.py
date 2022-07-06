
import pyodbc
from random import choice

pokeMoveCounter = 4

server = 'teppelin.net,1433\DESKTOP-M2K1N4K'
database = 'master'
username = 'amir'
password = 'tep'
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor = conn.cursor()

class Pokemon():

    def __init__(self):
        cursor.execute(f'SELECT count(*) FROM pokeInfo')
        counted = cursor.fetchone()
        RNGesus = choice(range(1, counted[0]))

        cursor.execute(f'SELECT * FROM pokeInfo WHERE PokeID = {RNGesus}')
        row = cursor.fetchone()

        self.pokeID = row[0]
        self.name = row[2]
        self.type1 = row[3]
        self.type2 = row[4]
        self.HP = row[8]
        self.ATK = row[9]
        self.DEF = row[10]
        self.SPATK = row[11]
        self.SPDEF = row[12]
        self.SPD = row[13]

        self.Level = 5

        self.HPIV = choice(range(0, 31))
        self.HPEV = 0
        self.actual_HP = round((((2 * self.HP + self.HPIV + (self.HPEV/4)) * self.Level)/100) + self.Level + 10)

        self.HPmax = self.actual_HP
        self.HPcurrent = self.HPmax

        self.move1 = PokeMove(self.pokeID, self.Level)
        self.move2 = PokeMove(self.pokeID, self.Level)
        self.move3 = PokeMove(self.pokeID, self.Level)
        self.move4 = PokeMove(self.pokeID, self.Level)
        
    def __str__(self):
        return f'{self.name}, {self.type1}, {self.type2}, HP:{self.HP}, ATK:{self.ATK}, DEF:{self.DEF}, SPATK:{self.SPATK}, SPDEF:{self.SPDEF}, SPD:{self.SPD}'

class PokeMove():
    # currently selects 1 random pokemon move with below settings
    def __init__(self, pokeID, pokelevel):
        global pokeMoveCounter
        global IDlist
        if pokeMoveCounter == 4:
            cursor.execute(f"""
            SELECT pokeLearnset.MoveID 
            FROM pokeLearnset
                JOIN pokeInfo
                ON pokeLearnset.PokeID = pokeInfo.PokeID
                JOIN pokeMoves
                ON pokeMoves.MoveID = pokeLearnset.MoveID

            WHERE (Category = 'Physical' 
            OR Category = 'Special')
            AND Power != 0
            AND pokeLearnset.PokeID = {pokeID};
            """)
            # AND pokeLearnset.level <= {pokelevel}  # insert in above for level restriction
            
            IDlistgetter = cursor.fetchall()
            IDlist = [i[0] for i in IDlistgetter]
            pokeMoveCounter = 0

        pokeMoveCounter += 1

        if len(IDlist) > 0:
            RNGesus = choice(IDlist)
            IDlist.remove(RNGesus)

            cursor.execute(f"""
            SELECT * FROM pokeMoves 
            WHERE MoveID = {RNGesus}
            """)
            row = cursor.fetchone()

            self.name = row[1]
            self.type = row[2]
            self.category = row[3]
            self.pp = row[4]
            self.power = int(row[5])
            #self.accuracy = int(row[6])
            self.accuracy = 1
        else:
            self.name = "N/A"
            self.type = "Normal"
            self.category = None
            self.pp = None
            self.power = None
            self.accuracy = None

    def __str__(self):
        return f'{self.name}, {self.type}, {self.category}, PP: {self.pp}, Power: {self.power}, Acc: {self.accuracy}'

class TypeEffectiveness():
    def __init__(self):
        self.Effectivenessdict = {}
        cursor.execute(f"""
        SELECT * FROM TypeEffectiveness
        """)
        for i in cursor.fetchall():
            self.Effectivenessdict[i[1:3]] = i[3]
    
    def calculate_effectiveness(self, moveType, defenderType1, defenderType2):
        # attacker uses selected move TYPE
        # defender uses pokemon TYPE
        # if the pokemon has 2 types?

        if defenderType2 != "":
            return self.Effectivenessdict[(moveType, defenderType1)] * self.Effectivenessdict[(moveType, defenderType2)]
        else: 
            return self.Effectivenessdict[(moveType, defenderType1)]
