const shipFactory = (length, n) => {
  let ship = Array(length).fill("o");
  let name = n;
  let life = length;
  function hit() {
    this.life -= 1;
  }
  const isSunk = () => {
    if (life == 0) {
      return true;
    } else {
      return false;
    }
  };

  return { length, ship, name, life, hit, isSunk };
};

let ship = shipFactory(1, "s1");
console.log(ship);
ship.hit();
console.log(ship.life);
console.log(ship);
