"use strict";

var shownTab = ".home";
function tabToggle(){
	$("li" + shownTab).removeClass("active");
	var classname = $(this).parent("li").attr("class");
	$("." + classname).slideDown(1000).delay(1000);
	$("div" + shownTab).slideUp(1000);
	shownTab = "." + classname;
	$(this).parent("li").addClass("active");
}

var ready = function() {
	$("li.home a, li.docs a, li.design a, li.demo a, li.about a").click(tabToggle);



	console.log("loaded");
};

$(document).ready(ready);
$(document).on('page:load', ready);