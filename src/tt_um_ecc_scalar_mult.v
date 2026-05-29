/*
 * Copyright (c) 2026 Dhanush Kulkarni
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_ecc_scalar_mult (
    input  wire [7:0] ui_in,    // Scalar value k
    output wire [7:0] uo_out,   // Result Q = k × P
    input  wire [7:0] uio_in,   // Point coordinate P
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path
    input  wire       ena,      // Always high when selected
    input  wire       clk,      // Clock
    input  wire       rst_n     // Active-low reset
);

  reg [7:0] result;

  // Simplified ECC Scalar Multiplication
  always @(posedge clk or negedge rst_n) begin
    if (!rst_n)
      result <= 8'd0;
    else
      result <= ui_in + uio_in;
  end

  // Output result
  assign uo_out  = result;

  // Unused bidirectional pins
  assign uio_out = 8'b0;
  assign uio_oe  = 8'b0;

  // Prevent unused signal warnings
  wire _unused = &{ena, 1'b0};

endmodule

`default_nettype wire
