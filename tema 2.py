w="""Bărbatul a fost atacat de urs, duminică, pe păşunea dintre localităţile Monor şi Batoş, județul Bistrița-Năsăud și a suferit multiple răni la nivelul capului, la mâini și la picioare. Victima a fost preluată de membri familiei cu o mașină de teren și dusă în întâmpinarea echipajului SMURD, informează Bistrițeanul.
Citeşte întreaga ştire: Bărbat atacat de urs în județul Bistrița-Năsăud: a fost rănit la cap, mâini și picioare."""
lung_sir=len(w)
jum_sir=lung_sir//2
jum_1=w[0:jum_sir]
jum_1=jum_1.upper().strip()
jum_2=w[jum_sir:lung_sir]
jum2_rev=jum_2[::-1].replace(".","").capitalize()
print(jum_1+jum2_rev)
  