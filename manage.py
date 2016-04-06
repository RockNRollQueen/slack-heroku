import web
import json

urls = (
  '/slap', 'Index',
  '/auth', 'Index'
)


app = web.application(urls, globals())

class Index(object):
    def GET(self):
        form = web.input()
        if 'code' in form:
          raise web.seeother("https://slack.com/oauth/authorize?client_id=10543882263.32313872259&scope=channels%3Aread+chat%3Awrite%3Abot")
        if 'error' in form:
          return "Canceled"
        return "Use as '/slap username'"

    def POST(self):
        form = web.input()
        if 'command' in form and 'text' in form and form.text.strip():
          web.header('Content-type', 'application/json')
          return json.dumps({"response_type": "in_channel", "text": "Slaps {} around a bit with a large trout".format(form.text)})
        return "Use as '/slap username'"

if __name__ == "__main__":
    app.run()
