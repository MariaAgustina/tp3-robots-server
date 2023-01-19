
class PredictionResult(object):

    def __init__(self, predictionID):

        #TODO: define yolo path and replace
        with open('../yolov5/runs/detect/' + predictionID + '/labels/prediction_image.txt') as f:
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
        print("Image prediction: ")
        print("Prediction class: " + self.prediction_class + " conf: " + self.conf + " x: " + self.x + " y: " + self.y + " width: " + self.w + " height: " + self.h)

    def translateTextura(self):
        if self.prediction_class == "0":
            return "nylon"
        elif self.prediction_class == "1":
            return "cuero"
        elif self.prediction_class == "2":
            return  "gamuza"