/////////一些工具函数/////////////////////
function format_time(sec)//格式化时间
{
 	var h=Math.floor(sec/3600);
 	var m=Math.floor((sec%3600)/60);
 	var s=sec%3600%60;
 	var out="";
	if(h<10)
	{
		out += "0"+h+" : ";
	}
	else
	{
 		out+=h+" : ";
	}
	
 	if(m<10)
	{
		out+="0"+m+" : ";
	}
	else
	{
 		out+=m+" : ";
	}
	
	if(s<10)
	{
		out += "0"+s+"";
	}
	else
	{
		out += s+"";
	}
 	return out;
}
 
function format_flux(byte)//格式化流量
{
	if(byte>(1000*1000))
		return (format_number((byte/(1000*1000)),2)+"M");
	if(byte>1000)
		return (format_number((byte/1000),2)+"K");
	return byte+"b";
}

function format_number(num, count)
{
	var n=Math.pow(10, count);
	var t=Math.floor(num*n);
	return t/n;
}

function setCookie(name,value)
{
	var Days = 360; 
	var exp  = new Date(); 
	exp.setTime(exp.getTime() + Days*24*60*60*1000);
	document.cookie = name + "="+ escape (value) + ";expires=" + exp.toGMTString();
}

function getCookie(name)      
{
	var arr = document.cookie.match(new RegExp("(^| )"+name+"=([^;]*)(;|$)"));
	if(arr != null) 
		return unescape(arr[2]); 
	return null;
}
/////////////////////////////////////////////////////

function get_online_info(ip) //获取在线信息
{
	$.post("/include/auth_action.php", {
			action: 'get_online_info',
			user_ip: ip
	}, function(res) {
		if(res!="" && res!="not_online") 
		{
			var arr3=res.split(",");
			//显示在线信息，可根据需求扩展
			$("#sum_bytes").html(format_flux(arr3[0]));
			$("#sum_seconds").html(format_time(arr3[1]));
			$("#user_balance").html("￥"+arr3[2]);
			$("#user_name").html(arr3[4]);
		}
	});
}

function Encrypt(s) 
{ 
	var r = "";
	var h = "";
	var j = 0;
	var hexes = new Array ("0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f");
	for (var i=0; i<s.length; i++) 
	{
		h = "0x" + (hexes [s.charCodeAt(i) >> 4] + hexes [s.charCodeAt(i) & 0xf]);
		j = parseInt(h);
		j = j ^ 0x33;
		if(j<10)
		{
			h = "0"+j;
		}
		else
		{
			h = ""+j;
		}
		r += h;
	}
	return r;
} 

function check(frm) //页面内认证
{
	if(frm.username.value=="")
	{
		alert("请填写用户名");
		frm.username.focus();
		return false;
	}
	
	if(frm.password.value=="")
	{
		alert("请填写密码");
		frm.password.focus();
		return false;
	}
	
	//var e = Encrypt(frm.password.value);
	//frm.password.value = "{B}"+e;
	return true;
}

function do_logout(frm)//远程注销
{
	$.post("/include/auth_action.php",{
			action: "logout",
			username: $("input[name='username']").val(),
			password: $("input[name='password']").val(),
			ajax: 1
			},function(res){
				alert(res);
	});
}

function redirect() //重定向到输入的网址
{
	var url = $("input[name='url']").val();
	if(url!="")
		location = url;
}

function check1(frm) //弹窗认证
{
	if(frm.username.value=="")
	{
		alert("请填写用户名");
		frm.username.focus();
		return false;
	}
	
	if(frm.password.value=="")
	{
		alert("请填写密码");
		frm.password.focus();
		return false;
	}
	
	var res1 = "";
	
	var e = Encrypt(frm.password.value);
	var save_me = (frm.save_me.checked) ? 1 : 0;
	var d = "action=login&username="+$("input[name='username']").val()+
			"&password="+frm.password.value+
			"&ac_id="+$("input[name='ac_id']").val()+
			"&user_ip="+$("input[name='user_ip']").val()+
			"&nas_ip="+$("input[name='nas_ip']").val()+
			"&user_mac="+$("input[name='user_mac']").val()+
			"&save_me="+save_me+
			"&ajax=1";
	//这里要用AJAX同步提交POST
	$.ajax({type: "post",
			url: "/include/auth_action.php", 
			action: 'login',
			data: d,
			async : false,
			success: function(res) {
		res1 = res;
	}
	});
	
	var p = /^login_ok,/;
	if(p.test(res1))//认证成功，弹出小窗口
	{
		var arr = res1.split(",");
		if(arr[1] != "")//写入用于双栈认证的COOKIE
		{
			setCookie("double_stack_login", arr[1]);
		}
		if(arr[2]!="")//写入用户名密码COOKIE
		{
			setCookie("login", arr[2]);
		}
		window.open("srun_portal_pc_succeed.php", "","width=400,height=300,left=0,top=0,resizable=1");//弹出小窗口
		
		setTimeout("redirect()", 2000); //重定向到输入的网址
	}
	else
	{
		alert(res1); //提示错误信息
	}
	
	return false;
}