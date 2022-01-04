** Generated for: hspiceD
** Generated on: Jun 13 21:33:30 2018
** Design library name: reram
** Design cell name: XORNET4
** Design view name: schematic
.PARAM blinresistor=20
.PARAM blresistor=30
VVDD VDD 0 DC 1.8
.TRAN 10e-12 200e-9 START=0.0

.TEMP 25.0
.OPTION
+    ARTIST=2
+    INGOLD=2
+    PARHIER=LOCAL
+    PSF=2
.OPTION PROBE=1
.PROBE tran v(l0bl)
.PROBE tran v(bldin)
.PROBE tran v(l0saa)
.PROBE tran v(l0sab)
.PROBE tran v(l0dl)
.PROBE tran v(l0dlb)

.measure tran avgval0 AVG v(l0bl) FROM = 199ns TO =200ns
.measure tran avgval1 AVG v(bldin) FROM = 199ns TO =200ns
.measure tran avgval2 AVG v(l0saa) FROM = 199ns TO =200ns
.measure tran avgval3 AVG v(l0sab) FROM = 199ns TO =200ns
.measure tran avgval4 AVG v(l0dl) FROM = 199ns TO =200ns
.measure tran avgval5 AVG v(l0dlb) FROM = 199ns TO =200ns

vl0bl l0bl 0 PWL
+    0n     0
+    5n     0
+    10n    0.7
+    200n    0.7

vbldin bldin 0 PWL
+    0n     0.6626
+    200n    0.6626


.INCLUDE "/home/user34/design/rules/rohm180/spice/hspice/bu40n1.mdl"
.LIB "/home/user34/design/rules/rohm180/spice/hspice/bu40n1.skw" NT
.LIB "/home/user34/design/rules/rohm180/spice/hspice/bu40n1.skw" PT


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


xl0sa l0bl bldin l0saa vdd SAVM2
xl0sainva 0 l0saa l0sab vdd INV1
xl0sainvb 0 l0sab l0dl vdd INV1
xl0dlinv 0 l0dl l0dlb vdd INV1