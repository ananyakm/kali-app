var slideIndex = 1;
var	slideIndex1 = 1;
showSlides(slideIndex);
showContent(slideIndex1);

function plusSlides(n) {
	showSlides((slideIndex += n));
	showContent((slideIndex1 += n));
}

function currentSlide(n) {
	showSlides((slideIndex = n));
	showContent((slideIndex1 = n));
}

function showSlides(n) {
	var i;
	var slides = document.getElementsByClassName('main-body-right-img-gallery');
	var dots = document.getElementsByClassName('dot');
	if (n > slides.length) {
		slideIndex = 1;
	}
	else if (n < 1) {
		slideIndex = slides.length;
	}
	for (i = 0; i < slides.length; i++) {
		slides[i].style.display = 'none';
	}
	for (i = 0; i < dots.length; i++) {
		dots[i].className = dots[i].className.replace(' active', '');
	}
	// console.log("img"+slideIndex)
	slides[slideIndex - 1].style.display = 'block';
	dots[slideIndex - 1].className += ' active';
}

function showContent(n) {
	var i;
	var slides = document.getElementsByClassName('main-body-left-contents');
	var dots = document.getElementsByClassName('dot');
	if (n > slides.length) {
		slideIndex1 = 1;
	}
	else if (n < 1) {
		slideIndex1 = slides.length;
	}
	for (i = 0; i < slides.length; i++) {
		slides[i].style.display = 'none';
	}
	for (i = 0; i < dots.length; i++) {
		dots[i].className = dots[i].className.replace(' active', '');
	}
	// console.log("show"+slideIndex1)
	slides[slideIndex1 - 1].style.display = 'block';
	dots[slideIndex1 - 1].className += ' active';
}
