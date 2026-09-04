const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 3000;
const PUBLIC_DIR = '/home/lnx/Pictures/test';

const server = http.createServer((req, res) => {
  // Strip query parameters
  const cleanUrl = req.url.split('?')[0];
  
  // Default to index.html
  let filePath = path.join(PUBLIC_DIR, cleanUrl === '/' ? 'index.html' : cleanUrl);
  filePath = decodeURIComponent(filePath);

  if (fs.existsSync(filePath) && fs.statSync(filePath).isFile()) {
    const ext = path.extname(filePath).toLowerCase();
    let contentType = 'text/html';
    if (ext === '.js') contentType = 'text/javascript';
    else if (ext === '.css') contentType = 'text/css';
    else if (ext === '.png') contentType = 'image/png';
    else if (ext === '.jpg' || ext === '.jpeg') contentType = 'image/jpeg';
    else if (ext === '.svg') contentType = 'image/svg+xml';
    
    res.writeHead(200, { 'Content-Type': contentType });
    fs.createReadStream(filePath).pipe(res);
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('404 Not Found');
  }
});

server.listen(PORT, () => {
  console.log(`Web server running at http://localhost:${PORT}/`);
});
