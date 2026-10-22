document.addEventListener("DOMContentLoaded", function () {
    const options = {defaultProtocol: "https"}
    const contentElements = document.querySelectorAll(".content");

    contentElements.forEach(function (contentElement) {
        const content = contentElement.innerHTML;
        const linkified = linkifyHtml(content);
        const fullFormat = marked.parse(linkified)
        contentElement.innerHTML = linkified;
    });
});