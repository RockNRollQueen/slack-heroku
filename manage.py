import web

urls = (
  '/hello', 'Index'
)


app = web.application(urls, globals())

class Index(object):
    def GET(self):
        form = web.input()
#        greeting = "Slaps %s with large trout" % form.name
        print form
        return form

if __name__ == "__main__":
    app.run()
