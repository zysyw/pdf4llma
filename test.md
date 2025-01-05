# Evaluation of Solar Panel Integration in Power Control Distribution Networks

**Toaza, Jimmy[1,*]** **; Pazmiño, Edwin[2]** **; Quinatoa, Carlos[1]** **; Salazar, Roberto[1]**

_1Universidad Técnica de Cotopaxi, Facultad de Ciencias de la Ingeniería y Aplicadas, Latacunga, Ecuador_

_2Universidad Técnica de Cotopaxi, Departamento de Ingeniería, Latacunga, Ecuador_

**Abstract:** The reduction of greenhouse gases, such as CO2, has led countries to adopt measures to reduce their
environmental impact, according to the goals of the 2030 agenda. As a result, changes in the operation and planning
of electricity systems and distribution networks are taking place, which have had to adapt to the incorporation of nonconventional renewable energies, such as photovoltaic. The integration of these technologies generated problems such
as voltages outside the allowed limits, fluctuations, overloads, reverse flows, sympathetic tripping and an increase in
fault currents, making it necessary to evaluate the percentage of renewable energies that can be safely integrated. This
research evaluated the integration capacity of solar panels in the distribution network of primary and secondary lines
using OpenDSS in the Chimbo feeder of the Guaranda substation of the Bolivar CNEL EP business unit. Two
methodologies are presented: the first one evaluates the maximum input capacity of solar panels in percentage terms,
and the second one implements a reactive power-voltage control using an optimization model. The results showed that,
with the first methodology, the maximum integration limit was 48%, while the second methodology allowed the
integration of 100% of the solar panels, without exceeding the power quality limits established by national regulations.

**Keywords: Photovoltaic panels, voltage profile, electrical distribution, electrical demand, solar irradiation**

# Evaluación de Integración de Paneles Solares en Redes de
 Distribución para Control de Potencia

**Resumen: La reducción de gases de efecto invernadero, como el CO2, ha llevado a los países a adoptar medidas para**
reducir su impacto ambiental, de acuerdo con los objetivos de la agenda 2030. Como consecuencia, se están
produciendo cambios en la operación y planificación de los sistemas eléctricos y las redes de distribución, que han
tenido que adaptarse a la incorporación de energías renovables no convencionales, como la fotovoltaica. La integración
de estas tecnologías generó problemas como tensiones fuera de los límites permitidos, fluctuaciones, sobrecargas,
flujos inversos, disparos por simpatía y aumento de las corrientes de falla, haciendo necesario evaluar el porcentaje de
energías renovables que pueden ser integradas de forma segura. En esta investigación se evaluó la capacidad de
integración de paneles solares en la red de distribución de líneas primarias y secundarias utilizando OpenDSS en el
alimentador Chimbo de la subestación Guaranda de la unidad de negocio Bolívar CNEL EP. Se presentan dos
metodologías: la primera, evalúa la capacidad máxima de aporte de los paneles solares en términos porcentuales, y la
segunda implementa un control de potencia reactiva-tensión utilizando un modelo de optimización. Los resultados
mostraron que, con la primera metodología, el límite máximo de integración era del 48%, mientras que la segunda
metodología permitía la integración del 100% de los paneles solares, sin superar los límites de calidad de energía
establecidos por la normativa nacional.

**Palabras clave: Paneles fotovoltaicos, perfil de tensión, red de distribución, demanda eléctrica, irradiación solar**


**11. INTRODUCTION**

The constant evolution of technology and the commitment to
reduce greenhouse gas emissions to meet the 2030 diary
(CEPAL, 2018), have made photovoltaic panels more efficient
and economical. To start with, the Agency for the Regulation

