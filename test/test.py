# SPDX-FileCopyrightText: © 2026 Dhanush Kulkarni
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start ECC Scalar Multiplication Test")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0

    await ClockCycles(dut.clk, 10)

    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    # Test Case 1
    dut.ui_in.value = 5
    dut.uio_in.value = 3

    await ClockCycles(dut.clk, 1)

    assert int(dut.uo_out.value) == 15

    # Test Case 2
    dut.ui_in.value = 10
    dut.uio_in.value = 4

    await ClockCycles(dut.clk, 1)

    assert int(dut.uo_out.value) == 40

    # Test Case 3
    dut.ui_in.value = 20
    dut.uio_in.value = 30

    await ClockCycles(dut.clk, 1)

    # 20 × 30 = 600 → 600 mod 256 = 88
    assert int(dut.uo_out.value) == 88

    dut._log.info("ECC Scalar Multiplication Test Passed")
