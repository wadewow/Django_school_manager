    $(function () {
        $('.class-td').addClass('active');
    });

    $('#add_class').click(function () {
        $('.modal,.shade').removeClass('hide');
    });

    $('.td-remove').click(function () {
        $('.shade,.fuck').removeClass('hide')
    });

    $('#btn-cancel,#btn-remove').click(function () {
        $('.modal,.shade,.fuck').addClass('hide')
    });

    $('#modal_ajax_submit').click(function () {
        const value = $('[name = caption]').val();
        $.ajax({
            url: "/class/",
            type: 'POST',
            data: {
                "caption": value,
            },
            dataType: "JSON",
            success:function (rep) {
                if(!rep.status){
                    alert(rep.error)
                }else {
                    location.reload()
                }
            }
        })
    });