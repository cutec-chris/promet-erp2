import bottle
app = bottle.app()
import promet_rest
@bottle.get('/')
@bottle.get('/index.html')
@bottle.get('/<filepath>')
def get_interface(filepath='/index.html'):
    return ''
app.run(port=8085)