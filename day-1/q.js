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
    let front = w.slice(0, i+1)

    if (front.length > 2) {
        for (let i = 2; i <= front.length; i++) {
            let slice = front.slice(i-2, i+1)
            let slice2 = slice.replace('one', 'o1ne') // added letters at end for edge case like 'twone' = 21
            slice2 = slice2.replace('two', 't2wo')
            slice2 = slice2.replace('six', 's6ix')
            front = front.replace(slice, slice2)
        }

        for (let i = 3; i <= front.length; i++) {
            let slice = front.slice(i-3, i+1)
            let slice2 = slice.replace('four', 'fo4ur')
            slice2 = slice2.replace('five', 'fi5ve')
            slice2 = slice2.replace('nine', 'ni9ne')
            front = front.replace(slice, slice2)
        }

        front = front.replaceAll('three', 't3hree')
        front = front.replaceAll('seven', 'se7ven')
        front = front.replaceAll('eight', 'ei8ght')
        
    }

    let back = w.slice(i+1, w.length)

    if (back.length > 2) {
        for (let i = 2; i <= back.length; i++) {
            let slice = back.slice(i-2, i+1)
            let slice2 = slice.replaceAll('one', 'o1ne')
            slice2 = slice2.replaceAll('two', 't2wo')
            slice2 = slice2.replaceAll('six', 's6ix')
            back = back.replaceAll(slice, slice2)
        }

        for (let i = 3; i <= back.length; i++) {
            let slice = back.slice(i-3, i+1)
            let slice2 = slice.replaceAll('four', 'f4our')
            slice2 = slice2.replaceAll('five', 'f5ive')
            slice2 = slice2.replaceAll('nine', 'n9ine')
            back = back.replaceAll(slice, slice2)
        }

        back = back.replaceAll('three', 't3hree')
        back = back.replaceAll('seven', 's7even')
        back = back.replaceAll('eight', 'e8ight')
        
    }


    return front + back
}
for (let i in arrWords) {
    w = wordsToNum(arrWords[i])
    console.log(`${arrWords[i]} = ${w}`)
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