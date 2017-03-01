import numpy as np

# Liste over koeffisientene til y-x-grafen til hakk1 take2, alle 10 forsøkene
hakk1_sy_sx = [-3.57, 1.743, 0.002446] # eks: s_y(s_x) = -3.57x^2 + 1.743x + +.002446
hakk2_sy_sx = [-4.315,  1.956, -0.00002245]
hakk3_sy_sx = [-4.107,  1.66,  0.004686]
hakk4_sy_sx = [-3.778,  1.95, 0.0000331]
hakk5_sy_sx = [-3.123, 1.691 , 0.002927 ]
hakk6_sy_sx = [-4.057,  1.766,  0.002901]
hakk7_sy_sx = [-3.24,  1.635,  0.0003832]
hakk8_sy_sx = [-2.986,  1.637, 0.0009006 ]
hakk9_sy_sx = [-3.242,  1.588,  0.00111]
hakk10_sy_sx = [-2.928, 1.554 ,  0.008048]

# Lager en liste med alle koeffisient-listene, slik at det blir lettere å lage for-løkke.
hakk1take2 = [hakk1_sy_sx, hakk2_sy_sx, hakk3_sy_sx,
              hakk4_sy_sx, hakk5_sy_sx, hakk6_sy_sx,
              hakk7_sy_sx, hakk8_sy_sx, hakk9_sy_sx,
              hakk10_sy_sx]

# Finner nullpunktene til grafen, retunerer kun det største (det som er lengst unna).
# Vi er ikke interessert i negativt nullpunkt.
def find_t_when_sy_is_0(coeffs):
    roots = np.roots(coeffs)
    if roots[0] > roots[1]:
        return roots[0]
    else:
        return roots[1]

# Lager en liste med alle skjæringspunktene, slik at vi kan finne gjennomsnitt senere.
alle_skjæringspkt = []

# Kun for å printe pent.
i = 0

# Finner nullpunkt i vårt eksperiment
for forsøk in hakk1take2:
    i+=1
    punkt = find_t_when_sy_is_0(forsøk)
    print("Kast",i, "skjæringspunkt:",punkt)
    alle_skjæringspkt.append(punkt)
print("Tallene angir hvor mange meter unna utskytningspunktet (origo) kula skjærer x-aksen. \n")

# Finner gjennomsnitt
gjennomsnitt = np.average(alle_skjæringspkt)
print("Gjennomsnitt:", gjennomsnitt)

