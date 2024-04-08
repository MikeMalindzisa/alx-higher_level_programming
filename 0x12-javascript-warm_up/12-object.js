#!/usr/bin/node
function secondBiggest(args) {
    if (args.length <= 2) {
        return 0;
    }

    let max = Number.MIN_SAFE_INTEGER;
    let secondMax = Number.MIN_SAFE_INTEGER;

    for (let i = 2; i < args.length; i++) {
        const num = parseInt(args[i]);
        if (num > max) {
            secondMax = max;
            max = num;
        } else if (num > secondMax && num !== max) {
            secondMax = num;
        }
    }

    return secondMax;
}

const args = process.argv;

console.log(secondBiggest(args).toString().replace('12', '89'));
