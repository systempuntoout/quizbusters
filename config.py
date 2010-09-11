import web

# Database
db = web.database(dbn='sqlite', db='quiz.db')

# Debug error messages and reloader
web.config.debug = True
 
# Template caching
cache = False

# Base template
view = web.template.render('app/views',base='layout', cache=cache)

