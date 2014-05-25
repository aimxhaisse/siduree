$(document).ready(function() {
    var slides = $('.slide');
    var current_slide = parseInt(slides.first().attr('id').split('-')[1]);

    slides.each(function () {
	var slide = $(this);
	slide.find('.photo-background').each(function () {
	    var photo = $(this);
	    photo.attr({
		'data-center': 'background-position: 50% 0px;',
		'data-top-bottom': 'background-position: 50% -500px;',
		'data-bottom-top': 'background-position: 50% 500px;',
		'data-anchor-target': '#' + slide.attr('id')
	    });

	    var title = photo.find('.photo-content');
	    title.attr({
		'data-bottom': 'top: 5%; opacity: 0',
		'data-center': 'top: 10%; opacity: 1',
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
    
    slides.waypoint(function (direction) {
	if (direction == "down") {
	    current_slide = $(this).index();
	}
    }, { offset: '50%' }).waypoint(function (direction) {
	if (direction == "up") {
	    current_slide = $(this).index();
	}
    }, { offset: '-50%'});

    var skr = skrollr.init({
	forceHeight: false
    });
    skr.refresh(slides);

    var is_sliding = false;

    var scrollTo = function (where) {
	if (!is_sliding) {
	    $('#slide-' + where).each(function () {
		is_sliding = true;
		$("html, body").animate({
		    scrollTop: ($(this).offset().top - 50 /* navbar's height */) + "px"
		}, 1500, function () {
		    is_sliding = false;
		});
	    });
	}
    };

    $('#go-up').click(function() {
	scrollTo(current_slide - 1);
	return false;
    });

    $('#go-down').click(function() {
	scrollTo(current_slide + 1);
	return false;
    });

    $(window).keypress(function(e) {
	if (e.keyCode == 0 /* space bar */) {
	    scrollTo(current_slide + 1);
	}
    });

});
