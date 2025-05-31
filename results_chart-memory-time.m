% Data Setup
files = {'sat\_small', 'unsat\_small', 'random\_medium'};
algorithms = {'Resolution', 'DP', 'DPLL'};

% Time (s)
time = [
    0.0003, 0.0002, 0.0002;
    0.0003, 0.0002, 0.0002;
    0.0041, 0.0023, 0.0017
];

% Memory (KB)
memory = [
    7.45, 6.30, 5.95;
    7.80, 6.35, 6.00;
    21.50, 17.20, 15.85
];

% SAT/UNSAT Results for each file/algorithm (same order as time & memory)
results = [
    "SAT", "SAT", "SAT";         % sat_small
    "UNSAT", "UNSAT", "UNSAT";   % unsat_small
    "SAT", "SAT", "SAT"          % random_medium
];

% -----------------------------
% Plot Time with Result Markers
% -----------------------------
figure;
b1 = bar(time);
title('Algorithm Runtime Comparison');
xlabel('File');
ylabel('Time (s)');
set(gca, 'XTickLabel', files);
legend(algorithms, 'Location', 'northwest');
grid on;

% Add result markers above bars
for i = 1:length(files)
    for j = 1:length(algorithms)
        x = b1(j).XData(i) + b1(j).XOffset; % Adjust for group offset
        y = time(i, j);
        text(x, y + 0.00005, results(i, j), 'HorizontalAlignment', 'center', 'FontSize', 9, 'Color', 'k');
    end
end

% -----------------------------
% Plot Memory with Result Markers
% -----------------------------
figure;
b2 = bar(memory);
title('Algorithm Memory Usage Comparison');
xlabel('File');
ylabel('Memory (KB)');
set(gca, 'XTickLabel', files);
legend(algorithms, 'Location', 'northwest');
grid on;

% Add result markers above bars
for i = 1:length(files)
    for j = 1:length(algorithms)
        x = b2(j).XData(i) + b2(j).XOffset;
        y = memory(i, j);
        text(x, y + 0.5, results(i, j), 'HorizontalAlignment', 'center', 'FontSize', 9, 'Color', 'k');
    end
end
