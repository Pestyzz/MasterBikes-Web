document.addEventListener('DOMContentLoaded', function () {
    let multipleCardCarousel = document.querySelector("#carouselBikes");
    let multipleCardCarousel2 = document.querySelector("#carouselAccesories");

    if (window.matchMedia("(min-width: 768px)").matches) {
        let carousel1 = new bootstrap.Carousel(multipleCardCarousel, {
            interval: true, // Disable automatic sliding
            wrap: true, // Prevent wrapping at the end
        });
        let carousel2 = new bootstrap.Carousel(multipleCardCarousel2, {
            interval: true, // Disable automatic sliding
            wrap: true, // Prevent wrapping at the end
        });

        let carouselInner1 = multipleCardCarousel.querySelector(".carousel-inner");
        let carouselItems1 = multipleCardCarousel.querySelectorAll(".carousel-item");
        let carouselWidth1 = carouselInner1.scrollWidth;
        let cardWidth1 = carouselItems1[0].offsetWidth;
        let scrollPosition1 = 0;

        let carouselInner2 = multipleCardCarousel2.querySelector(".carousel-inner");
        let carouselItems2 = multipleCardCarousel2.querySelectorAll(".carousel-item");
        let carouselWidth2 = carouselInner2.scrollWidth;
        let cardWidth2 = carouselItems2[0].offsetWidth;
        let scrollPosition2 = 0;

        document.querySelector("#carouselBikes .carousel-control-next").addEventListener("click", function () {
            if (scrollPosition1 < carouselWidth1 - cardWidth1 * 4) {
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
            if (scrollPosition2 < carouselWidth2 - cardWidth2 * 4) {
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
    } else {
        multipleCardCarousel.classList.add("slide");
        multipleCardCarousel2.classList.add("slide");
    }
});
