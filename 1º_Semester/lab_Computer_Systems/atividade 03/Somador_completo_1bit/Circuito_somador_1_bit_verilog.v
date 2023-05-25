module Circuito_somador_1_bit_verilog (E,F,G,S,Cout);

input E,F,G;
output S,Cout;

assign S=((E^F)^G);
assign Cout=(G&(E^F)) | (E&F);

endmodule