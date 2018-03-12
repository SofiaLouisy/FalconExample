import falcon
import json
#import io
#import cors
#import os



api = application = falcon.API()

class getFrontEndResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        greeting = {"greeting":'Hello world /Server!'}
        #print(json.dumps(greeting))
        #resp.content_type("text/html")

        htmlFile = open("FalconExample/Client/index.html","r")
        htmlText = htmlFile.read()
        print(htmlFile.read())
        resp.content_type = "text/html"
        resp.content_length = len(htmlText)
        resp.body = htmlText
        
        resp.append_header("Access-Control-Allow-Origin","http://localhost:8080")
        #resp.body = json.dumps(greeting)
        #resp.body = greeting


    def on_post(self, req, resp):
        """Handles POST requests"""
        doc = {
            'images': [
                {
                    'href': '/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png'
                }
            ]
        }
        # Create a JSON representation of the resource
        resp.body = "Hello"#json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200

class HelloResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        greeting = {'greeting':'Hello world /Server!'}
        print(json.dumps(greeting))
        #print(json.dumps(greeting))
        #resp.content_type("text/html")

        resp.content_type = "application/json"
        resp.content_length = len(greeting)
        
        #resp.append_header("Access-Control-Allow-Origin","http://localhost:8080")
        #resp.body = json.dumps(greeting)
        resp.body = json.dumps(greeting)


class OrdersResource(object):
    def on_get(self, req, resp, user_id):
        """Handles GET requests for orders"""
        resp.set_header('Content-Type', 'text/plain')
        resp.status = falcon.HTTP_200
        resp.body = 'You inquired about order: {0}'.format(user_id)

class StyleResource(object):
    def on_get(self,req,resp):
        cssFile = open("FalconExample/Client/styles/style.css","r")
        cssText = cssFile.read()
        print(cssFile.read())
        resp.content_type = "text/css"
        resp.content_length = len(cssText)
        resp.body = cssText

class JSResource(object):
    def on_get(self,req,resp):
        jsFile = open("FalconExample/Client/scripts/main.js","r")
        jsText = jsFile.read()
        print(jsFile.read())
        resp.content_type = "text/js"
        resp.content_length = len(jsText)
        resp.body = jsText

init = getFrontEndResource()
orders = OrdersResource()
style = StyleResource()
mainJs = JSResource()
hello = HelloResource()
 
# things will handle all requests to the '/things' URL path
api.add_route('/', init)
api.add_route('/hello', hello)
api.add_route('/orders/{user_id}', orders)
api.add_route('/styles/style.css', style)
api.add_route('/scripts/main.js', mainJs)
api.add_route('/scripts/main.js', mainJs)