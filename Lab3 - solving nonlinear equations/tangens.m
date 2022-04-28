clc
clear all
close all

options = optimset("Display","iter");
fzero(@tan,6, options);

disp("----------------------------------------------------")
fzero(@tan,4.5, options);

% w otoczeniu 6 ciagly i rozniczkowalny

