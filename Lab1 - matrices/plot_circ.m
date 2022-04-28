
function plot_circ(X, Y, R)
theta = linspace(0,2*pi);
x = R*cos(theta) + X;
y = R*sin(theta) + Y;
plot(x,y)
end