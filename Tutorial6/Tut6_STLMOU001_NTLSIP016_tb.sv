module tb_reg_mem;
parameter DATA_WIDTH = 8;
parameter ADDR_BITS = 5;//4 bit wide data parameter ADDR_BITS = 3; //8 Addresses
reg [ADDR_BITS-1:0] addr; 
reg [DATA_WIDTH-1:0] data_in; 
wire [DATA_WIDTH-1:0] data_out; 
reg wen, clk;
  
//Note passing of parameters syntax
reg_mem #(DATA_WIDTH,ADDR_BITS) RM (addr, data_in, wen, clk, data_out);
initial begin
// For use in EDAPlayground
$dumpfile("dump.vcd");
$dumpvars(1, tb_reg_mem);

clk = 0; wen = 1;

  for(int i=0;i<32;i=i+1) 
    begin 
      data_in = i; 
      addr = (i-0);
      $display("Write %d to address %d",data_in,addr); 
      repeat (2) #1 clk = ~clk;
end wen =0;
#1;
//Read 10-17 from addresses 0-7 
  for(int i=0;i<32;i=i+1) 
    begin data_in = i; 
      addr = (i-0);
      $display("Read %d from address %d",data_in,addr); repeat (2) #1 clk = ~clk;
end
end
endmodule