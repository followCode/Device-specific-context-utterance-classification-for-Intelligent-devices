import os, logging
logging.disable(logging.WARNING)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from sentence_classifier import Classifier
from dictionary_func import find

class Handler:
    def __init__(self):
        self.cls = Classifier()

    def start(self):
    
        text = input("Enter Text: ")
        _class = self.cls.predict([text])[0]

        #print("Predicted: "+str(_class))

        # Some logic to handle the processing based on class
        #
        #
        #print(type(_class))
        if _class == 3:
            if find(text) == 1:
                print("class: VALID")
                return "VALID"
            else:
                print("class: INVALID")
                return "INVALID"
        elif _class ==2 :
            print("class: INVALID")
            return "INVALID"
        else:
            print("class:VALID")
            return "VALID"

    def classify(self, text):
        _class = self.cls.predict([text])[0]

        # Some logic to handle the processing based on class
        #
        #
        print(type(_class))
        if _class == 3:
            if find(text) == 1:
                print("class: VALID")
                return "VALID"
            else:
                print("class: INVALID")
                return "INVALID"
        elif _class ==2 :
            print("class: INVALID")
            return "INVALID"
        else:
            print("class:VALID")
            return "VALID"


def main():
    """
        Example Usage
    """
    handle = Handler()
    is_valid = handle.start() 
while(True):
    main()

        
