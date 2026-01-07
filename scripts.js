let cartCount = 0;

function showProductDetails(title, description, price) {
    alert(`Title: ${title}\nDescription: ${description}\nPrice: $${price}`);
}

function addToCart() {
    cartCount++;
    document.getElementById('cartBtn').innerText = `Cart (${cartCount})`;
}
