#!/usr/bin/node
from 4-rectangle.js import Rectangle;
class Square extends Rectangle {
  constructor (size) {
    super();
    this.size = size;
  }

  charPrint (c) {
  if (isNaN(c)) {
    c = 'X';
  }
  for (let i = 0; i <= Rectangle.height; i++) {
    console.log(c.repeat(Rectangle.width));
  }

}
