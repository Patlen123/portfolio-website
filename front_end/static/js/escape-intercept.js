let escapeCount = 5;
let toastBox = document.getElementById("toastBox")

document.addEventListener('keydown', function (event) {
        if (event.key === 'Escape') {
            escapeCount--;
            console.log(escapeCount)
            if (escapeCount === 0) {
                event.preventDefault()
                window.location.replace("https://bbc.co.uk/weather");
            } else if (escapeCount !== 0)    {
                console.log("press esc " + escapeCount + " more times to leave")
                let toast = document.createElement('div');
                toast.classList.add('toast');
                toast.innerHTML = 'succ';
                toastBox.appendChild(toast)
            }
        } else {
            escapeCount = 0; // Reset the count if any other key is pressed
        }
    });

function escapeClicked()    {
    event.preventDefault()
    window.location.replace('https://bbc.co.uk/weather')
}