!function ($) {
	$(function(){
		$('#myCarousel').carousel();
	});
}(window.jQuery);
function show_screenshots(url, shots) {
	$.get(url).success(function(data) {
		if(shots === undefined) {
			shots = [];
		}
		$(data).find('a').each(
			function(i, ln) {
				var link = $(ln).attr('href');
				if( link.endsWith('/') ) {
					if(!link.startsWith('/')) {
						show_screenshots(url + '/' + link, shots);
					}
					return;
				}
				if(!link.contains('.')) { return; }
				var ext = link.split('.').pop().toLowerCase();
				if(ext === 'jpeg' || ext === 'jpg' || ext === 'png') {
					shots.push([url + '/' + link, link]);
				}
			}
			); //each link
		$.slimbox(shots, 0);
	} //get success
	);
}
$('#screenshot-link').css('cursor', 'pointer');
$('#screenshot-link').click(function() { show_screenshots('materiale/screenshot'); });
