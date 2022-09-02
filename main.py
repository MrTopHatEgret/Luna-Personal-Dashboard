from flask import Flask, request, jsonify
import Backend

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    text = request.args.get("text")
    processing_output = Backend.process(text)
    return jsonify(processing_output.to_json())


if __name__ == "__main__":
    app.run(debug=True)
