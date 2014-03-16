"""
Anscombe's quartet
==================

_thumb: .4, .4
"""
import seaborn as sns
sns.set(style="ticks")

df = sns.load_dataset("anscombe")
sns.lmplot("x", "y", col="dataset", hue="dataset", data=df,
           col_wrap=2, ci=None, palette="muted", size=4)