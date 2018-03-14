import falcon
import json
#import io
#import cors
#import os
class Access(object):
    def process_request(self,req,resp):
        print(req.remote_addr)

api = application = falcon.API(middleware = [Access()])

class RedResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        #JSON_object
        greeting = {'greeting':'Hello world /Server!'}

        resp.content_type = "application/json"
        resp.content_length = len(greeting)
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(greeting)


class HelloResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        #JSON_object
        greeting = {'greeting':'Hello client /Server!'}

        resp.content_type = "application/json"
        resp.content_length = len(greeting)
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(greeting)

    def on_post(self, req, resp):
        """Handles POST requests"""
        """doc = {
            'images': [
                {
                    'href': '/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png'
                }
            ]
        }"""
        print('req.params: '+str(req.params))
        print('req.headers: '+str(req.headers))
        print('req.uri: '+str(req.uri))
        print('req: '+str(req))

        #Get the data (it will be in bytes)
        data = req.stream.read()
        print('data-type: '+str(type(data)))
        
        #Decode into a string
        decodedData = data.decode('utf-8')
        print('decodedData-type: '+str(type(decodedData)))
        
        #Load into dictionary
        reqDoc = json.loads(decodedData)
        print('reqDoc-type: '+str(type(reqDoc)))

        doc = {'requestGreeting':reqDoc['greeting'],'greeting':'Hello client! /PostResponse!'}

        # Create a JSON representation of the resource
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(doc, ensure_ascii=False)

class ColorResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        #JSON_object
        greeting = {'greeting':'Hello client /Server!'}

        resp.content_type = "application/json"
        resp.content_length = len(greeting)
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(greeting)

    def on_post(self, req, resp):
        """Handles POST requests"""
        """A better way of using post is to store the
        incoming data (for instance, which color, and 
        which history of colors for this specific ID). 
        It can then give
        back the new color to use, or just send
        an OK message"""
        print('req.params: '+str(req.params))
        print('req.headers: '+str(req.headers))
        print('req.uri: '+str(req.uri))
        print('req: '+str(req))

        #Get the data (it will be in bytes)
        data = req.stream.read()     
        #Decode into a string
        decodedData = data.decode('utf-8')
        #Load into dictionary
        reqDoc = json.loads(decodedData)
        print(reqDoc)
        if(reqDoc['color'] == 'black'):
            doc = {'color':'gray'}
        elif(reqDoc['color'] == 'gray'):
            doc = {'color':'black'}
        else:
            doc = {'color':'black'}

        # Create a JSON representation of the resource
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(doc, ensure_ascii=False)

class OrdersResource(object):
    def on_get(self, req, resp, user_id):
        """Handles GET requests for orders"""
        #resp.set_header('Content-Type', 'text/plain')
        resp.content_type = 'text/plain'
        resp.status = falcon.HTTP_200
        resp.body = 'You inquired about order: {0}'.format(user_id)

#Initiation
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

# FrontEnd resources classes
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

# FrontEnd resources
style = StyleResource()
mainJs = JSResource()
hello = HelloResource()

# Other resources
init = getFrontEndResource()
orders = OrdersResource()
color = ColorResource()

#FrontEnd routes
api.add_route('/', init)
api.add_route('/styles/style.css', style)
api.add_route('/scripts/main.js', mainJs)

# Other routes
api.add_route('/hello', hello)
api.add_route('/orders/{user_id}', orders)
api.add_route('/color', color)
