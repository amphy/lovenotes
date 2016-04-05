window.addEventListener("load", setup, false);

var keystrokes = [];
var timings = [];
var time = [];
var textarea = null;

var keys = null;
var times = null;
var submit = null;

var startTime = null;
var endTime = null;
var delta = null;

function setup() {

  keys = document.getElementById("keys");
  times = document.getElementById("times");

  submit = document.getElementById("submit");
  submit.addEventListener("click", preprocess);

  textarea = document.getElementById("letter");
  textarea.addEventListener("keydown", backspace);
  textarea.addEventListener("keypress", record);
  textarea.addEventListener("keyup", stoprecord);
}

function backspace(event) {
  if(event.keyCode == 8) {
    time.push(Date.now());
    keystrokes.push(event.keyCode);
    console.log("backspace");
  }
}

function record(event) {
  //record start time using Date
  time.push(Date.now());
  //store keyCode
  keystrokes.push(event.charCode);
  console.log(event.charCode);
}

function stoprecord() {
  console.log("Time: " + time[keystrokes.length-1]);
  //timings.push(delta);
  //startTime = Date.now();
}

function preprocess() {
  var text = JSON.stringify(keystrokes);
  keys.value = text;

  for(i = 0; i < time.length-1; i++){
    delta = time[i+1]-time[i];
    timings.push(delta);
  }
  timings.push(0);
  
  var text2 = JSON.stringify(timings);
  times.value = text2;

  console.log(text2);
  console.log(text);
}
