$(document).ready(function() {
    $("button.delete").click(function() {
        $(".notification").hide();
    });
    $("#nav-toggle").click(function() {
        $("#nav-toggle").toggleClass("is-active");
        $("#nav-menu").toggleClass("is-active");
    });
});
