"""
- create an application instance and run the dev server
"""

if __name__ == '__main__':
    from surveyapi.application import create_app
    app = create_app()
    app.run()

