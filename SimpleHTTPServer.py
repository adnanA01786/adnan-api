from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os
import string
import API
# Custom HTTPRequestHandler class for responding to
# a GET
class HTTPHAndlerClass(BaseHTTPRequestHandler):
 
  # handle GET 
  def do_GET(self):

    API_STRING="API_Call="
    
    try:  
      index = self.path.find(API_STRING)

      # only respond to a valid GET
      if index > -1:
        parsed = API.checkCommand(self.path, API_STRING)
        try:
            response = API.constructResponse2(API.calculateReturn(int(parsed)))
        except:
            # invalid or no value given
            response = API.constructResponse2("Invalid Get Request")
        
        # send code 200 response
        self.send_response(200)
        # send header for the return file
        self.send_header('Content-Disposition', 'attachment;filename=json_Response')
        self.end_headers()
        # write the file
        self.wfile.write(response)
        
        return
      
    except IOError:
      self.send_error(404, 'file not found')
  
def run():
  print('http server is starting...')

  #ip and port of servr
  #by default http server port is 80
  server_address = ('127.0.0.1', 80)
  httpd = HTTPServer(server_address, HTTPHAndlerClass)
  print('http server is running...')
  httpd.serve_forever()
  
if __name__ == '__main__':
  run()