
 /* jQuery Pre loader
  -----------------------------------------------*/
$(window).load(function(){
    $('.preloader').fadeOut(10); // set duration in brackets
});

/* Istope Portfolio
-----------------------------------------------*/
jQuery(document).ready(function($){

  if ( $('.iso-box-wrapper').length > 0 ) {

      var $container  = $('.iso-box-wrapper'),
        $imgs     = $('.iso-box img');

      $container.imagesLoaded(function () {

        $container.isotope({
        layoutMode: 'fitRows',
        itemSelector: '.iso-box'
        });

        $imgs.load(function(){
          $container.isotope('reLayout');
        })

      });

      //filter items on button click

      $('.filter-wrapper li a').click(function(){

          var $this = $(this), filterValue = $this.attr('data-filter');

      $container.isotope({
        filter: filterValue,
        animationOptions: {
            duration: 750,
            easing: 'linear',
            queue: false,
        }
      });

      // don't proceed if already selected

      if ( $this.hasClass('selected') ) {
        return false;
      }

      var filter_wrapper = $this.closest('.filter-wrapper');
      filter_wrapper.find('.selected').removeClass('selected');
      $this.addClass('selected');

        return false;
      });

  }

});


 /* Navigation Bar
  -----------------------------------------------*/
$(document).ready(function() {
    "use strict";

    // Navbar Sticky

    (function() {
        var docElem = document.documentElement,
            didScroll = false,
            stickynav = 50;
            document.querySelector( '.nav-container' );
        function init() {
            window.addEventListener( 'scroll', function() {
                if( !didScroll ) {
                    didScroll = true;
                    setTimeout( scrollPage, 50 );
                }
            }, false );
        }

        function scrollPage() {
            var sy = scrollY();
            if ( sy >= stickynav ) {
                $( '.nav-container' ).addClass('sticky');
            }
            else {
                $( '.nav-container' ).removeClass('sticky');
            }
            didScroll = false;
        }

        function scrollY() {
            return window.pageYOffset || docElem.scrollTop;
        }
        init();
    })();

});


$(document).ready(function(){

    "use strict";

    $('.menu-container').each(function(index) {
        $(this).find('.circle').attr('menu-link', index);
        $(this).find('.list-menu').clone().appendTo('body').attr('menu-link', index);
    });

    $('.menu-container .circle').click(function() {
        var linkedVideo = $('section').closest('body').find('.list-menu[menu-link="' + $(this).attr('menu-link') + '"]');
        linkedVideo.toggleClass('reveal-modal');

    });

    $('section').closest('body').find('.close-iframe').click(function() {
        $(this).closest('.list-menu').toggleClass('reveal-modal');
    });


  /* wow
  -------------------------------*/
  new WOW({ mobile: false }).init();

  });

$(document).ready(function() {
    $('#reply-text').hide();

    $('.smooth-goto').on('click', function() {
      $('html, body').animate({scrollTop: $(this.hash).offset().top - 250}, 1000);
      return false;
    });

    $( ".toggle" ).on('click', function(event){
      var text = $("#reply-text").val()
      var value = $(this).attr('value').split("_");
      var tag = '<a id="close-toggle"><i class="fa fa-times"></i></a>'
      pk = value[1];
      name = value[0];
      $('#comment-reply').attr('value', pk);
      $('#reply-text').text('');
      $('#reply-text').show();
      $('#reply-text').append(tag);
      $('#reply-text').append("  Reply to: " + name);
    });
    $(document).on('click', '#close-toggle', function() {
      $('#reply-text').hide();
      $('#comment-reply').attr('value', "");
      $('#reply-text').text('');
    }) ;
});

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
