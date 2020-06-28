class SelectionSort:
    def __init__(self):
        pass

    def sort(self, input):
        out = input.copy()

        n = len(input)
        for i in range(n):
            min = i
            for j in range(i+1, n):
                if out[j] < out[min]:
                    min = j
                out[i], out[min] = out[min], out[j]

        return out