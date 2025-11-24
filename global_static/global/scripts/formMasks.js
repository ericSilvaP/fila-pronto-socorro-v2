function replaceNonNumbers(str) {
  return str.replace(/[^0-9]+/g, '')
}

function formatCPF(cpf) {
  cpf = replaceNonNumbers(cpf)

  const part1 = cpf.slice(0, 3)
  const part2 = cpf.slice(3, 6)
  const part3 = cpf.slice(6, 9)
  const part4 = cpf.slice(9, 11)
  if (cpf.length <= 3) return part1
  if (cpf.length <= 6) return [part1, part2].join('.')
  if (cpf.length <= 9) return [part1, part2, part3].join('.')
  return [[part1, part2, part3].join('.'), part4].join('-')
}

function formatPhoneNumber(phone) {
  phone = replaceNonNumbers(phone)

  if (phone.length <= 2) return `${phone}`
  return `(${phone.slice(0, 2)}) ${phone.slice(2, 11)}`.trim()
}

const cpfField = document.querySelector('.form-cpf-field')
cpfField.addEventListener('input', (e) => {
  const div = e.target
  div.value = formatCPF(div.value)
})

const phoneField = document.querySelector('.form-phone-field')
phoneField.addEventListener('input', (e) => {
  const div = e.target
  div.value = formatPhoneNumber(div.value)
})
