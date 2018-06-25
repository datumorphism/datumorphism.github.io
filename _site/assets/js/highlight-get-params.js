var url_string = window.location.href;
var url = new URL(url_string);
var url_main = window.location.href.split('?')[0];
var keywords = url.searchParams.get("keywords");
console.log(keywords);


var options = {
    "diacritics": true,
    "iframesTimeout": 5000,
    "acrossElements": true,
    "caseSensitive": false,
    "ignoreJoiners": false,
    "ignorePunctuation": [],
    "wildcards": "disabled",
    "noMatch": function(term){
        // term is the not found term
    },
    "done": function(counter){
      con = document.querySelector('div.posts').innerHTML
      document.querySelector('div.posts').innerHTML = '<div class="notification is-info has-text-centered" id="query-summary">All '+ counter +' items with the keyword "'+ keywords +'" are highlighted <a class="is-pulled-right is-primary button" href="'+url_main+'">Clear</a></div>' + con;
        // counter is a counter indicating the total number of all marks
    },
    "debug": false,
    "log": window.console
};

var context = document.querySelectorAll("a.keywords-mark");
var instance = new Mark(context);
instance.mark(keywords, options);
