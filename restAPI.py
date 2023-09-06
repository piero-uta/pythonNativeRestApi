import http.server
import socketserver

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*') 
            self.end_headers()
            response = '{"message": "Hola, esta es una respuesta de la API"}'
            self.wfile.write(response.encode())
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/api':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            print(post_data.decode())
            # Procesar los datos POST como sea necesario aquí
            self.send_response(200)
            self.send_header('Content-type', 'application/json')            
            self.send_header('Access-Control-Allow-Origin', '*') 
            self.end_headers()
            response = '{"message": "Solicitud POST recibida correctamente"}'
            self.wfile.write(response.encode())
        else:
            super().do_POST()

port = 8080
with socketserver.TCPServer(('', port), MyHandler) as httpd:
    print(f'Servidor API en el puerto {port}')
    httpd.serve_forever()
