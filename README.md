## NER Tagger

NER Tagger is an implementation of a Named Entity Recognizer that obtains state-of-the-art performance in NER on the 4 CoNLL datasets (English, Spanish, German and Dutch) without resorting to any language-specific knowledge or resources such as gazetteers. Details about the model can be found at: http://arxiv.org/abs/1603.01360


## Initial setup

To use the tagger, you need Python 2.7, with Numpy and Theano installed.

```
Install
- numpy
-scipy
- theano
- perl (i use strawberry perl https://strawberryperl.com/) to run evaluation/conlleval script
- mingw g++ for theano C-optimization (mingw get setup)

```

```
Set-ExecutionPolicy Unrestricted -Scope Process
.\venv\Scripts\activate
```
```
Download
- glove 100d (https://www.kaggle.com/datasets/pkugoodspeed/nlpword2vecembeddingspretrained/?select=glove.6B.100d.txt)
- phoNER - covid19: vietnamese ner dataset syllable and word (https://github.com/VinAIResearch/PhoNER_COVID19)
- phoW2v - vietnamese pretrained syllable and word embedding (https://github.com/datquocnguyen/PhoW2V)
```
## Compile

- Origin config (char + word + dropout + their eng dataset. Reduce to 10 epoch thui) 
```python ./train.py --train dataset/eng.train --dev dataset/eng.testa --test dataset/eng.testb```
- Origin config + pretrained glove 100d: 
```python ./train.py --train dataset/eng.train --dev dataset/eng.testa --test dataset/eng.testb --pre_emb dataset/embedding/glove/glove.6B.100d.txt```
- Origin config + viet dataset syllable
```python ./train.py --train dataset\\PhoNER_COVID19\\syllable\\train_syllable.conll --dev dataset\\PhoNER_COVID19\\syllable\\dev_syllable.conll --test dataset\\PhoNER_COVID19\\syllable\\test_syllable.conll --tag_scheme iob```
- Origin config + viet dataset word
```python ./train.py --train dataset\\PhoNER_COVID19\\word\\train_word.conll --dev dataset\\PhoNER_COVID19\\word\\dev_word.conll --test dataset\\PhoNER_COVID19\\word\\test_word.conll --tag_scheme iob```
- Origin config + viet word dataset + word embedding
```python ./train.py --train dataset\\PhoNER_COVID19\\word\\train_word.conll --dev dataset\\PhoNER_COVID19\\word\\dev_word.conll --test dataset\\PhoNER_COVID19\\word\\test_word.conll --tag_scheme iob --pre_emb dataset\\embedding\\pho_w2v\\word\\word2vec_vi_words_100dims.txt```

- Origin config + viet syll dataset + syll dataset
```python ./train.py --train dataset\\PhoNER_COVID19\\syllable\\train_syllable.conll --dev dataset\\PhoNER_COVID19\\syllable\\dev_syllable.conll --test dataset\\PhoNER_COVID19\\syllable\\test_syllable.conll --tag_scheme iob --pre_emb dataset\embedding\pho_w2v\syllable\word2vec_vi_syllables_100dims.txt```



## Tag sentences

The fastest way to use the tagger is to use one of the pretrained models:

```
./tagger.py --model models/english/ --input input.txt --output output.txt
```

The input file should contain one sentence by line, and they have to be tokenized. Otherwise, the tagger will perform poorly.


## Train a model

To train your own model, you need to use the train.py script and provide the location of the training, development and testing set:

```
./train.py --train train.txt --dev dev.txt --test test.txt
```

The training script will automatically give a name to the model and store it in ./models/
There are many parameters you can tune (CRF, dropout rate, embedding dimension, LSTM hidden layer size, etc). To see all parameters, simply run:

```
./train.py --help
```

Input files for the training script have to follow the same format than the CoNLL2003 sharing task: each word has to be on a separate line, and there must be an empty line after each sentence. A line must contain at least 2 columns, the first one being the word itself, the last one being the named entity. It does not matter if there are extra columns that contain tags or chunks in between. Tags have to be given in the IOB format (it can be IOB1 or IOB2).
