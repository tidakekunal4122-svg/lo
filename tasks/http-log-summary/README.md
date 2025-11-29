# HTTP Log Summary Task

This Terminal-Bench task asks an agent to parse the provided `data/access.log` file and generate HTTP method and status code summaries in the `reports/` directory.

## Quick start
1. Run the reference solution to generate the expected reports:
   ```bash
   bash solution.sh
   ```
2. Execute the tests to confirm the task passes with the solution:
   ```bash
   python -m pytest tests/test_outputs.py
   ```

The tests assume the `reports/` directory contains `method_counts.txt` and `status_counts.txt` produced by the agent (or by running the reference solution above).
