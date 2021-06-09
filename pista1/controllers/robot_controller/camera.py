import _thread
import socket

from PIL import Image


class Camera:
    def __init__(self, camera) -> None:
        self.camera = camera
        _thread.start_new_thread(
            self.servidor, (self.get_ip(), 8080))

    def get_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except:
            IP = '127.0.0.1'
        return IP

    def tirar_foto(self):
        img = self.camera.getImage()
        im = Image.frombytes(
            'RGBA', (self.camera.getWidth(), self.camera.getHeight()), img)
        imagem = Image.open('foto.jpg')
        imagem.paste(im)
        imagem.save('foto.jpg')

    def servidor(self, https, hport):
        print(f"Server em {https}:{hport}")
        sockHttp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sockHttp.bind((https, hport))
        except:
            sockHttp.bind(('', hport))

        sockHttp.listen(1)

        while True:
            client, addr = sockHttp.accept()
            msg = client.recv(2048).decode("utf-8")
            # print(msg)
            rota = msg.split("/")[1].split(" ")[0]
            print(rota)
            if(rota == "foto"):
                self.tirar_foto()

                # open file , r => read , b => byte format
                file = open('foto.jpg', 'rb')
                response = file.read()
                file.close()

                header = 'HTTP/1.1 200 OK\n'
                header += 'Content-Type: image/jpg\n\n'

                final_response = header.encode('utf-8')
                final_response += response
                client.sendall(final_response)
                client.close()
            else:
                # client.send(foto().encode())
                client.close()
