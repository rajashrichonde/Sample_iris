import config
import numpy as np
import pickle
import json

class IrisSpecies():
    def __init__(self,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm):
        self.SepalLengthCm = SepalLengthCm
        self.SepalWidthCm = SepalWidthCm
        self.PetalLengthCm = PetalLengthCm
        self.PetalWidthCm = PetalWidthCm

    def load_model(self):
        with open(config.ENCODER_FILE_PATH,'r') as f:
            self.enc = json.load(f)
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model =  pickle.load(f)

    def predict_species(self):
        self.load_model()
        test_arr = np.zeros(len(self.enc['columns']))
        test_arr[0] = self.SepalLengthCm
        test_arr[1] = self.SepalWidthCm
        test_arr[2] = self.PetalLengthCm
        test_arr[3] = self.PetalWidthCm

        test_pred = self.model.predict([test_arr])[0]
        prediction = self.enc['target'][str(test_pred)]

        return prediction
print("chonde")

        
