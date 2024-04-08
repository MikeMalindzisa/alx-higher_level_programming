#!/usr/bin/node
function factorial(n) {
    // Base case: factorial of 0 or 1 is 1
    if (isNaN(n) || n === 0 || n === 1) {
        return 1;
    } else {
        // Recursive case: factorial of n is n times factorial of (n-1)
        return n * factorial(n - 1);
    }
}

const arg = parseInt(process.argv[2]);
console.log(factorial(arg));
