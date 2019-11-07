$(function() {
    $('.appendLink').live('click',function(){
        var id=$(this).attr('data-id');
        $('#ul_'+id).toggle('slow');
        $(this).toggleClass('rm-append-inactive');
    })
    $('.dt-menu-toggle-1').live('click',function(){
        $('.menuTop ul.ul-parent').toggle('slow');
    })
});
