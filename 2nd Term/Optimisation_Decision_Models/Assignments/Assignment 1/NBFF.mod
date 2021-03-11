# decision variables
var S;
var B;
var H;
var V;

# objective function
maximize earnings: 0.22 * S + 0.20 * B +  0.18 * H + 0.18 * V;

# constraints
subject to carrots: 62.5 * S + 50 * B + 62.5 * V <= 3750000;
subject to mushrooms: 75 * S + 100 * H <= 2000000;
subject to green_peppers: 62.5 * S + 50 * B + 75 * H + 62.5 * V <= 3375000;
subject to broccoli: 50 * S + 75 * B + 75 * H + 62.5 * V <= 3500000;
subject to corn: 72 * B + 62.5 * V <= 3750000;
subject to nn_S: S >= 0;
subject to nn_B: B >= 0;
subject to nn_H: H >= 0;
subject to nn_V: V >= 0;
 