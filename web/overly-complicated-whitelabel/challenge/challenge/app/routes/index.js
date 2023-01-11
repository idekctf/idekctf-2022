const {spawnSync} = require('child_process');
const path = require('path');
const fs = require('fs');
const os = require('os');
const express = require('express');
const fse = require('fs-extra');

const router = express.Router();

const response = data => ({message: data});

router.get('/', (req, res) => {
	return res.render('index.html');
});

router.post('/api/create', async (req, res) => {
	const companyName = req.body;

	if (companyName && typeof companyName === 'string') {
		// make sure company name is not on black list
		if(['New Scripts Limited', 'Bad Dad Jokes ltd'].some(bannedName => {
			let splitNames = bannedName.toLowerCase().split(' ');
			return splitNames.some(namePart => companyName.toLowerCase().indexOf(namePart) !== -1)
		})) {
			return res.status(400).send(response('Nope! That name is reserved for me'));
		}

		const randomDirectory = fs.mkdtempSync(path.join(os.tmpdir(), 'generated-'));
		try {
			fse.copySync("/app/whitelabel", randomDirectory);
			const packageJsonPath = path.join(randomDirectory, 'package.json');
			const packageJson = fs.readFileSync(packageJsonPath, 'utf-8');
			const updatedPackageJson = packageJson.replace('##REPLACE_ME##', companyName);
			fs.writeFileSync(packageJsonPath, updatedPackageJson, 'utf-8');
			const result_encoded = spawnSync('yarn', ['build'], {cwd: randomDirectory, encoding: 'utf-8'});
			console.log(result_encoded.stdout)
			return res.send(response('Your new company website created! TODO: provide link to website created at: ' + randomDirectory));
		} catch (e) {
			return res.status(500).send(response('Error!'));
		}

	} else {
		return res.status(400).send(response('Please fill out all the required fields!'));
	}
});

module.exports = () => {
	return router;
};
