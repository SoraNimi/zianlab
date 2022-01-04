.OPTION POST=2 POST_VERSION=2001
*.OPTION MTTHRESH=10
*.OPTION PSF=2
*.OPTION runlvl=6
.OPTION INGOLD=2 ARTIST=2 PSF=2 HIER_DELIM=1
.OPTION SAVE
.TEMP = 27
*.TRAN 1p 10

** Library name: testRohm
** Cell name: 2jisub
** View name: schematic
.subckt sub g out vin+ vin- vh vref
m24 net10 net_51 g g N L=220e-9 W=10e-6
m6 net_16 net_47 g g N L=220e-9 W=10e-6
m21 net_17 net_07 net_16 g N L=300e-9 W=10e-6
m20 net_16 net_046 net_21 g N L=300e-9 W=10e-6
m12 ctrl~ ctrl g g N L=180e-9 W=220e-9
m10 ctrl net_30 g g N L=180e-9 W=220e-9
m9 net_28 net10 net_30 g N L=300e-9 W=1e-6
m8 net_29 net_24 net_28 g N L=300e-9 W=1e-6
m7 net_28 net_59 g g N L=220e-9 W=1.7e-6
m17 vref ctrl~ out g N L=300e-9 W=2e-6
m15 net10 ctrl out g N L=300e-9 W=2e-6
c1 out g 5e-12
c0 net10 net_49 100e-15
m23 vh net_17 net_17 vh P L=300e-9 W=20e-6
m22 net_21 net_17 vh vh P L=300e-9 W=20e-6
m19 net_30 net_29 vh vh P L=300e-9 W=1e-6
m18 vh net_29 net_29 vh P L=300e-9 W=1e-6
m13 ctrl~ ctrl vh vh P L=180e-9 W=300e-9
m11 ctrl net_30 vh vh P L=180e-9 W=300e-9
m16 out ctrl vref vh P L=300e-9 W=3e-6
m14 out ctrl~ net10 vh P L=300e-9 W=3e-6
m5 net10 net_21 vh vh P L=300e-9 W=20e-6
r4 vref net_046 100e3
r5 net_046 vin+ 100e3
r3 net_07 net10 100e3
r1 vin- net_07 100e3
r6 vh net_24 10e3
r7 net_24 g 10e3
r0 net_21 net_49 100e3
v0 net_51 g DC=800e-3
v3 net_59 g DC=800e-3
v1 net_47 g DC=800e-3
.ends sub


x0 g vout vin+ vin- vh vref sub


.DC Vvin+ 0 1.8 0.005
Vvin+ vin+ 0 DC

Vvin- vin- 0 DC 0.9
Vg g 0 DC 0
Vvref vref 0 DC 0.9 
Vvh vh 0 DC 1.8


.include "/home/user17/design/rules/rohm180/spice/hspice/bu40n1.mdl"
.lib "/home/user17/design/rules/rohm180/spice/hspice/bu40n1.skw" NT
.lib "/home/user17/design/rules/rohm180/spice/hspice/bu40n1.skw" PT

.END
