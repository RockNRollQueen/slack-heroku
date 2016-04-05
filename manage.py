import web
import json

urls = (
  '/slap', 'Index'
)


app = web.application(urls, globals())

class Index(object):
    def GET(self):
        form = web.input()
        if 'command' in form and 'text' in form and not form.text.isspace():
          print 'user -> \'' + form.text + '\''
          web.header('Content-type', 'application/json')
          return json.dumps({"response_type": "in_channel", "text": "Slaps {} with large trout.".format(form.text)})
        return form

if __name__ == "__main__":
    app.run()
