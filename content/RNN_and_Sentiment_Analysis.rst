RNN and Sentiment Analysis
########################################################

:date: 2016-05-15 10:20
:modified: 2016-10-12 00:04
:tags: python, deep-learning
:category: data
:slug: rnn-and-sentiment-analysis
:authors: Joydeep Bhattacharjee
:summary: deep-learning through theano in python

I have recently been trying to take a splash in the vast waters of deep learning. Deep learning is a special branch of machine learning and might as well be the only foray into the voodoo of artificial intelligence.

One class of problems that can be taken to understand how this whole thing works is through the classical problem of sentiment analysis. To approach this Recurrent Neural Networks work better. We shall create a model so that after the model is trained, it can read the input sentences and give determine if the sentence is a positive sentence or a negative sentence. I am doing the whole thing using `Theano`_ as the backend and the `keras`_ library. The documentation on how to install this can be found in the links provided. Also I will say that development in windows has some dependency issues for keras and theano so I will recommmend using any of the linux flavours but if you could resolve the dependencies please let me know. Please look into `this post`_ for additional information.

So first we can import all the libraries

.. code-block:: python
    from __future__ import absolute_import
    from __future__ import print_function
    import numpy as np
    np.random.seed(1337)

    from keras.preprocessing import sequence
    from keras.optimizers import SGD, RMSprop, Adagrad
    from keras.utils import np_utils
    from keras.models import Sequential
    from keras.layers.core import Dense, Dropout, Activation
    from keras.layers.embeddings import Embedding
    from keras.layers.recurrent import LSTM, GRU
    from keras.datasets import imdb
    from keras import backend as K

    from theano import function

One thing to note is that the seeding should be done at the top for reproducibility. Even after that please check carefully.The seeding does not guarantee anything as can be seen from this `stackoverflow post`_ or from this `keras issue tracker`_. You can see that we are importing the imdb dataset from the keras available datasets to train our model.

Moving on to the next part of the code.

<code>
max_features = 20000
maxlen = 100
batch_size = 32

print("Loading data...")
(X_train, y_train), (X_test, y_test) = imdb.load_data(nb_words = max_features, test_split = 0.2)
print(len(X_train), 'train sequences')
print(len(X_test), 'test sequences')
</code>

Here we initialise some values. "batch_size" is the number of phrases that our model reads at a time. Then we can see that the imdb dataset has been loaded.

<code>
print("Pad sequences(samples x time)")
X_train = sequence.pad_sequences(X_train, maxlen = maxlen)
X_test = sequence.pad_sequences(X_test, maxlen = maxlen)
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
</code>

Then we pad the sequences. From the `documentation`_ we can see that the maxlen arg is the maximum sequence length, longer sequences are truncated and shorter sequences are padded with zeros at the end. This does not have any major impact as we can see from `this thread`_ explained by fchollet.

The training dataset can be seen by printing the X_train[0]. We can see that this is a tensor.::

    [[  269   929    18     2     7     2  4284     8   105     5     2   182
        314    38    98   103     7    36  2184   246   360     7    19   396
         17    26   269   929    18  1769   493     6   116     7   105     5
        575   182    27     5  1002  1085   130    62    17    24    89    17
         13   381  1421     8  5167     7     5  2723    38   325     7    17
         23    93     9   156   252    19   235    20    28     5   104    76
          7    17   169    35 14764    17    23  1460     7    36  2184   934
         56  2134     6    17   891   214    11     5  1552     6    92     6
         33   256    82     7]]

As we can see the points in the vectors are really int scalars and they are id's of each word. This is done through good word to vector representations. For more clarity please look into `this google paper`_. Another good blog to understand how to make vectors out of sentences is `this blog post`_. For good word to vec representations please look into the google `word2vec`_ or standfords glove. For python implementations please visit `gensim`_ and `glove`_. 

Moving on to the next part of the code, we build the sequential model,

.. code-block:: python

    print("Build model..")
    model = Sequential()
    model.add(Embedding(max_features, 128, input_length = maxlen))

and then add the various layers

<code>
model.add(LSTM(128))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))
</code>

Please note that here we have used the LSTM algorithm with vector space having 128 dimensions. Please read more on LSTM `here`_. Also a sigmoid activation is used to provide us with a binary outputs.

Then we compile the function and then train it. One thing that needs to be noted in this step is that in older applications one might see a show_accuracy = True argument being passed to the model.fir function. But in case of keras 1.0 we need to pass the metrics = ["accuracy"] argument during the compile time, i.e. in the model.compile function so that we can get the accuracy in the output.

.. code-block:: python

    model.compile(loss='binary_crossentropy',
                  optimizer = 'adam',
                  metrics=["accuracy"])
    print("Train..")
    score = model.fit(X_train, y_train, batch_size = batch_size,
              nb_epoch = 4, validation_data = (X_test, y_test))

This should give the output in this manner.

<code>Train..
Train on 20000 samples, validate on 5000 samples
Epoch 1/4
20000/20000 [==============================] - 377s - loss: 0.1632 - acc: 0.9388 - val_loss: 0.4682 - val_acc: 0.8312
Epoch 2/4
20000/20000 [==============================] - 631s - loss: 0.0806 - acc: 0.9718 - val_loss: 0.5661 - val_acc: 0.8272
Epoch 3/4
20000/20000 [==============================] - 570s - loss: 0.0514 - acc: 0.9820 - val_loss: 0.6380 - val_acc: 0.8218
Epoch 4/4
20000/20000 [==============================] - 373s - loss: 0.0405 - acc: 0.9869 - val_loss: 0.8619 - val_acc: 0.8126
</code>

As you can see that the accuracy is around 81%

<code>
print("Test score", score)
print("Test accuracy:", acc)
#print(score.history)
#print(score)
print("Test score", score.history["val_loss"][nb_epoch - 1])
print("Test acc", score.history["val_acc"][nb_epoch - 1])

Test score 0.861895102954
Test accuracy: 0.8126
</code>

This is a basic model using the LSTM layer. Running this using GRU gives me the following output

<code>
Test score 0.564897893882
Test accuracy: 0.838
</code>

Please let me know of models which will have a better accuracy. Of course one thing needs to be noted is that the dataset that has been chosen is small and hence for better predictions we should have used one of the pre-trained models.


.. _Theano: http://deeplearning.net/software/theano/
.. _keras: http://keras.io/
.. _this post: https://datanoord.com/2016/02/01/setup-a-deep-learning-environment-on-windows-theano-keras-with-gpu-enabled/
.. _stackoverflow post: http://stackoverflow.com/questions/32419510/how-to-get-reproducible-results-in-keras
.. _keras issue tracker: https://github.com/fchollet/keras/issues/2479
.. _documentation: http://keras.io/preprocessing/sequence/#pad_sequences
.. _this thread: https://github.com/fchollet/keras/issues/85
.. _this google paper: http://arxiv.org/pdf/1301.3781.pdf
.. _this blog post: http://benjaminbolte.com/blog/2016/keras-language-modeling.html
.. _word2vec: https://code.google.com/archive/p/word2vec/
.. _gensim: https://github.com/piskvorky/gensim
.. _glove: https://github.com/stanfordnlp/GloVe
.. _here: https://en.wikipedia.org/wiki/Long_short-term_memory

