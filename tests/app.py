import bottle
import json

app = bottle.Bottle()

@app.route('/success')
def ok():
    return 'success'

@app.route('/status/403')
def forbidden():
    bottle.abort(403, 'forbidden')

@app.route('/status/404')
def not_found():
    bottle.abort(404, 'not found')

@app.route('/postfields', method='post')
def postfields():
    return json.dumps(dict(bottle.request.forms))
