from flask import Flask
import AdafruitDHT
app = Flask(__name__, static_url_path='')

@app.route("/")
def index():
    data = AdafruitDHT.temp()
    temp = ""
    if data[0] > 80:
        temp = "The fan is working now !"
    else:
        temp = "The fan is not working now !"
    return '<html><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous"><body style="background-color: #effffc"><div class="container" style="padding:10px"> <form action="GET"><button type="button" class="btn btn-info" onclick="window.location.reload()">Get Info</button></form><h1>' + 'Temperature={0:0.1f}* Humidity={1:0.1f}%'.format(data[1], data[0]) + '</h1><h1>' + temp + '</h1></div></body></html>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

