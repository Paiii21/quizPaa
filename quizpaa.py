import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
B = [0, 1, 2, 3, 4, 9, 8, 7, 6, 5]

start = time.time()
bubble_sort(A.copy())
end = time.time()
print("Bubble Sort A time:", end - start)

start = time.time()
bubble_sort(B.copy())
end = time.time()
print("Bubble Sort B time:", end - start)

start = time.time()
quick_sort(A.copy())
end = time.time()
print("Quick Sort A time:", end - start)

start = time.time()
quick_sort(B.copy())
end = time.time()
print("Quick Sort B time:", end - start)

# Quick Sort lebih efektif daripada Bubble Sort pada kasus A karena kompleksitas waktu lebih rendah dan eksekusi lebih cepat.
# Quick Sort lebih efektif dibandingkan Bubble Sort pada kasus B karena dapat memanfaatkan sebagian data yang sudah terurut untuk mengurangi jumlah operasi
# Untuk kedua kasus (A dan B), Quick Sort lebih efektif dibandingkan Bubble Sort. Quick Sort memiliki kompleksitas rata-rata lebih rendah dan bekerja lebih baik pada data yang tidak sepenuhnya acak, seperti pada kasus B.