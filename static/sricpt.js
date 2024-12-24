document.addEventListener("DOMContentLoaded", function () {
  const editButtons = document.querySelectorAll(".edit-btn");
  const bookForm = document.getElementById("bookForm");
  const formTitle = document.getElementById("form-title");
  const addButton = document.getElementById("addButton");
  const updateButton = document.getElementById("updateButton");
  const bookIdInput = document.getElementById("bookId");

  editButtons.forEach((button) => {
    button.addEventListener("click", function () {
      // Ambil data buku dari atribut data-* tombol edit
      const bookId = button.getAttribute("data-id");
      const bookTitle = button.getAttribute("data-title");
      const bookAuthor = button.getAttribute("data-author");
      const bookYear = button.getAttribute("data-year");

      // Isi form dengan data buku
      bookIdInput.value = bookId;
      document.getElementById("title").value = bookTitle;
      document.getElementById("author").value = bookAuthor;
      document.getElementById("year").value = bookYear;

      // Ubah judul form dan tampilkan tombol update
      formTitle.textContent = "Update Book";
      addButton.style.display = "none";
      updateButton.style.display = "inline-block";

      // Ubah action formulir agar mengarah ke route update_book
      updateButton.setAttribute("formaction", `/update_book/${bookId}`);
    });
  });
});
