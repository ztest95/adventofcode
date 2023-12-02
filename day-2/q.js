let input = document.querySelector('pre').innerText
let arrGames = input.split('\n')
arrGames = arrGames.slice(0, arrGames.length -1)
// ['Game1',
//  'Game2',
//  'Game3']

sum_of_possible = 0
let matches = []
for (let i in arrGames) {
    matches[i] = arrGames[i].replace(/.*:/, "")
}
for (let i in arrGames) {
    // Array containing each match of a game
    let matches = arrGames[i].replace(/.*:/, "") // removes Game number label
    // ['1 blue, 1 red; 2 blue, 2 red']
    for (let j in matches) { 
        let dict = {}
        let draws = matches.split(';')
        // ['1 blue, 1 red',
        //  '2 blue, 2 red']
        for (let ball of draws[j]) {

        }
        for (let draw of draws) {
            let n = draw.replace(/[^0-9]/, '')
            dict['r'] = draw.includes('red') ? parseInt(n) : 0
            dict['g'] = draw.includes('green') ? parseInt(n) : 0
            dict['b'] = draw.includes('blue') ? parseInt(n) : 0
        }
        matches[j] = dict
        // [{ 'b' : int, 'r': int, 'g': int },
        //  { 'b' : int, 'r': int, 'g': int }]
        if (matches[j]['r'] > 12) {
            break
        }
        if (matches[j]['g'] > 13) {
            break
        }
        if (matches[j]['r'] > 14) {
            break
        }
        // if nothing is above the limit
        
    }
    sum_of_possible =  sum_of_possible + parseInt(i) + 1
}
console.log(sum_of_possible)


let games = {
    'Game1': {
        'Match1': {
            'blue': 9,
            'red': 8
        },
        'Match2': {
            'blue': 2,
            'red': 7
        },
        'Match3': {
            'blue': 1,
            'red': 12
        }
    },
    'Game2': {
        'Match1': {
            'blue': 9,
            'red': 8
        },
        'Match2': {
            'blue': 2,
            'red': 7
        },
        'Match3': {
            'blue': 1,
            'red': 12
        }
    }
}

console.log(games.Game1)