var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.3.1.min.js';
script.type = 'text/javascript';
document.getElementsByTagName('head')[0].appendChild(script);
var post = document.querySelector('div.forum_op').innerHTML;
var pageCount = document.querySelectorAll('select').length;
var commentAuthor = document.querySelectorAll('div.commentthread_comment_author');
var comment = document.querySelectorAll('div.commentthread_comment_content');
var w = window.open("", "Steam Discussion", "width=666,height=666");
w.document.write('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">');
w.document.write('<style> .topic{font-weight: bold; font-size: 200%;} </style>')
w.document.write('<div class="alert alert-info m-5">'+post+'</div>');
for(var i=0; i<comment.length; i++){
	w.document.write('<hr/><div class="alert alert-secondary m-5">'+comment[i].innerHTML+'</div>');
}
loadXMLDoc("https://steamcommunity.com/discussions/forum/11/882960080249778126/?ctp=2");
var htmlObject = $(xmlhttp.responseText).innerHTML;
console.log(htmlObject);

function loadXMLDoc(theURL)
{
	if (window.XMLHttpRequest)
	{// code for IE7+, Firefox, Chrome, Opera, Safari, SeaMonkey
		xmlhttp=new XMLHttpRequest();
	}
	else
	{// code for IE6, IE5
		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlhttp.onreadystatechange=function()
	{
		if (xmlhttp.readyState==4 && xmlhttp.status==200)
		{
			page = (xmlhttp.responseText);
		}
	}
	xmlhttp.open("GET", theURL, false);
	xmlhttp.send();
}