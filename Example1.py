import falcon
import json

class ThingsResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        greeting = 'Hello world!'
        print(json.dumps(greeting))
        resp.body = json.dumps(greeting)
        
    def on_post(self, req, resp):
        """Handles POST requests"""
        print("!!!!!!!!!!!!!!!!!!!!!")
        #try:
        raw_json = req.stream.read()
        #except Exception as ex:
        #raise falcon.HTTPError(falcon.HTTP_400,
        #        'Error',
        #        ex.message)
        print("hestsnorre: " + str(raw_json))
 
        try:
            result_json = json.loads(raw_json.encode('UTF-8'))
        except ValueError as ex:
            #print(ex)
            raise falcon.HTTPError(falcon.HTTP_400,
                'Malformed JSON',
                'Could not decode the request body. The '
                'JSON was incorrect.')
 
        resp.status = falcon.HTTP_202
        resp.body = json.dumps(result_json, encoding='UTF-8')
        
class OrdersResource(object):
    def on_get(self, req, resp, user_id):
        """Handles GET requests for orders"""
        resp.set_header('Content-Type', 'text/plain')
        resp.status = falcon.HTTP_200
        resp.body = 'You inquired about order: {0}'.format(user_id)
 
 
# falcon.API instances are callable WSGI apps
wsgi_app = api = falcon.API()
 
# Resources are represented by long-lived class instances
things = ThingsResource()
orders = OrdersResource()
 
# things will handle all requests to the '/things' URL path
api.add_route('/things', things)
api.add_route('/orders/{user_id}', orders)

