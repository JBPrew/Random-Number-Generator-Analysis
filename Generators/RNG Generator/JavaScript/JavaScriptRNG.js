const readline = require('readline');
const fs = require('fs') 

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


rl.question('File Name: ', (desiredFile) => {
    rl.question('Number of Data Points: ', (trials) => {
        if (desiredFile == "") {
            desiredFile = (Math.floor(Math.random() * 1001)).toString();
        }
        if (trials == 0) {
            trials = 2500 * 2500;
        }
        console.log(`File Name: ${desiredFile}`);
        console.log(`Trials: ${trials}`);
        var streamClear = fs.createWriteStream("C:/Users/Jack's PC/Desktop/GHP/Project/Generators/txtFiles/JavaScript" + desiredFile + ".txt");
        streamClear.write("")
        streamClear.close();
        var stream = fs.createWriteStream("C:/Users/Jack's PC/Desktop/GHP/Project/Generators/txtFiles/JavaScript" + desiredFile + ".txt", {flags:'a'});
        var i;
        for (i = 0; i < trials; i++) {
            stream.write(((Math.floor(Math.random() * 2)).toString()));
            if (i % 100000 == 0) {
                console.log(i);
            }
        }
        stream.close();
        rl.close();
    });
});
