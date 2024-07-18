// server.js
const express = require('express');
const ytdl = require('ytdl-core');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.static('public'));

app.get('/api/download', async (req, res) => {
    const videoURL = req.query.url;
    
    if (!videoURL) {
        return res.status(400).json({ error: 'Nenhum URL fornecido.' });
    }
    
    try {
        const info = await ytdl.getInfo(videoURL);
        const downloadLink = ytdl.chooseFormat(info.formats, { quality: 'highest' }).url;
        
        res.json({ downloadLink });
    } catch (error) {
        console.error('Erro ao obter informações do vídeo:', error);
        res.status(500).json({ error: 'Falha ao baixar vídeo.' });
    }
});

app.listen(PORT, () => {
    console.log(`Servidor rodando na porta ${PORT}`);
});
