from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from loguru import logger
import utils
from log_config import InterceptHandler


app = Flask(__name__)
CORS(app, resources=r'/*')


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
    # 添加日志拦截器，使用loguru
    app.logger.addHandler(InterceptHandler())
    logger.info("正在启动服务: http://127.0.0.1:5000")
    # debug模式可以热加载
    # app.run(host="0.0.0.0", port=5000, debug=True)
    app.run(host="0.0.0.0", port=5000)
