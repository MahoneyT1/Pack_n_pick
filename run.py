
def run_app():
    from api.v1.app import app as g
    g.run()


run_app()