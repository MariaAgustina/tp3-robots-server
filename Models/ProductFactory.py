from Models import Product

class ProductFactory(object):

    def createProduct(self, dictionary):
        products = []
        productsDictionary = dictionary["results"]
        for productDic in productsDictionary:
            product = Product.Product()
            product.thumbnail = productDic["thumbnail"]
            product.price = productDic["price"]
            product.id = productDic["id"]
            product.permalink = productDic["permalink"]
            product.title = productDic["title"]
            products.append(product)
            product.print()
        return products


