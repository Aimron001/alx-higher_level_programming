#!/usr/bin/node
const dict = require('./101-data').dict;

const totalList = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};
for (const j in valsUniq) {
  const list = [];
  for (const k in totalList) {
    if (totalList[k][1] === valsUniq[j]) {
      list.unshift(totalList[k][0]);
    }
  }
  newDict[valsUniq[j]] = list;
}
console.log(newDict);
