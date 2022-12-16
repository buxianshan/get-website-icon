from flask import Flask, jsonify, request, render_template
import utils


app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """
    主页
    """
    return render_template("index.html")


@app.route("/get", methods=["GET"])
def get_icon():
    """
    url中需要传参: ?url={target website}
    """
    url = request.args.get("url")
    # if url is None:
    #     return jsonify({"errorMsg": "website url is null!"})
    try:
        icons = utils.get_icon(url)
        return jsonify({"success": True, "data": icons})
    except Exception as e:
        return jsonify({"success": False, "data": [], "errorMsg": str(e)})


if __name__ == "__main__":
    # debug模式可以热加载
    # app.run(host="0.0.0.0", port=5000, debug=True)
    app.run(host="0.0.0.0", port=5000)
