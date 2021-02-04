//VARIABLES DECLARATIONS

window.addEventListener('load', () => {
    const title = document.querySelector(".title");
    const strTitle = title.textContent;
    const splitTitle = strTitle.split("");
    title.textContent = "";
    const sounds = document.querySelectorAll(".sound");
    const pads = document.querySelectorAll(".pads div");
    const visual = document.querySelector(".visual");
    const colors = [
        "#60d394",
        "#d36060",
        "#c060d3",
        "#d3d160",
        "#6860d3",
        "#83d4ff"
    ];
    console.log(splitTitle);
    // console.log((sounds)[0]);

    // TITLE ANIMATION

    for( let i = 0; i < splitTitle.length; i++ ){
        title.innerHTML += "<span> " + splitTitle[i] + " </span>";
    }

    let letter = 0;
    let timer = setInterval(onTick, 50);

    function onTick(){
        const span = title.querySelectorAll('span')[letter];
        span.classList.add('fade');
        letter ++
        if (letter === splitTitle.length){
            complete();
            return;
        }
    }

    function complete(){
        clearInterval(timer);
        timer = null;
    }



    //KEYDOWN PRESS EVENTS
    
    document.addEventListener('keydown', function (e) {
        if (e.key === 'd') {
            sounds[0].currentTime = 0;
            sounds[0].play();
            createBublles(0);
        }
        if (e.key === 'f') {
            sounds[1].currentTime = 0;
            sounds[1].play();
            createBublles(1);
        }
        if (e.key === 'g') {
            sounds[2].currentTime = 0;
            sounds[2].play();
            createBublles(2);
        }
        if (e.key === 'h') {
            sounds[3].currentTime = 0;
            sounds[3].play();
            createBublles(3);
        }
        if (e.key === 'j') {
            sounds[4].currentTime = 0;
            sounds[4].play();
            createBublles(4);
        }
        if (e.key === 'k') {
            sounds[5].currentTime = 0;
            sounds[5].play();
            createBublles(5);
        }
    });

    // PLAY MUSIC FUNCTION


    pads.forEach((pad, index) => {
        pad.addEventListener('click', function () {
            sounds[index].currentTime = 0;
            sounds[index].play();

            createBublles(index);

        })
    })
    
    //Visual Animation/ BUBBLE CREATION

    function createBublles(index) {
        const bubble = document.createElement("div");
        visual.appendChild(bubble);
        bubble.style.background = colors[index];
        bubble.style.animation = "jump 1.5s ease";
        bubble.addEventListener('animationend', function () {
            visual.removeChild(this);
        })
    }

});


//MOUSE CURSOR DECORATION

let mouseCursor = document.querySelector(".cursor");

window.addEventListener("mousemove", cursor);

function cursor(e) {
    mouseCursor.style.top = e.pageY + "px";
    mouseCursor.style.left = e.pageX + "px";
}

//MUSICAL CHECKBOX

var audio = new Audio('sounds/energic piano.wav'),
    oneCheckbox = document.getElementById('one'),
    myfunction = function () {
        if (oneCheckbox.checked) {
            audio.play();
        }
        else {
            audio.pause();
        }
    };

audio.addEventListener('ended', function () {
    this.currentTime = 0;
    this.play();
}, false);


var audio2 = new Audio('sounds/sad guitare.wav'),
    twoCheckbox = document.getElementById('two'),
    mysecFunction = function () {
        if (twoCheckbox.checked) {
            audio2.play();
        }
        else {
            audio2.pause();
        }
    };

audio2.addEventListener('ended', function () {
    this.currentTime = 0;
    this.play();
}, false);

var audio3 = new Audio('sounds/guitare blue.wav'),
    treeCheckbox = document.getElementById('tree'),
    my3Function = function () {
        if (treeCheckbox.checked) {
            audio3.play();
        }
        else {
            audio3.pause();
        }
    };

audio3.addEventListener('ended', function () {
    this.currentTime = 0;
    this.play();
}, false);

var audio4 = new Audio('sounds/drum tempo.wav'),
    fourCheckbox = document.getElementById('four'),
    my4Function = function () {
        if (fourCheckbox.checked) {
            audio4.play();
        }
        else {
            audio4.pause();
        }
    };

audio4.addEventListener('ended', function () {
    this.currentTime = 0;
    this.play();
}, false);

var audio5 = new Audio('sounds/cello string.wav'),
    fiveCheckbox = document.getElementById('five'),
    my5Function = function () {
        if (fiveCheckbox.checked) {
            audio5.play();
        }
        else {
            audio5.pause();
        }
    };

audio5.addEventListener('ended', function () {
    this.currentTime = 0;
    this.play();
}, false);





