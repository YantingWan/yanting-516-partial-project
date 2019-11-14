from flask import jsonify
import connexion
from cloudmesh.common.StopWatch import StopWatch
from time import sleep

# Create the application instance
app = connexion.App(__name__, specification_dir="./")

# Read the yaml file to configure the endpoints
app.add_api("api.yaml")


# create a URL route in our application for "/"
@app.route("/")
def home():
    StopWatch.start("test")
    sleep(1)
    StopWatch.stop("test")
    msg = {"msg": "It's working!", "runtime": StopWatch.get("test")}
    return jsonify(msg)


if __name__ == "__main__":
    app.run(port=8000, debug=True)