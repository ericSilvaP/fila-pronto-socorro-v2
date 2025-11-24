function formatCPF(cpf) {
  console.log(cpf)
  cpf = cpf.replace(/[^0-9]+/g, '')

  const part1 = cpf.slice(0, 3)
  const part2 = cpf.slice(3, 6)
  const part3 = cpf.slice(6, 9)
  const part4 = cpf.slice(9, 11)
  if (cpf.length <= 3) return part1
  if (cpf.length <= 6) return [part1, part2].join('.')
  if (cpf.length <= 9) return [part1, part2, part3].join('.')
  return [[part1, part2, part3].join('.'), part4].join('-')
}

const cpfField = document.querySelector('.form-cpf-field')
cpfField.addEventListener('input', (e) => {
  const div = e.target
  div.value = formatCPF(div.value)
})
