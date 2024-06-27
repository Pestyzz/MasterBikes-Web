document.addEventListener("DOMContentLoaded", function() {
    function assignRemoveButtons() {
        document.querySelectorAll('.cart-remove-btn').forEach(button => {
            button.removeEventListener('click', handleRemoveButtonClick);  // Remove any existing listeners
            button.addEventListener('click', handleRemoveButtonClick);
        });
    }

    function handleAddButtonClick(event) {
        event.preventDefault();
        const productId = this.dataset.productId;
        const quantity = this.dataset.quantity || 1;

        fetch(`/cart/add/${productId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ quantity: quantity })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                // Aquí deberías actualizar la interfaz del carrito, por ejemplo, actualizando el HTML del carrito
                updateCartItems(data.cart_items);
                updateCartItemCount(data.cart_items_count);
                assignRemoveButtons();  // Reassign after updating the cart
            } else {
                console.error('Error al añadir el ítem al carrito:', data.error);
            }
        })
        .catch(error => console.error('Error al añadir el ítem al carrito:', error));
    }

    function updateCartItems(items) {
        const cartItemsContainer = document.querySelector('#cart-items-container');
        cartItemsContainer.innerHTML = '';  // Limpiar los ítems actuales
        items.forEach(item => {
            const cartItemElement = document.createElement('div');
            cartItemElement.id = `cart-item-${item.id}`;
            cartItemElement.className = 'cart-item';
            cartItemElement.innerHTML = `
                <span>${item.product_name}</span>
                <span>${item.quantity}</span>
                <button class="cart-remove-btn" data-item-id="${item.id}">Eliminar</button>
            `;
            cartItemsContainer.appendChild(cartItemElement);
        });
        assignRemoveButtons();  // Reassign after updating the cart items
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

    document.querySelectorAll('.cart-add-btn').forEach(button => {
        button.addEventListener('click', handleAddButtonClick);
    });

    assignRemoveButtons();  // Initial assignment
});