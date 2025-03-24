const express = require('express');
const app = express();


app.use(express.json());

app.get('/login', (req, res) => {
    // const { username, password } = req.body;

    const { username, password } = req.query; // Use req.query to get query parameters

    console.log(`Username: ${username}, Password: ${password}`); // Log the query parameters

    if (username === password) {
        // res.send("User login Successful Jacques")
        res.status(200).send(`User login Successful Jacques, Username: ${username}`);
            // .status(200);
    }
    else {
        res
            .send("User not Logged in")
            .status(401);
    }
})

app.listen(5050, () => {
    console.log("Server is Running");
})


// curl -X POST -H "Content-Type: application/json" -d '{"username":"admin","password":"admin"}' http://localhost:5050/login
// curl -X GET -H "Content-Type: application/json" -d '{"username":"admin","password":"admin"}' http://localhost:5050/login
// http://localhost:5050/login?username=admin&password=admin
// ngrok config add-authtoken 2t0KL5rlzF0ZdXkkmvg0C1MH2Hz_3ZErytXuyT431pbGMcvAz