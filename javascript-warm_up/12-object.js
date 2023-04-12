#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12,
};
console.log(myObject);

for (value in myObject) {
  const newObject = {
    type: 'object',
    value: 89,
  };
  myObject[value] = newObject[value];
}
console.log(myObject);
