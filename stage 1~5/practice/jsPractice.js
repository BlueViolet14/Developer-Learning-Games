"use strict";

const outer = document.getElementById("outer");
const inner = document.getElementById("inner");

outer.addEventListener('click', () => {
    console.log("outer 버블링");
});

inner.addEventListener('click', () => {
    console.log("inner 버블링");
});

outer.addEventListener('click', () => {
    console.log("outer 캡쳐링");
}, true);

const list = document.querySelector('.menu');

list.addEventListener('click', (e) => {
    const li = e.target.closest('li');
    if (!li || !list.contains(li)) return;
    console.log('클릭:', li.innerText);
});

const linkPrevent = document.getElementById('link');

linkPrevent.addEventListener('click', (e) => {
    e.preventDefault();
    console.log("이동이 차단되었습니다.");
});

const form = document.getElementById("login-form");
const status = document.getElementById("status");

form.addEventListener("submit", (e) => {
    e.preventDefault(); // 기본 제출(새로고침) 막기

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();

    if (!username || !password) {
        status.textContent = "아이디와 비밀번호를 모두 입력하세요.";
        return;
    }

    status.textContent = `로그인 시도: ${username}`;
});

const todoList = document.getElementById("todo-list");
const addBtn = document.getElementById("add");

// 1) 이벤트 위임: li 클릭 시 콘솔에 텍스트 출력
list.addEventListener("click", (e) => {
    // li 태그를 클릭했는지 확인
    if (e.target.tagName === "LI") {
        console.log("클릭한 항목:", e.target.innerText);
    }
});

// 2) 버튼 클릭 시 새로운 li 추가
addBtn.addEventListener("click", () => {
    const newItem = document.createElement("li");
    newItem.innerText = `할 일 ${todoList.children.length + 1}`;
    todoList.appendChild(newItem);
});
