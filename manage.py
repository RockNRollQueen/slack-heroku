import web
import json

urls = (
  '/hello', 'Index'
)


app = web.application(urls, globals())

class Index(object):
    def GET(self):
        form = web.input()
        print form
        if 'command' in form and 'text' in form and 'user_name' in form:
          web.header('Content-type', 'application/json')
          return json.dumps({"response_type": "in_channel", "text": "{} slaps {} with large trout.".format(form.user_name, form.text)})
        return form

if __name__ == "__main__":
    app.run()
