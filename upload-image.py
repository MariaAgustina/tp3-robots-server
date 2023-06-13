import falcon, json
import base64
import subprocess, sys
from GetColor import ImageProcessor
from datetime import datetime
import time
import PredictionResult
from Service import SearchProductService
from Service import ImagesService
from Models import SimilarImagesManager
from Models import Product
class ProcessImageResource(object):
  def __init__(self):
    print("Server initialized")


class ImagePredictor(object):
  def __init__(self):
    print("Process Image Predictor initialized")

  def on_post(self, req, resp):
    print("Started prediction")

    #TODO: this will not work for concurrent requests, should use results-id and uploaded-images-id and also remove it after getting answers
    SimilarImagesManager.SimilarImagesManager([]).removeContents("results/")
    SimilarImagesManager.SimilarImagesManager([]).removeContents("uploaded-images/")

    input_image_json = req.media
    image = input_image_json["image"]
    image_id = input_image_json["id"]

    if(image_id):
        image_dir = "uploaded-images/{}.png".format(image_id)

        decodeit = open(image_dir, 'wb')
        decodeit.write(base64.b64decode((image)))
        decodeit.close()

        dt = datetime.now()
        predictionID = str(time.mktime(dt.timetuple()) + dt.microsecond / 1e6).replace(".","")
        # TODO: define yolo path and replace
        # TODO: run the two process at the same time
        subprocess.run(
          ['python3',
           '../yolov5/detect.py',
           '--weights',
           'best-640.pt',
           '--img-size','640',
           '--conf','0.2',
           '--source',
           image_dir,
           '--save-crop',
           '--save-conf',
           '--save-txt',
           '--name',
           predictionID
           ]
        )
        pathTextura = predictionID + "-textura"
        subprocess.run(
            ['python3',
             '../yolov5/detect.py',
             '--weights',
             'best-texturas-mezcladas-640-new.pt',
             '--img-size','640',
             '--conf','0.2',
             '--source',
             image_dir,
             '--name',
             pathTextura,
             '--save-txt',
             '--save-conf'
             ])
        resultTextura = PredictionResult.PredictionResult(pathTextura)
        resultTextura.print()
        imageProcessor = ImageProcessor()
        imageProcessor.processColor(predictionID)

    print("Prediccion: " "cartera " + resultTextura.texturaTranslation + " " + imageProcessor.selectedColor.translation)

    products = SearchProductService.SearchProductService().getProducts()
    productsWithImages = ImagesService.ImagesService().getImages(products)
    mathcProduct = SimilarImagesManager.SimilarImagesManager(productsWithImages).searchSimiliar()

    print("Prediccion: " "cartera " + resultTextura.texturaTranslation + " " + imageProcessor.selectedColor.translation)
    resp.body = json.dumps( mathcProduct.encode() )




app = application = falcon.App()
companies_endpoint = ProcessImageResource()
app.add_route('/similar-image', companies_endpoint)
image_predictor_endpoint = ImagePredictor()
app.add_route('/predict-image', image_predictor_endpoint)