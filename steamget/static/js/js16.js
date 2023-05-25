
function setMoney(e){
	let p = document.getElementsByClassName('input_money')[0];
	p.value = e.target.value;
	chechmoney();
}

function changeConfirm(argument) {
	let p = document.querySelectorAll('.fake_input > img')[0];
	let p_input = document.querySelectorAll('.row_confirm > input')[0];

	if(p.style.display == "none"){
		p.style.display = "block";
		p_input.checked = true;
	}else{
		p.style.display = "none";
		p_input.checked = false;
	}
}

var p = document.querySelectorAll('.radio_input > span > input');
p.forEach((elem)=>{
	elem.addEventListener('click',setMoney);
});

var p = document.querySelectorAll('.fake_input')[0];
p.addEventListener('click',changeConfirm);



var base = 0
function chechmoney(){
	let input_field = document.getElementsByClassName('input_money')[0].value;

	сommission = 35;

	bank_com = input_field * base;
	sell = parseInt(input_field) + parseInt(сommission) + parseInt(bank_com);
	take = input_field*1;

	if(isNaN(sell) || isNaN(bank_com)){
		sell = 0;
		сommission = 0;
		bank_com = 0;
		take = 0;
	}
	var p = document.getElementsByClassName('money_calc');
	p[3].innerHTML = sell.toFixed(1) + " руб";
	p[0].innerHTML = take.toFixed(1) + " руб";
	p[1].innerHTML = сommission.toFixed(1) + " руб";
	p[2].innerHTML = bank_com.toFixed(1) + " руб";
}



function checkPromo(){
    let p = document.getElementById('checkpromo').value;

    $.ajax({
			url: '../coificent_check_promo',
			type: 'GET',
			dataType: "text",
			data: { promo: p },

			error: function() {
				alert("Ошибка");
			},
			success: function (response) {
			    //result = JSON.parse(response).coef;
			    //setCoef(JSON.parse(response).coef);
			    base = JSON.parse(response).coef;
			    chechmoney();
			}
	});
}

function basecoef(){
    let p = document.getElementById('checkpromo').value;

    $.ajax({
			url: '../coificent_check_promo',
			type: 'GET',
			dataType: "text",
			data: { promo: p },

			error: function() {
				alert("Ошибка");
			},
			success: function (response) {
			    //result = JSON.parse(response).coef;
			    //setCoef(JSON.parse(response).coef);
			    base = JSON.parse(response).coef;
			}
	});
}



window.onload = basecoef;

var p = document.getElementById('checkpromo');
p.addEventListener('keyup', checkPromo);//лучше input

var p = document.querySelectorAll('.input_money')[0];
p.addEventListener('input',chechmoney);


function shadowOn(e){
	let p = document.getElementsByClassName('shadowW')[0];
	p.setAttribute('class','shadowW open');
}

function shadowOff(e){
	var p = document.querySelectorAll('.open');
	p.forEach((elem)=>{
	 	elem.classList.remove('open');
	});
}

function login__info_show(){
	let p = document.getElementsByClassName('modal_login')[0];
	p.setAttribute('class','modal_login open');
}



var p = document.getElementsByClassName('info_inpit_login')[0];
p.addEventListener('click',shadowOn);
p.addEventListener('click',login__info_show);



var p = document.querySelectorAll('.modal_login > button')[0];
p.addEventListener('click',shadowOff);











function changebank(e){

	var p = document.querySelectorAll('.openimg');
	p.forEach((elem)=>{
	 	elem.classList.remove('openimg');
	});
	var p = document.querySelectorAll('.elem_select_banks');
	p.forEach((elem)=>{
	 	elem.classList.remove('elem_select_banks');
	});

	if(e.target.className == "elem_banks"){
		e.target.setAttribute('class','elem_banks elem_select_banks');
		// var p = e.target.getElementsByClassName("bank_pick")[0];
		// p.setAttribute('class','bank_pick openimg');
		var p = e.target.getElementsByTagName("input")[0];
		p.checked = true;
	}else{
		e.target.parentElement.setAttribute('class','elem_banks elem_select_banks');

		// var elem = e.target.parentElement.getElementsByClassName("bank_pick")[0];
		// elem.setAttribute('class','bank_pick openimg');

		var p = e.target.parentElement.getElementsByTagName("input")[0];
		p.checked = true;
	}
	
}


var p = document.querySelectorAll('.elem_banks');
p.forEach((elem)=>{
	elem.addEventListener('click',changebank);
});






// modal faq
// function modal_FAO_show() {
//   let element = document.querySelector(".popup");
//   element.setAttribute("class", "popup open");
// }
// var p = document.querySelectorAll('.question')[0];
// p.addEventListener("click", modal_FAO_show);

// var element = document.querySelector(".FAO");
// element.addEventListener("click", modal_FAO_show);

// var element = document.querySelector(".close-FAO");
// element.addEventListener("click", shadowOff);



//modal contact


function contact_show(){
	let p = document.getElementsByClassName('modal_contac')[0];
	p.setAttribute('class','modal_contac open');
}


var p = document.getElementsByClassName('contact')[0];
p.addEventListener('click',shadowOn);
p.addEventListener('click',contact_show);



function shadowOff_background2(e) {
  if (e.target.className == "shadowW open") {
    var p = document.querySelectorAll(".open");
    p.forEach((elem) => {
      elem.classList.remove("open");
    });
  }
}
var p = document.getElementsByClassName('shadowW')[0];
p.addEventListener('click',shadowOff_background2);


///////////
function modal_FAO_show() {
  let element = document.querySelector(".popup");
  element.setAttribute("class", "popup open");
}
// !!!НАписал
function shadowOff_background(e) {
  if (e.target.querySelector(".popup__content")) {
    var p = document.querySelectorAll(".open");
    p.forEach((elem) => {
      elem.classList.remove("open");
    });
  }
}
// ////////////////////////////
var element = document.querySelector(".FAO");
element.addEventListener("click", modal_FAO_show);
var p = document.querySelectorAll('.question')[0];
p.addEventListener("click", modal_FAO_show);



var element = document.querySelector(".popup");
element.addEventListener("click", shadowOff_background);

//modal polit conf
function modal_polit_show() {
  let element = document.querySelectorAll(".popup")[1];

  element.setAttribute("class", "popup open");
}

var element = document.querySelector(".polit");
element.addEventListener("click", modal_polit_show);



var element = document.querySelectorAll(".popup")[1];
element.addEventListener("click", shadowOff_background);



//modal polz soglash
function modal_user_agreement_show() {
	let element = document.querySelectorAll(".popup")[2];
  
	element.setAttribute("class", "popup open");
  }
  
  var element = document.querySelector(".user-agreement");
  element.addEventListener("click", modal_user_agreement_show);
  
 
  
  var element = document.querySelectorAll(".popup")[2];
  element.addEventListener("click", shadowOff_background);

  //крестики
  var element = document.querySelectorAll(".close-FAO");
  element.forEach((elem)=>{
	elem.addEventListener('click',shadowOff);
});
