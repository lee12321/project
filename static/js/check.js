//首先找到span位置，点击的
$('table label span').click(e=>{
    let tar = $(e.target)
    //判断是否选中
    if(tar.attr("name")==='false')
        tar.attr("name",'true').css("background-image","url('./image/check_true.png')")
    else
        tar.attr("name",'false').css("background-image","url('./image/check_false.png')")
})