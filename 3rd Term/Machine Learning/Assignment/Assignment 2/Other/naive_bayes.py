import numpy as np
import pandas as pd
class NaiveBayesForSpam:
    def train (self, hamMessages, spamMessages):
        self.words = set (' '.join (hamMessages + spamMessages).split())
        self.priors = np.zeros (2)
        self.priors[0] = float (len (hamMessages)) / (len (hamMessages) + len (spamMessages))
        self.priors[1] = 1.0 - self.priors[0]
        self.likelihoods = []
        for i, w in enumerate (self.words):
            prob1 = (1.0 + len ([m for m in hamMessages if w in m])) / len (hamMessages)
            prob2 = (1.0 + len ([m for m in spamMessages if w in m])) / len (spamMessages)
            self.likelihoods.append ([min (prob1, 0.95), min (prob2, 0.95)])
        self.likelihoods = np.array (self.likelihoods).T
        
    def train2 (self, hamMessages, spamMessages):
        self.words = set (' '.join (hamMessages + spamMessages).split())
        self.priors = np.zeros (2)
        self.priors[0] = float (len (hamMessages)) / (len (hamMessages) + len (spamMessages))
        self.priors[1] = 1.0 - self.priors[0]
        self.likelihoods = []
        spamkeywords = []
        for i, w in enumerate (self.words):
            prob1 = (1.0 + len ([m for m in hamMessages if w in m])) / len (hamMessages)
            prob2 = (1.0 + len ([m for m in spamMessages if w in m])) / len (spamMessages)
            if prob1 * 20 < prob2:
                self.likelihoods.append ([min (prob1, 0.95), min (prob2, 0.95)])
                spamkeywords.append (w)
        self.words = spamkeywords
        self.likelihoods = np.array (self.likelihoods).T

    def predict (self, message):
        posteriors = np.copy (self.priors)
        for i, w in enumerate (self.words):
            if w in message.lower():  # convert to lower-case
                posteriors *= self.likelihoods[:,i]
            else:                                   
                posteriors *= np.ones (2) - self.likelihoods[:,i]
            posteriors = posteriors / np.linalg.norm (posteriors)  # normalise
        if posteriors[0] > 0.5:
            return ['ham', posteriors[0]]
        return ['spam', posteriors[1]]    

    def score (self, messages, labels):
        confusion = np.zeros(4).reshape (2,2)
        for m, l in zip (messages, labels):
            if self.predict(m)[0] == 'ham' and l == 'ham':
                confusion[0,0] += 1
            elif self.predict(m)[0] == 'ham' and l == 'spam':
                confusion[0,1] += 1
            elif self.predict(m)[0] == 'spam' and l == 'ham':
                confusion[1,0] += 1
            elif self.predict(m)[0] == 'spam' and l == 'spam':
                confusion[1,1] += 1
        return (confusion[0,0] + confusion[1,1]) / float (confusion.sum()), confusion
