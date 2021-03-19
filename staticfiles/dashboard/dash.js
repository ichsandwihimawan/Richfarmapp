var bnb = 'https://indodax.com/api/ticker/bnbidr'
var usdt = 'https://indodax.com/api/ticker/usdtidr'
var tron = 'https://indodax.com/api/ticker/trxidr'
var doge = 'https://indodax.com/api/ticker/dogeidr'
var harga_tron
var harga_doge


var harga_usdt = $.ajax({
    type: "GET",
    url: usdt,
    async:false,
    success: function(data){
        $('#temp-usdt').val(data.ticker.last)
    }
  }).responseJSON.ticker.last

var harga_bnb = $.ajax({
    type: "GET",
    url: bnb,
    async:false,
    success: function(data){
        $('#temp-bnb').val(data.ticker.last)
    }
  }).responseJSON.ticker.last / harga_usdt

var harga_doge = $.ajax({
    type: "GET",
    url: doge,
    async:false,
    success: function(data){
        $('#temp-doge').val(data.ticker.last)
    }
  }).responseJSON.ticker.last / harga_usdt

var harga_tron = $.ajax({
    type: "GET",
    url: tron,
    async:false,
    success: function(data){
        $('#temp-tron').val(data.ticker.last)
    }
  }).responseJSON.ticker.last / harga_usdt

setInterval(function(){

var harga_usdt = $.ajax({
    type: "GET",
    url: usdt,
    async:false,
    success: function(data){
        $('#temp-usdt').val(data.ticker.last)
    }
  }).responseJSON.ticker.last


$.ajax({
    type: "GET",
    url: bnb,
    async:false,
    success: function(data){
        harga_bnb = data.ticker.last / harga_usdt
        var bnb_val = $('#bnb-input').val()
        var hasil_bnb = bnb_val/harga_bnb
        $('#bnb-amt').html(parseFloat(hasil_bnb + (hasil_bnb * 0.02)).toFixed(4).toLocaleString())
        $('#temp-bnb').val(data.ticker.last)
    }
  })

$.ajax({
    type: "GET",
    url: doge,
    async:false,
    success: function(data){
        harga_doge = data.ticker.last / harga_usdt
        var doge_val = $('#doge-input').val()
        var hasil_doge = doge_val / harga_doge
        $('#doge-amt').html(parseFloat(hasil_doge + (hasil_doge * 0.02)).toFixed(0).toLocaleString())
        $('#temp-doge').val(data.ticker.last)
    }
  })

$.ajax({
    type: "GET",
    url: tron,
    async:false,
    success: function(data){
        harga_tron = data.ticker.last / harga_usdt
        var tron_val = $('#tron-input').val()
        var hasil_tron = tron_val / harga_tron
        $('#tron-amt').html(parseFloat(hasil_tron + (hasil_tron * 0.02)).toFixed(0).toLocaleString())
        $('#temp-tron').val(data.ticker.last)
    }
  })

},120000)

$('#bnb-input').keyup(function(){
    var bnb_val = $(this).val()
    var hasil_bnb = bnb_val/harga_bnb
    $('#bnb-amt').html(parseFloat(hasil_bnb + (hasil_bnb * 0.02)).toFixed(4).toLocaleString())

})

$('#doge-input').keyup(function(){
    var doge_val = $(this).val()
    var hasil_doge = doge_val/harga_doge
    $('#doge-amt').html(parseFloat(hasil_doge + (hasil_doge * 0.02)).toFixed(0).toLocaleString())

})

$('#tron-input').keyup(function(){
    var tron_val = $(this).val()
    var hasil_tron = tron_val/harga_tron
    $('#tron-amt').html(parseFloat(hasil_tron + (hasil_tron * 0.02)).toFixed(0).toLocaleString())

})

$('#btn-sub').click(function(){
    if(!$('input[type="radio"]').is(":checked"))
    {
        return swal("Error","Please Check one from the package",'error')
    }
    else{
        $('#paket-modal').modal()
    }
})

var base_url = window.location.origin
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

$("#buy-btn").click(function(){
 $.ajax({
    type: "POST",
    url: base_url + "/transaction/invest/",
    headers: { "X-CSRFToken": csrftoken },
    data: $('#paket-form').serialize(),
    dataType: "json",
    success: function (data) {
        $('#paket-modal').modal('hide')
        setTimeout(location.reload.bind(location), 2000);
        swal(data,'','success')
    },
    error: function (errMsg) {
        $('#paket-modal').modal('hide')
       swal("Error",errMsg.responseText,'error')

    },
  });

})
