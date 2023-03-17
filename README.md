# get-website-icon

这是一个方便获取指定网站图标的工具。

可以使用在线工具、API或者私有部署。

## 在线工具

主页: [https://icon.bxs.ink](https://icon.bxs.ink)

输入一个网址，即可获取网站图标。

> 下方会显示所有解析到的图标

![主页](/doc/homepage.png)

## Docker私有部署

```bash
# 创建运行容器
docker run -d -p 5000:5000 --name icon-server buxianshan/icon-server
```

访问5000端口即可。

## API

> GET https://icon.bxs.ink/get?url={target-website-url}

响应数据样例: 

```json
{
    "data": [
        "https://github.com/fluidicon.png",
        "https://github.githubassets.com/pinned-octocat.svg",
        "https://github.githubassets.com/favicons/favicon.png",
        "https://github.githubassets.com/favicons/favicon.svg"
    ],
    "success": true
}
```

![Postman](/doc/api-postman.png)