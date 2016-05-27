import web
import json
import urllib

urls = (
  '/slap', 'Index',
  '/auth', 'Index'
)

client = "10543882263.32313872259"
secret = "57a21accddf8106e47cece4e9e6b3b52"
scope = "channels%3Aread+chat%3Awrite%3Abot"

app = web.application(urls, globals())

class Index(object):
    def GET(self):
        form = web.input()
        if 'code' in form and form.code == client:
          raise web.seeother("https://slack.com/oauth/authorize?client_id={}&scope={}".format(client, scope))
        if 'code' in form and form.code != client:
          # must save token from url #
          urllib.urlopen("https://slack.com/api/oauth.access?client_id={}&client_secret={}&code={}".format(client, secret, form.code))
          return "Installed"
        if 'error' in form:
          return "Canceled"
        return "Auth must be work from 'Add button'"

    def POST(self):
        form = web.input()
        if 'command' in form and 'text' in form and form.text.strip():
          web.header('Content-type', 'application/json')
          if form.text == "Kami-sama" or form.text == "@Kami-sama" or form.text == "Kami-sama" or form.text == "@masha":
            return json.dumps({"response_type": "in_channel", "text": "You can not beat the girls!"})
          else:
            return json.dumps({"response_type": "in_channel", "text": "Slaps {} around a bit with a large trout".format(form.text)})
        return "Use as '/slap username'"

if __name__ == "__main__":
    app.run()
