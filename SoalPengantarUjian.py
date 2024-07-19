# NOMOR 1
print("=== NOMOR 1 ===")
a = 15 % 5
b = 12 + 3 * 5 == 75
c = "PML" + "15523"
d = "100" + str(234)
e = ((11 % 3) + 2) != 8 / 2

print(a)  
print(b)  
print(c)  
print(d)  
print(e)  

# NOMOR 2
print("\n=== NOMOR 2 ===")

p = 11
q = 5
r = 4

a = (p - r) == (r + q)
b = ((p % 3) + q) != (r % 2)
c = (q - 3) == (p % 2 + q)
d = (r + q) != ((p * 2) % 2)
e = ((q % 3) + p) > (r % 2)
f = (r + p) <= (q * 5)

print("a:", a)  
print("b:", b)  
print("c:", c) 
print("d:", d)  
print("e:", e)  
print("f:", f)  

# NOMOR 3
print("\n=== NOMOR 3 ===")
hasil = "Honey" + "Boo"*3
print(hasil)

# NOMOR 4
print("\n=== NOMOR 4 ===")
capitals = {}
capitals['Murica'] = 'Warshington'
capitals['Germany'] = 'Bonn'
capitals['France'] = 'Paris'
capitals['Engalnd'] = 'London'
capitals['Germany'] = 'Berlin'

hasil = capitals['Germany']
print(hasil)

# NOMOR 5
print("\n=== NOMOR 5 ===")
a = "23"
b = "9"
print(a + b)

# NOMOR 6
print("\n=== NOMOR 6 ===")
letters = ["a", "b", "o", "c", "p"]

result_a = letters[1]
print(result_a) 

result_b = letters[len(letters) - 2]
print(result_b) 

result_c = letters + ["x"]
print(result_c) 

result_d = letters
print(result_d)  

# NOMOR 7
print("\n=== NOMOR 7 ===")
hasil = ' '.join('h a n d s'.split())
print(hasil)

# NOMOR 8
print("\n=== NOMOR 8 ===")
import json

json_string = """
[
  {"1": "one", "2": "two", "3": "three"},
  {"1": "un", "2": "deux", "3": "trois"},
  {"1": "eins", "2": "zwei", "3": "drei"}
]
"""

data = json.loads(json_string)

print(data)

# NOMOR 9
print("\n=== NOMOR 9 ===")
def pembagi_indeks(nums, divisor):
    for i in range(len(nums)):
        if nums[i] % divisor == 0:
            return i  
    return -1  

vals = [101, 4, 12, 24]
print(pembagi_indeks(vals, 2))  

vals = [100, 66, 55, 64, 41, 35, 18, 64]
print(pembagi_indeks(vals, 5))  

# NOMOR 10
print("\n=== NOMOR 10 ===")
def mystery(n, m):
    p = 0
    e = 0
    while n > 0:
        p += 1
        e += m
        n -= 1
    return p

print(mystery(4, 3))  
