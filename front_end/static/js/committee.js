function openModal(counter) {
    //In this case modal refers to the background and modalcontent to the inside, it's a bit stupid
    const modal = document.getElementById('modal' + counter);
    modal.style.display = 'block';
    document.addEventListener(
        "click",
        function (event) {
            if(event.target.id === "modal" + counter) {
                modal.style.display = 'none';
            }
        },
        false
    )
}

function closeModal(counter) {
    var modal = document.getElementById('modal' + counter);
    modal.style.display = 'none';
}

