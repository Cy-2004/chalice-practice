from chalice import Chalice

app = Chalice(app_name='sample-api')


@app.route('/')
def index():
    return {'howdy': 'Chelsea'}

@app.route('/chelsea')
def name():
	return{'hey':'there!'}
