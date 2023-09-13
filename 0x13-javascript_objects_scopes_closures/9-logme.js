#!/usr/bin/node
exports.logMe = function logMe (item){
    if (typeof logMe.counter === 'undefined') {
	logMe.counter = 0;
    }
    logMe.counter += 1;
    console.log(`${logMe.counter}: ${item}`);
}
