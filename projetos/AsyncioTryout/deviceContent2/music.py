# Refs: https://en.wikipedia.org/wiki/Note_value
# https://en.wikipedia.org/wiki/Octave
# https://en.wikipedia.org/wiki/Chromatic_scale

from machine import Pin, PWM
import time
notepow=[1.0,1.05946,1.12246,1.18921,1.25992,1.33484,
        1.41421,1.49831,1.58740,1.68179,1.78180,1.88775,
        2.0]

# for octaves and values
#     -    1    2    3   4   5   6   7    8
#     -  1/64 1/32 1/16 1/8 1/4 1/2  1    2   4    8 
pow2=[0,   1,   2,   4,  8,  16, 32, 64, 128, 256, 512]

# maps diatonic with flat and sharp accidentals to chromatic
diat={'c':1.0,'c+':1.05946,'d-':1.05946,'d': 1.12246,
      'd+': 1.18921, 'e-': 1.18921, 'e': 1.25992,
      'f': 1.33484, 'f+': 1.41421, 'g-': 1.41421,
      'g':1.49831, 'g+': 1.58740, 'a-': 1.58740,
      'a': 1.68179, 'a+': 1.78180,'b-': 1.78180,
      'b': 1.88775}

# maps figure names to pow2

fig={'semifusa':1,'fusa':2,'semicolcheia': 3, 'colcheia': 4,
      'seminima': 5, 'minima': 6, 'semibreve': 7,
      'breve':8, 'longa': 9, 'maxima': 10}

pitch= 1  # whole note (semibreve) = 1 sec

baseFreq=65.4064 #c1 

def setPitch (newPitch):
    pitch=newPitch

def playNote (note, octave, val) :
    pn=diat[note]
    beeper = PWM(Pin(27, Pin.OUT), freq=int(pow2[octave]*baseFreq*pn), duty=512)
    time.sleep(pow2[val]/64.0) # synchronous programming
    beeper.deinit()

lastoctave=3

def playFig (figure, note, octave=lastoctave) :
    pn=diat[note]
    beeper = PWM(Pin(27, Pin.OUT), freq=int(pow2[octave]*baseFreq*pn), duty=512)
    time.sleep(pow2[fig[figure]]/64.0) # synchronous programming
    beeper.deinit()
    lastoctave=octave

def playAquarela() :
  #notasAquarela=['d', 'd', 'g', 'g', 'f+', 'e', 'd', 'd', 'g', 'g', 'f+', 'e', 'd', 'd', 'e', 'e'] # tem uma emenda
  #figAquarela=['colcheia', 'colcheia', 'colcheia', 'seminima', 'colcheia', 'seminima', 'colcheia', 'colcheia', 'colcheia', 'seminima', 'colcheia', 'seminima', 'colcheia', 'colcheia', 'seminima', 'semibreve']
  notasAquarela=['d', 'd', 'g', 'g', 'f+', 'e', 'd', 'd', 'g', 'g', 'f+', 'e', 'd', 'd', 'e', 'e',# tem uma emenda
                 'd', 'd', 'g', 'g', 'f+', 'e', 'd', 'd', 'g', 'g', 'f+', 'e', 'd', 'd', 'e', 'd', 'c'] 
  figAquarela=['colcheia', 'colcheia', 'colcheia', 'seminima', 'colcheia', 'seminima', 'colcheia', 'colcheia', 'colcheia', 'seminima', 'colcheia', 'seminima', 'colcheia', 'colcheia', 'seminima', 'semibreve',
               'colcheia', 'colcheia', 'colcheia', 'seminima', 'colcheia', 'seminima', 'colcheia', 'colcheia', 'colcheia', 'seminima', 'colcheia', 'seminima', 'colcheia', 'colcheia', 'colcheia', 'colcheia', 'seminima', 'semibreve']
  print (len(notasAquarela))
  print (len(figAquarela))
  for n, f in zip (notasAquarela, figAquarela):
    playFig(f, n)
    time.sleep(0.1)
