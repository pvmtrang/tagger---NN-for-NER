import codecs
import numpy as np

pretrained = {}
emb_invalid = 0
pre_emb = "dataset\\PhoNER_COVID19\\word\\test_word.conll"
word_dim = 100

for i, line in enumerate(codecs.open(pre_emb, 'r', 'utf-8')):
    if i < 5: 
        print (i)
        print (line)
        line = line.rstrip().split()
        print ("len = ", str(len(line)))
        if len(line) == word_dim + 1:
            print ("ok")
            pretrained[line[0]] = np.array(
                [float(x) for x in line[1:]]
            ).astype(np.float32)
        else:
            emb_invalid += 1
    else:
        if emb_invalid > 0:
            print ('WARNING: %i invalid lines', emb_invalid)
        break
    