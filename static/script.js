    setTimeout(function() {
        let flashMessages = document.querySelectorAll('.flash');
        flashMessages.forEach(function(message) {
            message.style.display = 'none';
        });
    }, 5000);
