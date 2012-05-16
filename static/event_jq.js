$(document).ready(function(){
    $("a.a_confirm_link").click(function(){
        var r = confirm("是否确认删除");
        return r;
    });
});

function show_child(index){
    var name = 'child_' + index;
    if ( $('#'+name).css("display") == "block"){
        $('#'+name).hide();
    } else {
        $('#'+name).show();
    }
}

function loads(item_stuff, auto_fill, item_type) {
    if (item_type == "一口价") {
        item_type = "fixed";
    }else{
        item_type = "auction";
    }
    if (item_stuff != '') {
        $('#' + item_stuff).attr("selected","selected");
    }
    if (auto_fill == '') {
        $("#item-auto-fill-list").attr("disabled", "false");
    } else {
        $('#' + auto_fill).attr("selected", "selected");
    }
    if(item_type != '') {
        $('#' + item_type).attr("selected", "selected");
    }
}
