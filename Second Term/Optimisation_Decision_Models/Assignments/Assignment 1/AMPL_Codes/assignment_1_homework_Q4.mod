var SW1>=0;
var SW2>=0;
var SW3>=0;
var SW4>=0;
var SP1>=0;
var SP2>=0;
var SP3>=0;
var SP4>=0;
var PW1>=0;
var PW2>=0;
var PW3>=0;
var PW4>=0;
var PP1>=0;
var PP2>=0;
var PP3>=0;
var PP4>=0;

maximize earnings: 0.13*(SW1+SW2+SW3+SW4) + 0.10*(SP1+SP2+SP3+SP4);

subject to required_steel_1: 1.5*PW1+1*PP1<=15000;
subject to required_steel_2: 1.5*PW2+1*PP2<=15000;
subject to required_steel_3: 1.5*PW3+1*PP3<=15000;
subject to required_steel_4: 1.5*PW4+1*PP4<=15000;
subject to required_molding_machine_1: 1*PW1+1*PP1<=12000;
subject to required_molding_machine_2: 1*PW2+1*PP2<=12000;
subject to required_molding_machine_3: 1*PW3+1*PP3<=12000;
subject to required_molding_machine_4: 1*PW4+1*PP4<=12000;
subject to required_assembly_machine_1: 0.3*PW1+0.5*PP1<=8000;
subject to required_assembly_machine_2: 0.3*PW2+0.5*PP2<=8000;
subject to required_assembly_machine_3: 0.3*PW3+0.5*PP3<=8000;
subject to required_assembly_machine_4: 0.3*PW4+0.5*PP4<=8000;
subject to Wrenches_production_sale_1: SW1<=PW1;
subject to Wrenches_production_sale_2: SW1+SW2<=PW1+PW2;
subject to Wrenches_production_sale_3: SW1+SW2+SW3<=PW1+PW2+PW3;
subject to Wrenches_production_sale_4: SW1+SW2+SW3+SW4<=PW1+PW2+PW3+PW4;
subject to pilers_production_sale_1: SP1<=PP1;
subject to pilers_production_sale_2: SP1+SP2<=PP1+PP2;
subject to pilers_production_sale_3: SP1+SP2+SP3<=PP1+PP2+PP3;
subject to pilers_production_sale_4: SP1+SP2+SP3+SP4<=PP1+PP2+PP3+PP4;
subject to wrenches_sales_demand_1: SW1<=5000;
subject to wrenches_sales_demand_2: SW2<=9000;
subject to wrenches_sales_demand_3: SW3<=10000;
subject to wrenches_sales_demand_4: SW4<=15000;
subject to pilers_sales_demand_1: SP1<=6000;
subject to pilers_sales_demand_2: SP2<=11000;
subject to pilers_sales_demand_3: SP3<=12000;
subject to pilers_sales_demand_4: SP4<=15000;



