
module qpsktest(
	input clk,
	input [3:0] x_in,
	output [7:0] y_out
);

  reg [7:0] temp;

  initial begin
	temp <= 8'd0;
  end
  
  assign y_out = ~temp;

  always@(posedge clk) begin
	temp[0] <= x_in[0];
	temp[2] <= x_in[1];
	temp[4] <= x_in[2];
	temp[6] <= x_in[3];
  end

endmodule
	
