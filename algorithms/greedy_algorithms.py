import pickle
from pprint import pprint as print
from materials import binolar

# with open('binolar.txt', 'rb') as file:
#     binolar = pickle.load(file)
#     hududlar = pickle.load(file)

hududlar = binolar


yakuniy_binolar = set()
while hududlar:
    best_bino = None
    qamralgan_hududlar = set()
    for bino, binolar_qamrovi in binolar.items():
        qamrov = hududlar & binolar_qamrovi
        print(f"{bino}:{qamrov}")
        if len(qamrov) > len(qamralgan_hududlar):
            best_bino = bino
            qamralgan_hududlar = qamrov
    hududlar -= qamralgan_hududlar
    yakuniy_binolar.add(best_bino)
    print(f"Tanlangan bino: {best_bino}")
    print(f"Qolgan hududlar: {hududlar}")
    print(f"Tanlangan binolar: {yakuniy_binolar}")
    input()