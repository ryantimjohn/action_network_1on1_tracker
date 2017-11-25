$(document).foundation();

function updateURLParameter(url, param, paramVal){
    var newAdditionalURL = "";
    var tempArray = url.split("?");
    var baseURL = tempArray[0];
    var additionalURL = tempArray[1];
    var temp = "";
    if (additionalURL) {
        tempArray = additionalURL.split("&");
        for (var i=0; i<tempArray.length; i++){
            if(tempArray[i].split('=')[0] != param){
                newAdditionalURL += temp + tempArray[i];
                temp = "&";
            }
        }
    }

    var rows_txt = temp + "" + param + "=" + paramVal;
    return baseURL + "?" + newAdditionalURL + rows_txt;
}

function one_on_one_search(){
	var query = $("input[name='q']").val();
	window.location = updateURLParameter(window.location.href, 'q', query);
}

$("#submit").on('click', function(){
	one_on_one_search();
});
$("input[name='q']").keypress(function (e) {
	  if (e.which == 13) {
	    one_on_one_search();
	    return false;   
	  }
});