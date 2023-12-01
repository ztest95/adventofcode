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
    let i = w.search(/[0-9]/)
    let front = w.slice(0, i)

    if (i > 2) {
        front = front.replaceAll('one', '1')
        front = front.replaceAll('two', '2')
        front = front.replaceAll('three', '3')
        front = front.replaceAll('four', '4')
        front = front.replaceAll('five', '5')
        front = front.replaceAll('six', '6')
        front = front.replaceAll('seven', '7')
        front = front.replaceAll('eight', '8')
        front = front.replaceAll('nine', '9')
    }

    let j = w.lastIndexOf(/[0-9]/)
    let back = w.slice(i+1, w.length)

    if (back.length > 2) {
        back = back.replaceAll('one', '1')
        back = back.replaceAll('two', '2')
        back = back.replaceAll('three', '3')
        back = back.replaceAll('four', '4')
        back = back.replaceAll('five', '5')
        back = back.replaceAll('six', '6')
        back = back.replaceAll('seven', '7')
        back = back.replaceAll('eight', '8')
        back = back.replaceAll('nine', '9')
    }

    return front + w[i] + w[j] + back
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