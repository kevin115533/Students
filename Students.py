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
    import random
    kids = []
    bob = Student("Bob", 7)
    billy = Student("Billy", 7)
    sara = Student("Sara", 7)
    maggie = Student("Maggie", 7)
    john = Student("John", 7)
    for count in range(7):
        maggie.setScore(count, random.randint(0, 100))
        bob.setScore(count, random.randint(0, 100))
        billy.setScore(count, random.randint(0, 100))
        sara.setScore(count, random.randint(0, 100))
        john.setScore(count, random.randint(0, 100))
    kids.extend([bob, billy, sara, maggie, john])
    for count in range(len(kids)):
        kids.sort()
        print(kids[count])


main()