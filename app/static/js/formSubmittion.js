function SubForm() {
  $("#input-field-div").submit(function(e){
    e.preventDefault();
  });
  
	val=document.getElementById('input-field').value
	fetch('https://api.apispreadsheets.com/data/15146/', {
		method: 'POST',
		body: JSON.stringify({
			data: { 'email-field': val }
			
		}),
	}).then((res) => {
		if (res.status === 201) {
			alert('Email Submitted')
		} else {
			alert('Error Email Not Submitted')
		}
	});
}
