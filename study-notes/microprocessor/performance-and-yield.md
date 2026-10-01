# 2. Work and Execution Rate Determine CPU Time, While Defects Limit Chip Yield

A faster clock or fewer instructions does not automatically mean a faster program. **CPU time equals executed instruction count × average cycles per instruction (CPI) ÷ clock rate.** Completing more tasks per second increases throughput, but does not necessarily shorten each task. Speeding up only part of a program leaves the unchanged work as a limit on overall speedup. Manufacturing has a separate constraint: at the same defect density, larger dies tend to have lower yield—the fraction of dies that work. Chiplets and harvesting can reduce the silicon wasted by defects.

## Contents

- [1. Software Defines the Work That the Machine Executes](#1-software-defines-the-work-that-the-machine-executes)
  - [1.1 High-Level Code Expresses Operations, Assembly Names Instructions, and Hardware Uses Bits](#11-high-level-code-expresses-operations-assembly-names-instructions-and-hardware-uses-bits)
  - [1.2 Algorithms, Compilers, Hardware, and I/O All Affect Execution Time](#12-algorithms-compilers-hardware-and-io-all-affect-execution-time)
  - [1.3 Personal, Server, Embedded, and Supercomputers Serve Different Purposes](#13-personal-server-embedded-and-supercomputers-serve-different-purposes)
  - [1.4 Main Memory Loses Its Data Without Power but Storage Keeps It](#14-main-memory-loses-its-data-without-power-but-storage-keeps-it)
- [2. Performance Is Measured as Time per Task or Tasks per Second](#2-performance-is-measured-as-time-per-task-or-tasks-per-second)
  - [2.1 Giga Is a Billion and Nano Is a Billionth](#21-giga-is-a-billion-and-nano-is-a-billionth)
  - [2.2 CPI Is the Average Number of Clock Cycles per Instruction](#22-cpi-is-the-average-number-of-clock-cycles-per-instruction)
  - [2.3 CPU Time Equals Instruction Count Times CPI Divided by Clock Rate](#23-cpu-time-equals-instruction-count-times-cpi-divided-by-clock-rate)
  - [2.4 Instructions per Second Equal Clock Rate Divided by CPI](#24-instructions-per-second-equal-clock-rate-divided-by-cpi)
  - [2.5 Higher Throughput Does Not Necessarily Shorten Each Task](#25-higher-throughput-does-not-necessarily-shorten-each-task)
- [3. No Single Factor Decides How Fast a Program Runs](#3-no-single-factor-decides-how-fast-a-program-runs)
  - [3.1 The Fastest Clock Can Lose When Its CPI Is High](#31-the-fastest-clock-can-lose-when-its-cpi-is-high)
  - [3.2 At the Same Clock Rate, Fewer Total Cycles Mean Less CPU Time](#32-at-the-same-clock-rate-fewer-total-cycles-mean-less-cpu-time)
  - [3.3 More Cycles in Less Time Require a Faster Clock](#33-more-cycles-in-less-time-require-a-faster-clock)
  - [3.4 Amdahl's Law Shows How Unchanged Work Limits Overall Speedup](#34-amdahls-law-shows-how-unchanged-work-limits-overall-speedup)
- [4. Chiplets and Harvesting Reduce Silicon Wasted by Manufacturing Defects](#4-chiplets-and-harvesting-reduce-silicon-wasted-by-manufacturing-defects)

## 1. Software Defines the Work That the Machine Executes

### 1.1 High-Level Code Expresses Operations, Assembly Names Instructions, and Hardware Uses Bits

The same operation can be represented at different levels. Use **adding two numbers** as an example.

**1. High-level language — express the calculation**

In C, you might write:

```c
sum = a + b;
```

This says what to calculate without specifying registers or individual machine instructions.

- **Productivity:** less low-level detail to write and manage.
- **Portability:** the same source code can often be compiled for different processors.

**2. Assembly language — name the machine operations**

Assembly is a readable, textual representation of machine instructions. For example, an instruction named `ADD` might add values held in registers—small storage locations inside the CPU. The exact instruction and syntax depend on the processor.

One high-level statement can require **several machine instructions**, such as loading values, adding them, and storing the result. There is not necessarily a one-to-one mapping between a line of C and a machine instruction.

**3. Hardware representation — encode instructions and data as bits**

The CPU does not read the word `ADD`. The machine instruction is encoded as a **binary bit pattern** identifying the operation and its operands—the values or locations it operates on. The numbers being added are also represented as bits.

### 1.2 Algorithms, Compilers, Hardware, and I/O All Affect Execution Time

Separate **how much work a program requires** from **how quickly the system completes it**. Imagine a program that **reads 100 numbers from a file and adds them together**.

**1. Algorithm — choose the steps**

Start with the first number, then add the remaining 99 numbers. This algorithm requires **99 additions**. The algorithm determines the operations needed to solve the problem.

**2. Programming language, compiler, and architecture — turn operations into instructions**

An addition in the algorithm is not necessarily one machine instruction. Executing the program may also require instructions to load values, advance through the numbers, and control a loop.

The language expresses the algorithm, the compiler translates the code, and the **instruction-set architecture** defines the machine instructions available. Together, they influence how many machine instructions execute per operation and therefore the **total executed instruction count**.

**3. Processor and memory system — execute the instructions**

The processor executes instructions, but it also needs their data. Waiting for data from memory can add CPU cycles. The **clock rate** and **average cycles per instruction (CPI)** determine how long a given number of executed instructions takes.

**4. I/O system and OS — move data into and out of the program**

To obtain the numbers, the program asks the OS to read the file. If the data must be fetched from storage, the program may wait for the read to finish. That waiting increases **response time**, even while the program is not using the CPU.

### 1.3 Personal, Server, Embedded, and Supercomputers Serve Different Purposes

| Class | Typical purpose and constraints |
| --- | --- |
| Personal computer | Serves an individual user |
| Server computer | Provides network-based services, emphasizing capacity, performance, and reliability; server systems range from small machines to building-sized installations |
| Embedded computer | Forms part of another system, often with strict power, performance, and cost constraints |
| Supercomputer | Targets large computational workloads |

### 1.4 Main Memory Loses Its Data Without Power but Storage Keeps It

- **Volatile memory** needs power to retain its contents. Main memory such as SDRAM is volatile.
- **Nonvolatile storage** retains data without continuous power. Examples include flash memory, magnetic disks, and optical disks such as DVDs and CD-ROMs.

Storage capacity or executable-file size alone does not tell you how much work a CPU performs during a program run.

## 2. Performance Is Measured as Time per Task or Tasks per Second

### 2.1 Giga Is a Billion and Nano Is a Billionth

| Number | Digits | Power of ten |
| --- | ---: | ---: |
| Thousand | 1,000 | `10³` |
| Million | 1,000,000 | `10⁶` |
| Billion | 1,000,000,000 | `10⁹` |

- **Giga (`G`)** means `10⁹`: `1 GHz = 1 billion cycles/s`.
- **Nano (`n`)** means `10⁻⁹`: `1 ns = one billionth of a second`.
- Therefore, `1 s = 1 billion ns`. A rate of `1 cycle/ns` equals `1 billion cycles/s = 1 GHz`.

### 2.2 CPI Is the Average Number of Clock Cycles per Instruction

Use one example throughout this section: **100 machine instructions executed on a 1 GHz CPU**.

- **CPU:** the processor that executes instructions, such as loading a value or adding numbers.
- **Instruction count (`IC`):** the number of machine instructions *executed during the run*. Here, `IC = 100`; it is not a count of source-code lines or executable-file bytes.
- **Clock cycle:** one repetition of the clock signal, from one rising edge to the next. A cycle is not necessarily one completed instruction.
- **Clock rate (`f`):** cycles per second. At `1 GHz`, the clock repeats `10⁹` times per second.
- **Clock period:** the duration of one cycle, `1/f`. At `1 GHz`, one cycle lasts `1 ns`.
- **CPI (cycles per instruction):** the average number of cycles per executed instruction.

For example, if 50 instructions take one cycle each and 50 take two:

```text
total cycles = 50 × 1 + 50 × 2 = 150 cycles
CPI = 150 cycles / 100 instructions = 1.5 cycles/instruction
```

No individual instruction in this example takes 1.5 cycles; **1.5 is the average**.

The 1 GHz clock looks like this:

```text
          |<-- 1 cycle -->|
          ↑       ↓       ↑       ↓       ↑
           _______         _______         ____
clock   __|       |_______|       |_______|
          0      0.5     1.0     1.5     2.0 ns

↑ rising edge (low → high)   ↓ falling edge (high → low)
```

### 2.3 CPU Time Equals Instruction Count Times CPI Divided by Clock Rate

CPU time answers: **how much processor time does this run require?**

```text
cycles = IC × CPI
CPU time = cycles / f = IC × CPI / f
         = cycles × clock period
```

For the 100-instruction example:

1. **Count cycles:** `100 instructions × 1.5 cycles/instruction = 150 cycles`.
2. **Convert cycles to time:** `150 cycles × 1 ns/cycle = 150 ns`.

The run therefore needs **150 ns of CPU time**. The units agree: `(instructions × cycles/instruction) / (cycles/second) = seconds`.

**Working backward from time:** suppose a different run uses a 2 GHz CPU for 5 s at CPI 2.

1. Cycles: `5 s × 2 billion cycles/s = 10 billion cycles`.
2. Instructions: `10 billion cycles / 2 cycles/instruction = 5 billion instructions`.

### 2.4 Instructions per Second Equal Clock Rate Divided by CPI

Instruction throughput answers: **how many instructions complete per second?** It is a rate, not the duration of one run.

```text
instruction throughput = f / CPI
```

For the same 1 GHz CPU at CPI 1.5:

1. The clock supplies `1 billion cycles/s`.
2. Each instruction uses `1.5 cycles` on average.
3. Throughput is `1 billion cycles/s / 1.5 cycles/instruction ≈ 667 million instructions/s`.

The cycle units cancel, leaving **instructions per second**. This rate applies at the given clock rate and CPI; a different instruction mix can change CPI and therefore throughput.

**Cross-check using the run:**

```text
100 instructions / 150 ns ≈ 0.667 instructions/ns
0.667 instructions/ns × 1 billion ns/s ≈ 667 million instructions/s
```

A **1 GHz** CPU does not necessarily execute **1 billion instructions/s**. The clock counts cycles; at CPI 1.5, instructions require more than one cycle on average.

### 2.5 Higher Throughput Does Not Necessarily Shorten Each Task

| Measure | What it describes | Example unit |
| --- | --- | --- |
| CPU time | Processor time used by a program | ns or s |
| Response time (elapsed time) | Time from starting a task to finishing it, including waiting and I/O | ns or s |
| Throughput | Work completed per unit time | instructions/s or program runs/s |

A **run** means executing the entire 100-instruction program once. Each run needs **150 ns of CPU time**. Assume no waiting, I/O, or additional overhead, so its **response time is also 150 ns**.

**One CPU — runs happen one after another**

```text
       0 ns            150 ns          300 ns
CPU 1  |---- Run A ----|---- Run B ----|
```

Run A finishes after 150 ns, then Run B starts. The CPU completes **one run every 150 ns**. Since one second contains 1 billion nanoseconds:

```text
throughput = 1,000,000,000 ns/s ÷ 150 ns/run
           ≈ 6.67 million runs/s
```

**Two identical CPUs — separate runs happen at the same time**

```text
       0 ns            150 ns          300 ns
CPU 1  |---- Run A ----|---- Run C ----|
CPU 2  |---- Run B ----|---- Run D ----|
```

With independent runs and no shared bottleneck, **two runs finish every 150 ns**, rather than one:

```text
total throughput ≈ 2 × 6.67 million runs/s
                 ≈ 13.3 million runs/s
```

But **Run A still takes 150 ns**. CPU 2 executes a separate run; it does not help CPU 1 finish Run A faster.

## 3. No Single Factor Decides How Fast a Program Runs

### 3.1 The Fastest Clock Can Lose When Its CPI Is High

For program performance, compare **execution times for the same program and workload**. A higher clock rate alone is not enough: instruction count and CPI also matter.

Consider three processors executing the same instruction set, with the following CPIs for the workloads being considered:

| Processor | Clock rate | CPI |
| --- | ---: | ---: |
| P1 | 3 GHz | 1.5 |
| P2 | 2.5 GHz | 1.0 |
| P3 | 4.0 GHz | 2.2 |

**Instruction throughput:** divide each clock rate by its CPI.

| Processor | Instructions per second |
| --- | ---: |
| P1 | `3 billion / 1.5 = 2.0 billion` |
| P2 | `2.5 billion / 1.0 = 2.5 billion` |
| P3 | `4 billion / 2.2 ≈ 1.82 billion` |

**P2 has the highest instruction throughput**, even though P3 has the fastest clock.

**Work performed in 10 seconds:** multiply the clock rate by 10 s, then divide cycles by CPI.

| Processor | Cycles in 10 s | Instructions in 10 s |
| --- | ---: | ---: |
| P1 | `3 billion × 10 = 30 billion` | `30 billion / 1.5 = 20 billion` |
| P2 | `2.5 billion × 10 = 25 billion` | `25 billion / 1.0 = 25 billion` |
| P3 | `4 billion × 10 = 40 billion` | `40 billion / 2.2 ≈ 18.18 billion` |

The table above fixes the **time at 10 s** and asks how many instructions each CPU executes. At their stated CPIs, P1 executes 20 billion instructions, P2 executes 25 billion, and P3 executes about 18.18 billion. Equal running time does not mean equal instruction counts.

To compare completion times instead, fix the **instruction count**. Suppose all three execute 20 billion instructions, still at their stated clock rates and CPIs. Use `CPU time = IC × CPI / f`:

| Processor | Time to execute 20 billion instructions |
| --- | --- |
| P1 | `20 billion × 1.5 / (3 billion cycles/s) = 10 s` |
| P2 | `20 billion × 1.0 / (2.5 billion cycles/s) = 8 s` |
| P3 | `20 billion × 2.2 / (4 billion cycles/s) = 11 s` |

### 3.2 At the Same Clock Rate, Fewer Total Cycles Mean Less CPU Time

Compiler optimization options can change both instruction count and the mix of instruction classes. To compare runtimes, **sum cycles, not just instructions**.

Suppose three compiled versions have these executed instruction counts:

| Class | A | B | C |
| --- | ---: | ---: | ---: |
| CPI | 1 | 2 | 3 |
| Program 1 instruction counts | 5 | 2 | 2 |
| Program 2 instruction counts | 1 | 2 | 4 |
| Program 3 instruction counts | 3 | 2 | 3 |

```text
total instructions = sum of the class instruction counts
total cycles = sum of (class instruction count × class CPI)
overall CPI = total cycles / total instructions
CPU time = total cycles / f
```

| Program | Total instructions | Total cycles | Overall CPI |
| --- | ---: | ---: | ---: |
| 1 | `5 + 2 + 2 = 9` | `5×1 + 2×2 + 2×3 = 15` | `15/9 ≈ 1.67` |
| 2 | `1 + 2 + 4 = 7` | `1×1 + 2×2 + 4×3 = 17` | `17/7 ≈ 2.43` |
| 3 | `3 + 2 + 3 = 8` | `3×1 + 2×2 + 3×3 = 16` | `16/8 = 2` |

At the same clock rate:

- **Runtime:** program 1 needs the fewest cycles (15), followed by program 3 (16) and program 2 (17). Program 1 finishes first; programs 2 and 3 do not take the same time.
- **Executed instruction count:** program 2 executes the fewest instructions (7) but needs the most cycles (17). Program 1 executes more instructions (9) than program 3 (8), yet finishes sooner. These counts do **not** tell us the executable files' sizes in bytes.
- **Class CPI:** class A averages 1 cycle per instruction, while class B averages 2. These are class averages, not guaranteed latencies for each individual instruction.
- **Faster clock:** at 1 GHz, a cycle lasts 1 ns, so programs 1, 2, and 3 take 15, 17, and 16 ns. At 2 GHz, a cycle lasts 0.5 ns. **If their cycle counts stay the same**, their times become 7.5, 8.5, and 8 ns. Each takes half its previous time, so all three have a 2× speedup.

### 3.3 More Cycles in Less Time Require a Faster Clock

Return to P1, P2, and P3. Suppose execution time must fall **30%**, but CPI rises **20%**, with instruction count unchanged.

**Translate the percentages:**

- New time is `100% − 30% = 70%`, or `0.7 ×` old time.
- New CPI is `100% + 20% = 120%`, or `1.2 ×` old CPI.
- The unknown is the new clock rate, `f_new`.

**Write the old and new times, then solve:**

```text
old time = IC × CPI / f
new time = IC × (1.2 × CPI) / f_new

IC × 1.2 × CPI / f_new = 0.7 × IC × CPI / f
1.2 / f_new = 0.7 / f             (cancel IC × CPI)
1.2 × f = 0.7 × f_new            (multiply by f × f_new)
f_new = f × 1.2 / 0.7 ≈ 1.714 × f
```

The clock must compensate for **more cycles per instruction** while also completing the run in **less time**.

| Processor | Required new clock rate |
| --- | ---: |
| P1 | `3 GHz × 1.2 / 0.7 ≈ 5.14 GHz` |
| P2 | `2.5 GHz × 1.2 / 0.7 ≈ 4.29 GHz` |
| P3 | `4.0 GHz × 1.2 / 0.7 ≈ 6.86 GHz` |

**Check with P1 and 100 instructions:**

1. Old run: `100 × 1.5 = 150 cycles` at `3 cycles/ns` takes `150 / 3 = 50 ns`.
2. Target time: `0.7 × 50 = 35 ns`.
3. New CPI: `1.5 × 1.2 = 1.8`; the run now needs `100 × 1.8 = 180 cycles`.
4. Required rate: `180 cycles / 35 ns ≈ 5.14 cycles/ns = 5.14 GHz`.

### 3.4 Amdahl's Law Shows How Unchanged Work Limits Overall Speedup

A program takes **150 seconds**: 120 seconds multiplying and 30 seconds doing other work. Only multiplication can be sped up. Let `s` mean **how many times faster multiplication becomes**; `s` is a factor, not seconds.

| Part | Original time | New time |
| --- | ---: | ---: |
| Other work | 30 s | 30 s (unchanged) |
| Multiplication | 120 s | `120/s` seconds |
| Whole program | 150 s | `30 + 120/s` seconds |

**How fast must multiplication become to make the whole program 3× faster?**

1. A 3× whole-program speedup means a new total time of `150/3 = 50 s`.
2. Other work still takes 30 s, so multiplication can take only `50 − 30 = 20 s`.
3. Multiplication must fall from 120 s to 20 s: `s = 120/20 = 6`.

Check with the table: `new time = 30 + 120/6 = 50 s`; whole-program speedup is `150/50 = 3×`. **The multiplication part becomes 6× faster, but the whole program becomes only 3× faster.**

**Where does Amdahl's formula come from?** Divide each term in the table's new-time equation by the **original 150 seconds**:

```text
new time / old time = 30/150 + (120/150)/s
                    =    0.2 +     0.8/s
```

Here `0.2` is the fraction of original time spent on unchanged work, and `0.8` is the fraction spent multiplying. With `s = 6`, the new-time fraction is `0.2 + 0.8/6 = 1/3`: the new run takes one-third as long. Speedup is **old time / new time**, so it is `1 / (1/3) = 3×`.

For any program, call the **original-time fraction being improved** `p` (here `p = 120/150 = 0.8`). The remaining fraction is `1 − p` (here `30/150 = 0.2`):

```text
new time / old time = (1 − p) + p/s
whole-program speedup = 1 / [(1 − p) + p/s]
```

**The limit:** even if multiplication took almost no time (`s` grew without bound), the 30 seconds of other work would remain. The maximum possible whole-program speedup is `150/30 = 5×`, or in the fraction form `1/(1 − p) = 1/0.2 = 5×`. These numbers measure different things: **6×** is the improvement multiplication needs for the whole program to run **3×** faster; **5×** is the greatest improvement the *whole program* could ever achieve by speeding up multiplication alone.

## 4. Chiplets and Harvesting Reduce Silicon Wasted by Manufacturing Defects

Chips are made many at a time on one round slice of silicon, the **wafer**. The finished wafer is cut into rectangles, and each rectangle is one chip, a **die**. The circuit layout fixes the die boundaries before fabrication; cutting only separates the finished dies. For this comparison, hold wafer area and fabrication cost fixed.

Manufacturing can introduce flaws, for example from contamination. **Yield** is the fraction of candidate dies that work: `working dies / candidate dies`. In the simplified diagram below, each `x` marks a defect that makes its die unusable, and the three defects hit different dies. Real defects do not always ruin a whole die; the location and the design matter.

```text
   small dies                     big dies
   illustrative layouts, not to scale
 ┌──┬──┬──┬──┬──┬──┐           ┌─────┬─────┬─────┐
 │  │x │  │  │  │  │           │  x  │     │     │
 ├──┼──┼──┼──┼──┼──┤           │     │     │  x  │
 │  │  │  │  │x │  │           ├─────┼─────┼─────┤
 ├──┼──┼──┼──┼──┼──┤           │     │     │     │
 │  │  │x │  │  │  │           │  x  │     │     │
 └──┴──┴──┴──┴──┴──┘           └─────┴─────┴─────┘
 3 of 18 dies dead              3 of 6 dies dead
 yield ≈ 83%                    yield = 50%
```

In this example, the rest of a damaged die cannot be sold independently, so **the whole die is discarded**. Each discarded die takes otherwise usable silicon with it. Ignoring wafer-edge losses, the area comparison is:

```text
small dies: each die = 1/18 of the wafer
  3 defects → throw away 3 × 1/18 = 3/18 of the wafer → 17% lost, 83% works

big dies:   each die = 1/6 of the wafer
  3 defects → throw away 3 × 1/6  = 3/6  of the wafer → 50% lost, 50% works
```

The same number of defects discards more silicon in the big-die example. **At the same defect density, a larger die has a greater chance of containing a damaging defect and therefore tends to have lower yield.** Two design approaches can reduce this waste.

**Chiplets — build from separately tested pieces.** Design the accelerator as several smaller dies connected inside one package, rather than one huge die. Test the dies before assembly and select good ones. A bad die can then be discarded without discarding the other pieces. Packaging and die-to-die connections have their own costs and failure risks.

```text
one huge die                 chiplets tested before assembly
┌───────────────┐            ┌──────┐ ┌──────┐
│        x      │            │  x   │ │ good │
│               │            └──────┘ └──────┘
└───────────────┘             discard    keep
 discard if unusable         ┌──────┐ ┌──────┐
                             │ good │ │ good │
                             └──────┘ └──────┘
                                keep     keep
                             select another good die,
                             then assemble the package
```

**Harvesting — disable a faulty block and keep the usable chip.** A GPU contains repeated compute units as well as shared components. Picture the compute units as workers doing similar jobs. In a simplified example, there are 8 units and a defect breaks unit 2:

```text
unit:  0  1  2  3  4  5  6  7
       ✓  ✓  ✗  ✓  ✓  ✓  ✓  ✓     ← a defect broke unit 2
```

If the design allows unit 2 to be disabled and the rest of the chip passes testing, the factory can **permanently disable** it, for example through fuse settings. The chip might then be sold with fewer enabled units rather than discarded. Seven remaining units is an illustration, not a claim about a real product; some designs disable units in groups. A defect in essential shared circuitry may still make the chip unusable.

**Why the enabled hardware configuration matters to the driver.** Two chips using the same design can expose different numbers of enabled units:

```text
chip A:  ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓    all 8 on
chip B:  ✓ ✓ ✗ ✓ ✓ ✓ ✓ ✓    unit 2 off
```

A driver must use the device's supported configuration rather than assume every designed unit is enabled. Depending on the GPU, hardware registers or firmware can report which resources are available. The driver can use that information for configuration and capability reporting. **The driver does not generally assign each piece of work directly to an individual compute unit; GPU hardware and/or firmware handles that dispatch.** This is a general distinction, not a description of a specific driver implementation.
