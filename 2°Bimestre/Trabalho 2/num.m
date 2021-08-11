j=sqrt(-1);
u=2300;
r1=0.262;
x1=1.206;
x2=x1;
xm=54.02;
r2=0.187;
vf=u/sqrt(3); %tensão por fase
ws=(120/4)*60; %velocidade sincroda (rpm)
ns=ws*2*pi/60 %velodicade angular sincrona(rad/s)
rlin=0.0670806455261595+j*0.0750137601294734

dt=1/ws;

vth=vf*(xm/sqrt(r1^2+(x1+xm)^2));
zth=((j*xm)*(r1+j*x1)/(r1+j*(x1+xm)));
rth=real(zth);
xth=imag(zth);

s=(1:-0.001:-1);
vm=(1-s)*ns %velocidade mecanica

for ii =1:2001
    tind1(ii)=(3*vth^2*(r2+0.7)/s(ii))/(ns*((rth+(r2+0.7)/s(ii))^2+(xth+x2)^2))-1970;
end

figure(1)
plot(vm,tind1,'Color','b','LineWidth',2.)
xlabel('\bf\itn_{vm}')
ylabel('\bf\tau_{tind1}')
grid on;

