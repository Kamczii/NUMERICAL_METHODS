clc
clear all
close all

% stałe
EPS = 1e-3;
START = 1;
FINISH = 60000;

%metoda bisekcji
l = START;
r = FINISH;
[iterations, approximation, diffs] = bisection(@t,l,r, EPS);
%
figure;
semilogy(1:iterations,approximation)
xlabel("Numer iteracji");
ylabel("Kolejne przybliżenia");
title("1.1 Czas t[s] - Metoda bisekcji - kolejne przybliżenia"); 
saveas(gcf,'1_bisekcji_wykres_aproksymacji.png');
%
figure;
semilogy(2:iterations,diffs)
xlabel("Numer iteracji");
ylabel("Różnica przybliżeń");
title("1.2 Czas t[s] - Metoda bisekcji - różnica przybliżeń"); 
saveas(gcf,'1_bisekcji_wykres_przbliżeń.png');
%


%metoda siecznych
l = START;
r = FINISH;
[iterations, approximation, diffs] = secant(@t, l, r, EPS);
%
figure;
plot(1:iterations,approximation)
xlabel("Numer iteracji");
ylabel("Kolejne przybliżenia");
title("1.3 Czas t[s] - Metoda siecznych - kolejne przybliżenia"); 
saveas(gcf,'1_sieczna_wykres_aproksymacji.png');
%
figure;
semilogy(2:iterations,diffs)
xlabel("Numer iteracji");
ylabel("Różnica przybliżeń");
title("1.4 Czas t[s] - Metoda siecznych - różnica przybliżeń"); 
saveas(gcf,'1_sieczna_wykres_przbliżeń.png');
%

%funkcja
function time = t(N)
    time = (N.^(1.43) + N.^(1.14))./1000 - 5000;
end
