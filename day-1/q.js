// first star

let input = document.querySelector('pre').innerText
let arrWords, arrNums = []
arrWords = input.split('\n')
arrWords = arrWords.slice(0, 1000)
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

// second star

let arrNums2 = []

function wordsToNum(word) {
    let w = word

    w = w.replaceAll('one', 'o1e')
    w = w.replaceAll('two', 't2o')
    w = w.replaceAll('six', 's6x')
    w = w.replaceAll('four', 'f4r')
    w = w.replaceAll('five', 'f5e')
    w = w.replaceAll('nine', 'n9e')
    w = w.replaceAll('three', 't3e')
    w = w.replaceAll('seven', 's7n')
    w = w.replaceAll('eight', 'e8t')

    return w
}
for (let i in arrWords) {
    w = wordsToNum(arrWords[i])
    arrNums2[i] = w.replace(/[^0-9]/g, '') 
}
let sum2 = 0
for (let stringNums of arrNums2) {
    let num = stringNums[0] + stringNums.at(-1)
    num = parseInt(num)
    sum2 = sum2 + num
}
console.log(sum2) 

// References
// https://stackoverflow.com/questions/10003683/how-can-i-extract-a-number-from-a-string-in-javascript
// https://www.w3schools.com/jsref/jsref_parseint.asp
// https://www.w3schools.com/jsref/jsref_slice_array.asp
// https://stackoverflow.com/questions/5582574/how-to-check-if-a-string-contains-text-from-an-array-of-substrings-in-javascript
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace