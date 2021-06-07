import numpy as np
from secrets import randbelow
import big_o
import collections
import timeit
from datetime import datetime

alphabet = np.array(list('abcdefghijklmnopqrstuvwxyz'))
alphabetInt = alphabet.view(np.int32)


def checkSoup(message: str, letters: str) -> bool:
    if len(message) > len(letters):
        return False

    #Interesting, what happens is message is zero-sized?
    #Could we compose it with letters? No, unless letters itself is zero-sized
    #Then if both are zero-sized, answer would be True
    if len(message) == 0:
        if len(letters) == 0: return True
        else: return False

    lettersCount = collections.Counter(letters)

    for letter in message:
            if lettersCount[letter] >= 1:
                lettersCount[letter] -= 1
            else:
                return False
    else:
        return True
    
def fillArray(m: int) -> np.ndarray:
    return np.random.choice(alphabetInt,m)

def benchmarkedCheckSoup(l: int) -> bool:
    letters = fillArray(l).astype('str')
    m = randbelow(l.item())
    message = fillArray(m).astype('str')
    return checkSoup(message,letters)

def benchmarkedCheckSoupNumpy(l: int) -> bool:
	letters = fillArray(l)
	m = randbelow(l.item())
	message = fillArray(m)
	return checkSoupNumpy(message,letters)	

def checkSoupNumpy(message: np.ndarray, letters: np.ndarray) -> bool:

    if len(message) > len(letters):
        return False

    #Interesting, what happens is message is zero-sized?
    #Could we compose it with letters? No, unless letters itself is zero-sized
    #Then if both are zero-sized, answer would be True
    if len(message) == 0:
        if len(letters) == 0: return True
        else: return False

    lettersCount = np.bincount(letters)

    for letter in  np.nditer(message, flags=['buffered'], op_dtypes=['int32']):
            if letter < len(lettersCount):
                if lettersCount[letter] and lettersCount[letter]>= 1:
                    lettersCount[letter] -= 1
                else:
                    return False
    else:
        return True
    

##### Not numpy
beginning = datetime.now()
print(big_o.big_o(benchmarkedCheckSoup,big_o.datagen.n_, max_n=100000, n_repeats=100))
end = datetime.now()

print("Ellapsed =" + str(end - beginning))

#True
message = 'theraininspainstaysmainlyintheplain'
letters = 'kwertytheraininspainstaysmainlyintheplainpoiuy'
print(checkSoup(message,letters))

#False
message = 'theraininspainstaysmainlyintheplain'
letters = 'kwertytheraininsaistaysmainlyinthlainoiuy'
print(checkSoup(message,letters))


##### Numpy block
beginning = datetime.now()
print(big_o.big_o(benchmarkedCheckSoupNumpy,big_o.datagen.n_, max_n=100000, n_repeats=100))
end = datetime.now()
print("Ellapsed =" + str(end - beginning))
#True
message = np.array(list('theraininspainstaysmainlyintheplain')).view(np.int32)
letters = np.array(list('kwertytheraininspainstaysmainlyintheplainpoiuy')).view(np.int32)
print(checkSoupNumpy(message,letters))

#False
message = np.array(list('theraininspainstaysmainlyintheplain')).view(np.int32)
letters = np.array(list('kwertytheraininsaistaysmainlyinthlainoiuy')).view(np.int32)
print(checkSoupNumpy(message,letters))




