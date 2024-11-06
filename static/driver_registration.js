document.querySelectorAll('.numbers-only').forEach(input => {
    input.addEventListener('input', function(e) {
        // Remove any non-numeric characters
        let value = this.value.replace(/[^0-9]/g, '');
        
        // If the value changed (i.e., non-numeric characters were entered)
        if (this.value !== value) {
            // Show error message
            let errorElement = document.getElementById(this.id + 'Error');
            if (errorElement) {
                errorElement.style.display = 'block';
                // Hide error message after 2 seconds
                setTimeout(() => {
                    errorElement.style.display = 'none';
                }, 2000);
            }
        }
        
        // Update the input value with only numbers
        this.value = value;
    });

    // Prevent paste of non-numeric characters
    input.addEventListener('paste', function(e) {
        e.preventDefault();
        let text = (e.originalEvent || e).clipboardData.getData('text/plain');
        let numericText = text.replace(/[^0-9]/g, '');
        if (numericText) {
            // Only paste if there are numbers
            this.value = numericText;
        }
    });

    // Prevent keypress of non-numeric characters
    input.addEventListener('keypress', function(e) {
        if (!/^\d*$/.test(e.key)) {
            e.preventDefault();
            let errorElement = document.getElementById(this.id + 'Error');
            if (errorElement) {
                errorElement.style.display = 'block';
                setTimeout(() => {
                    errorElement.style.display = 'none';
                }, 2000);
            }
        }
    });
});