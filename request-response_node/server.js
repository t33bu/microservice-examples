const http = require('http');
const port = 5544;

sensor_data = {
    'type': 'humidity',
    'sensorId': 123,
    'value': 0,
    'unit': '%',
    'eventId': 0
}

http.createServer((req,res) => {
    console.log(`Request received for '${req.url}'`);
    res.writeHead(200, { "Content-Type": "application/json" });
    res.write(JSON.stringify(sensor_data));
    res.end();
    sensor_data["eventId"] = sensor_data["eventId"] + 1;
}).listen(port,() => {
    console.log(`Server in running on port ${port}`);
});
