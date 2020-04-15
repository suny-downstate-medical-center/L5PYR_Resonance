figure('units','normalized','outerposition',[0 0 1 1]);
load('L5PCtemplate[0].dend[12]_traces.mat');
time = linspace(-5,25,length(cis_np));
cis_np = cis_np(time >= -1 & time <= 21);
soma_np = soma_np(time >= -1 & time <= 21);
time = time(time >= -1 & time <= 21);
subplot(4,3,1)
plot(time, cis_np - cis_np(1), 'b', 'LineWidth', 1)
xlim([-1,21])
title('Basal Dendrite')
ylabel('\Delta V_m (mV)')
ylim([-2,2])
set(gca, 'FontSize' ,12, 'fontweight', 'bold')
subplot(4,3,4)
plot(time, soma_np - soma_np(1), 'k', 'LineWidth', 1)
ylim([-.13, .13])
xlim([-1,21])
ylabel('\Delta V_s (mV)')
set(gca, 'FontSize' ,12, 'fontweight', 'bold')
clear

load('L5PCtemplate[0].apic[33]_traces.mat');
time = linspace(-5,25,length(cis_np));
cis_np = cis_np(time >= -1 & time <= 21);
soma_np = soma_np(time >= -1 & time <= 21);
time = time(time >= -1 & time <= 21);
subplot(4,3,2)
plot(time, cis_np - cis_np(1), 'r', 'LineWidth', 1)
xlim([-1,21])
title('Apical Oblique')
set(gca, 'FontSize' ,12, 'fontweight', 'bold')
subplot(4,3,5)
plot(time, soma_np - soma_np(1), 'k', 'LineWidth', 1)
ylim([-.13, .13])
xlim([-1,21])
xlabel('Time (s)')
set(gca, 'FontSize' ,12, 'fontweight', 'bold')
clear

load('L5PCtemplate[0].apic[58]_traces.mat');
time = linspace(-5,25,length(cis_np));
cis_np = cis_np(time >= -1 & time <= 21);
soma_np = soma_np(time >= -1 & time <= 21);
time = time(time >= -1 & time <= 21);
subplot(4,3,3)
plot(time, cis_np - cis_np(1), 'g', 'LineWidth', 1)
xlim([-1,21])
title('Apical Tuft')
set(gca, 'FontSize' ,12, 'fontweight', 'bold')
subplot(4,3,6)
plot(time, soma_np - soma_np(1), 'k', 'LineWidth', 1)
ylim([-.13, .13])
xlim([-1,21])
title('Soma')
xlabel('Time (s)')
set(gca, 'FontSize' ,12, 'fontweight', 'bold')
clear

basal = load('L5PCtemplate[0].dend[12].mat');
obliq = load('L5PCtemplate[0].apic[33].mat');
tuft  = load('L5PCtemplate[0].apic[58].mat');

subplot(2,4,5)
plot(smooth(basal.ZinRes - basal.ZinRes(1), 25), smooth(basal.ZinReact - basal.ZinReact(1), 25), 'b', 'lineWidth', 2)
hold on
plot(smooth(obliq.ZinRes - obliq.ZinRes(1), 25), smooth(obliq.ZinReact - obliq.ZinReact(1), 25), 'r', 'lineWidth', 2)
plot(smooth(tuft.ZinRes - tuft.ZinRes(1), 50), smooth(tuft.ZinReact - tuft.ZinReact(1), 50), 'g', 'lineWidth', 2)
xlabel('\Delta Resistance (M\Omega)')
ylabel('\Delta Reactance (M\Omega)')
title('Z_i_n')
set(gca, 'FontSize' ,12, 'fontweight', 'bold')

subplot(2,4,6)
plot(basal.Freq, smooth(basal.ZinAmp / max(basal.ZinAmp), 20), 'b', 'lineWidth', 2)
hold on
plot(obliq.Freq, smooth(obliq.ZinAmp / max(obliq.ZinAmp), 20), 'r', 'lineWidth', 2)
plot(tuft.Freq, smooth(tuft.ZinAmp / max(tuft.ZinAmp), 20), 'g', 'lineWidth', 2)
xlabel('Frequency (Hz)')
ylabel('Normalized Amplitude (a.u.)')
title('|Z_i_n|')
set(gca, 'FontSize' ,12, 'fontweight', 'bold')

subplot(2,4,7)
plot(basal.Freq, smooth(basal.ZinPhase, 20), 'b', 'lineWidth', 2)
hold on
plot(obliq.Freq, smooth(obliq.ZinPhase, 20), 'r', 'lineWidth', 2)
plot(tuft.Freq, smooth(tuft.ZinPhase, 20), 'g', 'lineWidth', 2)
xlabel('Frequency (Hz)')
ylabel('Phase (radians)')
title('\Phi_i_n')
set(gca, 'FontSize' ,12, 'fontweight', 'bold')

subplot(2,4,8)
plot(basal.Freq, smooth(basal.ZcAmp / max(basal.ZcAmp), 20), 'b', 'lineWidth', 2)
hold on
plot(obliq.Freq, smooth(obliq.ZcAmp / max(obliq.ZcAmp), 20), 'r', 'lineWidth', 2)
plot(tuft.Freq, smooth(tuft.ZcAmp / max(tuft.ZcAmp), 20), 'g', 'lineWidth', 2)
xlabel('Frequency (Hz)')
ylabel('Normalized Amplitude (a.u.)')
title('|Z_c|')
set(gca, 'FontSize' ,12, 'fontweight', 'bold')