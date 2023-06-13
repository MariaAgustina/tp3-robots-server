from os.path import exists

class PredictionResult(object):

    def __init__(self, predictionID):

        #TODO: define yolo path and replace
        path = '../yolov5/runs/detect/' + predictionID + '/labels/prediction_image.txt'
        self.texturaTranslation = ""
        file_exists = exists(path)
        self.hasPrediction = file_exists
        if self.hasPrediction:
            with open(path) as f:
                line = f.readline()
            predictionRow = line.split(" ")
            f.close()

            self.prediction_class = predictionRow[0]
            self.x = predictionRow[1]
            self.y = predictionRow[2]
            self.w = predictionRow[3]
            self.h = predictionRow[4]
            self.conf = predictionRow[5]
            self.texturaTranslation = self.translateTextura()

    def print(self):
        if self.hasPrediction:
            print("Image prediction: ")
            print("Prediction class: " + self.prediction_class + " conf: " + self.conf + " x: " + self.x + " y: " + self.y + " width: " + self.w + " height: " + self.h)
        else:
            print("No prediction")

    def translateTextura(self):
        if self.hasPrediction:
            if self.prediction_class == "0":
                return "nylon"
            elif self.prediction_class == "1":
                return "cuero"
            elif self.prediction_class == "2":
                return  "gamuza"
        else:
            return ""