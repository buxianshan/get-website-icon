let loading = `
    <div id="loading" class="d-flex justify-content-center">
        <div class="spinner-border" role="status">
            <span class="visually-hidden">Loading...</span>
        </div>
    </div>`

$(function () {
    $("#searchIcon").click(function () {
        // 清空图标
        $("#container").empty()
        // 添加loading元素
        $("#container").append($(loading))
        let target = $("input").val()
        $.ajax({
            url: "/get?url=" + target,
            type: "GET",
            dataType: "json",
            data: {},
            success: function (data) {
                $("#container").empty()
                for (let i of data.data) {
                    let split = i.split("/")
                    let fileName = split[split.length - 1]
                    let div = $(`
                            <a class="tile" title="${fileName}" target="_blank" href="${i}">
                                <div class="tile-icon">
                                    <img src="${i}">
                                </div>
                                <div class="tile-title title-ltr">
                                    <span>${fileName}</span>
                                </div>
                            </a>`)
                    $("#container").append(div)
                }
                let tip = "<br/>If you think this is a bug, please <a href='https://github.com/buxianshan/get-website-icon/issues' target=\"_blank\">create an issue in here.<a/>"
                if (data.success === false) {
                    $("#container").append($(`<p class="errorMsgBox">API error.${tip}</p>`))
                } else if (data.data.length === 0) {
                    $("#container").append($(`<p class="errorMsgBox">API returns 0 icon.${tip}</p>`))
                }
            },
            error: function (e) {
                $("#container").empty()
                $("#container").append($(`<p class="errorMsgBox">${e.errorText}</p>`))
                console.log(e)
            }
        })
    });
});