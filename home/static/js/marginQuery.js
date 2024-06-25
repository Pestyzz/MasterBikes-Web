document.addEventListener("DOMContentLoaded", function() {
    function setQueryMargin() {
        const containerSection = document.querySelector('.container');
        const queryElement = document.querySelector('.s-query');
    
        if (containerSection && queryElement) {
            const containerLeftMargin = containerSection.offsetLeft;
            queryElement.style.marginLeft = containerLeftMargin + 'px';
        }
    }
    
    // Inicialmente establece el margen cuando el contenido esté cargado
    setQueryMargin();
    
    // Opcional: Vuelve a calcular el margen cuando la ventana cambia de tamaño
    window.addEventListener('resize', setQueryMargin);
});