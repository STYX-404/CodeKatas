function score(dice) {
  let counts = {};
  let points = 0;
  dice.forEach((x) => {
    counts[x] = (counts[x] || 0) + 1;
  });

  let ones = counts[1];
  let fives = counts[5];

  if (ones) {
    if (ones >= 3) {
      points += 1000 + (ones - 3) * 100;
    } else points += ones * 100;
  }
  if (fives) {
    if (fives >= 3) {
      points += 500 + (fives - 3) * 10;
    } else points += fives * 50;
  }

  let threes = Object.keys(counts).filter(
    (e) => e != 1 && e != 5 && counts[e] >= 3
  );
  if (threes.length) {
    points += threes * 100;
  }
  return points;
}