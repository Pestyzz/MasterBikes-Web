document.addEventListener("DOMContentLoaded", function() {
    function setQueryWidth() {
        const containerSection = document.querySelector('section.container');
        const queryElement = document.querySelector('.s-query');

        if (containerSection && queryElement) {
            const containerWidth = containerSection.offsetWidth;
            queryElement.style.width = containerWidth + 'px';
        }
    }

    // Inicialmente establece el ancho cuando el contenido esté cargado
    setQueryWidth();

    // Opcional: Vuelve a calcular el ancho cuando la ventana cambia de tamaño
    window.addEventListener('resize', setQueryWidth);
});