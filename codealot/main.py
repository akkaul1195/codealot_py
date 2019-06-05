from random import Random

class Knight(object):
    __isInTavern = False
    __isInTrainingYard = False

    def __init__(self):
        self.__xp = 0
        self.__stamina = 0

    def getXp(self):
        return self.__xp

    def setXp(self, xp):
        self.__xp = xp

    def incrementXp(self, xp):
        self.__xp += xp

    def getStamina(self):
        return self.__stamina

    def setStamina(self, stamina):
        self.__stamina = stamina

    def incrementStamina(self, stamina):
        self.__stamina += stamina

    def isInTavern(self):
        return self.__isInTavern

    def setInTavern(self, isInTavern):
        self.__isInTavern = isInTavern

    def isInTrainingYard(self):
        return self.__isInTrainingYard

    def setInTrainingYard(self, isInTrainingYard):
        self.__isInTrainingYard = isInTrainingYard


class Codalot(object):
    knights = []

    def __init__(self):
        self.knights = list()

    def clearKnights(self):
        del self.knights[:]

    def addKnightToTrainingYard(self, knight):
        self.knights.append(knight)
        knight.setInTrainingYard(True)
        knight.setInTavern(False)

    def addKnightToTavern(self, knight):
        self.knights.append(knight)
        knight.setInTavern(True)
        knight.setInTrainingYard(False)

    def process(self):
        for knight in self.knights:
            knight.incrementStamina(1 if knight.isInTavern() else -1)
            knight.incrementXp(1 if knight.isInTrainingYard() and knight.getStamina() > 0 else 0)

    def grantBonusXp(self):
        bonusKnights = 0
        for knight in self.knights:
            if knight.getXp() >= 3:
                bonusKnights = bonusKnights + 1

        if bonusKnights == 4:
            for knight in self.knights:
                if knight.getXp() >= 3:
                    knight.setXp(knight.getXp() + 5)

        if bonusKnights == 6:
            for knight in self.knights:
                if knight.getXp() >= 3:
                    knight.setXp(knight.getXp() + 10)

        if bonusKnights == 10:
            for knight in self.knights:
                if knight.getXp() >= 3:
                    knight.setXp(knight.getXp() + 15)

        if bonusKnights == 12:
            for knight in self.knights:
                if knight.getXp() >= 3:
                    knight.setXp(knight.getXp() + 20)

if __name__ == "__main__":
    codalot = Codalot()

    knights = list()
    for i in range(12):
        knights.append(Knight())

    random = Random(1)
    for i in range(24):
        codalot.clearKnights()
        for knight in knights:
            randomVal = random.randint(0, 1)
            if randomVal == 0:
                codalot.addKnightToTrainingYard(knight)
            elif randomVal == 1:
                codalot.addKnightToTavern(knight)
        codalot.process()
    codalot.grantBonusXp()

    totalXp = 0
    for knight in knights:
        totalXp = totalXp + knight.getXp()

    print "Total XP earned by all " + str(len(knights)) + " knights: " + str(totalXp)


