let myButton = document.getElementById("my-button");
let myText= document.getElementById("some-text");

myButton.onclick = function() {
    myText.innerText += "\n You clicked the button!";
    myText.style.backgroundColor = "lavender";
    myText.style.color = "grey";
};
