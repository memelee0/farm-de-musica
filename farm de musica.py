from random import randint

melodia = ['a','b','c#m','d#m','e','f#m','g#m']
baixos = ['a','b','c#m','d#m','e','f#m','g#m']
num_baixos = 0
num_melodia = 0

print ("baixos")
print(" ")
while num_baixos<4:
  random_num = (randint(0,6))
  baixo_ = baixos[random_num]
  print (baixo_)
  num_baixos+=1

print(" ")
print ("melodia")
print(" ")
while num_melodia<16:
  random_num=(randint(0,6))
  melodi_a = melodia[random_num]
  print (melodi_a)
  num_melodia+=1
