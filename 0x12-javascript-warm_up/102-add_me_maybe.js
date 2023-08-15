#!/usr/bin/node

//function increments

exports.addMeMaybe = function(number, theFunction)
{
	number++;
	theFunction(number);
}

