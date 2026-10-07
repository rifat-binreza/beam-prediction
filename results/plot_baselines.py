"""Render recorded baseline metrics; this script does not evaluate models."""
import csv
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT = Path(__file__).resolve().parents[1]
with (ROOT / 'results/baseline_metrics.csv').open() as f:
    rows = list(csv.DictReader(f))
plt.rcParams.update({'font.family':'DejaVu Sans', 'svg.fonttype':'none'})
fig, ax = plt.subplots(figsize=(12, 4.4), facecolor='#0c1428')
ax.set_facecolor('#0c1428')
labels=['Position', 'Position + height', 'Position + height + distance', 'Refined ResNet-50 image']
values=[float(row['top1_percent']) for row in rows]
ax.barh(labels, values, color=['#64748b','#818cf8','#a78bfa','#22d3ee'], height=.55)
for i, value in enumerate(values):
    ax.text(value+1.2,i,f'{value:.2f}%',va='center',color='#f1f5f9',weight='bold',fontsize=12)
ax.set_xlim(0,102)
ax.set_xticks([0,20,40,60,80,100])
ax.set_xlabel('Top-1 accuracy (%)',color='#cbd5e1',labelpad=10)
ax.tick_params(colors='#cbd5e1',length=0,labelsize=11)
ax.set_axisbelow(True)
ax.grid(axis='x',alpha=.12,color='#94a3b8')
for s in ax.spines.values(): s.set_visible(False)
ax.set_title('RECORDED BASELINE RESULTS',color='#67e8f9',loc='left',fontweight='bold',pad=22,fontsize=15)
fig.text(.04,.025,'Historical baseline runs • not fusion scores • see docs/RESULTS.md for provenance',color='#94a3b8',fontsize=10)
fig.tight_layout(rect=[.02,.07,.99,1])
fig.savefig(ROOT/'assets/baseline-results.svg',facecolor=fig.get_facecolor())
plt.close(fig)
