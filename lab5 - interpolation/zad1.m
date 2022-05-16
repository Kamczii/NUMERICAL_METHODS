close all;
clear all;
    [XX,YY]=meshgrid(linspace(0,100,101),linspace(0,100,101));
for k = [ 5, 15, 25, 35 ]
    [x,y,f, xp, yp] = lazik(k);
    figure;
    subplot(2,2,1)
    plot(xp,yp,'-o','linewidth',1, 'LineWidth', 1); 
    grid minor
    title("Tor ruchu łazika dla K="+ num2str(k))
    ylabel("y [m]")
    xlabel("x [m]")
    
    subplot(2,2,2)
    plot3(x,y,f,'o', 'LineWidth', 1, 'LineWidth', 1);
    grid minor
    title("Zakres wartości próbek dla K="+ num2str(k))
    ylabel("y [m]")
    xlabel("x [m]")
    zlabel("f(x,y)")

    subplot(2,2,3)
    [p]=polyfit2d(x,y,f);
    [FF]=polyval2d(XX,YY,p);
    surf(XX,YY,FF);
    shading flat;
    title("Interpolacja wielomianowa dla K="+ num2str(k))
    ylabel("y [m]")
    xlabel("x [m]")
    zlabel("f(x,y)")

    subplot(2,2,4)
    [p]=trygfit2d(x,y,f);
    [FF]=trygval2d(XX,YY,p);
    surf(XX,YY,FF);
    shading flat;
    title("Interpolacja trygonometryczna dla K="+ num2str(k))
    ylabel("y [m]")
    xlabel("x [m]")
    zlabel("f(x,y)")
    
    filename = strcat('Zad1_k_',num2str(k),'.png');
    print(gcf,filename,  '-dpng','-r850');
end