class C:
    def __init__(self, points):
        self.points = points

    def m(self, n):
        count = 0
        for point in self.points:
            x = point[0]
            y = point[1]
            if x > 0 and y > 0:
                count += 1
        return count >= n