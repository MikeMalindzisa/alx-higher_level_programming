#!/usr/bin/node

if (!process.argv[2] || !process.argv[3]) {
  console.log(0);
} else {
  let max = Number(process.argv[2]);
  let secondMax = Number(process.argv[3]);

  for (let i = 2; i < process.argv.length; i++) {
    const num = Number(process.argv[i]);
    if (num > max) {
      secondMax = max;
      max = num;
    } else if (num > secondMax && num !== max) {
      secondMax = num;
    }
  }

  console.log(secondMax);
}
