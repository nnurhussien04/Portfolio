// 1. Programmer: We know how much user money have User: Deposit some money
// 2. Programmer: Determine how much the user is betting User: Determine number of lines to bet on
// 3. Programmer/User: Collect a bet amount
// 4. Programmer: Create a slot machine for user User: Spin the slot machine
// 5. Programmer/User: Check the user won
// 6. Programmer: Give the user thier winnings
// 7. Programmer: Determine if the user wants to play again User: Play Again


const prompt = require("prompt-sync")(); // Access to a function you can use to get user input

const ROWS = 3;
const COLS = 3;

const SYMBOLS_COUNT = { //This is a MAP
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

const SYMBOLS_VALUE = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

const spin = () => {
    const symbols = [];
    for(const[symbol,count] of Object.entries(SYMBOLS_COUNT)){ //Allow us to loop through all the values
        for(let i=0;i<count;i++){
            symbols.push(symbol);
        }
    }
    const reels = [];
    for(let i = 0;i < COLS;i++){
        reels.push([])
        const reelSymbols = [...symbols];
        for(let j = 0;j<ROWS;j++){
            const randomIndex = Math.floor(Math.random()*reelSymbols.length) //This does the maximum number, so goes between 0 and length of symbolsReels, the math floor rounds down to the nearest whole number
            const selectedSymbol = reelSymbols[randomIndex];
            reels[i].push(selectedSymbol);
            reelSymbols.splice(randomIndex,1); //Removes the element and the number says how many to remove
        }
        
    }

    return reels;
    

}


const userDeposit = () => { //This is a function
    while(true){
        const userAmount = prompt("Enter a deposit amount: "); //User input
        const numAmount = parseFloat(userAmount); //Convert from string to float

        if(isNaN(numAmount) || numAmount <=0){ //if the user input is not a number or less than 0
            console.log("Invalid deposit amount. Try again.");
        }
        else{
            return numAmount;
        }
    }

}

const getNumberofLines = () => {
    while(true){
        const numLines = prompt("Enter the number of lines to bet on(1-3): "); //User input
        const linesAmount = parseFloat(numLines); //Convert from string to float

        if(isNaN(linesAmount) || linesAmount <=0 || linesAmount > 3){ //if the user input is not a number or less than 0
            console.log("Invalid number of lines. Try again.");
        }
        else{
            return linesAmount;
        }
    }

}

const total = (balance,lines) => { // Need to keep balance in this function
    while(true){
        const betAmount = prompt("Enter the total bet: "); //User input
        const totalBet = parseFloat(betAmount); //Convert from string to float

        if(isNaN(totalBet) || totalBet <=0 || totalBet > balance/lines){ //if the user input is not a number or less than 0
            console.log("Invalid bet. Try again.");
        }
        else{
            return totalBet;
        }
    }
}



const transpose = (reels) => {
    const rows = [];
    for(let i=0;i<ROWS;i++){
        rows.push([]);
        for(let j = 0;j<COLS;j++){
            rows[i].push(reels[j][i]);

        }
    }

    return rows;
}

const printRows = (rows) => {
    for(const row of rows){ //This is a for each symbol
        let rowString = "";
        for (const [i,symbol] of row.entries()){ //This would output the index and the symbol together 
            rowString += symbol;
            if(i!= row.length-1){
                rowString += " | ";
            }
        }
        console.log(rowString)
    }

}

const getWinnings = (rows,bet,lines) => {
    let winnings = 0;
    for(let row = 0;row < lines;row++){
        const symbols  = rows[row];
        let allSame = true;
    
        for(const symbol of symbols){
            if(symbol != symbols[0]){
                allSame = false;
                break;
            }
        }
        if(allSame){
            winnings += bet * SYMBOLS_VALUE[symbols[0]]; //Multiply the value of the symbol by the bet
        }
    }
    return winnings;
}

const game = () => {
    let money = userDeposit();
    while(true){
        console.log("Balance: " + money)
        const lines = getNumberofLines();
        const bet = total(money,lines);
        money -= bet*lines;
        const reels = spin();
        const rows = transpose(reels);
        printRows(rows);
        const winnings = getWinnings(rows,bet,lines);
        money+=winnings;
        console.log("You won, $" + winnings.toString());

        if(money <= 0){
            console.log("Balance too low");
            break;
        }

        const playAgain = prompt("Do you want to play again (y/n)");
        if(playAgain != "y"){
            break;
        }
    }
}





game();











