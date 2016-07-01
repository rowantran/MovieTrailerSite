$(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
    $("#trailer-video-container").empty();
});
$(document).on('click', '.movie', function (event) {
    var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
    var sourceUrl = 'https://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
    console.log(sourceUrl);
    $("#trailer-video-container").empty().append($("<iframe></iframe>", {
        'id': 'trailer-video',
        'type': 'text-html',
        'src': sourceUrl,
       'frameborder': 0
     }));
});