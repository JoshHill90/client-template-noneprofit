const eventList = document.getElementById('eventList')
console.log(eventList)
document.addEventListener('DOMContentLoaded', () => {
	getEventList()
	.then((response) => {
		console.log(response.length)
		const eventsList = response
		for (i = 0; i < eventsList.length; ++i) {
			const id = eventsList[i].id
			console.log(id, 'id')
			const title = eventsList[i].title
			const date = eventsList[i].date
			let startHour
			let endHour
			let startMarta
			let endMarta
			// star time
			const checkStartHour = eventsList[i].start.split(":")[0]
			if (checkStartHour > 12 ) {
				startHour = checkStartHour - 12
				startMarta = 'PM'
			} else {
				startHour = checkStartHour
				 = 'AM'
			}
			const startMin = eventsList[i].start.split(":")[1]
			const start = `${startHour}:${startMin} ${startMarta}`
			//end time
			const checkEndHour = eventsList[i].start.split(":")[0]

			if (checkEndHour > 12 ) {
				endHour = checkEndHour - 12
				endMarta = 'PM'
			} else {
				endMarta = "AM"
				endHour = checkEndHour
			}
			const endMin = eventsList[i].end.split(":")[1]
			const end = `${endHour}:${endMin}  ${endMarta}`

			const details = eventsList[i].details
			const imageLink = eventsList[i].image_link
			const eventType = eventsList[i].event_type
	
			const rowDiv = document.createElement('button');
			rowDiv.classList.add('row', 'event-item');
			
	
			// Create three divs with class "col-4" and different ids
			const titleDiv = document.createElement('div');
			titleDiv.classList.add('col-4');
			titleDiv.id = 'title';
	
			const dateDiv = document.createElement('div');
			dateDiv.classList.add('col-4');
			dateDiv.id = 'date';
	
			const timeDiv = document.createElement('div');
			timeDiv.classList.add('col-4');
			timeDiv.id = 'time';
	
			// Create p elements with class "p-p" and append them to the respective divs
			const titleP = document.createElement('p');
			titleP.classList.add('p-p');
			titleP.textContent = title;
			titleDiv.appendChild(titleP);
	
			const dateP = document.createElement('p');
			dateP.classList.add('p-p');
			dateP.textContent = date;
			dateDiv.appendChild(dateP);
	
			const timeP = document.createElement('p');
			timeP.classList.add('p-p');
			timeP.appendChild;
			timeP.textContent = `${start} - ${end}`
			timeDiv.appendChild(timeP);
	
			// Append the divs to the row div
			rowDiv.appendChild(titleDiv);
			rowDiv.appendChild(dateDiv);
			rowDiv.appendChild(timeDiv);
			eventList.appendChild(rowDiv);
	
		}

	})
})