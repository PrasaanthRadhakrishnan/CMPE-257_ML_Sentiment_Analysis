
const express = require('express')
const {spawn} = require("child_process");
const cors = require('cors')
const bodyParser = require("body-parser");
const app = express()
const PORT = 5000;


app.use(cors())
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.json())

app.use(function(req, res, next){
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
})

app.post('/getAnalysis', (req, res, next) => {
    console.log("Inside Post")
    const { url } = req.body

    //const process = spawn('python', ["./python_scripts/run.py", url]);
    const process = spawn('python', ['./scripts/hello.py', url]);

    process.stdout.on('data', data => {
        const score = parseInt(data.toString());
        if(score >= 5){
            res.status(200).send({
                "response" : "Good"
            })
        }
        else if(score < 5){
            res.status(200).send({
                "response" : "Bad"
            })
        }

    })

})


app.listen(PORT, ()=>console.log(`NodeJS server is running on http://localhost:${PORT}`))
