const express = require('express');
const app = express();
const path = require('path');
const bodyParser = require('body-parser');
const routes = require('./routes');
const nunjucks = require('nunjucks');

app.use(bodyParser.text());
app.use('/static', express.static(path.resolve('static')));

nunjucks.configure('./views', {
	autoescape: true,
	express: app
});

app.set('views', './views');
app.use(routes());

app.all('*', (req, res) => {
	return res.status(404).send({
		message: '404 page not found'
	});
});

(async () => {
	app.listen(1337, '0.0.0.0', () => console.log('Listening on port 1337'));
})();
