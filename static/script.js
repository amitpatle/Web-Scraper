document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        const url = form.querySelector('#url').value;
        const response = await fetch('/scrape', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url })
        });
        const data = await response.json();

        // Update the lists with scraped data
        updateList('image-list', 'Images', data.images);
        updateList('audio-list', 'Audio', data.audio);
        updateList('video-list', 'Videos', data.video);
    });

    function updateList(listId, heading, items) {
        const list = document.getElementById(listId);
        list.innerHTML = `<h3>${heading}</h3>`;
        items.forEach(item => {
            const listItem = document.createElement('li');
            listItem.textContent = item;
            list.appendChild(listItem);
        });
    }
});
