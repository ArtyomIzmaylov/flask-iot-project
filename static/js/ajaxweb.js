function send_data() {
    $.ajax({
        type: 'GET',
        url: '/Temp',
        dataType: 'json',
        contentType: 'application/json',
        data: {
            "TempIn": document.getElementById("TempIn").value,
        },
        success: function(response){}
    });
}

function send_data_x2() {
    $.ajax({
        type: 'GET',
        url: '/Davl',
        dataType: 'json',
        contentType: 'application/json',
        data: {
            "DavlIn": document.getElementById("DavlIn").value,
        },
        success: function(response){}
    });
}

function send_data_x3() {
    $.ajax({
        type: 'GET',
        url: '/Kislor',
        dataType: 'json',
        contentType: 'application/json',
        data: {
            "KislorIn": document.getElementById("KislorIn").value,
        },
        success: function(response){}
    });
}

function send_data_x4() {
    $.ajax({
        type: 'GET',
        url: '/Sleeping',
        dataType: 'json',
        contentType: 'application/json',
        data: {
            "hours": document.getElementById("hours").value,
        },
        success: function(response){}
    });
}

function send_data_x5() {
    $.ajax({
        type: 'GET',
        url: '/Puls',
        dataType: 'json',
        contentType: 'application/json',
        data: {
            "pulsIn": document.getElementById("pulsIn").value,
        },
        success: function(response){}
    });
}

function send_control_commands() {
    $.ajax({
        type: 'GET',
        url: '/ControlCommands',
        dataType: 'json',
        contentType: 'application/json',
        data: ({
            "TempIn": document.getElementById("TempIn").value,
            "DavlIn": document.getElementById("DavlIn").value,
            "KislorIn": document.getElementById("KislorIn").value,
            "hours": document.getElementById("hours").value,
            "pulsIn": document.getElementById("pulsIn").value
        }),
        success: function(response){}

    });
}











