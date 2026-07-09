const fs = require('fs');
const html = fs.readFileSync('products.html', 'utf8');
const cards = html.split('<div class="product-card');
console.log('Total cards:', cards.length - 1);
for(let i=1; i<cards.length; i++) {
  const card = cards[i];
  const titleMatch = card.match(/<h3[^>]*>([^<]+)<\/h3>/i);
  console.log('Card', i, 'Title:', titleMatch ? titleMatch[1].trim() : 'N/A');
}
