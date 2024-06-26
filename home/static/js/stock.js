document.addEventListener("DOMContentLoaded", () => {
    const numberInput = document.querySelector('.number-input');
    const maxStock = parseInt(numberInput.getAttribute('data-stock')) > 3 ? 3 : parseInt(numberInput.getAttribute('data-stock')); // Limitar a 4 o el stock disponible

    document.getElementById('increment').addEventListener('click', function() {
        var quantity = document.getElementById('quantity');
        if (parseInt(quantity.value) < maxStock) {
            quantity.value = parseInt(quantity.value) + 1;
        }
    });

    document.getElementById('decrement').addEventListener('click', function() {
        var quantity = document.getElementById('quantity');
        if (parseInt(quantity.value) > 1) {
            quantity.value = parseInt(quantity.value) - 1;
        }
    });

    document.getElementById('quantity').addEventListener('input', function() {
        var quantity = document.getElementById('quantity');
        if (quantity.value < 1) {
            quantity.value = 1;
        } else if (quantity.value > maxStock) {
            quantity.value = maxStock;
        }
    });
});
