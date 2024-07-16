document.addEventListener("DOMContentLoaded", function() {
    // Validación del formulario de pago
    document.querySelector(".form-pago").addEventListener("submit", function(event) {
        var cardNumber = document.getElementById("card_number");
        var expiryDate = document.getElementById("expiry_date");
        var cvv = document.getElementById("cvv");

        clearErrors();

        var valid = true;

        if (!validateCardNumber(cardNumber.value)) {
            showError(cardNumber, "Número de tarjeta inválido. Debe tener 16 dígitos.");
            valid = false;
        }
        if (!validateExpiryDate(expiryDate.value)) {
            showError(expiryDate, "Fecha de expiración inválida. Debe tener el formato MM/YY y ser posterior a la fecha actual.");
            valid = false;
        }
        if (!validateCVV(cvv.value)) {
            showError(cvv, "CVV inválido. Debe tener 3 dígitos.");
            valid = false;
        }

        if (!valid) {
            event.preventDefault();
        }
    });

    function validateCardNumber(cardNumber) {
        var regex = /^\d{16}$/;
        return regex.test(cardNumber);
    }

    function validateExpiryDate(expiryDate) {
        var regex = /^(0[1-9]|1[0-2])\/\d{2}$/;
        if (!regex.test(expiryDate)) {
            return false;
        }

        var parts = expiryDate.split('/');
        var month = parseInt(parts[0], 10);
        var year = parseInt('20' + parts[1], 10);

        var now = new Date();
        var currentMonth = now.getMonth() + 1;
        var currentYear = now.getFullYear();

        if (year < currentYear || (year === currentYear && month < currentMonth)) {
            return false;
        }

        return true;
    }

    function validateCVV(cvv) {
        var regex = /^\d{3}$/;
        return regex.test(cvv);
    }

    function showError(input, message) {
        var error = document.createElement("div");
        error.className = "error";
        error.style.color = "red";
        error.innerText = message;
        input.parentNode.appendChild(error);
    }

    function clearErrors() {
        var errors = document.querySelectorAll(".error");
        errors.forEach(function(error) {
            error.remove();
        });
    }

    // Formatear automáticamente la fecha de expiración (MM/YY) mientras se escribe
    document.getElementById("expiry_date").addEventListener("input", function(event) {
        var input = event.target;
        var value = input.value.replace(/\D/g, ''); // Eliminar caracteres que no sean dígitos

        if (value.length > 4) {
            value = value.substr(0, 4); // Limitar a 4 caracteres (MMYY)
        }

        if (value.length >= 2) {
            // Insertar el separador '/' automáticamente después de los primeros dos dígitos
            input.value = value.substr(0, 2) + '/' + value.substr(2);
        } else {
            input.value = value;
        }
    });
});
