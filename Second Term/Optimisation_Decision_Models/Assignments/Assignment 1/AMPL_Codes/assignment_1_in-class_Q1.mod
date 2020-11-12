var F_oven >= 0;
var C_oven >= 0;

maximize earning: 120 * F_oven + 130 * C_oven;

subject to general_assembly: 2 * F_oven + C_oven <= 510;
subject to electronic_assembly: 2 * F_oven + 3 * C_oven <= 800;
subject to F_demand: F_oven <= 220;
subject to C_demand: C_oven <= 180;
