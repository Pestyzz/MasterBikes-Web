document.addEventListener("DOMContentLoaded", function() {
    function setFilterHeight() {
        const filterSection = document.querySelector('.filter');
        const containerSection = document.querySelector('.container-content');

        if (filterSection && containerSection) {
            const containerHeight = containerSection.offsetHeight;
            filterSection.style.height = containerHeight + 'px';
        }
    }

    // Inicialmente establece la altura cuando el contenido esté cargado
    setFilterHeight();

    // Opcional: Vuelve a calcular la altura cuando la ventana cambia de tamaño
    window.addEventListener('resize', setFilterHeight);
});