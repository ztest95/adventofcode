// part 1
// This took me like 6 hours man

let input = document.querySelector('pre').innerText
let arrGames = input.split('\n')
arrGames = arrGames.slice(0, arrGames.length -1)
// ['Game1: qweqwe',
//  'Game2: qweqwe',
//  'Game3: qweqwe']

sum_of_possible = 0
for (let i in arrGames) {
    arrGames[i] = arrGames[i].replace(/.*:/, "")
    // ['1 blue, 1 red; 2 blue, 2 red; 3 blue, 3 red',
    //  '1 blue, 1 red; 2 blue, 2 red; 3 blue, 3 red']
}

for (let i in arrGames) {
    // arrGames[i] = '1 blue, 1 red; 2 blue, 2 red; 3 blue, 3 red'
    let matches = arrGames[i].split(';')
    // ['1 blue, 1 red', '2 blue, 2 red', '3 blue, 3 red]
    let dict = {
        0: 0,
        1: 0,
        2: 0
    }

    for (let draw in matches) {
        // matches[draw] = '1 blue, 1 red'
        // or arrGames[i][draw]
        let dictarr = []
        let pick = matches[draw].split(',')
        // Array ['1 blue', '1 red'] 
        // replace(/[^0-9]/, '')
        for (let item in pick) {

            // pick[item] = '1 blue'
            let n = pick[item].replace(/[^0-9]/g, '')
            n = parseInt(n)
            if (pick[item].includes('red')) {
                dict[0] = n
            }
            if (pick[item].includes('green')) {
                dict[1] = n
            }
            if (pick[item].includes('blue')) {
                dict[2] = n
            }
 
            dictarr[item] = dict
            
        }
        // After it goes through a match (multiple picks / draw)
        matches[draw] = values(dict)
        dictarr = []
    }
    arrGames[i] = matches
}

for (let matches in arrGames) {
    matches = parseInt(matches)
    let possible = true

    for (let draws in arrGames[matches]) {
        draws = parseInt(draws)

        if (arrGames[matches][draws][0] > 12) {
            possible = false
        }  
        if (arrGames[matches][draws][1] > 13) {
            possible = false
        } 
        
        if (arrGames[matches][draws][2] > 14) { 
            possible = false
        } 

    }

    if (possible) {
        sum_of_possible = sum_of_possible + 1 + parseInt(matches)
    }
    
}
console.log(sum_of_possible)


// [ //Games
//     [ //Matches
//         { // Draw
//             'r': 0,
//             'g': 0,
//             'b': 0
//         },
//         { // Draw
//             'r': 0,
//             'g': 0,
//             'b': 0
//         }
//     ],
//     [
//         // Match 2
//     ]
// ]


// part 2
sum_of_power = 0
for (let matches in arrGames) {
    matches = parseInt(matches)
    let red = 0
    let green = 0
    let blue = 0

    for (let draws in arrGames[matches]) {
        draws = parseInt(draws)

        if (arrGames[matches][draws][0] > red) {
            red = arrGames[matches][draws][0]
        }  
        if (arrGames[matches][draws][1] > green) {
            green = arrGames[matches][draws][1]
        } 
        if (arrGames[matches][draws][2] > blue) { 
            blue = arrGames[matches][draws][2]
        } 
    }
    sum_of_power = sum_of_power + (red * blue * green )
}
console.log(sum_of_power)
// References
// ChatGPT for RegEx (.replace(/.*:/, ""))
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration
// https://www.geeksforgeeks.org/how-to-replace-multiple-spaces-with-single-space-in-javascript/