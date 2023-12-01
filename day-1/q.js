// first star

let input = document.querySelector('pre').innerText
let arrWords = []
let arrNums = []
arrWords = input.split('\n').slice(0, 1000)
for (let i in arrWords) {
    arrNums[i] = arrWords[i].replace(/[^0-9]/g, '')
}
let sum = 0
for (let stringNums of arrNums) {
    let num = stringNums[0] + stringNums.at(-1)
    num = parseInt(num)
    sum = sum + num
}
console.log(sum) 

// References
// https://stackoverflow.com/questions/10003683/how-can-i-extract-a-number-from-a-string-in-javascript
// https://www.w3schools.com/jsref/jsref_parseint.asp
// https://www.w3schools.com/jsref/jsref_slice_array.asp