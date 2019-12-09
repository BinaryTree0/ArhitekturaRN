$(document).ready(function() {
  $('img[data-enlargable]').addClass('img-enlargable').click(function(){
      var src = $(this).attr('src');
      $('<div>').css({
          background: 'RGBA(0,0,0,.5) url('+src+') no-repeat center',
          backgroundSize: 'contain',
          width:'100%', height:'100%',
          position:'fixed',
          zIndex:'10000',
          top:'0', left:'0',
          cursor: 'zoom-out'
      }).click(function(){
          $(this).remove();
      }).appendTo('body');
  });
});

function myFunction() {
  var input = document.getElementById("Search");
  var filter = input.value.toLowerCase();
  var nodes = document.getElementsByClassName('blog-name');
  for (i = 0; i < nodes.length; i++) {
    var id = nodes[i].getAttribute("value");
    var div = document.getElementById("blog_"+id);
    if (nodes[i].innerText.toLowerCase().includes(filter)) {
      div.style.display = "block";
    } else {
      div.style.display = "none";
    }
  }
}
