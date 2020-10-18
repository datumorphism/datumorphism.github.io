document.addEventListener('DOMContentLoaded', function () {
	var cardToggles = document.getElementsByClassName('card-toggle');
	for (var i = 0; i < cardToggles.length; i++) {
		cardToggles[i].addEventListener('click', function (e) {
			e.currentTarget.parentElement.parentElement.childNodes[3].classList.toggle('is-hidden');
		});
	}


});
