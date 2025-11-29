#!/bin/bash
set -euo pipefail

cd "$(dirname "$0")"

mkdir -p reports

awk '{
    gsub(/"/,"",$6)
    method=$6
    status=$9
    methods[method]++
    statuses[status]++
}
END {
    for (m in methods) {
        print m, methods[m]
    }
}' data/access.log | LC_ALL=C sort > reports/method_counts.txt

awk '{
    gsub(/"/,"",$6)
    status=$9
    statuses[status]++
}
END {
    for (s in statuses) {
        print s, statuses[s]
    }
}' data/access.log | LC_ALL=C sort -k2,2nr -k1,1n > reports/status_counts.txt