*jimmy.toaza1062@utc.edu.ec
Recibido: 02/07/2024
Aceptado:16/12/2024
Publicado en línea: 31/12/2024
[10.33333/rp.vol54n3.07](https://doi.org/10.33333/rp.vol54n3.07)
[CC 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)


and Control of Non-Renewable Energy and Natural Resources
ARCERNNR approves resolution No. ARCERNNR001/2021 corresponding to the Regulatory Framework of
Distributed Generation for self-supply of regulated consumers
of electrical energy (ARCERNNR, 2021). Therefore, there is
a high probability that regulated and non-regulated users


Revista Politécnica Diciembre 2024 Vol 54 No 3


-----

install photovoltaic panels along the feeder and problems such
as: overvoltage, unbalances, harmonics, flows in two
directions, sympathetic tripping, increased levels appear. short
circuit, among others.

Currently, this document evaluates the power input of
photovoltaic panels through two methodologies that help the
analysis of voltages in the nodes, power through the lines and
currents in the electrical distribution network of the GuarandaChimbo feeder of the Guaranda substation belonging to CNEL
EP BOLIVAR in order to control the massive input of
photovoltaic panels in compliance with the integral regulation
for the distribution and commercialization of electrical energy
in the country No. ARCERNNR-002/20.

Through this study, it is intended to analyze in depth the
problems that the electrical network has when there is a
massive entry of photovoltaic panels into the Chimbo feeder,
being renewable energies these help to protect the environment
and its ecosystem, since, if distributed photovoltaic or
conventional generation mainly thermal power plants will
decrease and reduce greenhouse gas or CO2 emissions, except
for the introduction of solar cells, as well as help reduce
technical losses in the electrical distribution network.

To address the problem of massive entry of photovoltaic
generators into the electrical grid, they carry out a hosting
capacity theorem to determine the amount of photovoltaic
generation capacity distributed for each client with security
and protection (Khomarudin et al. 2022), this Capacity
Methodology Lodging consists of installing Photovoltaic in
client to client with the maximum capacity without exceeding
the limit of the system. However, as the photovoltaic panels
depend on the solar irradiation that is variable during the day
and weather conditions in Kahrobaee et al. (2020) proposes a
probabilistic approach to determine the impact of the reduction
of photovoltaic energy on the improvement of the
accommodation capacity of a distribution circuit in different
integration locations.

Today, there are efforts by electric distribution companies to
determine the accommodation capacity in their networks in
Niederhuemer et al. (2015) they carry out a probabilistic
planning approach that increases the accommodation capacity
of photovoltaic energy while accepting an active power
reduction, performed with the P(U) control of the photovoltaic
inverter, for short periods of time. Ebe et al. (2017) compare
different methods for assigning future photovoltaic capacity
based on analysis of solar potential at the distribution system
level. Rule-based methods are developed and compared with a
probabilistic method, which is repeated several times as a
Monte Carlo analysis.

Likewise, to determine the allocation of photovoltaic power to
the grid nodes, Bhusal et al. (2019) propose a stochastic
method to calculate the distributed generation accommodation
capacity for photovoltaic panels while guaranteeing that no
voltage requirements are violated, the proposed method takes
electric vehicle charges into account. As photovoltaic panels
power electronics as an interface to connect to the electrical
network in Nakhodchi et al. (2021) proposes a new approach


to estimate a safe accommodation capacity in terms of
harmonic distortion, considering standard limits for harmonic
voltages and currents. It is shown that triple harmonics and
seven harmonics are the harmonic orders that determine the
total accommodation capacity. Likewise, electrical
distribution networks consist of primary and secondary
networks. Navarro et al. (2021) developed a methodology to
determine the photovoltaic solar energy hosting capacity of a
distribution network, considering the interactions between
medium-voltage (MV) and low-voltage (LV) networks at
different voltage levels. Their approach included detailed LV
network modeling features for a comprehensive analysis. A
novel solution to calculate hosting capacity based on network
congestion risk. In addition to the classical voltage and current
constraints, the proposed approach also integrates the
stochastic allocation of distributed generation and separately
assesses its impact on the value of hosting capacity. In
Ezzeddine et al. (2021) he proposes a topology agnostic
estimation method for the PV hosting capacity of distribution
networks, this method uses the strength of the direct path from
the slack bus to the customer and an assumed topology to avoid
a complete knowledge about the network topology. Using an
assumed topology, an estimate of the minimum surge carrying
capacity for each penetration level and the transformer surge
carrying capacity is obtained for any combination of customers
having PV panels. The inclusion of solar panels requires
mathematical optimization models or in this sense in
Alrushoud et al. (2020) proposes a PV allocation method based
on the optimal capacity to evaluate the PV hosting capacity,
Firstly, we use the load allocation method to assign realistic
load profiles to each charging node up to each household,
instead of randomly assigning the PV installed capacity to
each household, secondly, the optimal PV size for each
household is calculated. based on annual load profiles.

Wang et al. (2016) propose a maximum accommodation
capacity evaluation method taking into account the optimal
and robust operation of on-load tap changers (OLTC) and
static var compensators in the uncertain context of power
outputs from distributed generation and load consumption. In
Hassan et al. (2022) a new multi-stage algorithm is developed
based on an analytical approach and an optimal power flow for
the evaluation of the hosting capacity of distributed renewable
generation. In the first stage, the optimal locations of the
distributed renewable generation are determined analytically,
and the second stage involves the calculation of the optimal
sizes of the distributed renewable generation for the evaluation
of the optimal accommodation capacity.

The reviewed investigations do not address the control
strategies of inverters and voltage regulators for the large-scale
integration of renewable energy sources into electrical
distribution networks. The entrance of the photovoltaic panels
to the electrical distribution network is of a random nature due
to the variability of the primary energy and the uncertain
knowledge of the installation of the users. This causes the
analysis to be performed using stochastic methods.

Regarding our investigation, it is proposed to evaluate the state
variables of the system with the entry of photovoltaic panels
using the random method of load profiles and solar irradiation


-----

and after that a strategy is carried out control in the voltage
power inverter with a method of mathematical optimization.
For this, the OpenDSS software will be used, which allows
modeling the electrical distribution network (Ochoa, 2015)
and the python platform for the interface and data management
(Hariri, 2017) together with Pyomo and the solver knitro.

The rest of this document is organized as follows. Then, it
presents the general data of the Guranda - Chimbo feeder of
the company CNEL - BOLIVAR is presented. Subsequently,
the methodology used is explained. Then the results and
discussion are presented. Finally, additional information to be
considered is detailed, after which conclusions and
recommendations are presented.
