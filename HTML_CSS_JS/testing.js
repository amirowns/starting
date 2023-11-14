function sumArray(array) {
  if (Array.isArray(array) == false) {
    return 0;
  } else {
    return array
      .sort(function (a, b) {
        return a - b;
      })
      .slice(1, -1)
      .reduce((a, b) => a + b, 0);
  }
}
