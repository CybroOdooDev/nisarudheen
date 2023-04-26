
     $(document).ready(function () {
            var owl = $('.owl-theme1');
            owl.owlCarousel({
                loop: true,
                margin: 10,
                nav: false,
                items: 1,
                autoplay: false,
            });
            $('.custom-nav .prev').click(function () {
                owl.trigger('prev.owl.carousel');
            });
            $('.custom-nav .next').click(function () {
                owl.trigger('next.owl.carousel');
            });
        });
        $('.slider').on('initialized.owl.carousel changed.owl.carousel', function (e) {
            if (!e.namespace) {
                return;
            }
            var carousel = e.relatedTarget;
            $('.slider-counter').text(carousel.relative(carousel.current()) + 1 + '-' + carousel.items().length);
        }).owlCarousel({
            items: 1,
            loop: true,
            margin: 0,
            smartSpeed: 450,
            autoplay: 8000,
            autoPlaySpeed: 1000,
            autoPlayTimeout: 1000,
        });

     $(document).ready(function () {
            var owl = $('.owl-theme2');
            owl.owlCarousel({
                loop: true,
                margin: 10,
                nav: false,
                items: 1,
            });
            $('.custom-nav .prev').click(function () {
                owl.trigger('prev.owl.carousel');
            });
            $('.custom-nav .next').click(function () {
                owl.trigger('next.owl.carousel');
            });
        });
         window.addEventListener("scroll", function () {
            var navbar = document.querySelector(".navigation");
            if (window.pageYOffset > 0) {
                navbar.classList.add("b_shadow");
            } else {
                navbar.classList.remove("b_shadow");
            }
        });