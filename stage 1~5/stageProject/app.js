"use strict";

const btn = document.getElementById("btn");
const mainTitle = document.getElementById("main-title");

const nameInput = document.getElementById("name-input");
const helloBtn = document.getElementById("hello-btn");
const message = document.getElementById("message");

const item = document.querySelectorAll(".features li");

btn.addEventListener("click", () => {
    mainTitle.textContent = "자바스크립트로 바뀜!"
});

helloBtn.addEventListener("click", () => {
    const name = nameInput.value.trim();
    if (!name) {
        message.innerText = "이름을 입력하세요.";
        return;
    }
    message.innerText = `안녕하세요, ${name}님!`
    mainTitle.innerText = `환영합니다, ${name}님!`
});

nameInput.addEventListener("keydown", (e) => {
    if (e,key === "Enter") {
        helloBtn.click();
    }
});

item.forEach((item) => {
    item.addEventListener("click", () => {
        console.log(item.innerText);
    });
});

