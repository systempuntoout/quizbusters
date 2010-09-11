#!/usr/bin/env python
from config import view 
import web

# App handling
urls = (
    '/?', 'app.controllers.quizbusters.index',
    '/quiz', 'app.controllers.quizbusters.quiz',
    '/ranking', 'app.controllers.quizbusters.ranking',
    '/ranking/(\d+)', 'app.controllers.quizbusters.ranking',
    '/downloads', 'app.controllers.quizbusters.downloads',
    '/about', 'app.controllers.quizbusters.about',
    '/api/ranking', 'app.api.web.quizbusters.ranking',
    '/api/statistics', 'app.api.web.quizbusters.statistic',
    
)
app = web.application(urls, globals())

# Session handling
if web.config.get('_session') is None:
    session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'current_game':None})
    web.config._session = session
    web.localsession=session
else:
    session = web.config._session
    web.localsession=session

# Error handling
def notfound():
    return web.notfound(view.oops())
def internalerror():
    return web.notfound(view.oops())
app.internalerror = internalerror
app.notfound = notfound


if __name__ == "__main__":
    app.run()