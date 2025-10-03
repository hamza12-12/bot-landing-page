<!DOCTYPE html>
<html lang="ar">
<head>
  <meta charset="UTF-8">
  <title>نجوم متوهجة</title>
  <style>
    body {
      margin: 0;
      background-color: #000;
      overflow: hidden;
    }

    .stars {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: -1;
    }

    .star {
      position: absolute;
      width: 2px;
      height: 2px;
      background: #ff00ff;
      box-shadow: 0 0 6px #ff00ff;
      animation: twinkle 5s infinite ease-in-out;
    }

    @keyframes twinkle {
      0% { opacity: 0.2; transform: scale(1); }
      50% { opacity: 1; transform: scale(1.5); }
      100% { opacity: 0.2; transform: scale(1); }
    }
  </style>
</head>
<body>

  <div class="stars" id="stars"></div>

  <script>
    const starsContainer = document.getElementById("stars");
    for (let i = 0; i < 50; i++) {
      const star = document.createElement("div");
      star.className = "star";
      star.style.top = Math.random() * 100 + "%";
      star.style.left = Math.random() * 100 + "%";
      starsContainer.appendChild(star);
    }
  </script>

</body>
</html>
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <title>متجر AB الرقمي</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body {
      background: linear-gradient(135deg, #2c003e, #4b0070);
      color: white;
      font-family: 'Segoe UI', sans-serif;
      margin: 0;
      padding: 20px;
      text-align: center;
      overflow-x: hidden;
    }

    h1 {
      color: #ffccff;
      text-shadow: 0 0 15px #ff00ff;
      animation: pulse 2s infinite;
    }

    @keyframes pulse {
      0% { text-shadow: 0 0 5px #ff00ff; }
      50% { text-shadow: 0 0 20px #ff00ff; }
      100% { text-shadow: 0 0 5px #ff00ff; }
    }

    .category {
      margin-top: 30px;
      animation: fadeIn 1s ease-in;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
   .products {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 15px;
    }

    .product {
      background-color: #3e005c;
      border: 2px solid #ff00ff;
      border-radius: 10px;
      padding: 15px;
      width: 200px;
      box-shadow: 0 0 15px #ff00ff;
      transition: transform 0.3s ease;
    }

    .product img {
      width: 100%;
      border-radius: 8px;
      margin-bottom: 10px;
      box-shadow: 0 0 10px #ff00ff;
    }

    .product:hover {
      transform: scale(1.05);
      box-shadow: 0 0 25px #ff00ff;
    }

    button {
      background-color: #ff00ff;
      color: white;
      border: none;
      padding: 8px 12px;
      border-radius: 5px;
      cursor: pointer;
      animation: bounce 1.5s infinite;
    }

    @keyframes bounce {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-5px); }
    }

    #cart {
      margin-top: 40px;
      background-color: #1a0026;
      padding: 15px;
      border-radius: 10px;
      box-shadow: 0 0 15px #ff00ff;
    }

    #cart-list {
      list-style: none;
      padding: 0;
      margin-top: 10px;
    } }
    <script>
    const products = {
      "🎮 ألعاب": [
        { name: "660 UC – PUBG", price: "45,000 ل.س", image: "images/pubg.png" },
        { name: "1000 Diamonds – Free Fire", price: "4,500 ل.س", image: "images/freefire.png" }
      ],
      "💳 بطاقات رقمية": [
        { name: "Google Play – 10$", price: "45,000 ل.س", image: "images/googleplay.png" },
        { name: "Steam Wallet – 5$", price: "22,000 ل.س", image: "images/steam.png" }
      ],
      "📱 أرقام جاهزة": [
        { name: "رقم واتساب جاهز", price: "10,000 ل.س", image: "images/whatsapp.png" },
        { name: "رقم تلجرام جاهز", price: "9,000 ل.س", image: "images/telegram.png" }
      ],
      "🚀 خدمات رشق": [
        { name: "رشق متابعين إنستقرام – 1000", price: "6,000 ل.س", image: "images/instagram.png" },
        { name: "رشق لايكات تيك توك – 1000", price: "5,500 ل.س", image: "images/tiktok.png" }
      ]
    };
    
    let cartItems = [];

    function renderProducts() {
      const container = document.getElementById("product-sections");

      for (const category in products) {
        const section = document.createElement("div");
        section.className = "category";

        const title = document.createElement("h2");
        title.textContent = category;
        section.appendChild(title);

        const productContainer = document.createElement("div");
        productContainer.className = "products";

        products[category].forEach(product => {
          const div = document.createElement("div");
          div.className = "product";
          div.innerHTML = `
            <img src="${product.image}" alt="${product.name}">
            <h3>${product.name}</h3>
            <p>السعر: ${product.price}</p>
            <button onclick="addToCart('${product.name}', '${product.price}')">أضف إلى السلة</button>
          `;
          productContainer.appendChild(div);
        });

        section.appendChild(productContainer);
        container.appendChild(section);
      }
    }
    
    function addToCart(name, price) {
      cartItems.push({ name, price });
      updateCart();
    }

    function updateCart() {
      const countSpan = document.getElementById("count");
      const cartList = document.getElementById("cart-list");
      countSpan.textContent = cartItems.length;
      cartList.innerHTML = "";

      cartItems.forEach((item, index) => {
        const li = document.createElement("li");
        li.innerHTML = `
          ${index + 1}. ${item.name} – ${item.price}
          <button onclick="removeFromCart(${index})" style="margin-right:10px; background-color:red; border:none; color:white; padding:3px 6px; border-radius:4px;">❌ حذف</button>
