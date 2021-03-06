# input_data.py
# Graphs
# 
# Copyright � 2018  Dominik Witczak & Krzysztof Sychla
# 
# This program is free software : you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.If not, see <https://www.gnu.org/licenses/>.
# 
# This part was written by Krzysztof Sychla
 

import random

ilosc = [500,1000,1500,2000,2500,3000,3500,4000,4500,5000]

def losowo(ile):
    return [random.randrange(i+1)+1 for i in range(ile)]

def malejace(ile):
    return sorted([i+1 for i in range(ile)],reverse=True)

def rosnace(ile):
    return [i+1 for i in range(ile)]

def aksztaltne(ile):
    return [i+1 if i < ile/2 else ile-i for i in range(ile)]

def staly(ile):
    i = random.randrange(ile+1%20+1)
    return [i for j in range(ile)]

def los_bez_pow(ile):
    a = [i+1 for i in range(ile)]
    for i in range(int(ile)):
        r1 = random.randrange(ile)
        r2 = random.randrange(ile)
        a[r1],a[r2] = a[r2],a[r1]
    return a

def shuffle(tab):
    for i in range(len(tab)):
        r1 = random.randrange(len(tab))
        r2 = random.randrange(len(tab))
        tab[r1],tab[r2] = tab[r2],tab[r1]
    return tab


def adjacency_random(ile):
    ones = [1 for i in range(int((ile*(ile-1))/4))]
    zeros = [0 for i in range(int((ile*(ile-1))/4))]
    whole_tab = ones + zeros
    return shuffle(whole_tab)


def Main():
    with open('input_data.txt','w') as f:
        for ile in ilosc:
            a = ''.join(str(i)+' ' for i in adjacency_random(ile))
            f.write(a+'\n')
            print('Koniec: ',ile,' : ',len(a.split(' ')))

# def check_if(tab):
#     for i in tab:
#         if tab.count(i) > 1:
#             print("HALOOOOO: ",i)

if __name__=="__main__":
    Main()
