const express = require('express');
const cors = require('cors');
const app = express();
const PORT = 4000; // Or any other port

app.use(cors());
app.use(express.json()); // To parse JSON request bodies

// Define your API routes
app.get('/api/data', (req, res) => {
    res.json({ message: 'Hello from the Node.js backend!' });
});

app.get('/', (req, res) => {
    res.json({
        'message': "This is the root of the application."
    });
})

app.listen(PORT, () => {
    console.log(`Backend server running on port ${PORT}`);
});
