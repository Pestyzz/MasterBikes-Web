document.addEventListener("DOMContentLoaded", function() {
    function assignRemoveButtons() {
        document.querySelectorAll('.cart-remove-btn').forEach(button => {
            button.removeEventListener('click', handleRemoveButtonClick);  // Remove any existing listeners
            button.addEventListener('click', handleRemoveButtonClick);
        });
    }

    function handleRemoveButtonClick(event) {
        event.preventDefault();
        const itemId = this.dataset.itemId;

        fetch('/cart/remove-ajax/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ item_id: itemId })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                document.getElementById('cart-item-' + itemId).remove();
                updateCartItemCount(data.cart_items_count);
                assignRemoveButtons();  // Reassign after updating the cart
            } else {
                console.error('Error al eliminar el ítem del carrito:', data.error);
            }
        })
        .catch(error => console.error('Error al eliminar el ítem del carrito:', error));
    }

    function updateCartItemCount(count) {
        const cartItemCount = document.querySelector('.cart .nav-link .cart-item-count');
        if (cartItemCount) {
            cartItemCount.textContent = count;
        }
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    assignRemoveButtons();  // Initial assignment
});
