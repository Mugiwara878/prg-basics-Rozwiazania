# statistics_class.py
class Statistics:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def show_numbers(self):
        print('Numbers:', ' '.join(str(n) for n in self.numbers))

    def maximum(self):
        return max(self.numbers)

    def minimum(self):
        return min(self.numbers)

    def mean(self):
        return sum(self.numbers) / len(self.numbers)

    def median(self):
        sorted_nums = sorted(self.numbers)
        n = len(sorted_nums)
        if n % 2 == 1:
            return sum(self.numbers) / len(self.numbers)

    def median(self):
        sorted_nums = sorted(self.numbers)
        n = len(sorted_nums)
        if n % 2 == 1:
            return sorted_nums[n // 2]
        else:
            return (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2

    def show_statistics(self):
        print('Maximum:', self.maximum())
        print('Minimum:', self.minimum())
        print('Mean:', self.mean())
        print('Median:', self.median())