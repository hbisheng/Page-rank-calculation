% read csv
res = csvread('result.csv', 1,1);

% Indegree Distribution
indegree = res(:,2);
[a,b] = hist(indegree,50);
figure;bar(1:length(a), a);
set(gca,'xticklabel', [0 b+(b(2)-b(1))/2],'yscale','log','FontSize',12);
in_min = min(indegree);
in_max = max(indegree);
in_mean = mean(indegree);
in_median = median(indegree);
title('In-degree distribution');
xlabel('Indegree');
ylabel('Frequency');

% Outdegree Distribution
outdegree = res(:,3);
[a,b] = hist(outdegree,50);
figure;bar(1:length(a), a);
set(gca,'xticklabel', [0 b+b(1)],'yscale','log','FontSize',12);
out_min = min(outdegree);
out_max = max(outdegree);
out_mean = mean(outdegree);
out_median = median(outdegree);
title('Out-degree distribution');
xlabel('Outdegree');
ylabel('Frequency');

% Pagerank Distribution
pagerank = res(:,1);
[a,b] = hist(pagerank, 50);
figure;bar(1:length(a), a);
set(gca,'xticklabel', [0 b+b(1)],'yscale','log','FontSize',20);
pg_max = max(pagerank);
pg_min = min(pagerank);
pg_mean = mean(pagerank);
pg_median = median(pagerank);
title('PageRank distribution');
xlabel('PageRank');
ylabel('Frequency');

% Pagerank and In-degree
figure;plot(res(:,2),res(:,1),'*');
title('PageRank vs. In-degree');
xlabel('In-degree');
ylabel('PageRank');
set(gca,'xscale','log');
set(gca,'yscale','log');
corr_pg_in = corrcoef(res(:,1),res(:,2));

% Pagerank and Out-degree
figure;plot(res(:,3),res(:,1),'*');
title('PageRank vs. Out-degree');
xlabel('Out-degree');
ylabel('PageRank');
set(gca,'xscale','log');
set(gca,'yscale','log');
corr_pg_out = corrcoef(res(:,1),res(:,3));





