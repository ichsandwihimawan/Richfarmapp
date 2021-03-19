var bnb = 'https://indodax.com/api/ticker/bnbidr'
var usdt = 'https://indodax.com/api/ticker/usdtidr'
var tron = 'https://indodax.com/api/ticker/tronidr'
var doge = 'https://indodax.com/api/ticker/dogeidr'
var harga_usdt
var harga_bnb
var harga_tron
var harga_doge
setInterval(function(){
fetch(bnb)
    .then((res) => res.json())
    .then(function(data) {
        harga_bnb = data.ticker.last
    })
    .catch(function(err) {
        console.log(err)
    });

 fetch(usdt)
    .then((res) => res.json())
    .then(function(data) {
        harga_usdt = data.ticker.last
    })
    .catch(function(err) {
        console.log(err)
    });
    console.log(harga_bnb)
    console.log(harga_usdt)
    usdt_bnb = harga_bnb / harga_usdt
    console.log(usdt_bnb)
    var bnb_price = parseInt(usdt_bnb).toLocaleString()
    $('#bnb-price').html(bnb_price)
    $('#temp-bnb').val(usdt_bnb)


},10000)
