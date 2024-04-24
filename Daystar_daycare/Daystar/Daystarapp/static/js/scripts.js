$(document).ready(function() {
    $('.menu-toggle').on('click', function() {
        $('.navli').toggleClass('showing');
        $('.navli ul').toggleClass('showing');
    });
});