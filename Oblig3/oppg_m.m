
T_hat = 0.9;
n = 1000;

rho_hat = linspace(0.2, 2.0, n);

p_hat = (8.*rho_hat*T_hat)./(3. - rho_hat) - 3*rho_hat.*rho_hat;

g_hat = -3*rho_hat -(8./3)*T_hat*log(3./rho_hat - 1) + p_hat./rho_hat;

V_hat = 1./rho_hat;

figure 
subplot(3, 1, 1);
plot(rho_hat, p_hat);
subplot(3, 1, 2);
plot(p_hat, V_hat);
subplot(3, 1, 3);
plot(p_hat, g_hat);

[p_hat_intersection, g_hat_intersection, segments] = selfintersect(p_hat, g_hat);
p_hat_intersection

figure
plot(rho_hat, p_hat);
hold 'on'
plot([0.426,1.66], [p_hat_intersection, p_hat_intersection], 'r')
xlabel('$$\hat{\rho}$$','Interpreter','Latex')
ylabel('$$\hat{p}$$', 'Interpreter', 'Latex')
print('oppg_m1.png', '-dpng')


figure
plot(V_hat, p_hat);
hold 'on'
plot([0.603, 2.35], [p_hat_intersection, p_hat_intersection], 'r')
xlabel('$$\hat{V}$$','Interpreter','Latex')
ylabel('$$\hat{p}$$', 'Interpreter', 'Latex')
legend('T = 0.9')
%print('oppg_m2.png', '-dpng')
%print('oppgo_9.png', '-dpng')
