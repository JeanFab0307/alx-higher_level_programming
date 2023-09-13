#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  const len = list.length;
  for (i in list) {
    newList[len - i - 1] = list[i];
  }
  return newList;
};
