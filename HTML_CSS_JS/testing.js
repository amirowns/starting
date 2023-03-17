function digPow(n, p) {
  let arr = String(n)
    .split("")
    .map((num) => parseInt(num));

  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    sum += arr[i] ** (i + p);
  }

  if (sum % n == 0) {
    return sum / n;
  } else {
    return -1;
  }
}

digPow(89, 1);
digPow(92, 1);
digPow(46288, 3);
