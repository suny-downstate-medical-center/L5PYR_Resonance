function varyChannelsHeatMaps(sec_name)
% sec_name: path to file + section name that starts the file name

QfactorInMat = zeros(11,11);
ZinResAmpMat = zeros(11,11);
ZinResFreqMat = zeros(11,11);
ZcResFreqMat = zeros(11,11);
ZinLeadPhaseBWMat = zeros(11,11);
ZinSynchFreqMat = zeros(11,11);

%factors = {'-0.2', '-0.15', '-0.1', '-0.05', '0', '0.05', '0.1', '0.15', '0.2'};
factors = {'-0.25', '-0.2', '-0.15', '-0.1', '-0.05', '0.0', '0.05', '0.1', '0.15', '0.2', '0.25'};
r_count = 1;
c_count = 1;
%file_part1 = 'KoleCell[0].apic[86]_km_';
%file_part1 = 'KoleCell[0].dend[8]_km_';
% file_part1 = '_km_';
% file_part2 = '_ih_';
file_part1 = 'ih_';
file_part2 = '_im_';
file_part3 = '.mat';

for km_factor = factors
    for ih_factor = factors
        % load(strcat(sec_name, file_part1, km_factor{1}, file_part2, ih_factor{1}, file_part3))
        load(strcat(file_part1, km_factor{1}, file_part2, ih_factor{1}, file_part3))
        QfactorInMat(r_count,c_count) = QfactorIn;
        ZinResAmpMat(r_count,c_count) = ZinResAmp;
        ZinResFreqMat(r_count,c_count) = ZinResFreq;
        ZcResFreqMat(r_count,c_count) = ZcResFreq;
        ZinLeadPhaseBWMat(r_count,c_count) = ZinLeadPhaseBW; %Freq(find(ZinPhase > 0, 1, 'last')) - Freq(find(ZinPhase > 0, 1, 'first'));
        ZinSynchFreqMat(r_count,c_count) = ZinSynchFreq; %Freq(find(ZinPhase > 0, 1, 'last'));
        c_count = c_count + 1;
    end
    r_count = r_count + 1;
    c_count = 1;
end

% keep QfactorInMat ZinResAmpMat  ZinResFreqMat ZcResFreqMat ZinLeadPhaseBW ZinSynchFreq ZinLeadPhaseBWMt ZinSynchFreqMat

labels = {'-20%', '0%', '20%'};
x_ticks = [-0.2, 0, 0.2];
%figure('units','normalized','outerposition',[0 0 1 1]);

figure()
subplot(2,3,1)
imagesc(-0.2:0.05:0.2, -0.2:0.05:0.2, ZinResAmpMat)
colormap('jet')
set(gca,'YDir','normal')
colorbar
xticks(x_ticks)
yticks(x_ticks)
xticklabels(labels)
yticklabels(labels)
xlabel('\Delta Ih g_b_a_r')
ylabel('\Delta Im g_b_a_r')
xlabel('\Delta I_h g_b_a_r')
ylabel('\Delta I_m g_b_a_r')
title('Peak Amplitude (M\Omega)')
axis square
set(gca, 'FontSize', 14)

subplot(2,3,2)
imagesc(-0.2:0.05:0.2, -0.2:0.05:0.2, ZinResFreqMat)
set(gca,'YDir','normal')
colorbar
xticks(x_ticks)
yticks(x_ticks)
xlabel('\Delta I_h g_b_a_r')
ylabel('\Delta I_m g_b_a_r')
xticklabels(labels)
yticklabels(labels)
axis square
set(gca, 'FontSize', 14)
title('Peak Frequency (Hz)')

subplot(2,3,3)
imagesc(-0.2:0.05:0.2, -0.2:0.05:0.2, QfactorInMat)
set(gca,'YDir','normal')
xlabel('\Delta I_h g_b_a_r')
ylabel('\Delta I_m g_b_a_r')
xticklabels(labels)
yticklabels(labels)
title('Resonance Strength (Q-factor)')
axis square
colorbar
xticks(x_ticks)
yticks(x_ticks)
set(gca, 'FontSize', 14)

subplot(2,3,4)
imagesc(-0.2:0.05:0.2, -0.2:0.05:0.2, ZcResFreqMat)
set(gca,'YDir','normal')
axis square
colorbar
xticks(x_ticks)
yticks(x_ticks)
xlabel('\Delta I_h g_b_a_r')
ylabel('\Delta I_m g_b_a_r')
title('Transfer Frequency (Hz)')
xticklabels(labels)
yticklabels(labels)
set(gca, 'FontSize', 14)

subplot(2,3,5)
imagesc(-0.2:0.05:0.2, -0.2:0.05:0.2, ZinSynchFreqMat)
set(gca,'YDir','normal')
axis square
colorbar
xticks(x_ticks)
yticks(x_ticks)
xlabel('\Delta I_h g_b_a_r')
ylabel('\Delta I_m g_b_a_r')
title('Synchronous Frequency (Hz)')
xticklabels(labels)
yticklabels(labels)
set(gca, 'FontSize', 14)

subplot(2,3,6)
imagesc(-0.2:0.05:0.2, -0.2:0.05:0.2, ZinLeadPhaseBWMat)
set(gca,'YDir','normal')
axis square
colorbar
xticks(x_ticks)
yticks(x_ticks)
xlabel('\Delta I_h g_b_a_r')
ylabel('\Delta I_m g_b_a_r')
title('Lead Phase Bandwidth (Hz)')
xticklabels(labels)
yticklabels(labels)
set(gca, 'FontSize', 14)

end