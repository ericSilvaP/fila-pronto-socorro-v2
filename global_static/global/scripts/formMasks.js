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

function formatDate(date) {
  date = replaceNonNumbers(date)

  const days = date.slice(0, 2)
  if (date.length <= 2) return `${days}`
  const months = date.slice(2, 4)
  if (date.length <= 4) return `${days}/${months}`
  const year = date.slice(4, 8)
  return `${days}/${months}/${year}`
}

function addMask(selector, maskFunction) {
  const target = document.querySelector(selector)
  if (target) {
    target.addEventListener('input', (e) => {
      const div = e.target
      div.value = maskFunction(div.value)
    })
  } else {
    console.warn(`addMask: Campo com seletor "${selector}" não existe`)
  }
}

addMask('.form-cpf-field', formatCPF)
addMask('.form-phone-fiel1d', formatPhoneNumber)
addMask('.form-date-field', formatDate)
addMask('.form-sus-field', replaceNonNumbers)
