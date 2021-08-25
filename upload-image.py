import falcon, json
import base64
import os

class ProcessImageResource(object):
  def on_post(self, req, resp):
    input_image_json = req.media
    image = input_image_json["image"]
    name = input_image_json["name"]
    if(name):
      image_dir = "uploaded-images/{}".format(name)

      decodeit = open(image_dir, 'wb')
      decodeit.write(base64.b64decode((image)))
      decodeit.close()
      os.system('python yolov5/detect.py --weights weights-yolo.pt --source {} --project results/ --save-txt --save-crop --save-conf --augment'.format(image_dir))

      os.chdir('results/exp/crops') #TODO: muchos exp
      all_subdirs = [d for d in os.listdir('.') if os.path.isdir(d)] #TODO: podriamos pasarlos con la confianza para cuando hay mas de uno y asi el cliente muestra el de mayor confianza o hacerlo aca directamente, aparte si no hay subdirs ver que pasa
      self.result = {"result": all_subdirs}
      resp.body = json.dumps(self.result)

    else:
      #TODO: reponder 500
      self.result = []
      resp.body = json.dumps(self.result)


api = falcon.API()
companies_endpoint = ProcessImageResource()
api.add_route('/upload-image', companies_endpoint)