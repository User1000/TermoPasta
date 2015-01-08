/**
 * Created by Александр on 07.01.2015.
 */


$('document').ready(function(){
    var order_url;

    $('#OrderFormSubmitBtn').on('click',function(){
        //alert('ko');
        $.post(order_url, $('#OrderForm').serialize())
        alert('Ваш заказ принят! Мы свяжемся с Вами в ближайшее время.');
        $('[id^=myModal_]').modal('hide');


    });

    $('a.order_item').on('click', function( event ){

        event.preventDefault();
        order_url = $(this).attr("href");
        var itemName = $(this).closest('.panel-info').find('h3').html();
        console.log(order_url);
        $('[id=orderAddModal] h3').html(itemName);//return false;
        $('[id=orderAddModal]').modal('show');

    });

    //$('a.nav_link').on('click', function(){
    //    //$("li").removeClass("active");
    //    console.log('3');
    //    alert('w');
    //    //$(this).parent().addClass('active');
    //});

    $("[href]").each(function() {
        //$("li").removeClass("active");
        var s = window.location.href;
        if (s.indexOf(this.href) >= 0) {
            console.log($(this).parent().addClass("active"));

            $(this).parent().addClass("active");
        }

});
});
