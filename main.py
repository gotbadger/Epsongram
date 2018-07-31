import os.path
import cherrypy
import pos


class Espongram:

    def show(self):
        with open('index.html', 'r') as index:
          return index.read()

    def submit(self, url):
        pos.Pos(url)
        return "Printed: %s" %  url

    @cherrypy.expose
    def index(self, url=None):
        if url:
            return self.submit(url)
        else:
            return self.show()

if __name__ == '__main__':
    cherrypy.quickstart(Espongram())
