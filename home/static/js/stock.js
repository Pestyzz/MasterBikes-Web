document.addEventListener("DOMContentLoaded", () => {
    document.getElementById('increment').addEventListener('click', function() {
        var quantity = document.getElementById('quantity');
        quantity.value = parseInt(quantity.value) + 1;
    });

    document.getElementById('decrement').addEventListener('click', function() {
        var quantity = document.getElementById('quantity');
        if (quantity.value > 1) {
            quantity.value = parseInt(quantity.value) - 1;
        }
    });
});