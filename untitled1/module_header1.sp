** Generated for: hspiceD
** Generated on: Jun 13 21:33:30 2018
** Design library name: reram
** Design cell name: XORNET4
** Design view name: schematic
.PARAM blinresistor=20
.PARAM blresistor=30

.TRAN 10e-12 100e-9 START=0.0

.TEMP 25.0
.OPTION
+    ARTIST=2
+    INGOLD=2
+    PARHIER=LOCAL
+    PSF=2




.INCLUDE "/home/user34/design/rules/rohm180/spice/hspice/bu40n1.mdl"
.INCLUDE "/home/user34/design/rules/rohm180/spice/hspice/bu40n3.mdl"
.LIB "/home/user34/design/rules/rohm180/spice/hspice/bu40n1.skw" NT
.LIB "/home/user34/design/rules/rohm180/spice/hspice/bu40n1.skw" PT

** Library name: reram
** Cell name: CELLD
** View name: schematic
.subckt CELLD bl sl wl wlb
m1 sl wlb net08 0 N L=180e-9 W=5e-6
m0 sl wl net09 0 N L=180e-9 W=5e-6
r1 net08 bl r1
r0 net09 bl r0
.ends CELLD
** End of subcircuit definition.

** Library name: reram
** Cell name: SAVM2
** View name: schematic
.subckt SAVM2 bl blb dl vdd
m1 dl net19 vdd vdd P L=180e-9 W=1e-6
m0 net19 net19 vdd vdd P L=180e-9 W=1e-6
m3 dl blb 0 0 N L=180e-9 W=1e-6
m2 net19 bl 0 0 N L=180e-9 W=1e-6
.ends SAVM2
** End of subcircuit definition.

** Library name: testRohm_n
** Cell name: INV1
** View name: schematic
.subckt INV1 g in out v
m1 out in v v P L=180e-9 W=5e-6
m0 out in g g N L=180e-9 W=2e-6
.ends INV1
** End of subcircuit definition.

** Library name: reram
** Cell name: CELLDREF
** View name: schematic
.subckt CELLDREF bl sl wl wlb
m1 sl wlb net13 net13 N L=180e-9 W=5e-6
m0 sl wl net14 net14 N L=180e-9 W=5e-6
r8 net018 bl 900e3
r7 net13 net018 10000e3
r6 net14 net020 900e3
r5 net020 bl 10000e3
r4 net017 bl 900e3
r3 net019 bl 10000e3
r1 net13 net017 10000e3
r0 net14 net019 900e3
.ends CELLDREF
** End of subcircuit definition.

** Library name: reram
** Cell name: XORNET4
** View name: schematic
