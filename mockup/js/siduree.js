$(document).ready(function() {
    var slides = $('.slide');
    slides.each(function () {
	var slide = $(this);
	slide.find('.photo-background').each(function () {
	    var photo = $(this);
	    photo.attr({
		'data-center': 'background-position: 50% 0px;',
		'data-top-bottom': 'background-position: 50% -200px;',
		'data-anchor-target': '#' + slide.attr('id')
	    });
	    var content = photo.find('.photo-content');
	    content.attr({
		'data-center': 'bottom: 200px; opacity: 1',
		'data-top': 'bottom: 1200px; opacity: 0.5'
	    });
	    var img_url = slide.attr('data-photo');
	    photo.css({
		'background-image': 'url(' + img_url + ')',
		'background-position': 'center center',
		'background-repeat': 'no-repeat',
		'background-attachment': 'fixed',
		'background-size': 'cover',
		'height': '100%',
		'width': '100%'
	    });
	});
	slide.height($(window).height());
    });

    var skr = skrollr.init({
	forceHeight: false
    });
    skr.refresh(slides);
}); 
