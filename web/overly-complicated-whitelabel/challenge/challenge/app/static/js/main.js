let createBtn = document.querySelector('#create');
let companyNameInput = document.querySelector('#company-name');
let responseMsg = document.querySelector('#resp-msg');
createBtn.addEventListener('click', async () => {
	responseMsg.classList.remove('hidden');
	responseMsg.innerText = 'Please wait...';
	await fetch('/api/create', {
		method: 'POST',
		body: companyNameInput.value
	})
		.then((response) => response.json()
			.then((resp) => {
				responseMsg.innerText = resp.message;
			}))
		.catch((error) => {
			console.error(error);
		});
})
