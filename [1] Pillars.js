function pillars(num_pill, dist, width) {
  // if there is one pillar --> there is no distance
  if (num_pill < 2) {
    return 0;
  }
  //more than one pillar
  else {
    var distance = (num_pill - 2) * width + dist * 100 * (num_pill - 1);
  }
  return distance;
}
