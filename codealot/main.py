from random import Random
import sys

class Knight(object):
    __isInTavern = False
    __isInTrainingYard = False
    __isInRoundTable = False
    __staminaStillValid = True
    __RoundTableCount = 0

    def __init__(self, KA):
        self.__totalxp = 0
        self.__xp = 0
        self.__stamina = 0
        self.__KingArthur = KA

    def getXp(self):
        return self.__xp

    def setXp(self, xp):
        self.__xp = xp

    def incrementXp(self, xp):
        if self.__staminaStillValid:
            self.__xp += xp
        else: 
            self.__xp = 0

    def getStamina(self):
        return self.__stamina

    def setStamina(self, stamina):
        self.__stamina = stamina

    def incrementStamina(self, stamina):
        self.__stamina += stamina
        if self.__stamina < 0:
            self.__staminaStillValid = False

    def incrementRT(self, val):
        self.__RoundTableCount += val

    def isInTavern(self):
        return self.__isInTavern

    def setInTavern(self, isInTavern):
        self.__isInTavern = isInTavern

    def isInRoundTable(self):
        return self.__isInRoundTable

    def setInRoundTable(self, isInRoundTable):
        self.__isInRoundTable = isInRoundTable

    def isInTrainingYard(self):
        return self.__isInTrainingYard

    def setInTrainingYard(self, isInTrainingYard):
        self.__isInTrainingYard = isInTrainingYard

    def addXpToTotal(self):
        if self.__RoundTableCount >= 3:
            self.__totalxp += self.__xp
        self.__xp = 0
        self.__staminaStillValid = True
        self.__RoundTableCount = 0

    def getTotalXp(self):
        return self.__totalxp

    def isKingArthur(self):
        return self.__KingArthur

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
        knight.setInRoundTable(False)

    def addKnightToTavern(self, knight):
        self.knights.append(knight)
        knight.setInTavern(True)
        knight.setInTrainingYard(False)
        knight.setInRoundTable(False)

    def addKnightToRoundTable(self, knight):
        self.knights.append(knight)
        knight.setInRoundTable(True)
        knight.setInTavern(False)
        knight.setInTrainingYard(False)

    def process(self):
        for knight in self.knights:
            knight.incrementStamina(1 if knight.isInTavern() else 0 if knight.isInRoundTable() else -1)
            knight.incrementXp(1 if knight.isInTrainingYard() and knight.getStamina() > 0 else 0)
            knight.incrementRT(1 if knight.isInRoundTable() else 0)

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

    def addDailyXpToTotal(self):
        for knight in self.knights:
            knight.addXpToTotal()


if __name__ == "__main__":
    try:
        days = int(sys.argv[1])
    except IndexError:
        days = 1
    except ValueError:
        print "Invalid Input: please leave blank or enter a number using numerals"
        sys.exit(1)

    codalot = Codalot()

    knights = list()
    knights.append(Knight(True))
    for i in range(12):
        knights.append(Knight(False))

    random = Random(1)
    for j in range(days):
        for i in range(24):
            codalot.clearKnights()
            for knight in knights:
                randomVal = random.randint(0, 2)
                if randomVal == 0:
                    codalot.addKnightToTrainingYard(knight)
                elif randomVal == 1:
                    codalot.addKnightToTavern(knight)
                elif randomVal == 2:
                    codalot.addKnightToRoundTable(knight)
            codalot.process()
        codalot.grantBonusXp()
        codalot.addDailyXpToTotal()

    totalXp = 0
    for knight in knights:
        if knight.isKingArthur():
            KingXP = knight.getTotalXp()
        else:
            totalXp += knight.getTotalXp()

    print "Total XP earned by all " + str(len(knights)-1) + " knights in " + str(days) + " day(s): " + str(totalXp) 
    print "Total XP earned by King Arthur in " + str(days) + " day(s): " + str(KingXP)


