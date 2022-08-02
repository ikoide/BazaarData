from bazaar.app import create_app, register_scheduler

app = create_app()
register_scheduler(app)

if __name__ == "__main__":
    ## Development
    app.run(port=9000)

    ## Production
    #app.run(config_filename="flask_prod.cfg")
