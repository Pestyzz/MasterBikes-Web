document.addEventListener("DOMContentLoaded", function() {
    function assignAddButtons() {
        document.querySelectorAll('.add-to-cart-btn').forEach(button => {
            button.removeEventListener('click', handleAddButtonClick); // Remove any existing listeners
            button.addEventListener('click', handleAddButtonClick);    // Add the new listener
        });
    }

    function handleAddButtonClick(event) {
        event.preventDefault();
        const productId = this.dataset.productId;
        const quantityInput = this.closest('.d-flex').querySelector('#quantity');
        const quantity = quantityInput ? parseInt(quantityInput.value) : 1;

        fetch(`/cart/add/${productId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ quantity: quantity })
        })
        .then(response => {
            if (response.status === 403) {
                window.location.href = '/login/';
                return;
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                updateCartItems(data.cart_items);
                updateCartItemCount(data.cart_items_count);
                assignRemoveButtons();
            } else {
                console.error('Error al añadir el ítem al carrito:', data.error);
            }
        })
        .catch(error => console.error('Error al añadir el ítem al carrito:', error));
    }

    function assignRemoveButtons() {
        document.querySelectorAll('.cart-remove-btn').forEach(button => {
            button.removeEventListener('click', handleRemoveButtonClick); // Remove any existing listeners
            button.addEventListener('click', handleRemoveButtonClick);    // Add the new listener
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
            if (response.status === 403) {
                window.location.href = '/login/';
                return;
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                updateCartItems(data.cart_items);
                updateCartItemCount(data.cart_items_count);
                assignRemoveButtons();
            } else {
                console.error('Error al eliminar el ítem del carrito:', data.error);
            }
        })
        .catch(error => console.error('Error al eliminar el ítem del carrito:', error));
    }

    function updateCartItems(items) {
        const cartItemsContainer = document.querySelector('#cart-items-list');
        if (cartItemsContainer) {
            cartItemsContainer.innerHTML = '';  // Clear current items
            if (items.length > 0) {
                items.forEach(item => {
                    const cartItemElement = document.createElement('li');
                    cartItemElement.id = `cart-item-${item.id}`;
                    cartItemElement.innerHTML = `
                        ${item.product_name} - Cantidad: ${item.quantity}
                        <button class="cart-remove-btn" data-item-id="${item.id}">Eliminar</button>
                    `;
                    cartItemsContainer.appendChild(cartItemElement);
                });
            } else {
                cartItemsContainer.innerHTML = '<p>No hay productos en el carro.</p>';
            }
        } else {
            console.error('Error: Contenedor de items del carrito no encontrado');
        }
    }

    function updateCartItemCount(count) {
        const cartItemCountElement = document.querySelector('.cart-item-count');
        if (cartItemCountElement) {
            console.log('Actualizando el contador del carrito a:', count);
            cartItemCountElement.textContent = count;
        } else {
            console.error('Error: Elemento contador de ítems del carrito no encontrado');
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

    assignAddButtons();
    assignRemoveButtons();
});
