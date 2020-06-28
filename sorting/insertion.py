class InsertionSort:
    def __init__(self):
        pass

    def sort(self, input):
        out = input.copy()

        for i in range(1, len(input)):
            j = i
            while j > 0 and out[j] < out[j-1]:
                out[j], out[j-1] = out[j-1], out[j]
                j = j - 1

        return out