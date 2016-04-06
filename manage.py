import web
import json

urls = (
  '/slap', 'Index'
)


app = web.application(urls, globals())

class Index(object):
    def POST(self):
        form = web.input()
        if 'command' in form and 'text' in form and form.text.strip():
          web.header('Content-type', 'application/json')
          return json.dumps({"response_type": "in_channel", "text": "Slaps {} around a bit with a large trout".format(form.text)})
        return "Use as '/slap username'"

if __name__ == "__main__":
    app.run()
