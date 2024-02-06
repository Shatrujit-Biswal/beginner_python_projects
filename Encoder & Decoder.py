import random

def random_letter():
    random_letters = [chr(random.randint(ord('A'), ord('z'))) for _ in range(3)]
    return ''.join(random_letters)

def encoding(words):
    nwords = []
    for word in words:
        if len(word) >= 3:
            stnew = random_letter() + word[1:] + word[0] + random_letter()
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

def decoding(words):
  nwords = []
  for word in words:
    if(len(word)>=3): 
      stnew = word[3:-3]
      stnew = stnew[-1] + stnew[:-1]
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))

while True:
    coding = (input("C for Coding | D for Decoding | q to exit\n")).lower()
    if coding == "q":
        break
    elif coding == "c":
        st = input("Enter message:\n")
        words = st.split(" ")
        encoding(words)
    elif coding == "d":
        st = input("Enter message:\n")
        words = st.split(" ")
        decoding(words)
    else:
        print("Wrong Input")