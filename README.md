# Device-specific-context-utterance-classification-for-Intelligent-devices


## Introduction
Utterance is any sentence given to an intelligent device. Valid utterances are the sentences for which the device could perform some action. If no action is possible for a sentence, then it is simply an invalid utterance. This project describes a method for utterance classification that does not require manual transcription of training data.
It emphasizes on classifying any given input as a valid or invalid utterance, based on the action coupled with the utterance.
 
## Dataset
The dataset used for training is created from parsing out the SQuAD dataset and combining it with the SPAADIA dataset.
Stanford Question Answering Dataset (SQuAD) is a reading comprehension dataset, consisting of questions posed by crowdworkers on a set of Wikipedia articles, where the answer to every question is a segment of text, or span, from the corresponding reading passage, or the question might be unanswerable.
Speech Act Annotated DIAlogues is a small corpus of 35 timetable information and booking interactions between a female call-centre agent and her callers. The sentences are categorized into questions, commands and statements.

## CNN for sentence classification
Even though the originally intended purpose of Convolutional Neural Networks was to recognize images, our model is built using CNN mainly for the mathematical operations performed by it’s hidden layers which allows the network to identify features from the input data that may not have been learnt by other models such as the Multilayer perceptron. Also, of all the models that were developed the CNN model was able to provide an inference in the least amount of time. One aspect of implementing a CNN is that the input vectors are to be padded so as to have the desired input size for the model.

