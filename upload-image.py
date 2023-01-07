import falcon, json
import base64
import os, shutil
import subprocess, sys


class ProcessImageResource(object):
  def __init__(self):
    print("Server initialized")

  def removeContents(self,folder):
    for filename in os.listdir(folder):
      file_path = os.path.join(folder, filename)
      try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
          os.unlink(file_path)
        elif os.path.isdir(file_path):
          shutil.rmtree(file_path)
      except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

  def on_post(self, req, resp):
    self.removeContents("results/")
    self.removeContents("uploaded-images/")

    input_image_json = req.media
    for image_and_id_dictionaries in input_image_json:
      image = image_and_id_dictionaries["image"]
      name = image_and_id_dictionaries["id"]

      if(name):
        image_dir = "uploaded-images/{}.png".format(name)

        decodeit = open(image_dir, 'wb')
        decodeit.write(base64.b64decode((image)))
        decodeit.close()

    os.system('python3 get_image_feature_vectors.py')
    os.system('python3 cluster_image_feature_vectors.py')

    f = open('nearest_neighbors.json','rb')
    data = json.load(f)
    resp.body = json.dumps(data)
    f.close()

class ImagePredictor(object):
  def __init__(self):
    print("Process Image Predictor initialized")

  def on_post(self, req, resp):
    input_image_json = req.media
    image = input_image_json["image"]
    image_id = input_image_json["id"]

    if(image_id):
        image_dir = "uploaded-images/{}.png".format(image_id)

        decodeit = open(image_dir, 'wb')
        decodeit.write(base64.b64decode((image)))
        decodeit.close()

        subprocess.run(['python3', '../yolov5/detect.py','--weights','best-640.pt','--img-size','640','--conf','0.2','--source',image_dir])

    resp.body = json.dumps({"prediction": "cartera cuero negra"})


app = application = falcon.App()
companies_endpoint = ProcessImageResource()
app.add_route('/similar-image', companies_endpoint)
image_predictor_endpoint = ImagePredictor()
app.add_route('/predict-image', image_predictor_endpoint)