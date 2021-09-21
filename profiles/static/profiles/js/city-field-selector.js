let citySelected = $('#id_default_town_or_city').val();
if (!citySelected) {
    $('#id_default_town_or_city').css('color', '#93a5b6');
};
$('#id_default_town_or_city').change(function () {
    citySelected = $(this).val();
    if (!citySelected) {
        $(this).css('color', '#93a5b6');
    } else {
        $(this).css('color', '#000000');
    }
});