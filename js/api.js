const baseURL = "http://127.0.0.1:8000/" 

async function getEventList() {
	try {
	  const response = await fetch(baseURL + 'api/v1/event/', {
		method: 'GET',
		headers: {
		  'Content-Type': 'application/json'
		}
	  });
	  if (!response.ok) {
		throw new Error('Network response was not ok');
	  }
	  return response.json();
	} catch (error) {
	  return Promise.reject(error);
	}
  }


//form.addEventListener('submit', (event) => {
//	event.preventDefault()
//	document.getElementById('formBtn').hidden = true;
//
//	// Fetch the form data
//	const formData = new FormData(form);
//
//	// Convert form data to JSON object
//	const data = {};
//	formData.forEach((value, key) => {
//		data[key] = value;
//	});
//	fetch(`https://worker.silkthreaddev.com/api/v1/SiteForm/`, {
//		method: 'POST',
//		body: JSON.stringify(data),
//		headers: {
//		'Content-Type': 'application/json'
//		}
//	})
//	.then((res) => {
//		if (res.ok) {
//			window.location.href = "/contact/thanks.html"; 
//		} else {
//			return res.json();
//		}
//	})
//	.catch((error) => alert('Services form backend issue:', error));
//	
//});