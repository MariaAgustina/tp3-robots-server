import os
import shutil
import subprocess, sys
import base64, json

class SimilarImagesManager(object):

    def __init__(self,products):
        self.products = products

    def searchSimiliar(self):
        for product in self.products:
            image = product.imageData
            name = product.id

            if (name):
                image_dir = "uploaded-images/{}.png".format(name)

                decodeit = open(image_dir, 'wb')
                decodeit.write(image)
                decodeit.close()

        os.system('python3 get_image_feature_vectors.py')
        os.system('python3 cluster_image_feature_vectors.py')

        f = open('nearest_neighbors.json', 'rb')
        data = json.load(f)
        print(data)
        f.close()
       # matchProduct = [product for product in self.products if data[0]["similar_pi"] == product.id]
        for product in self.products:
            if data[0]["similar_pi"] == product.id:
                product.print()
                return product


    def removeContents(self, folder):
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))