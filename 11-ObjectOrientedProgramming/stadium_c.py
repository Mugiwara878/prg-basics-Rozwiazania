class C:
    def __init__(self, sectors):
        self.sectors = sectors

    def m1(self, s, n):
        self.sectors[s] = n

    def m2(self, s):
        total = 0
        for letter in s:
            if letter in self.sectors:
                total += self.sectors[letter]
        return total