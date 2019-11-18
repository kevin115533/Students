class Student(object):
    def __init__(self, name, number):
        self._name = name
        self._scores = []
        for count in range(number):
            self._scores.append(0)

    def getName(self):
        return self._name

    def setScore(self, i, score):
        self._scores[i - 1] = score

    def getScore(self, i):
        return self._scores[i - 1]

    def getAverage(self):
        return sum(self._scores) / len(self._scores)

    def getHighScore(self):
        return max(self._scores)

    def __str__(self):
        return "Name: " + self._name + "\nScores: " + " ".join(map(str, self._scores))

    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return "Billy's Avg Score == Bob's Avg Score: " + str(self.getAverage() == other.getAverage())

    def __lt__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return "Billy's High Score < Bob's High Score: " + str(self.getHighScore() < other.getHighScore())

    def __gt__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return "Billy's High Score > Bob's High Score: " + str(self.getHighScore() > other.getHighScore())

def main():
    bob = Student("Bob", 4)
    bob.setScore(1, 95)
    bob.setScore(2, 57)
    bob.setScore(3, 80)
    bob.setScore(4, 40)
    billy = Student("Billy", 4)
    billy.setScore(1, 100)
    billy.setScore(2, 60)
    billy.setScore(3, 70)
    billy.setScore(4, 90)
    print(bob)
    print(billy)
    print(billy == bob)
    print(billy < bob)
    print(billy > bob)


main()