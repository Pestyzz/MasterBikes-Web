document.addEventListener('DOMContentLoaded', function() {
    const incrementButton = document.getElementById('increment');
    const decrementButton = document.getElementById('decrement');
    const quantityInput = document.getElementById('quantity');
    const maxQuantity = 3;

    incrementButton.addEventListener('click', function(e) {
        e.preventDefault();
        let quantity = parseInt(quantityInput.value);
        if (quantity < maxQuantity) {
            quantityInput.value = quantity + 1;
        }
    });

    decrementButton.addEventListener('click', function(e) {
        e.preventDefault();
        let quantity = parseInt(quantityInput.value);
        if (quantity > 1) {
            quantityInput.value = quantity - 1;
        }
    });
});
