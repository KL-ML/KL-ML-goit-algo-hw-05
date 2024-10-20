import os
import timeit

# Боєра-Мура
def bm(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return -1
    
    last = {}
    for i in range(m):
        last[pattern[i]] = i
    
    i = m - 1
    while i < n:
        j = m - 1
        k = i
        while j >= 0 and text[k] == pattern[j]:
            k -= 1
            j -= 1
        if j == -1:
            return i - m + 1
        i += m - min(j, 1 + last.get(text[i], -1))
    return -1

# Кнута-Морріса-Пратта
def kmp(text, pattern):
    def compute_prefix(pattern):
        m = len(pattern)
        pi = [0] * m
        k = 0
        for q in range(1, m):
            while k > 0 and pattern[k] != pattern[q]:
                k = pi[k - 1]
            if pattern[k] == pattern[q]:
                k += 1
            pi[q] = k
        return pi
    
    m = len(pattern)
    n = len(text)
    if m == 0:
        return -1
    
    pi = compute_prefix(pattern)
    q = 0
    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]
        if pattern[q] == text[i]:
            q += 1
        if q == m:
            return i - m + 1
            q = pi[q - 1]
    return -1

# Рабіна-Карпа
def rk(text, pattern):
    n = len(text)
    m = len(pattern)
    d = 256
    p = 1
    for i in range(m - 1):
        p *= d
    h = 0
    for i in range(m):
        h = h * d + ord(pattern[i])
    t = 0
    for i in range(m):
        t = t * d + ord(text[i])
    i = 0
    while i < n - m + 1:
        if h == t:
            if pattern == text[i:i + m]:
                return i
        if i + m < n:
            t = (t - ord(text[i]) * p) * d + ord(text[i + m])
        i += 1
    return -1

# Функція для вимірювання часу виконання алгоритмів
def measure_time(algorithm, text, pattern):
    start_time = timeit.default_timer()
    algorithm(text, pattern)
    end_time = timeit.default_timer()
    return end_time - start_time

# Прочитаємо текстові файли
def read_file(filename):
    project_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(project_dir, filename)
    with open(full_path, "r", encoding="utf-8", errors="ignore") as file:
        return file.read()


text_file_1 = "article_1.txt"
text_file_2 = "article_2.txt"
files = [
    text_file_1,
    text_file_2
]

algorithms = {"Boyer-Moore": bm, "Knuth-Morris-Pratt": kmp, "Rabin-Karp": rk}

patterns = ["структури даних", "Загалом, алгоритми пошуку - це основний компонент ефективного програмування"]

for i, file in enumerate(files, start=0):
    text = read_file(file)
    print(f"Текст {(i+1)}")
    for pattern in patterns:
        print("Підрядок: ", pattern, "")
        for algorithm_name, algorithm in algorithms.items():
            execution_time = measure_time(algorithm, text, pattern)
            # Додамо вивід результату пошуку підрядка
            result = algorithm(text, pattern)
            if result != -1:
                print(f"    {algorithm_name}: {execution_time:.6f} сек")
                print(f"      Результат: підрядок '{pattern}' знайдено по позиції {result}.")
            else:
                print(f"    {algorithm_name}: {execution_time:.6f} сек")
                print(f"    {algorithm_name}: підрядок '{pattern}' НЕ знайдено.")
