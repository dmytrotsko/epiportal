// Add an event listener to each 'bulk-select' element
let bulkSelectDivs = document.querySelectorAll('.bulk-select');
bulkSelectDivs.forEach(div => {
    div.addEventListener('click', function (event) {
        let form = this.nextElementSibling;
        let showMoreLink = form.querySelector('a');
        let checkboxes = form.querySelectorAll('input[type="checkbox"]');

        if (event.target.checked === true) {
            checkboxes.forEach((checkbox, index) => {
                checkbox.checked = true;
                if (index > 4) {
                    checkbox.parentElement.style.display = checkbox.parentElement.style.display === 'none' ? 'block' : null;
                }
            })
            if (showMoreLink) {
                showMoreLink.innerText = 'Show less...';
            }
        } else if (event.target.checked === false) {
            checkboxes.forEach((checkbox, index) => {
                checkbox.checked = false
                if (index > 4) {
                    checkbox.parentElement.style.display = checkbox.parentElement.style.display === 'block' ? 'none' : null;
                }
            });
            if (showMoreLink) {
                showMoreLink.innerText = 'Show more...';
            }
        }
    });
});

function showLoader() {
    document.getElementById('loaderOverlay').style.display = 'flex';
    document.querySelector('.table-container').classList.add('faded');
}

$("#filterIndicatorSetsForm").find("input[type='checkbox']").on("change", function (e) {
    // Show loader and fade table
    showLoader();
    this.form.submit();
});

$("#location_search").on({
    "change": function (e) {
        // Show loader and fade table
        showLoader();
        this.form.submit();
    }
});