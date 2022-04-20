#!/usr/bin/node
const {argv} = require('process');
let out = [];
argv.forEach((val, index) => {
	if (`${index}` == 2)
	{
		out = "Argument found";
	}
	else if (`${index}` < 2)
	{
		out = "Argument not found";
	}
	else
	{
		out = "Arguments found";
	}
});
console.log(out);
