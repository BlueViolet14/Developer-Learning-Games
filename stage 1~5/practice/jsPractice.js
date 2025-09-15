// 1번
const title = document.getElementById("title");
console.log(title.innerText);

// 2번
const desc = document.getElementById("desc");
desc.textContent = "자바스크립트로 바꿨다!";

// 3번
const btn = document.getElementById("btn");
const text = document.getElementById("text");

btn.addEventListener('click', () => {
    text.style.color = '#ff0000';
});

// 4번
const nameInput = document.getElementById("name")
const ok = document.getElementById("ok");
const msg = document.getElementById("msg");

ok.addEventListener('click', () => {
    const name = nameInput.value.trim();
    if (!name) {
        msg.innerText = "이름을 입력하세요.";
        return;
    }
    msg.innerText = `안녕하세요, ${name}님!`
});

// 5
const items = document.querySelectorAll(".features li")

items.forEach((items) => {
    items.addEventListener("click", () => {
        console.log(items.innerText);
    });
});