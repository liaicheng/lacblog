$(document).ready(function (){
    var	codeLength = 4;
    submit_comment();
    back_to_post();
    create_code(codeLength);
    change_code(codeLength);
    control_submit(codeLength);
    modify_perview();
    initial_blog_page();
    hide_top_btn();
    show_top_btn();
    top_btn();
});

function back_to_post(){
     //实现返回按钮
     $("#back_to_post").click(function () {
         window.history.back();
      });
}

function submit_comment() {
    //实现ctrl+enter提交评论
    $(document).keypress(function e() {
        if (e.ctrlKey && e.which === 13 || e.which === 10) {
            $("#comment_from").submit();
        }
    });
}

function change_code(codeLength) {
    //更改验证码
    $("#checkCode").click(function () {
        create_code(codeLength);
    });
}

var code ;
function create_code(codeLength){
    //生成验证码
    code = "";
    var checkCode = $("#checkCode");
    var selectChar = new Array(0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','I','J','K','L',
                'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z');

    for(var i=0;i<codeLength;i++){
        var charIndex = Math.floor(Math.random()*36);
        code +=selectChar[charIndex];
    }
    if(checkCode){
        checkCode.addClass("code");
        checkCode.val(code);
    }
}

function verify_code (){
    //验证验证码
    var user_input_code = $("#user_input_code").val().toLowerCase().trim();
    if(user_input_code.length <=0){
        return false;
    } else if(user_input_code != code.toLowerCase()){
        return false;
    }
    return true;
}

function control_submit(codeLength) {
    //当验证码验证成功后，才允许提交评论
    $("#user_input_code").keyup(function () {
        var code_len = $("#user_input_code").val().trim().length
            if (code_len < codeLength) {
                $("#valid_failed").text("");
            } else if (code_len > codeLength) {
                $("#valid_failed").text("验证码错误");
    	  $("#submit_comment").attr("disabled", true);
           } else {
                if (verify_code()) {
                    $("#submit_comment").attr("disabled", false);
	 } else {
	      $("#valid_failed").text("验证码错误");			       
	  }
           }
    });
}

function initial_blog_page() {
    //防止从评论模块的perview页面后退到blog页面时，评论的提交按钮仍然维持disable=“false”状态
    $("#submit_comment").attr("disabled", true);
}

function modify_perview() {
    //修改评论模块的perview页面
    $("#my_preview").find("#id_name").attr("placeholder", "请输入您的昵称");
    $("#my_preview").find("#id_email").attr("placeholder", "请输入您的邮箱（不会被公开）");
    $("#my_preview").find("#id_comment").attr("placeholder", "请输入您的评论");
    $("#my_preview").find("#id_url").parent().remove();
}

function hide_top_btn() {
   $("#back-to-top").hide();
}

function show_top_btn() {
	$(window).scroll(function () {
		if ($(window).scrollTop()>100) {
			$("#back-to-top").fadeIn(1200);
		} else {
			$("#back-to-top").fadeOut(1200);
		}
		});
}

function top_btn() {
  $("#back-to-top").click(function () {
    $("body, html").animate({scrollTop: 0}, 1200);
    return false;
  	});
}
