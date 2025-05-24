let count = 2;

function addIngredient() {
    const container = document.getElementById('ingredient-container');
    const input = document.createElement('input');
    input.name = "ingredient";
    input.placeholder = "Ingredient " + count++;
    container.appendChild(input);
}

// On form submit, gather all ingredient inputs into a single hidden input
function gatherIngredients() {
    const inputs = document.querySelectorAll('input[name="ingredient"]');
    const values = Array.from(inputs).map(input => input.value.trim()).filter(Boolean);
    document.getElementById("ingredients-final").value = values.join(',');
}

// Auto-expand textarea
const steps = document.getElementById('steps');
steps.addEventListener('input', function () {
    this.style.height = 'auto';
    this.style.height = this.scrollHeight + 'px';
});


async function searchRecipes() {
    const query = document.getElementById("searchBox").value.trim();
    if (query !== "") {
        window.location.href = `/search?query=${encodeURIComponent(query)}`;
    }
}
