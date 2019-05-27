import csv


class Frame:
    def __init__(self, csv_path, separator=',', has_header=True):
        self.data = []
        self.header = []

        with open(csv_path) as csv_file:
            csv_iter = csv.reader(csv_file, delimiter=separator)
            row_count = 0
            for idx, row in enumerate(csv_iter):
                print(row)
                if has_header and idx == 0:
                    self.header = row
                self.data.append(row)
                row_count = idx
            self.row_count = row_count
            self.col_count = len(self.header) or len(self.data[0])

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError("Only int allowed")
        if not item >= 0 and item < self.row_count:
            raise ValueError("Index should be between 0 and {}".format(self.row_count))
        return self.data[item]

    def reset(self):
        self.data = []
        self.row_count = self.col_count = 0


path = './data/train.csv'
frame = Frame(path)
print(frame.header)


