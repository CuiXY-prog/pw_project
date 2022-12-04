$(document).ready(function(){
    // 动画处理
    $(".login-title").animate({
        opacity:'1'
    }, 800);
    $(".login-page").animate({
        opacity:'1',
        'margin-top':'0px'
    }, 800);

    // 记住我
    var username = $.cookie("username")
    var password = $.cookie("password")
    var remember = $.cookie("remember")
    var mySwitch = $.cookie("mySwitch")
    if(!window.isNaN(username)){
        $("#username").val(username)  
    }
    if(!window.isNaN(password)){
        $("#password").val(password)
    }
    if(remember === 'true'){
        $("#remember").attr("checked", remember)
    }

    console.log(!window.isNaN(mySwitch) && mySwitch === 'false')
    if(mySwitch === 'false'){
        $("#mySwitch").attr("checked", false)
        $(".form-check-label").children().eq(0).css("color", "rgba(0, 0, 0, 0.482)")
        $(".form-check-label").children().eq(2).css("color", "black")
    } 

    // 登录选择处理
    $("#mySwitch").click(function(){
        $(".form-check-label").children().eq(0).css("color", "rgba(0, 0, 0, 0.482)")
        $(".form-check-label").children().eq(2).css("color", "rgba(0, 0, 0, 0.482)")

        if($('#mySwitch').is(":checked")){
            $(".form-check-label").children().eq(0).css("color", "black")
            $("#username").attr("placeholder", "请输入工号");

        }else{
            $(".form-check-label").children().eq(2).css("color", "black")
            $("#username").attr("placeholder", "请输入用户名");
        }
    })

    // 表单登录
    $('#submit').click(function(){
        // 记住我功能实现
        if($('#remember').is(':checked')){
            // 如果选就储存账户密码到 cookie
            $.cookie('username', $("#username").val(), { expires: 7 });
            $.cookie('password', $("#password").val(), { expires: 7 });
            $.cookie('remember', true, { expires: 7 });
            if(!$('#mySwitch').is(':checked')){
                // 是否是用户名
                $.cookie('mySwitch', false, { expires: 7 })
            }
        }else{
            // 如果没选就清除 cookie 的值
            $.cookie('username', null);
            $.cookie('password', null);
            $.cookie('remember', null);
            $.cookie('mySwitch', null)
        }

        // 对密码和用户名进行加密
        
        $('#loginForm').submit()
    })
})