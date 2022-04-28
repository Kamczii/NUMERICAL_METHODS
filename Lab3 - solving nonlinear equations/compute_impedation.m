clc
clear all
close all

% stałe
EPS = 1e-12;
START = 1;
FINISH = 50;

%metoda bisekcji
l = START;
r = FINISH;
[iterations, approximation, diffs] = bisection(@i,l,r, EPS);
%
figure;
semilogy(1:iterations,approximation)
xlabel("Numer iteracji");
ylabel("Aproksymacja");
title("2.1 Impedancja |Z|[Ω] - Metoda bisekcji - przybliżenia"); 
saveas(gcf,'2_bisekcji_wykres_aproksymacji.png');
%
figure;
semilogy(2:iterations,diffs)
xlabel("Numer iteracji");
ylabel("Różnica przybliżeń");
title("2.2 Impedancja |Z|[Ω]- Metoda bisekcji - różnica przybliżeń"); 
saveas(gcf,'2_bisekcji_wykres_przbliżeń.png');
%


%metoda siecznych
l = START;
r = FINISH;
[iterations, approximation, diffs] = secant(@i, l, r, EPS);
%
figure;
plot(1:iterations,approximation)
xlabel("Numer iteracji");
ylabel("Aproksymacja");
title("2.3 Impedancja |Z|[Ω]- Metoda siecznych - przybliżenia"); 
saveas(gcf,'2_sieczna_wykres_aproksymacji.png');
%
figure;
semilogy(2:iterations,diffs)
xlabel("Numer iteracji");
ylabel("Różnica przybliżeń");
title("2.4 Impedancja |Z|[Ω]-  Metoda siecznych - różnica przybliżeń"); 
saveas(gcf,'2_sieczna_wykres_przbliżeń.png');
%

%funkcja
function impedantion = i(mO) % mała omega 
    R = 725; % Ω
    C = 8*(1e-5); % F
    L = 2; % H
    impedantion = 1/(sqrt(1/R^2 + (mO*C - 1/(mO*L))^2))-75;
                  %  1/(sqrt(1/725^2 + (omega*8*10^-5 - 1/(omega*2))^2)) - 75;
    
end
