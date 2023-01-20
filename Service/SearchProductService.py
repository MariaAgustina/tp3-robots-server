import urllib3
from Service import ServiceConstants
from Models import ProductFactory
import json
from Service import ImagesService

class SearchProductService(object):

    def __init__(self):
        #TODO: eliminar valores hardcodeados
        self.url = "https://api.mercadolibre.com/sites/MLA/search?q=cartera%20cuero%20negra"
        self.accessToken = ServiceConstants.access_token

    def getProducts(self):
        headers = { "Authorization": self.accessToken }
        http = urllib3.PoolManager()
        r = http.request(
            'GET',
            self.url,
            headers=headers
        )

        #TODO: si hay error?
        products = ProductFactory.ProductFactory().createProduct(json.loads(r.data))
        return products
