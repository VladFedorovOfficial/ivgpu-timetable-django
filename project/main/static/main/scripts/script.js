function timetableDisplay(groupType, weekType, weekDay) {
    $('.timetable').css('display', 'none')
    $('.timetable[data-timetable-group="' + groupType +
    '"][data-timetable-weekType="' + weekType +
    '"][data-timetable-weekDay="' + weekDay + '"]').css('display', 'flex')
}

function getWeekNum(day, month, year) {
    month++;
    let a = Math.floor((14 - month) / 12);
    let y = year + 4800 - a;
    let m = month + 12 * a - 3;
    let J = day + Math.floor((153 * m + 2) / 5) + 365 * y + Math.floor(y / 4) -
        Math.floor(y / 100) + Math.floor(y / 400) - 32045;
    d4 = (((J + 31741 - (J % 7)) % 146097) % 36524) % 1461;
    let L = Math.floor(d4 / 1460);
    let d1 = ((d4 - L) % 365) + L;
    let week = Math.floor(d1 / 7) + 1;
    if (week < 10) week = '0' + week;
    return week;
}

$(document).ready(function() {
    $('.tt-additInfo').each(function(){
        if ($(this).is(':empty')) {
            $(this).parent('.tt-lesson').addClass('free-time')
            $(this).parent('.tt-lesson').html('Свободное время<span class="tt-additInfo"></span>')
        }
    })
})

$('.tt-lesson').click(function() {
    if (!($(this).children('.tt-additInfo').is(':empty'))) {
        $('.tt-additInfo').css('opacity', '0')
        $('.tt-row').css('height', '3rem')

        $(this).children('.tt-additInfo').css('opacity', '0.7')
        $(this).parent('.tt-row').css('height', '4.5rem')
    }
})

$(function() {
    $( "#datepicker" ).datepicker({
        beforeShowDay: $.datepicker.noWeekends,
        showOtherMonths: true,
        firstDay: 1,
        onSelect: function (date, datepicker) {
            if (date != '') {
                var date = date.split('/')
                if (getWeekNum(parseInt(date[1]), parseInt(date[0]), parseInt(date[2]))%2==1) {
                    var weekType = "Первая"
                } else {
                    var weekType = "Вторая"
                }

                weekDay = ["Воскресенье","Понедельник","Вторник","Среда","Четверг","Пятница","Суббота"][(new Date(date[2]+'-'+date[0]+'-'+date[1])).getDay()]
                
                if ($('#ui-group-first:checked').length > 0) {
                    timetableDisplay('x', weekType, weekDay)
                } else if ($('#ui-group-second:checked').length > 0) {
                    timetableDisplay('xx', weekType, weekDay)
                }
            }
        }
    })
});