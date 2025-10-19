// Shows one page and hides the other two
function showPage(page) {
    console.log('Switching to page:', page);
    
    // Hide all of the divs:
    document.querySelectorAll('div').forEach(div => {
        div.style.display = 'none';
    });

    // Show the div provided in the argument
    const targetDiv = document.querySelector(`#${page}`);
    if (targetDiv) {
        targetDiv.style.display = 'block';
        console.log('Page displayed successfully');
    } else {
        console.error('Page not found:', page);
    }
}

// Wait for page to loaded:
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded, setting up button listeners');
    
    // Select all buttons
    const buttons = document.querySelectorAll('button');
    console.log('Found buttons:', buttons.length);
    
    buttons.forEach(button => {
        console.log('Button data-page:', button.dataset.page);
        
        // When a button is clicked, switch to that page
        button.onclick = function() {
            console.log('Button clicked, page:', this.dataset.page);
            showPage(this.dataset.page);
        }
    });
    
    // Show first page by default
    showPage('page1');
});