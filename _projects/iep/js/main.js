"use strict";

var shownTab = ".home";
function tabToggle(){
	//$("div" + shownTab).hide(500);
	//$(this).show(500);
	//shownTab = id;
	console.log($(this));
	//$(this).parent().addClass("active");
}

var ready = function() {
	$("li.home a, li.docs a, li.design a, li.demo a, li.about a").click(tabToggle);



	console.log("loaded");
};

$(document).ready(ready);
$(document).on('page:load', ready);