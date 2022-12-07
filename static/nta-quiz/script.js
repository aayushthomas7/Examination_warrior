const startingHr = 2;
let time = Number(startingHr*60*60);
let timer = document.getElementById('timer')
setInterval(updateTimer,1000);
function updateTimer() {
    let hrs= Math.floor(time/3600);
    let min = (Math.floor(time/60))%60;
    min= min<10?'0'+min:min
    let sec = time%60;
    sec = sec <10 ?'0' +sec:sec
    timer.innerHTML=`0${hrs}:${min}:${sec}`;
    time--;
}

// const clearOption = (name1) => {
//     const radioBtns = document.querySelectorAll(
//         `input[type='radio'][name='${name1}']`
//     )
//     radioBtns.forEach(radioBtn => {
//         if(radioBtn.checked===true) radioBtn.checked= false;
//     });
//     }




