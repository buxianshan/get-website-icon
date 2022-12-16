# get-website-icon

这是一个方便获取指定网站图标的工具。

## 在线工具

主页: [https://icon.bxs.ink](https://icon.bxs.ink)

输入一个网址，即可获取网站图标。

> 下方会显示所有解析到的图标

![主页](/doc/homepage.png)


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