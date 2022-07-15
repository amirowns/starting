
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
        self.HPtransition = (self.HPcurrent / self.HPmax)

        self.move1 = PokeMove(self.pokeID, self.Level)
        self.move2 = PokeMove(self.pokeID, self.Level)
        self.move3 = PokeMove(self.pokeID, self.Level)
        self.move4 = PokeMove(self.pokeID, self.Level)

        self.movelist = [self.move1, self.move2, self.move3, self.move4]

        self.selected_move = None
        self.damage = None
        self.howeffectivewasit = None

    def select_player_move(self, move):
        self.selected_move = move

    def select_enemy_move(self):
        # pick a random move
        x = choice(range(1, 4))
        self.selected_move = self.movelist[x - 1] # picks a random move from the movelist

    def attack(self, target):

        effectiveness = TypeEffectiveness().calculate_effectiveness(self.selected_move.type, target.type1, target.type2)
        power = self.selected_move.power
        targets = 1
        weather = 1
        crit = 1 # 6.25% to crit add in later
        random = choice(range(85, 100)) / 100
        STAB = 1.5 if self.selected_move.type == self.type1 or self.selected_move.type == self.type2 else 1
        burn = 1

        if self.selected_move.category == "Physical":
            self.damage = round(((((((2 * self.Level)/5) * power * (self.ATK/target.DEF))/50) + 2) * targets * weather * crit * random * STAB * burn) * effectiveness)
        elif self.selected_move.category == "Special":
            self.damage = round(((((((2 * self.Level)/5) * power * (self.SPATK/target.SPDEF))/50) + 2) * targets * weather * crit * random * STAB * burn) * effectiveness)
        else:
            self.damage = 0

        target.HPcurrent -= self.damage
        if target.HPcurrent < 0:
            target.HPcurrent = 0
        # need to update the display text for HP current
        if effectiveness == 0:
            self.howeffectivewasit = " The Pokemon was immune!"
        elif effectiveness > 1:
            self.howeffectivewasit = " It was super effective!"
        elif effectiveness == 1:
            self.howeffectivewasit = ""
        elif effectiveness < 1:
            self.howeffectivewasit = " It was not really effective."  
        
        
        
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
            self.name = "Struggle"
            self.type = "Normal"
            self.category = "Physical"
            self.pp = 1
            self.power = 50
            self.accuracy = 1

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
        # self uses selected move TYPE
        # defender uses pokemon TYPE
        # if the pokemon has 2 types?

        if defenderType2 != "":
            return self.Effectivenessdict[(moveType, defenderType1)] * self.Effectivenessdict[(moveType, defenderType2)]
        else: 
            return self.Effectivenessdict[(moveType, defenderType1)]
