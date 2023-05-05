   $(document).ready(function () {
      var s = $(".sticker");
      var pos = s.position();
      $(window).scroll(function () {
        var windowpos = $(window).scrollTop();
        if ((windowpos >= pos.top) & (windowpos >= 100)) {
          s.addClass("fadeInDown");
          s.addClass("bg_white");
          s.addClass("b_shadow");
        } else {
          s.removeClass("fadeInDown");
          s.removeClass("bg_white");
          s.removeClass("b_shadow");
        }
      });
    });


          //service slider
  $(document).ready(function () {
      var owl = $('.test_slider2');
      owl.owlCarousel({
          loop: true,
          margin: 10,
          nav: false,
          dots:false,
          items: 3,
          center:true,
      });
      $('.custom-nav .prev').click(function () {
          owl.trigger('prev.owl.carousel');
      });
      $('.custom-nav .next').click(function () {
          owl.trigger('next.owl.carousel');
      });
  });