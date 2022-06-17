function showTime() {
    var time =  new Date();
    var hora = time.getHours();
    var minuto = time.getMinutes();
    var segundo = time.getSeconds();

    if(hora < 10) hora = "0" + hora;
    if(minuto < 10) minuto = "0" + minuto;
    if(segundo < 10) segundo = "0" + segundo;

    var tempo = hora + ":" + minuto + ":" + segundo;

    document.getElementById("timer").innerHTML = tempo;
}

function initTime() {
    setInterval(showTime, 1000);
}