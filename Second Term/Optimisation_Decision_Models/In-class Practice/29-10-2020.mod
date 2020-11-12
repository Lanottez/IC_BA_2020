var wrenches >= 0;
var pilers >= 0;

maximize earnings: 0.13 * wrenches + 0.10 * pilers;

subject to steel: 1.5 * wrenches + 1.0 * pilers <= 27000;
subject to molding: 1.0 * wrenches + 1.0 * pilers <= 21000;
subject to assemply: 0.3 * wrenches + 0.5 * pilers <= 9000;
subject to demand_w: wrenches <= 15000;
subject to demand_p: pilers <= 16000;
