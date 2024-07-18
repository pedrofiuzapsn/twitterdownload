// script.js
function baixarVideo() {
    const videoURL = document.getElementById('videoURL').value;
    
    if (!videoURL) {
        alert('Por favor, insira um URL de vídeo.');
        return;
    }
    
    // Placeholder para chamada de API ao servidor backend
    fetch(`/api/download?url=${encodeURIComponent(videoURL)}`)
        .then(response => response.json())
        .then(data => {
            const resultsSection = document.getElementById('results');
            resultsSection.innerHTML = `
                <h2>Links de Download</h2>
                <a href="${data.downloadLink}" target="_blank">Baixar Vídeo</a>
            `;
        })
        .catch(error => {
            console.error('Erro ao baixar vídeo:', error);
        });
}
