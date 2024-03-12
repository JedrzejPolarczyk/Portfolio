


def get_numbers():
    numbers = [float(x) for x in input("Wprowadź liczby oddzielone przecinkiem: ").split(",")]
    return numbers

def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    numbers.sort()
    if len(numbers) % 2 == 0:
        mid = len(numbers) / 2
        return (numbers[mid] + numbers[mid-1]) / 2
    else:
        mid = len(numbers) // 2
        return numbers[mid]

def mode(numbers):
    frequency_dict = {}
    for number in numbers:
        if number not in frequency_dict:
            frequency_dict[number] = 1
        else:
            frequency_dict[number] += 1
    mode = max(frequency_dict, key=frequency_dict.get)
    return mode

def variance(numbers):
    mean_value = mean(numbers)
    variance = sum((x - mean_value) ** 2 for x in numbers) / (len(numbers) - 1)
    return variance

def stddev(numbers):
    return variance(numbers) ** 0.5

def correlation(numbers, numbers2):
    n = len(numbers)
    x_mean = sum(numbers) / n
    y_mean = sum(numbers2) / n
    x_diff = [i - x_mean for i in numbers]
    y_diff = [i - y_mean for i in numbers2]
    x_diff_sq = [i ** 2 for i in x_diff]
    y_diff_sq = [i ** 2 for i in y_diff]
    x_y_diff_prod = [x_diff[i] * y_diff[i] for i in range(n)]
    x_stddev = (sum(x_diff_sq) / (n - 1)) ** 0.5
    y_stddev = (sum(y_diff_sq) / (n - 1)) ** 0.5
    corr = sum(x_y_diff_prod) / ((n - 1) * x_stddev * y_stddev)
    return corr


def regression(numbers, numbers2):
    n = len(numbers)
    x_mean = sum(numbers) / n
    y_mean = sum(numbers2) / n
    b = sum([x_i * y_i for x_i, y_i in zip(numbers, numbers2)]) - n * x_mean * y_mean
    b /= sum([x_i ** 2 for x_i in numbers]) - n * x_mean ** 2
    a = y_mean - b * x_mean
    return a, b

def main():
    numbers = get_numbers()
    numbers2 = [float(x) for x in input("Wprowadź drugą listę dla współczynnika korelacji ").split(",")]
    print("Średnia: ", mean(numbers))
    print("Mediana: ", median(numbers))
    print("Moda: ", mode(numbers))
    print("Odchylenie standardowe: ", stddev(numbers))
    print("Wariancja: ", variance(numbers))
    print("Korelacja: ", correlation(numbers, numbers2))
    print("Współczynnik regresji liniowej: ", regression(numbers, numbers2))

if __name__ == "__main__":
    main()


    print("Aby zamknąć okno wciśnik dowolny przycisk")
    input()
