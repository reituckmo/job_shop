import matplotlib.pyplot as plt

# case 1
# optimal_line = 901300
# case 2
# optimal_line = 252000
# case 3
# optimal_line = 67700
# case 4
# optimal_line = 110300
# case 5
optimal_line = 623600

# log_data = [1122500, 1122500, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1100800, 1092800, 1092800, 1092800, 1092800, 1092800, 1092800, 1092800, 1092800, 1092800, 1092800, 1092800, 1092800, 1092800, 1092800, 1092800, 1092800, 1079400, 1079400, 1079400, 1079400, 1079400, 1079400, 1079400, 1079400, 1067200, 1067200, 1067200, 1067200, 1067200, 1067200, 1067200, 1067200, 1067200, 1067200, 1067200, 1065500, 1054800, 1054800, 1051100, 1020300, 1020300, 1020300, 1020300, 1020300, 1020300, 1015300, 1004100, 1004100, 999000, 999000, 992000, 992000, 992000, 992000, 992000, 980900, 980900, 979200, 971400, 971400, 971400, 971400, 971400, 970300, 970300, 970300, 970300, 970300, 968400, 968400, 968400, 968000, 968000, 968000, 968000, 965600, 965600, 958400, 923900, 923900, 923900, 923900, 923900, 923900, 923900, 923900, 923900, 923900, 923900, 923900, 923900, 923900, 923900, 923900, 923900, 923900, 923900, 923900, 923900, 923900, 923900, 923900, 923900, 923900, 923900, 923900, 923900, 923900, 923900, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 892300, 889000, 889000, 889000, 889000, 889000, 889000, 889000, 889000, 889000, 889000, 889000, 889000, 889000, 889000, 889000, 889000, 889000, 889000, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879600, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300, 879300]
# log_data = [306200, 305700, 298000, 298000, 298000, 298000, 293300, 293300, 293300, 293300, 293300, 293300, 293300, 293300, 293300, 293300, 293300, 293300, 293300, 291450, 291450, 291450, 291450, 291450, 291450, 291450, 291450, 291450, 291450, 291450, 291450, 291450, 291450, 291450, 291450, 291450, 291450, 291450, 291450, 291450, 291450, 291450, 291450, 291450, 291450, 291450, 282900, 282900, 282900, 282900, 282900, 282900, 282900, 282900, 282900, 282900, 282900, 282900, 282900, 282900, 278650, 278650, 278650, 278650, 278650, 278650, 278650, 278450, 278450, 278450, 278450, 278450, 278450, 278450, 278450, 276650, 276650, 276650, 276650, 276650, 276650, 276650, 276650, 276650, 276650, 274450, 274450, 274450, 274450, 274450, 274450, 274450, 274450, 274450, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 266950, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400, 265400]
# log_data = [134400, 134400, 133570, 133570, 132760, 132760, 131940, 131940, 128750, 123890, 123890, 123890, 123890, 123890, 123890, 123890, 123890, 123890, 123890, 123890, 123890, 123890, 123890, 123890, 123890, 123890, 123890, 123890, 123890, 123890, 123890, 123890, 123890, 123890, 123890, 123890, 123890, 123890, 123890, 123890, 123890, 123890, 123260, 123260, 123260, 123260, 123260, 123260, 123260, 123260, 118670, 118260, 118260, 118260, 118260, 118260, 118260, 118260, 115870, 115870, 115870, 115110, 115110, 115110, 115110, 115110, 114690, 113430, 113430, 106260, 106260, 106260, 106260, 106260, 106260, 106260, 106260, 106260, 106260, 105860, 105860, 105860, 105860, 105860, 105860, 105860, 105860, 105860, 105860, 105860, 105860, 105860, 105860, 105860, 105860, 105860, 105860, 105860, 105860, 104380, 104380, 104380, 104380, 104380, 104380, 104380, 102280, 102280, 102280, 102280, 102280, 102280, 100390, 100390, 100390, 100390, 100390, 100390, 100390, 100390, 100390, 100390, 100390, 100390, 100390, 100390, 100390, 100390, 100390, 100140, 100140, 100140, 100140, 100140, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 93700, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800, 92800]
# log_data = [169450, 163700, 161950, 161950, 161950, 161950, 161950, 158550, 158550, 158550, 158550, 158550, 158550, 158550, 158550, 158550, 158550, 158550, 158550, 158550, 158550, 158550, 158550, 158550, 158550, 154900, 154900, 154900, 154900, 154900, 154900, 154900, 154900, 154900, 154900, 154900, 154900, 154900, 154900, 154900, 154900, 154900, 154900, 154900, 154900, 154900, 154900, 154900, 154900, 150500, 150500, 150500, 150500, 150500, 150500, 150500, 150500, 150500, 150500, 150500, 150500, 150500, 150500, 150500, 150050, 150050, 145250, 145250, 145250, 145250, 145250, 145250, 145250, 145250, 145250, 145250, 145250, 139850, 139850, 139850, 139850, 139850, 139850, 139850, 139850, 139850, 139850, 139850, 139850, 138450, 138450, 138450, 138450, 138450, 136300, 136300, 135000, 135000, 135000, 135000, 135000, 135000, 135000, 135000, 135000, 132700, 132700, 132700, 132700, 132700, 132700, 132700, 132700, 132700, 132700, 132700, 132700, 132700, 132700, 132700, 132700, 132700, 132700, 132700, 132700, 132700, 132700, 132700, 132700, 132700, 132700, 132700, 132700, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300, 124300]
log_data = [768600, 733700, 733700, 733700, 733700, 733700, 733700, 733700, 733700, 733700, 733700, 733700, 733700, 733700, 733700, 733700, 733700, 733700, 733700, 733700, 733700, 733700, 733700, 733700, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 729100, 705900, 705900, 705900, 705900, 705900, 705900, 705900, 705900, 705900, 705900, 705900, 705900, 705900, 705900, 705900, 705900, 705900, 705900, 705900, 705900, 705900, 705900, 703800, 701700, 701700, 701700, 701700, 696800, 696800, 696800, 696800, 696800, 696800, 696800, 696800, 696800, 690400, 690400, 690000, 690000, 690000, 675800, 675800, 675800, 675800, 675800, 675800, 675800, 675800, 675800, 672800, 672800, 672800, 672800, 672800, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 655500, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651600, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200, 651200]


plt.plot(log_data, linewidth=2)
plt.hlines(optimal_line, 0, len(log_data), color='red', linewidth=2)
plt.xlabel("epoch")
plt.ylabel("time")
plt.show()