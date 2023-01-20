import urllib3
import concurrent
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait
from Models import Product

class ImagesService(object):

    def __init__(self):
        self.productWithImages = []

    def getImages(self,products):
        connection_mgr = urllib3.PoolManager(maxsize=5)
        thread_pool = ThreadPoolExecutor(5)

        futures = [thread_pool.submit(self.download, product.thumbnail, connection_mgr, product) for product in products]
        wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
        return self.productWithImages

    def download(self, url, cmanager, product):
        response = cmanager.request('GET', url)
        if response and response.status == 200:
            # TODO: si hay error?
            product.imageData = response.data
            self.productWithImages.append(product)