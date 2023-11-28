document.addEventListener("DOMContentLoaded", function () {
  const title = document.querySelector('.grid');
  const cursor = document.createElement('div');
  const cursorWidth = 25;
  const cursorHeight = 25;

  cursor.classList.add('cursor');
  document.body.appendChild(cursor);

  document.body.addEventListener("mousemove", function (e) {
    let x = e.clientX;
    let y = e.clientY;
    const rect = title.getBoundingClientRect();

    cursor.style.top = (y - cursorHeight / 2) + "px";
    cursor.style.left = (x - cursorWidth / 2) + "px";
    cursor.style.width = cursorWidth + "px";
    cursor.style.height = cursorHeight + "px";
  });
});
