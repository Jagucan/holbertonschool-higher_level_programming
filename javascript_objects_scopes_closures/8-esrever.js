#!/usr/bin/node
exports.esrever = function (list) {
  const reverList = list.length;
  for (let x = 0; x < reverList / 2; x++) {
    const temp = list[x];
    const num = reverList - x - 1;
    list[x] = list[num];
    list[num] = temp;
  }
  return list;
};
