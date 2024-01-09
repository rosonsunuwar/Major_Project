// Get all elements with the class 'update-cart'
var updateBtns = document.getElementsByClassName('update-cart');

// Iterate through each 'update-cart' button
for (var i = 0; i < updateBtns.length; i++) {
    // Add a click event listener to each button
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('productId:', productId, 'Action:', action);
        console.log('USER:', user);

        if (user === 'AnonymousUser') {
            console.log('User is not authenticated');
			alert("Login in order to shop")
        } else {
            updateUserOrder(productId, action);
        }
    });
}

function updateUserOrder(productId, action) {
	console.log('User is authenticated, sending data...')

	var url = '/update_item/'

	fetch(url, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			'X-CSRFToken': csrftoken,
		},
		body: JSON.stringify({ 'productId': productId, 'action': action })
	})
		.then((response) => {
			return response.json();
		})
		.then((data) => {
			location.reload()
		});
}

