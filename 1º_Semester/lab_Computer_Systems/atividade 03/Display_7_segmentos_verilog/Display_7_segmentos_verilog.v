module Display_7_segmentos_verilog(A, B , C, D, D0, D1, D2, D3, D4, D5, D6);
	input A, B, C, D;
	output D0, D1, D2, D3, D4, D5, D6;
	
	assign D0 = ((~A&~C)&(B^D))|((A&D)&(B^C)); 
	assign D1 = (A&C)&(B^D)|(~A&B)&(C^D)|(A&B&~C&~D)|(A&B&C&D);
	assign D2 = (A&B&C)|(~A&~B&C&~D)|(A&B&~C&~D);
	assign D3 = (((~A)&(~C))&(B^D))|(B&C&D)|(A&(~B)&C&(~D));
	assign D4 = ((~A&~C)&(B^D))|((~A&D)&(B^C))|(~A&B&C&D)|(A&~B&~C&D);
	assign D5 = ((~A&~B)&(C^D))|((B&D)&(A^C))|(~A&~B&C&D);
	assign D6 = (~A&~B&~C)|(~A&B&C&D)|(A&B&~C&~D);
endmodule