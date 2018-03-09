import falcon
import json
import io

api = application = falcon.API()

#var io = require('socket.io')()

class ThingsResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        greeting = 'Hello world /Server!'
        #print(json.dumps(greeting))
        resp.body = json.dumps(greeting)
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
        resp.body = json.dumps(doc, ensure_ascii=False)

        # The following line can be omitted because 200 is the default
        # status returned by the framework, but it is included here to
        # illustrate how this may be overridden as needed.
        resp.status = falcon.HTTP_200
        
class OrdersResource(object):
    def on_get(self, req, resp, user_id):
        """Handles GET requests for orders"""
        resp.set_header('Content-Type', 'text/plain')
        resp.status = falcon.HTTP_200
        resp.body = 'You inquired about order: {0}'.format(user_id)
 
 
# falcon.API instances are callable WSGI apps
#wsgi_app = api = falcon.API()
 
# Resources are represented by long-lived class instances
things = ThingsResource()
orders = OrdersResource()
#colorsorbeast = 
 
# things will handle all requests to the '/things' URL path
api.add_route('/things', things)
api.add_route('/orders/{user_id}', orders)
#api.add_route('/colorsorbeasts', colorsorbeast)