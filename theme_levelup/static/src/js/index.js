odoo.define('theme_levelup.index', function(require){
    'use strict';
    var publicWidget = require('web.public.widget');


    $(document).ready(function () {
        var s = $(".header_modern_light");
        var nav = $('.navigation');
        var pos = s.position();
        $('#wrapwrap').scroll(function () {
            var windowpos = $('#wrapwrap').scrollTop();
            if (windowpos >= pos.top & windowpos >= 100) {
                nav.addClass("fadeInDown");
                nav.addClass("bg_white");
                nav.addClass("b_shadow");
            } else {
                nav.removeClass("fadeInDown");
                nav.removeClass("bg_white");
                nav.removeClass("b_shadow");
            }
        });
    });
    var a = 0;
    var counter = $(".counter_main")
    var selected = document.querySelector('.counter_main');
    if (selected != null) {
        $('#wrapwrap').scroll(function () {
            var oTop = $("#counter-box").offset().top - window.innerHeight;
            if (a == 0 && $(window).scrollTop() > oTop) {
                $(".counter").each(function () {
                    var $this = $(this),
                        countTo = $this.attr("data-number");
                    $({
                        countNum: $this.text()
                    }).animate(
                        {
                            countNum: countTo
                        },
                        {
                            duration: 5000,
                            easing: "swing",
                            step: function () {
                                $this.text(
                                    Math.ceil(this.countNum).toLocaleString("en")
                                );
                            },
                            complete: function () {
                                $this.text(
                                    Math.ceil(this.countNum).toLocaleString("en")
                                );
                            }
                        }
                    );
                });
                a = 1;
            }
        });
    }
});

