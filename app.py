from flask import Flask, jsonify, request
import utils


app = Flask(__name__)


@app.route("/icon/get", methods=["GET"])
def icon_get():
    """
    url中需要传参: ?website=url
    """
    url = request.args.get("website")
    if url is None:
        return jsonify({"errorMsg": "website url is null!"})
    return jsonify(utils.get_icon(url))


if __name__ == "__main__":
    # debug模式可以热加载
    app.run(port=5000, debug=True)
    # app.run(port=5000)
