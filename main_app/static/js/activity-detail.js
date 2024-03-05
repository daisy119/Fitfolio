const dateInput = document.getElementById('id_date')

const fileInput = document.getElementById('file-input')
const fileName = document.getElementById('file-name')

fileInput.addEventListener('change', evt => {
  const fileToUpload = evt.target.files[0].name
  if(fileToUpload) {
    fileName.innerText = fileToUpload
  } else {
    fileName.innerText = ""
  }
})

const picker = MCDatepicker.create({
  el: '#id_date',
  dateFormat: 'yyyy-mm-dd',
  closeOnBlur: true,
  selectedDate: new Date(),
})

dateInput.addEventListener("click", () => {
  picker.open()
})