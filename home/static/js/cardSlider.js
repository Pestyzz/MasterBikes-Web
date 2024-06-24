document.addEventListener('DOMContentLoaded', function () {
    let multipleCardCarousel1 = document.querySelector("#carouselBikes");
    let multipleCardCarousel2 = document.querySelector("#carouselAccesories");
    let multipleCardCarousel3 = document.querySelector("#carouselServices");

    if (window.matchMedia("(min-width: 768px)").matches) {
        let carousel1 = new bootstrap.Carousel(multipleCardCarousel1, {
            interval: false,
            wrap: false,
        });
        let carousel2 = new bootstrap.Carousel(multipleCardCarousel2, {
            interval: false,
            wrap: false,
        });
        let carousel3 = new bootstrap.Carousel(multipleCardCarousel3, {
            interval: false,
            wrap: false,
        });

        let carouselInner1 = multipleCardCarousel1.querySelector(".carousel-inner");
        let carouselItems1 = multipleCardCarousel1.querySelectorAll(".carousel-item");
        let carouselWidth1 = carouselInner1.scrollWidth;
        let cardWidth1 = carouselItems1[0].offsetWidth;
        let scrollPosition1 = 0;

        let carouselInner2 = multipleCardCarousel2.querySelector(".carousel-inner");
        let carouselItems2 = multipleCardCarousel2.querySelectorAll(".carousel-item");
        let carouselWidth2 = carouselInner2.scrollWidth;
        let cardWidth2 = carouselItems2[0].offsetWidth;
        let scrollPosition2 = 0;

        let carouselInner3 = multipleCardCarousel3.querySelector(".carousel-inner");
        let carouselItems3 = multipleCardCarousel3.querySelectorAll(".carousel-item");
        let carouselWidth3 = carouselInner3.scrollWidth;
        let cardWidth3 = carouselItems3[0].offsetWidth;
        let scrollPosition3 = 0;

        document.querySelector("#carouselBikes .carousel-control-next").addEventListener("click", function () {
            if (scrollPosition1 < carouselWidth1 - cardWidth1 * 3) {
                scrollPosition1 += cardWidth1;
                carouselInner1.scroll({ left: scrollPosition1, behavior: 'smooth' });
            }
        });

        document.querySelector("#carouselBikes .carousel-control-prev").addEventListener("click", function () {
            if (scrollPosition1 > 0) {
                scrollPosition1 -= cardWidth1;
                carouselInner1.scroll({ left: scrollPosition1, behavior: 'smooth' });
            }
        });

        document.querySelector("#carouselAccesories .carousel-control-next").addEventListener("click", function () {
            if (scrollPosition2 < carouselWidth2 - cardWidth2 * 3) {
                scrollPosition2 += cardWidth2;
                carouselInner2.scroll({ left: scrollPosition2, behavior: 'smooth' });
            }
        });

        document.querySelector("#carouselAccesories .carousel-control-prev").addEventListener("click", function () {
            if (scrollPosition2 > 0) {
                scrollPosition2 -= cardWidth2;
                carouselInner2.scroll({ left: scrollPosition2, behavior: 'smooth' });
            }
        });

        document.querySelector("#carouselServices .carousel-control-next").addEventListener("click", function () {
            if (scrollPosition3 < carouselWidth3 - cardWidth3 * 3) {
                scrollPosition3 += cardWidth3;
                carouselInner3.scroll({ left: scrollPosition3, behavior: 'smooth' });
            }
        });

        document.querySelector("#carouselServices .carousel-control-prev").addEventListener("click", function () {
            if (scrollPosition3 > 0) {
                scrollPosition3 -= cardWidth3;
                carouselInner3.scroll({ left: scrollPosition3, behavior: 'smooth' });
            }
        });
    } else {
        multipleCardCarousel1.classList.add('slide');
        multipleCardCarousel2.classList.add('slide');
        multipleCardCarousel3.classList.add('slide');
    }
});
