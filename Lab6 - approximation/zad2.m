close all;
clear all;
load('trajektoria1.mat');
plot3(x,y,z,'o');
grid on;
axis equal;
title("Położenie drona")
xlabel("x [m]");
ylabel("y [m]");
zlabel("z [m]");
saveas(gcf,'184374_czepiel_zad2.png');