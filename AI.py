import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import random


class AI:
    def __init__(self, noofInputs=5, outputs=3):
        self.noofInputs = 5
        self.createNeuralNet()

    def createNeuralNet(self, hiddenLayers=[4]):
        """Create Neural Net-#of Inputs=# of distances and 3 outputs matching ARROW_LEFT ARROW_UP ARROW_RIGHT"""
        model = Sequential()
        model.add(Dense(5, activation="relu", input_shape=(5,), use_bias=False))

        for i in hiddenLayers:
            model.add(Dense(i, activation="relu", use_bias=False))

        model.add(Dense(3, activation="sigmoid", use_bias=False))
        model.compile(optimizer="adam", loss="categorical_crossentropy")
        self.model = model

    def predict(self, distances):
        # print(distances)
        return self.model.predict(np.expand_dims(distances, axis=0))

    def getWeightsVector(self):
        weights = np.array(self.model.get_weights())
        # print(weights)

        self.weightsShapes = []
        self.weightsVector = []
        for i in weights:
            self.weightsShapes.append(i.shape)
            vec = i.flatten()
            for j in vec:
                self.weightsVector.append(j)

        return self.weightsVector

    def setWeightsFromVector(self):
        # noflayers=len(self.weightsShape)#  # oflayers
        weights = []
        start = 0
        for shape in self.weightsShapes:
            noofWeigths = shape[0] * shape[1]
            data = np.array(self.weightsVector[start : start + noofWeigths])

            weights.append(data.reshape(shape))
            start += noofWeigths
        # print(self.weightsVector)
        # print("================================NEW WEIGTHS================================")
        # for i in weights:
        #    print("================================================================")
        #    print(i)
        self.model.set_weights(weights)


if __name__ == "__main__":
    x = AI()
    x.createNeuralNet()
    distances = list(range(5))
    x.predict(distances)
