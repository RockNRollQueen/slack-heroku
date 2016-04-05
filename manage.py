import web

urls = (
  '/hello', 'Index'
)


app = web.application(urls, globals())

class Index(object):
    def GET(self):
        form = web.input()
        print form
        if 'command' in form and 'text' in form and 'user_name' in form:
          return "{} slaps {} with large trout".format(form.user_name, form.text)          
        return form

if __name__ == "__main__":
    app.run()
