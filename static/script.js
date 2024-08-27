document.getElementById('upload-form').addEventListener('submit', async function (e) {
    e.preventDefault();
    
    const fileInput = document.getElementById('file-input');
    if (fileInput.files.length === 0) {
        alert('Please select a file!');
        return;
    }

    const formData = new FormData();
    const fileName = fileInput.files[0].name;
    formData.append('file', fileInput.files[0]);

    const resultDiv = document.getElementById('result');
    const fileInfoDiv = document.getElementById('file-info');
    resultDiv.textContent = 'Uploading...';

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Accept-Language': 'en-US,en;q=0.5',
                'Origin': 'http://127.0.0.1:8000',
                'Referer': 'http://127.0.0.1:8000/docs',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0',
            },
            body: formData
        });

        if (!response.ok) {
            throw new Error('Upload failed!');
        }

        const data = await response.json();
        resultDiv.innerHTML = `<a href="/${data.folder}" download>Download Processed File</a>`;

        // Display the uploaded file name
        fileInfoDiv.innerHTML = `<span>File:</span> ${fileName}`;
    } catch (error) {
        resultDiv.textContent = `Error: ${error.message}`;
        fileInfoDiv.textContent = '';
    }
});
