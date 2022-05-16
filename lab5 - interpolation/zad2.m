clear all;
close all;

NR = 5:45;
Div_p = zeros(length(NR));
Div_t = zeros(length(NR));
for k = NR
    [XX,YY]=meshgrid(linspace(0,100,101),linspace(0,100,101)); 
    [x,y,f, xp, xy] = lazik(k);

    [p]=polyfit2d(x,y,f);
    [FF_p]=polyval2d(XX,YY,p);

    [p]=trygfit2d(x,y,f);
    [FF_t]=trygval2d(XX,YY,p);
    
    if k == 5
        FF_p_prev = FF_p;
        FF_t_prev = FF_t;
    else
        Div_p(k-5) = max(max(abs(FF_p-FF_p_prev)));
        Div_t(k-5) = max(max(abs(FF_t-FF_t_prev)));
        FF_p_prev = FF_p;
        FF_t_prev = FF_t;
    end
end
figure;
plot(5:45,Div_p)
title("Zbieżność interpolacji wielomianowej")
ylabel("Maksymalna różnica")
xlabel("Ilość punktów pomiarowych")
saveas(gcf,'zbieznosc_interpolacji_wielomanowej.png');

figure;
plot(5:45,Div_t)
title("Zbieżność interpolacji trygonometrycznej")
ylabel("Maksymalna różnica")
xlabel("Ilość punktów pomiarowych")
saveas(gcf,'zbieznosc_interpolacji_trygonometrycznej.png');