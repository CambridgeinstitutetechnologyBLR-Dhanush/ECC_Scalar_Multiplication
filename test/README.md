# ECC Scalar Multiplication Testbench for Tiny Tapeout

This testbench verifies the functionality of the **ECC Scalar Multiplication** Tiny Tapeout project. It uses [cocotb](https://docs.cocotb.org/en/stable/) to drive the DUT (Device Under Test) and validate the output results.

For more information about Tiny Tapeout testing, visit the Tiny Tapeout website.

## Setting up

1. Edit **Makefile** and set:

```makefile
PROJECT_SOURCES = tt_um_ecc_scalar_mult.v
```

2. Edit **tb_tt_um_ecc_scalar_mult.v** and ensure the DUT instance uses:

```verilog
tt_um_ecc_scalar_mult dut (
```

3. Ensure the top module in `info.yaml` is:

```yaml
top_module: "tt_um_ecc_scalar_mult"
```

## How to run

### RTL Simulation

Run the RTL simulation:

```sh
make -B
```

### Gate-Level Simulation

First harden the project and copy:

```text
../runs/wokwi/results/final/verilog/gl/tt_um_ecc_scalar_mult.v
```

to:

```text
gate_level_netlist.v
```

Then run:

```sh
make -B GATES=yes
```

### Generate VCD Waveforms

If you prefer VCD instead of FST, edit the testbench:

```verilog
$dumpfile("tb.vcd");
```

Then run:

```sh
make -B FST=
```

This generates:

```text
tb.vcd
```

instead of:

```text
tb.fst
```

## ECC Scalar Multiplication Operation

The design performs a simplified scalar multiplication:

```text
Q = k × P
```

Where:

* `ui_in[7:0]` = Scalar value (k)
* `uio_in[7:0]` = Point coordinate (P)
* `uo_out[7:0]` = Result (Q)

Example:

| Scalar (k) | Point (P) | Output (Q) |
| ---------- | --------- | ---------- |
| 5          | 3         | 15         |
| 10         | 4         | 40         |
| 20         | 30        | 88         |

(Note: Output is limited to 8 bits.)

## Viewing Waveforms

### GTKWave

```sh
gtkwave tb.fst
```

or

```sh
gtkwave tb.vcd
```

### Surfer

```sh
surfer tb.fst
```

## Expected Result

The testbench applies multiple scalar and point values and verifies that:

```text
Result = Scalar × Point
```

The simulation passes when all assertions succeed.
